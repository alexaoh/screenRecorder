from selenium import webdriver

class Webdriver():
    """Class using selenium to open a webpage in Firefox with Geckodriver."""

    def __init__(self, url, zoom_recording = False):
        self.url = url
        self.driver = webdriver.Firefox()
        self.zoom_recording = zoom_recording

    def get_url(self):
        """Get url via Firefox driver and open the url in browser."""
        if not self.zoom_recording:
            self.driver.get(self.url)
        else:
            self.zoom()

        return self

    def set_fullscreen(self):
        """Set browser to fullscreen."""
        self.driver.maximize_window()
        return self

    def close_driver(self):
        "Closes driver when no longer needed."
        self.driver.close()
        self.driver.quit()

    def zoom(self):
        """Special function made to get Zoom-url, input necessary data and click buttons to end up in a meeting."""\
        
        driver = self.driver

        # Installed extension (Zoom redirector) to stop Zoom from redirecting to the desktop app. 
        zoom_extension_dir = "/home/ajo/.mozilla/firefox/4b3v1ml0.default-release/extensions/"
        extension_name = "{2d0a18e8-6b0a-4c8c-9256-6e00c01f07fe}.xpi"

        # Install the extension to the webdriver window. 
        driver.install_addon(zoom_extension_dir + extension_name)

        driver.get(self.url)
        
        # Input name in call.
        name = driver.find_element_by_xpath('//*[@id="inputname"]')
        name.send_keys("Alex")

        # Now we are stuck at the Captcha!? Solve this how!?
        '''
        # Click "I'm not a robot checkbox".
        checkbox = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]')
        checkbox.click()
        
        # Bypass Captcha.

        # Submit.
        button = driver.find_element_by_xpath('/*[@id="joinBtn"]')
        button.click()

        # Next page: Join by computer audio.
        audio = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/button')
        audio.click()

        # Open chat.
        chat = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/footer/div/div[2]/button[3]/div/div')
        chat.click()
        '''
        return self
