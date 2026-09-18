# Test File for Link Checker Project

This file contains various types of links (valid, broken, and malformed) to test your Python link checking script.

## 1. Valid Links
These links should return a `200 OK` status code under normal conditions:
* **Search Engine:** [Google](https://www.google.com)
* **Coding Platform:** [GitHub](https://github.com)
* **Python Official:** [Python Website](https://www.python.org)

## 2. Broken Links (Dead / 404 Not Found)
These URLs point to domains that exist, but the specific pages do not, which should trigger a `404` error:
* **Dead Page 1:** [GitHub Non-Existent Page](https://github.com/this-page-definitely-does-not-exist-12345)
* **Dead Page 2:** [Google 404 Test](https://www.google.com/invalid-page-path-test)

## 3. Invalid Domains (Connection / DNS Errors)
These domains do not exist at all. Your script should handle these without crashing (e.g., catching `requests.exceptions.ConnectionError`):
* **Fake Domain 1:** [Fake Domain Link](https://www.thisisacompletelyfakeddomainnamethatdoesnotexist.com)
* **Fake Domain 2:** [Broken Domain](https://example.invalid-domain-extension)

## 4. Edge Cases & Formats
* **HTTP Link:** [HTTP Example](http://example.com)
* **Duplicate Link:** [Google](https://www.google.com) (Your script could optionally de-duplicate this)
* **Relative Link:** [Local Document](relative/path/to/file.md) (Good for testing if your script filters out non-web links)
