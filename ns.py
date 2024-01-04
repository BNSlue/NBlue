# First, you need to install the necessary libraries. You can do this by running:
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://example.com'

# Send an HTTP request to the URL and retrieve the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract specific data from the webpage
    # For example, let's say you want to extract all the links from the page
    links = soup.find_all('a')

    # Print the extracted links
    for link in links:
        print(link.get('href'))
else:
    print('Failed to retrieve the webpage')
