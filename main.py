import requests, time
import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options, DesiredCapabilities


def combine():
#READ ALL CSVS INTO LISTS AND COMBINE THEM TOGETHER

    df1 = pd.read_csv("360Sraped_addresses.csv")
    addresses = df1['Addresses'].values.tolist() 

    df2 = pd.read_csv("360Sraped_names.csv")
    names = df2['Name'].values.tolist()

    df3 = pd.read_csv("360Sraped_sleeps.csv")
    sleeps = df3['Sleeps'].values.tolist() 

    df4 = pd.read_csv("360Sraped_bathrooms.csv")
    bathrooms = df4['Bathrooms'].values.tolist() 

    df5 = pd.read_csv("360Sraped_bedrooms.csv")
    bedrooms = df5['Bedrooms'].values.tolist() 

    df7 = pd.read_csv("360Sraped_urls.csv")
    urls = df7['Image Urls'].values.tolist() 


    df6 = pd.read_csv("360Sraped_namessss.csv", encoding="utf8")
    descriptions = df6['Description'].values.tolist()
    descriptions = [x for x in descriptions if x]


    df = pd.DataFrame({'Name':names,'Address':addresses,'Description':descriptions, 'Sleep':sleeps, 'Bedroom':bedrooms, 'Bathroom':bathrooms, 'Image Urls':urls}) 
    df.to_csv('360Sraped.csv')


def get_image_urls(links,names):

    image_urls = get_urls_from(links, names)

    print("Image Urls: " + str(len(image_urls)))
    df = pd.DataFrame({'Image Urls':image_urls}) 
    df.to_csv('360Sraped_urls.csv')


def load_links_names():

    df = pd.read_csv("360Sraped_links.csv")
    links = df['Links'].values.tolist()

    df2 = pd.read_csv("360Sraped_names.csv")
    names = df2['Name'].values.tolist()

    return links, names

def get_all_descriptions(links):
    count =0
    descriptions = []
    for link in links:
         description = get_descriptions_from(link)
         descriptions.append(str(description))
         print(str(count) + '/' + str(len(links)))

    print("Descriptions: " + str(len(descriptions)))
    df = pd.DataFrame({'Description':descriptions}) 
    df.to_csv('360Sraped_namessss.csv')
     

def get_bathrooms_bedrooms_sleeps(links, names):


    addresses = []
    sleeps = []
    bathrooms = []
    bedrooms = []

    count = 0
    for link in links:

         sleep = get_sleeps_from(link)
         sleeps.append(sleep["sleep"])
         bedrooms.append(sleep["bedroom"])
         bathrooms.append(sleep["bathroom"])

         count+=1
         print(str(count) + '/' + str(len(links)))

    for name in names:
    	address = get_addresses_from(names)
    	addresses.append(address)


    print("Sleeps: " + str(len(sleeps)))
    df = pd.DataFrame({'Sleeps':sleeps}) 
    df.to_csv('360Sraped_sleeps.csv')

    print("Bedrooms: " + str(len(bedrooms)))
    df = pd.DataFrame({'Bedrooms':bedrooms}) 
    df.to_csv('360Sraped_bedrooms.csv')

    print("Bathrooms: " + str(len(bathrooms)))
    df = pd.DataFrame({'Bathrooms':bathrooms}) 
    df.to_csv('360Sraped_bathrooms.csv')

    print("Addresses: " + str(len(addresses)))
    df = pd.DataFrame({'Addresses':addresses}) 
    df.to_csv('360Sraped_addresses.csv')




def get_name_from(link):
     page = requests.get(link)
     soup = BeautifulSoup(page.text, 'html.parser')
     name = soup.find('div', {'class': 'wpb_column vc_column_container vc_col-sm-8'})
     name = name.find_all('h1')
     name = name[0]
     name = name.text

     


     return name
def get_images_from(links, names):

  url_list = []

  for name, link in zip(names, links):

     link = link + 'gallery/'

 
     page = requests.get(link)

     soup = BeautifulSoup(page.text, 'html.parser')
     div1 = soup.find('div', {"class": "img-gallery-container"})
     div2 = div1.find_all('div', {"class": "row"})
     name = name.lower()
     name = name.replace(" ", "_")
     name = name.replace(".", "_")
     name = name.replace('"', "_")
     name = name.replace("\\", "_")
     name = name.replace("//", "_")
     name = name.replace("/", "_")
     name = name.replace(":", "_")
     name = name.replace("|", "_")
     newdire = "D:\\April\\360scraper\\images\\" + str(name)

     try:
        os.mkdir(newdire)
     except Exception as e:
        print(str(e))

     for div in div2:
        urls = div.find_all('img')

        count = 0
        for url in urls:
           urls__ = []
           url_text = url['src']
           urls__.append(url_text)
           url = url.get('src')
           

           url_text = url_text.lower()
           url_text = url_text.replace(" ", "_")
           url_text = url_text.replace(".", "_")
           url_text = url_text.replace('"', "_")
           url_text = url_text.replace("\\", "_")
           url_text = url_text.replace("//", "_")
           url_text = url_text.replace("/", "_")
           url_text = url_text.replace(":", "_")



           response = requests.get(url).content


           
           filename = "D:\\April\\360scraper\\images\\" + str(name) + '\\' + str(name) + str(count) + '.jpg'
           count+=1
           


           

           with open(filename, "wb") as f:
               f.write(response)
               print("written")
           


