import os

ROOT_PROJECT = os.path.dirname(os.path.abspath("__file__"))
CHROME_PATH = os.getenv('CHROME_PATH', 'chromedriver')
USE_CHROME_HEADLESS = os.getenv('USE_CHROME_HEADLESS', '0') == '1'