URL = "https://www.scrapethissite.com/pages/simple/"
OUTPUT_FILE = "scraping_result.csv"

FIELD_NAMES = [
    "国名",
    "首都",
    "人口",
    "面積(km2)"
]

TIMEOUT = 10

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}
