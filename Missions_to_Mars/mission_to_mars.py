'''
Mission to Mars Web Scrape Script
Author: Andrew McKinney
Creation Date: 2020-02-14
'''

# importing dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser

def houston():

    ### Top NASA new title and paragraph

    # defining web url 
    # NOTE: THIS HAS PROBLEMS WITH CALLING THIS URL RECURRENT AND DOES NOT GET BACK THE ACTUAL HTML AND GETS CSS INSTEAD
    url_nasa_news = 'https://mars.nasa.gov/news'

    print(f'Visiting {url_nasa_news}')

    # creating splinter browser and visint url
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url_nasa_news)
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text.strip()
    news_para = soup.find('div', class_='article_teaser_body').text.strip()

    print('Done')


    ### NASA featured image

    # defining web url
    url_nasa_imgs = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    print(f'Visiting {url_nasa_imgs}')

    # visiting url
    browser.visit(url_nasa_imgs)
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('a', class_='button fancybox')['data-fancybox-href']

    print('Done')


    ### Mars Weather

    # defining web url
    url_mars_weath = 'https://twitter.com/marswxreport'

    print(f'Requesting {url_mars_weath}')

    # get html using requests, browser scraping does not work for this
    response = requests.get(url_mars_weath).text

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response, 'html.parser')

    mars_weather = soup.find('p', class_='TweetTextSize').text.replace('\n', ' ').split(' hPapic')[0]

    print('Done')


    ### Mars Facts

    # defining web url
    url_mars_fact = 'https://space-facts.com/mars/'

    print(f'Reading {url_mars_fact}')

    # scraping with pandas
    mars_facts = pd.read_html(url_mars_fact)[1].drop(columns={'Earth'})

    mars_facts_html = mars_facts.to_html()

    print('Done')


    ### Mars Hem Images

    url_main_mars_images = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    print(f'Visiting {url_main_mars_images}')

    # soupifying main page
    browser.visit(url_main_mars_images)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # creating image list for searches
    image_headers = soup.find_all('div', class_='description')
    image_list = []
    for items in image_headers:
        image_list.append(items.h3.text)

    # creating empty ouptput dictionary
    mars_hem_dict = []
        
    #cycling through image list to navigate website and scrape info
    for image in image_list:
        
        # navigating to image page
        browser.click_link_by_partial_text(image)
        
        # resetting html object to current page
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        # scraping items per image
        title = soup.find('h2', class_='title').text.strip()
        img_url = 'https://astrogeology.usgs.gov/' + soup.find('img', class_='wide-image')['src']
        dl_img_url = soup.find('a', text='Original')['href']
        
        # appending image items to dictionary
        mars_hem_dict.append({'title' : title, 'img_url' : img_url ,'dl_img_url' : dl_img_url})
        
        
        # navigating back to master page list
        browser.back()
        
    print('Done')

    to_houston = ({
        'news_title' : news_title,
        'news_para' : news_para,
        'featured_image_url' : featured_image_url,
        'mars_weather' : mars_weather,
        'mars_facts_html' : mars_facts_html,
        'mars_hem_dict' : mars_hem_dict
    })

    return to_houston