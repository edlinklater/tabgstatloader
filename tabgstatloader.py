import requests
import os
import sys
from bs4 import BeautifulSoup

current_page = 1
max_page = 5

if os.path.isfile('username.txt'):
    with open('username.txt', 'r') as f:
        username = f.read().strip()
else:
    username = input('TABG display name: ').strip()
    with open('username.txt', 'w') as f:
        f.write(username)

for page in range(current_page, max_page):
    r = requests.get('http://jlot.tk:1337/{}'.format(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    for row in soup.table.find_all('tr'):
        td = soup.find('td', string=username)
        if td:
            data = td.parent.find_all('td')
            rank = data[0].string.strip()
            kills = data[2].string.strip()
            with open('totalkills.txt', 'w') as f:
                f.write(kills)
            with open('rank.txt', 'w') as f:
                f.write(rank)
            print('Updated, rank #{} with {} total kills'.format(rank, kills))
            sys.exit(0)

sys.exit('Couldn\'t find {} in leaderboard.'.format(username))
