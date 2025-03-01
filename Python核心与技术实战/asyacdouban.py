"""
协程爬取豆瓣电影
"""
import time
import asyncio

import aiohttp
from bs4 import BeautifulSoup


async def fetch_content(url):
    print('fetching {}'.format(url))
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')
    
    movie_names, movie_dates, url_to_fetch = [], [], []
    
    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        url_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)
    
    tasks = [fetch_content(url) for url in url_to_fetch]
    pages = await asyncio.gather(*tasks, return_exceptions=True)
    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')
        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print('cost {} seconds'.format(end_time - start_time))













