from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser=webdriver.Chrome()
browser.get(START_URL)
time.sleep(10)

headers=['hyperlink','planet_type','planet_radius','orbital_radius','orbital_period','eccentricity','name','light-years from earth','planet mass','stellar magnitude','discovery date']
planetData=[]


def scrape():
    for i in range(0,453):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for ultag in soup.find_all('ul',attrs={'class','exoplanet'}):
            litags=ultag.find_all('li')
            tempList=[]
            for index,litag in enumerate(litags):
                if index==0:
                    tempList.append(litag.find_all('a')[0].contents[0])
                else:
                    try:
                        tempList.append(litag.contents[0])
                    except:
            
                        tempList.append('')
            hyperlink_litag=litags[0]
            tempList.append('https://exoplanets.nasa.gov' + hyperlink_litag.find_all('a',href=True)[0]['href'])
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


def scrapeMoreData(hyperlink):
    pass
    page=requests.get(hyperlink)
    soup=BeautifulSoup(page.content,'html.parser')
    for trtag in soup.find_all('tr',attrs={'class':'fact_row'}):
        tdtags=trtag.find_all('td')
        temp_List=[]
        for tdtags in tdtags:
            try:
                temp_List.append(tdtags.find_all('div',attrs={'class':'value'})[0].contents[0])
            except:
                temp_List.append('')

        newPlanetData.append(temp_List)
newPlanetData=[]
scrape()
for data in planetData:
    scrapeMoreData(data[5])
finalPlanetData=[]
for index,data in enumerate(planetData):
    finalPlanetData.append(data+finalPlanetData[index])
with open('scraper2.csv','w') as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(finalPlanetData)   
