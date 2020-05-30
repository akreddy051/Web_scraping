import requests
from bs4 import BeautifulSoup
import pprint


def print_by_sorting_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'],reverse=True)


res = requests.get('https://news.ycombinator.com/news')
res2=requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')
links2 = soup2.select('.storylink')
votes2 = soup2.select('.score')

mega_links=links+links2
mega_votes=votes+votes2

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        if points > 99:
            hn.append({'title': title, 'link': href, 'votes': points})
    return print_by_sorting_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_votes))
