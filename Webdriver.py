

from selenium import webdriver 

class Webdriver():
    """Class using selenium to open a webpage in Firefox with Geckodriver."""

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    def get_url(self):
        "Get url via Firefox driver and open the url in browser."
        self.driver.get(self.url)
        return self

    def set_fullscreen(self):
        "Set browser to fullscreen."
        self.driver.maximize_window()
