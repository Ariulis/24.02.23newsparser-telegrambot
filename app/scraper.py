import os
from datetime import datetime

from requests_html import HTMLSession

from misc import URL, write_json, read_json


class NewsParser:

    @staticmethod
    def get_html(session):
        response = session.get(URL)

        if response.ok:
            return response.html
        return response.status_code

    @staticmethod
    def get_id(link):
        return link.split('/')[-1].split('.')[0]

    @staticmethod
    def refined_date(date):
        date = datetime.fromisoformat(date)
        date = datetime.strftime(date, '%d.%m.%Y %H:%M')
        return date

    def get_data(self):
        session = HTMLSession()
        response = self.get_html(session)
        articles = response.find('.article-card')

        data = {}

        for article in articles:
            id = self.get_id(article.attrs["href"])
            date = article.find('time', first=True).attrs['datetime']
            title = article.find('h2', first=True).text
            link = f'https://www.securitylab.ru{article.attrs["href"]}'
            excerpt = article.find('p', first=True).text

            data[id] = {
                'date': self.refined_date(date),
                'title': title,
                'link': link,
                'excerpt': excerpt
            }

        write_json(data)
