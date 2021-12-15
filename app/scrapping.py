import click
from time import sleep
from log import logger
from parsel import Selector
from selenium import webdriver
from const import chrome_headless
from selenium.common.exceptions import NoSuchElementException
from settings import ROOT_PROJECT
import os

def get_categories(driver, url):
    logger.info(f'Extraindo html de {url}')

    driver.execute_script(f'window.open("{url}")')
    driver.switch_to.window(driver.window_handles[1])

    
    links_categories = []
    links_categories = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_xpath("//ul[@class='nav nav-list']/li/ul/li/a")]
    
    return links_categories


def get_books(driver, link):
    while True:
        driver.get(link)
        title_categorie = driver.find_element_by_xpath("//div[@class='page-header action']/h1").text
        
        links_books = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_xpath("//article[@class='product_pod']/h3/a")]
        save_html_books(driver, links_books, title_categorie)
        try:
            next_page = driver.find_element_by_xpath("//li[@class='next']/a")
            link = next_page.get_attribute('href')
            get_books(driver, link)
        except NoSuchElementException:
            break


def save_html_books(driver, links_books, title_categorie):
    for book in links_books:
        driver.get(book)
        path_save = f'{ROOT_PROJECT}/books/{title_categorie}'

        title_book = driver.find_element_by_xpath("//div[@class='col-sm-6 product_main']/h1").text

        if not os.path.exists(path_save):
            os.makedirs(path_save)

        if not os.path.exists(f"{path_save}/{title_book}"):
            with open(f"{path_save}/{title_book}", "w") as f:
                f.write(driver.page_source)

@click.command()
def run():
    with chrome_headless() as driver:
        categories = get_categories(driver, f'http://books.toscrape.com/')
        for i in categories:
            get_books(driver, i)


if __name__ == '__main__':
    run()
