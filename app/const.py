from log import logger
from selenium import webdriver
from settings import CHROME_PATH, USE_CHROME_HEADLESS

class chrome_headless():
    def __enter__(self):
        logger.info('Opening browser')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        if USE_CHROME_HEADLESS:
            options.add_argument('--headless')

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        self.driver.maximize_window()

        return self.driver

    def __exit__(self, *exc):
        logger.info('Closed browser')
        self.driver.quit()
