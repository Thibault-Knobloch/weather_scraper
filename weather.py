import requests
from bs4 import BeautifulSoup

city = "rotterdam"

#You can change the part in URL after q= to the city you want to scrape the weather for!
url = 'https://www.wetter.de/niederlande/wetter-rotterdam-1811359.html?q=rotterdam'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

html_line = soup.find(attrs={"class": "weather-daybox__minMax__max"})

output = html_line.get_text()

print("The current weather in Rotterdam is", output)