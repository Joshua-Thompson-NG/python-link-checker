import requests
import os
import re

#--------------------------------
# Entry and input handling
filename = "testing.md"
url_pattern = r'(?:https?://|www\.)[^\s<>"]+?(?=[),.:;]?(?:\s|$))'

def check_files_exists(filename:str) -> bool:
    if os.path.isfile(filename):
        return True
    else:
        return False


#---------------------------------
# Link Extraction
def extract_links(url_pattern:str, filename:str) -> set[str]:
    with open(filename, "r") as f:
        content = f.read()

    links = re.findall(url_pattern, content)

    return set(links)

#-----------------------------------
# URL Validation
def validate_urls(urls:set[str]) -> dict[str, str]:
    print("Validating URLs...")
    link_maps = {}
    for url in urls:
        if not url.startswith(("http://","https://")):
            url = "https://" + url
        try:
            response = requests.head(url, timeout=5)
            response.raise_for_status()
            if response.status_code:
                link_maps[url] = "Link is valid."
                print(f"URL {url} is valid.")


        except requests.exceptions.Timeout as e:
            link_maps[url] = "Link timed out."
            print(f"Request timed out for {url}. {e}")

        except requests.exceptions.ConnectionError as e:
            link_maps[url] = "DNS failure or connection refused"
            print(f"DNS failure or connection refused for {url}. {e}")

        except requests.exceptions.SSLError as e:
            link_maps[url] = "SSL/TLS certificate error"
            print(f" SSL/TLS certificate error: {e}")

        except requests.exceptions.HTTPError as e:
            link_maps[url] = "HTTP Error occurred"
            print(f"HTTP Error occurred: {e}")

        except requests.exceptions.RequestException as e:
            # Parent class for all Requests exceptions (catches anything missed above)
            link_maps[url] = "An ambiguous network error occurred"
            print(f"⚠️ An ambiguous network error occurred: {e}")


    return link_maps

#-----------------------------------------
# Report Generation
def generate_report(link_maps:dict[str, str]) -> None:
    print("Generating report...")
    with open("report.txt", "w") as f:
        for url, status in link_maps.items():
            f.write(f"{url} - {status}\n")

# Testing
if check_files_exists(filename):
    print("File exists...")
    generate_report(validate_urls(extract_links(url_pattern, filename)))
else:
    print("File does not exist...")
    # create file
    open(filename, "w").close()
    print("File created...")