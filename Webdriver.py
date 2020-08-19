from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

class Webdriver():
    """Class using selenium to open a webpage in Firefox with Geckodriver."""

    def __init__(self, url, zoom_recording = False):
        self.url = url
        self.driver = webdriver.Firefox()
        self.zoom_recording = zoom_recording
        self.min_wait = 2
        self.max_wait = 10

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
        """Special function made to get Zoom-url, input necessary data and click buttons to end up in a meeting."""

        self.about_config()

        # Some random waits are used in between, to try to trick Google. 
        self.wait_between()

        # Installed extension (Zoom redirector) to stop Zoom from redirecting to the desktop app. 
        extensions_dir = "/home/ajo/.mozilla/firefox/4b3v1ml0.default-release/extensions/"
        zoom_extension_name = "{2d0a18e8-6b0a-4c8c-9256-6e00c01f07fe}.xpi"

        # Install the extension to the webdriver window. 
        self.driver.install_addon(extensions_dir + zoom_extension_name)

        self.driver.get(self.url)
        
        # Input name in call.
        name = self.driver.find_element_by_xpath('//*[@id="inputname"]')
        name.send_keys("Alex")

        # Bypass reCAPTCHA with Buster extension for Firefox. 
        buster_name = "{e58d3966-3d76-4cd9-8552-1582fbc800c1}.xpi"
        # Need to figure out something to do if Buster does not solve it the first time!! press the retry button until it is solved!
        self.driver.install_addon(extensions_dir + buster_name)
        
        self.wait_between()
        
        # Click "I'm not a robot checkbox".
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[3]/div/div/div/div/div/iframe'))
        checkbox = self.driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]')
        self.driver.implicitly_wait(6) # Wait (a bit longer) to find element. 
        checkbox.click()

        # Use the extension to solve the reCAPTCHA. 
        self.driver.switch_to.default_content()
        #print(len(self.driver.find_elements_by_tag_name("iframe")))
        #self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[3]) 
        self.driver.switch_to.frame(self.driver.find_elements_by_xpath('//*[@title="recaptcha challenge"]')[0])

        self.wait_between()

        self.driver.find_element_by_xpath('//*[@id="solver-button"]').click()

        self.wait_between()

        # Press sound button first.
        #self.driver.find_element_by_xpath('//*[@id=":2"]').click()

        self.wait_between()

        self.driver.find_element_by_xpath('//*[@id="recaptcha-verify-button"]').click()

        self.wait_between()

        self.driver.switch_to.default_content()

        self.driver.implicitly_wait(6) # Wait to find element. 

        # Join button. btn btn-primary btn-block btn-lg submit
        button = self.driver.find_element_by_class_name('submit')
        button.click()

        self.wait_between()

        # Agree to terms of service
        terms = self.driver.find_element_by_xpath('//*[@id="wc_agree1"]')
        terms.click()

        self.wait_between()

        # Need to wait for the following buttons to pop up now! (in case the meeting has not started yet)!

        # Need to paste meeting password and click the join button. (Probably take passcode as a variable from the command line also!)

        # Next page: Join by computer audio.
        audio = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/button')
        audio.click()

        # Then need to confirm browser pop-up for sound! (in the left corner)

        self.wait_between()

        # Open chat.
        chat = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/footer/div/div[2]/button[3]/div/div')
        chat.click()
    
        return self

    def wait_between(self):
        """Used to sleep between clicks, to make interaction more human-like."""
        rand = random.uniform(self.min_wait, self.max_wait)
        time.sleep(rand)

    def about_config(self):
        """Open Firefox about:config and set 'dom.webdriver.enabled' to False."""

        self.driver.get("about:config")

        self.wait_between()

        warning_button = self.driver.find_element_by_xpath('//*[@id="warningButton"]')

        warning_button.click()

        input_field = self.driver.find_element_by_xpath('//*[@id="about-config-search"]')
        input_field.send_keys("dom.webdriver.enabled")

        self.driver.implicitly_wait(3) # Wait to find element. 

        set_false = self.driver.find_element_by_xpath('/html/body/table/tr/th')
        actionChains = ActionChains(self.driver)
        actionChains.double_click(set_false).perform()
