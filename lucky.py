#!/bin/env python3
''' Open the first four search results '''

import sys
import webbrowser
from bs4 import BeautifulSoup
import requests

QUERY = ' '.join(sys.argv[1:])

response = requests.get(f'https://duckduckgo.com/html/?q={QUERY}', headers={'user-agent': 'lucky/1.0.0'})
response.raise_for_status()

soup = BeautifulSoup(response.text)
results = soup.select('a.result__url')
for result in results[:4]:
    result_url = f'https:{result["href"]}'
    #print(result_url)
    webbrowser.open(result_url)
