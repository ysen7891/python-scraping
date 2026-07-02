import logging


from scraper import Scraper
from write_csv import Csv_Writer
from config import URL,OUTPUT_FILE

logger = logging.getLogger(__name__)

def main():
    logger.info("処理開始")
    scraper = Scraper(URL)


    html = scraper.fetch_html()


    parsed_html = scraper.parser(html)


    Csv_Writer.write_csv(OUTPUT_FILE,parsed_html)

    logger.info("処理終了")


if __name__ == "__main__":
    main()






        