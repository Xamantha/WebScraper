from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
  print("Xammy's WebScraper")
  data = input("Web URL to Scrape:")
  searchData = input("Word/Tag to scrape for:")
  requestURL = urlopen(data)
  soup = BeautifulSoup(requestURL, 'html.parser')
  print(soup.find_all(searchData))
  main()
if __name__ == '__main__':
  main()
