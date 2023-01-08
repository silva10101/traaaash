import requests
from bs4 import BeautifulSoup

url = 'http://anekdotov.net/anekdot/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

name = soup.find_all("body")
anekdots = soup.find_all('div', class_='anekdot')
vid_anekdots = soup.find_all('table', class_='nizposta')

for i in range(len(anekdots)):

    print(anekdots[i].text)
    try:
        print(vid_anekdots[i].find('i').text)
    except AttributeError:
        pass
    print('\n\n')

