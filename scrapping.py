import click
from time import sleep
from log import logger
from parsel import Selector
from selenium import webdriver
from const import chrome_headless


def get_categories(driver, url):
    logger.info(f'Extraindo html de {url}')

    driver.execute_script(f'window.open("{url}")')
    driver.switch_to.window(driver.window_handles[1])

    categories = driver.find_elements_by_xpath("//ul[@class='nav nav-list']/li/ul/li/a")
    links_categories = []

    for i in categories:
        links_categories.append(i.get_attribute('href'))

    for link in links_categories:
        driver.execute_script(f'window.open("{link}")')
        
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        breakpoint()
@click.command()
def run():
    with chrome_headless() as driver:
        pages = get_categories(driver, f'http://books.toscrape.com/')


if __name__ == '__main__':
    run()
