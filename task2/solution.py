import sys
import time
import csv
from collections import Counter

import aiohttp
import asyncio
from bs4 import BeautifulSoup

URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
RUSSIAN_ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


async def fetch_page(session: aiohttp.ClientSession, url: str) -> str:
    """
    Загружает HTML-страницу по указанному URL.

    :param session: Сессия aiohttp.
    :param url: URL страницы.
    :return: HTML-код страницы.
    """
    async with session.get(url) as response:
        return await response.text()


async def get_all_animals() -> Counter:
    """
    Считает количество животных на каждую букву русского алфавита
    на страницах Википедии.

    :return: Counter с количеством животных по первой букве.
    """
    counter = Counter()
    next_page = URL
    async with aiohttp.ClientSession() as session:
        while next_page:
            html = await fetch_page(session, next_page)
            soup = BeautifulSoup(html, 'html.parser')
            for ul in soup.select('div.mw-category div.mw-category-group ul'):
                for li in ul.find_all("li"):
                    name = li.get_text(strip=True)
                    if name:
                        first = name[0].upper()
                        if first in RUSSIAN_ALPHABET:
                            counter[first] += 1
            next_link = soup.select_one('a:-soup-contains("Следующая страница")')
            if next_link and next_link.has_attr('href'):
                next_page = 'https://ru.wikipedia.org' + next_link['href']
            else:
                next_page = None
    return counter


def save_to_csv(counter: Counter, filename: str = 'beasts.csv') -> None:
    """
    Сохраняет результаты подсчёта в CSV-файл.

    :param counter: Counter с количеством животных по буквам.
    :param filename: Имя файла для сохранения.
    """
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for letter in RUSSIAN_ALPHABET:
            if letter in counter:
                writer.writerow([letter, counter[letter]])


if __name__ == '__main__':
    print('Сбор данных с Википедии. Подождите, пожалуйста...', file=sys.stderr)
    start_time = time.time()
    counter = asyncio.run(get_all_animals())
    save_to_csv(counter)
    elapsed = time.time() - start_time
    print(f'Поиск завершён за {elapsed:.1f} секунд.', file=sys.stderr)
