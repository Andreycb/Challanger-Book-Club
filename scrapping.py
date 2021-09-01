import click

from log import logger
from parsel import Selector
from selenium import webdriver
from const import chrome_headless

def scrap(driver, url):
    logger.info(f'Extraindo html de {url}')

    driver.execute_script(f'window.open("{url}")')
    driver.switch_to.window(driver.window_handles[1])

    selector = Selector(text=driver.page_source)
    breakpoint()

@click.command()
def run():
    with chrome_headless() as driver:
        page = scrap(driver, f'http://books.toscrape.com/')

if __name__ == '__main__':
    run()
