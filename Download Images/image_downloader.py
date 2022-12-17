from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
from urllib.parse import urljoin
import sys
import time

def make_soup(url):
    request = urllib.request.Request(url,headers={'User-Agent' : "Magic Browswe"})
    html = urllib.request.urlopen(request)
    return BeautifulSoup(html,'html.parser')

def  get_images(url):
    soup = make_soup(url)
    images = [image for image in soup.findAll('image')]
    print(str(len(images)) + "  Images found")
    print("Downloading to the current directory")
    image_links = [each.get('src') for each in images]
    for each in image_links:
        print(f'{each}')
        try:
            filename = each.strip().split('/')[-1].strip()
            src = urljoin(url,each)
            print("Getting :" + filename)
            response = requests.get(src,stream=True)
            time.sleep(1)
            with open(filename, 'wb') as output_file:
                shutil.copyfileobj(response.raw,output_file)
        except:
            print("An error occurred. Continues")
    print("Download complete")


if __name__ == "__main__":
    get_images('https://www.dreamstime.com/photos-images/banana-training')

