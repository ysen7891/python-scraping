import csv
from config import FIELD_NAMES

import logging

logger = logging.getLogger(__name__)

class Csv_Writer():
    
    @staticmethod
    def write_csv(filename,data):

        with open(filename,"w",newline="",encoding="utf-8-sig") as f:
            writer = csv.DictWriter(
                f,
                fieldnames = FIELD_NAMES
            )

            writer.writeheader()

            writer.writerows(data)

            logger.info(f"{filename}を保存しました")



