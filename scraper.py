import requests
import logging
import time
from bs4 import BeautifulSoup

from config import TIMEOUT,HEADERS


logger = logging.getLogger(__name__)


class Scraper():


    def __init__(self,url):
        self._url = url


    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self,value):
        if len(value) > 0:
            self._url = value
        else:
            raise ValueError("URLを入力して下さい")
        
    def fetch_html(self):
        
        logger.info("Webサイトへアクセス開始")

        time.sleep(2)

        try:
            response = requests.get(self._url,
                timeout=TIMEOUT,
                headers=HEADERS)
            response.raise_for_status()
            
            logger.info("HTML取得完了")
            
            return response.text
        
        except requests.Timeout:
            logger.error("タイムアウトしました")
            raise

        except requests.RequestException as e:
            logger.error(f"通信エラー: {e}")
            raise

    

    
    
    def parser(self,html):
        logger.info("HTML解析開始")

        soup = BeautifulSoup(html,"html.parser")

        countries = soup.select(".country")

        logger.info(f"{len(countries)}件取得")


        for country in countries:
            
            

            country_name = country.select_one(".country-name")
            capital = country.select_one(".country-capital")
            population = country.select_one(".country-population")
            area = country.select_one(".country-area")


            yield{
                "国名":country_name.text.strip() if country_name else "",
                "首都":capital.text.strip() if capital else "",
                "人口":population.text.strip() if population else "",
                "面積(km2)":area.text.strip() if area else ""
            }