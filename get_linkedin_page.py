import os
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver

def match_class(target):                                                        
    def do_match(tag):                                                          
        classes = tag.get('class', [])                                          
        return all(c in classes for c in target)                                
    return do_match     

url = 'https://www.linkedin.com/company/enigma-technologies-inc-'

# start driver to retrieve HTML of company page
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# print soup.find_all(match_class(['basic-info-description'])).find_all('p').text

# get only company information
print soup.find(class_='basic-info-description').find('p').text
driver.close()
driver.quit()


