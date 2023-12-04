# 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи: цитата, автор, інфа про автора тощо.
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл

import csv
import os

import requests
from bs4 import BeautifulSoup


class QuotesScraper:
    url = "http://quotes.toscrape.com"
    authors = {}

    def add_data_to_file(self, data):

        headers = ["Quote", "Author", "Tags", "Born", "Description"]
        with open("data.csv", "a+", encoding="utf-8") as f:
            needs_header = os.stat("data.csv").st_size == 0
            writer_obj = csv.writer(f)

            if needs_header:
                writer_obj.writerow(headers)
                needs_header = False

            writer_obj.writerow(data)

    def get_author_info(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        born_info = soup.find("div", "author-details").find("p").text
        description = soup.find("div", "author-description").text.strip()

        return [born_info, description]

    def get_data(self):
        r = requests.get(self.url)
        while True:
            soup = BeautifulSoup(r.text, "html.parser")
            all_quotes_on_page = soup.find_all("div", "quote")

            for i in range(len(all_quotes_on_page)):
                quote_tag = all_quotes_on_page[i]

                quote_text = quote_tag.find("span", "text").text
                author = quote_tag.find("small", "author").text
                tags_list = [t.text for t in quote_tag.find_all("a", "tag")]

                new_record = [quote_text, author, tags_list]

                if author in self.authors.keys():
                    new_record.append(self.authors[author])
                else:
                    link = f"{self.url}{quote_tag.find('a').get('href')}"
                    new_record.extend(self.get_author_info(link))

                self.add_data_to_file(new_record)

            try:
                next_page_link = soup.find("li", "next").find("a").get("href")
            except AttributeError:
                print("Scrapping is finished!")
                break

            r = requests.get(f"{self.url}{next_page_link}")


q = QuotesScraper()
q.get_data()
