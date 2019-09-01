# Dependencies

from bs4 import BeautifulSoup

from splinter import Browser

import pandas as pd

import time


# Function to initialize Splinter browser

def init_browser():

    executable_path = {'executable_path': "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"}

    return Browser("chrome", **executable_path, headless=False)

