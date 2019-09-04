# Dependecies 
from bs4 import BeautifulSoup as BS
from splinter import Browser
import pandas as pd 
import requests 
import time

# Browser Setup
def init_browser(): 
    executable_path = {"executable_path": "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

mars_data = {}

# News Scrape
def news_scrape():
    try: 
 
        browser = init_browser()

        url = 'https://mars.nasa.gov/news/'
        
        browser.visit(url)

        html = browser.html

        soup = BS(html, 'html.parser')

        news_title = soup.find('div', class_='content_title').find('a').text
        
        news_p = soup.find('div', class_='article_teaser_body').text

        mars_data['news_title'] = news_title
        
        mars_data['news_paragraph'] = news_p

        return mars_data

    finally:

        browser.quit()

# Image Scrape
def image_scrape():

    try: 

        browser = init_browser()

        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        
        browser.visit(image_url_featured)

        html_image = browser.html

        soup = BS(html_image, 'html.parser')

        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        main_url = 'https://www.jpl.nasa.gov'

        featured_image_url = main_url + featured_image_url

        featured_image_url 

        mars_data['featured_image_url'] = featured_image_url 
        
        return mars_data
    finally:

        browser.quit()

        

# Weather Scrape
def weather_scrape():

    try: 

        browser = init_browser()

        weather_url = 'https://twitter.com/marswxreport?lang=en'
        
        browser.visit(weather_url)

        weather_browser = browser.html

        soup = BS(weather_browser, 'html.parser')

        mars_tweets = soup.find_all('div', class_='js-tweet-text-container')

        for tweet in mars_tweets: 
            weather_tweet = tweet.find('p').text
            if 'Sol' and 'pressure' in weather_tweet:
                print(weather_tweet)
                break
            else: 
                pass

        
        mars_data['weather_tweet'] = weather_tweet
        
        return mars_data
    finally:

        browser.quit()


# Facts Scrape
def facts_scrape():
 
    facts_url = 'http://space-facts.com/mars/'

    mars_facts = pd.read_html(facts_url)

    mars_df = mars_facts[0]
    
    #Drop Earth Stats
    del mars_df['Earth']

    mars_df.columns = ['Description','Value']

    mars_df.set_index('Description', inplace=True)

    
    mars_html = mars_df.to_html()

    
    mars_data['mars_facts'] = mars_html

    return mars_data


# Hemispheres Scrape

def hemispheres_scrape():

    try: 

        browser = init_browser()
 
        hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemi_url)

        hemi_browser = browser.html

        soup = BS(hemi_browser, 'html.parser')

        hemi_items = soup.find_all('div', class_='item')

        hemispheres_url = []

        hemispheres_main_url = 'https://astrogeology.usgs.gov' 
        
        for hemi_item in hemi_items: 
           
            title = hemi_item.find('h3').text
            
            partial_img_url = hemi_item.find('a', class_='itemLink product-item')['href']
            
            browser.visit(hemispheres_main_url + partial_img_url)
             
            partial_img_html = browser.html
            
            soup = BS( partial_img_html, 'html.parser')
            
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            hemispheres_url.append({"title" : title, "img_url" : img_url})

        mars_data['hemispheres_url'] = hemispheres_url

        return mars_data
    finally:

        browser.quit()