def get_urls_from(links, names):

  url_list = []

  for name, link in zip(names, links):

     link = link + 'gallery/'

 
     page = requests.get(link)

     soup = BeautifulSoup(page.text, 'html.parser')
     div1 = soup.find('div', {"class": "img-gallery-container"})
     div2 = div1.find_all('div', {"class": "row"})
     name = name.lower()
     name = name.replace(" ", "_")
     name = name.replace(".", "_")
     name = name.replace('"', "_")
     name = name.replace("\\", "_")
     name = name.replace("//", "_")
     name = name.replace("/", "_")
     name = name.replace(":", "_")
     name = name.replace("|", "_")

     urls__ = []
     for div in div2:

        urls = div.find_all('img')

        count = 0
        for url in urls:
           
           url_text = url['src']
           urls__.append(url_text)
           
     url_list.append(urls__)

  return url_list

def get_descriptions_from(link):

     try:
       page = requests.get(link)
       soup = BeautifulSoup(page.text, 'html.parser')
       description = soup.find('div', {'id': 'description-tab'})
       description = description.find_all('p')
       description = description[0]
       description = description.text
     except Exception as e:
       print(str(e))
       description = ''

     


     return description

def get_sleeps_from(link):


     page = requests.get(link)
     soup = BeautifulSoup(page.text, 'html.parser')
     try:
        sleep = soup.find('table', {'class': 'propamen-tbl'})
        sleep = sleep.find_all('td', {'abbr': 'propamen-row'})
     except Exception as e:
        print(str(e))


     attribs = []

     try:
         for sl in sleep:
           attribs.append(sl.text)


         sleep = attribs[0]
         bedroom = attribs[1]
         bathroom = attribs[2]
         dict_ = {
         "sleep": str(sleep),
         "bedroom" : str(bedroom),
         "bathroom" : str(bathroom)
         }
     except Exception as e:
        print(str(e))
        dict_ = {
         "sleep": "Not Found",
         "bedroom" : "Not Found",
         "bathroom" : "Not Found"
         }

     return dict_

def get_addresses_from(name):

     communities = ['Adagio', 
          'Blue Mountain Beach',
          'Blue Mountain',
          'Destin', 
          'Dune Allen Beach',
          'Dune Allen',
          'Grayton Beach',
          'Grayton',
          'Inlet Beach',
          'Inlet',
          'Miramar Beach',
          'Miramar', 
          'Panama City Beach',
          'Panama City',
          'Panama',
          'Rosemary Beach',
          'Rosemary',
          'Seacrest Beach',
          'Seacrest',
          'Seagrove Beach',
          'Seagrove Beach', 
          'Seaside', 
          'Villa Coyaba', 
          'WaterColor', 
          'WaterSound',
          'WaterSound West']

     for community in communities: 
        if community in name:
          address = name.replace(str(community),"")
          return address
          break

browser = webdriver.Firefox(executable_path="D:/April/360scraper/env/geckodriver.exe") #CONFIGURE PATH TO DRIVER
print("Firefox Browser Invoked")
#LOG-IN SESSION
print("I will start scraping!")


#---- FIRST STEP

url = 'https://www.360blue.com/rentals/listproperties/'
browser.get(url)
time.sleep(10)
items = browser.find_elements_by_class_name("property-name")




links = []


SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")


####UNCOMMET THIS FOR FIRST TIME RUN, AS SELENIUM IS UNFORGIVING

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    items = browser.find_elements_by_class_name("property-name")

    for item in items:
        item = item.find_element_by_tag_name("a")

        link = item.get_attribute("href")

        links.append(link)

    
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


print("Retrieved all states in website")



links = list(set(links))
links = [x for x in links if x]

print("Links: " + str(len(links)))
df = pd.DataFrame({'Links':links}) 
df.to_csv('360Sraped_links.csv')



#### THIS PART GETS LINKS AND NAMES AND PUTS THEM INTO CSV I AHD TROUBLE DOING THIS ALL IN ONE RUN BECAUSE OF THEIR WBESITE
#### STRUCTURE



### LOAD PRE RETRIEVED LINKS AND NAMES WHICH ARE RHE ORIGINS OF ALL SECTIONS
links, names = load_links_names()


print("Done scraping links and names")

print("Total Scraped Links: " + str(len(links)))






get_bathrooms_bedrooms_sleeps(links,names)

get_all_descriptions(links)

get_image_urls(links,names) #GET URLS

get_images_from(links, names) # DOWNLOAD IMAGE URLS

combine()

print("Done Scraping Data... Downloading pictures now")
