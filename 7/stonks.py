import asyncio
import os

import aiohttp
from bs4 import BeautifulSoup

import json

COMPANIES_URL = 'https://markets.businessinsider.com/index/components/s&p_500'
CURRENCY_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
JSON_DIR = 'json'

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_currency_rate():
    async with aiohttp.ClientSession() as session:
        xml = await fetch(session, CURRENCY_URL)
        soup = BeautifulSoup(xml, 'xml')
        rate = soup.find('Record', {'ID': 'R01235'}).Value.string.replace(',', '.')
        return float(rate)

async def get_company_info(session, url):
    html = await fetch(session, url)
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('h1', {'class': 'price-section__name'}).text.strip()
    code = soup.find('span', {'class': 'price-section__category'}).text.strip()
    price = soup.find('span', {'class': 'price-section__current-value'}).text.strip()
    pe = soup.find('div', {'class': 'snapshot__data-item snapshot__data-item--small'}).text.strip()
    growth = soup.find('td', {'class': 'table__td positive'}).text.strip()
    low = soup.find('td', {'class': 'snapshot__low'}).text.strip()
    high = soup.find('td', {'class': 'snapshot__high'}).text.strip()
    return {
        'name': name,
        'code': code,
        'price': price,
        'pe': pe,
        'growth': growth,
        'low': low,
        'high': high
    }

async def get_companies_info():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, COMPANIES_URL)
        soup = BeautifulSoup(html, 'html.parser')
        companies = soup.find_all('a', {'class': 'table__link'})
        tasks = []
        for company in companies:
            url = 'https://markets.businessinsider.com' + company['href']
            tasks.append(asyncio.ensure_future(get_company_info(session, url)))
        return await asyncio.gather(*tasks)

async def save_json(data, filename):
    with open(os.path.join(JSON_DIR, filename), 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

async def main():
    if not os.path.exists(JSON_DIR):
        os.makedirs(JSON_DIR)
    currency_rate = await get_currency_rate()
    companies_info = await get_companies_info()
    for company in companies_info:
        price = float(company['price'].replace(',', ''))
        company['price'] = round(price * currency_rate, 2)
        pe = float(company['pe'].replace(',', ''))
        company['pe'] = round(pe, 2)
        growth = float(company['growth'].replace('%', ''))
        company['growth'] = round(growth, 2)
        low = float(company['low'].replace(',', ''))
        high = float(company['high'].replace(',', ''))
        potential_profit = round((high - low) / low * 100, 2)
        company['potential_profit'] = potential_profit
    companies_info.sort(key=lambda x: x['price'], reverse=True)
    await save_json(companies_info[:10], 'top_10_expensive.json')
    companies_info.sort(key=lambda x: x['pe'])
    await save_json(companies_info[:10], 'top_10_low_pe.json')
    companies_info.sort(key=lambda x: x['growth'], reverse=True)
    await save_json(companies_info[:10], 'top_10_growth.json')
    companies_info.sort(key=lambda x: x['potential_profit'], reverse=True)
    await save_json(companies_info[:10], 'top_10_potential_profit.json')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
