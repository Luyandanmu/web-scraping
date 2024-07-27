import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.example.com/local-weather'

# Send a GET request to the page
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired information
weather = soup.find('div', class_='weather-forecast').text

print(f'Local Weather: {weather}')
