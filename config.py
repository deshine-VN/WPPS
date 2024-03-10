headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"
}

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

filenames = ["readme.txt", "changelog.txt"]

version_regex = r"(?i)Stable.tag:\s+?([\w.]+)"