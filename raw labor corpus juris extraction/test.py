from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, InvalidSelectorException
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests
from urllib.error import URLError, HTTPError

import pandas as pd

from typing import Union


# USING SELENIUM

# collects and returns links and link texts of page
def collect_link_details(driver: webdriver.Chrome, link: str, link_selector: str) -> pd.DataFrame:
    try:
        driver.get(link)
        wait_val = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))

        # narrow down using selector 
        content = driver.find_element(By.CSS_SELECTOR, link_selector)
        links = content.find_elements(By.TAG_NAME, "a")

        # collect link texts and hrefs
        link_texts = []
        link_hrefs = []
        for link in links:
            # extract href of link through get dom attribute
            # extract text of link through self.text
            link_hrefs.append(link.get_attribute('href'))
            link_texts.append(link.text)
        return pd.DataFrame({'link_text': link_texts, 'href': link_hrefs})
    except TimeoutError as error:
        print("Error {} has occured".format(error))


# collects and returns link, headers, and text content of page
def collect_content(driver: webdriver.Chrome, links: list[str], header_selector: str, text_content_selector: str, threshold: int=128) -> pd.DataFrame:
    page_headers = []
    page_text_content = []
    accepted = []
    rejects = []
    for link in links:
        # otherwise if the callback does not return a true value and time
        # period is up, then WebDriverWait raises a timeout error
        try:
            driver.get(link)
            wait_val = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))
            print("Wait value: {}\nPage title: {}\n".format(wait_val, driver.title))
            
            # grab html elements that contain important header content
            # exhaust the list returned by appending
            header = " ".join([element.text for element in driver.find_elements(By.CSS_SELECTOR, header_selector)])
            
            # display header
            print("\033[92m {}\033[00m".format("Header: {}\n".format(header)))

            # grab a single html element only since it cannto be generalized 
            # across multiple pages since the structure may change and some
            # elements may not be grabbed
            text_content = driver.find_element(By.CSS_SELECTOR, text_content_selector)

            # display text content
            print("\033[96m {}\033[00m".format("Text content: {}\nLength: {}\n\n".format(text_content.text, len(text_content.text))))

            # raise error if text dom.select_one() returns None
            if text_content is None or len(text_content.text) <= threshold:
                raise ValueError('dom.select_one returned none for link due to text content selector or length of text content is below threshold'.format(link))
            
            # store accepted headers and text content
            page_headers.append(header)
            page_text_content.append(text_content.text)

            # append if no error is raised
            accepted.append(link)
            
        except TimeoutError as error:
            print("Error {} has occured".format(error))
            driver.quit() # or .close()

        # catch both NoSuchElementException and StaleElementReferenceException errors
        except (NoSuchElementException, StaleElementReferenceException) as error:
            print("Error {} has occured".format(error))
            rejects.append(link)

        # catch threshold error if length of content is below 
        # certain threshold value
        except ValueError as error:
            print("Error: {} has occured".format(error))
            rejects.append(link)

        finally:
            print("will go to next link")

    print("number of total links: {}\nnumber of accepted links: {}\nnumber of reject links: {}\n".format(len(links), len(accepted), len(rejects)))
    print(accepted, end='\n')
    print(rejects, end='\n')

    # place text in data frame if no error is raised
    return pd.DataFrame({'page_link': accepted, 'page_header': page_headers, 'page_text_content': page_text_content})


# collects and returns link, headers, and text content of page individually
def collect_content_individually(driver: webdriver.Chrome, link: str, locator: str='CSS', header_selector: str='N/A', text_content_selector: str='N/A') -> Union[list, None]:
    header = ""
    text_content = ""

    locators = {
        'CSS': By.CSS_SELECTOR,
        'XPATH': By.XPATH
    } 

    try:
        driver.get(link)
        wait_val = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))
        print("Wait value: {}\nPage title: {}\n".format(wait_val, driver.title))
        
        
        if header_selector != 'N/A':
            # grab html elements that contain important header content
            # exhaust the list returned by appending
            header = " ".join([element.text for element in driver.find_elements(locators[locators[locator.upper()]], header_selector)])

        if text_content_selector != 'N/A':
            # grab a single html element only since it cannto be generalized 
            # across multiple pages since the structure may change and some
            # elements may not be grabbed
            text_content = driver.find_element(locators[locator.upper()], text_content_selector)
            print("Header: {}\nText content: {}\n\n".format(header, text_content.text))
        
        return [header, text_content]

        
    except TimeoutError as error:
        print("Error {} has occured".format(error))
        driver.quit() # or .close()
        return None

    # catch both NoSuchElementException and StaleElementReferenceException errors
    except (NoSuchElementException, StaleElementReferenceException, InvalidSelectorException) as error:
        print("Error {} has occured".format(error))
        return None

    finally:
        print("will go to next link")
    

# USING BEAUTIFUL SOUP

# collects link details 
def collect_link_details_bs(link: str, selector: str) -> pd.DataFrame:
    # store all link text and hrefs for dataframe
    link_texts = []
    link_hrefs = []

    try:
        # open page
        dom_text = requests.get(link).text
        dom = BeautifulSoup(dom_text)        

        # using css selector, like class, id, attribute etc, grab the
        # subtree in the dom that contains all the links then extract all a elements
        links_container = dom.select_one(selector)
        for a_element in links_container.find_all('a'):
            # get text and href of each a element
            link_hrefs.append(a_element['href'])
            link_texts.append(a_element.get_text())

    # raise a URLError or HTTPError if url pattern is invalid
    # or if url does not exist in the server respectively
    except (URLError, HTTPError) as error:
        print("Error {} has occured".format(error))

    return pd.DataFrame({'link_text': link_texts, 'href': link_hrefs})


# collects and returns link, headers, and text content of page
def collect_content_bs(links: list[str], header_selector: str, text_content_selector: str) -> pd.DataFrame:
    page_headers = []
    page_text_content = []
    accepted = []
    rejects = []
    
    for link in links:
        try:
            # open page, and raise a URLError exception if url entered is
            # not valid, and similarly an HTTPError if the url is in fact
            # valid but the url does not exist in the server
            dom_text = requests.get(link).text
            dom = BeautifulSoup(dom_text, 'lxml')
            
            # grab html elements that contain important header content
            # exhaust the list returned by appending
            header = " ".join([element.get_text() for element in dom.select(header_selector)]) if dom.select(header_selector) != [] else None
            if header is None:
                raise ValueError('dom.select() returned an empty list for link {} due to header selector'.format(link))

            # grab a single html element only since it cannto be generalized 
            # across multiple pages since the structure may change and some
            # elements may not be grabbed
            text_content = dom.select_one(text_content_selector)
            if text_content is None:
                raise ValueError('dom.select_one returned none for link due to text content selector'.format(link))

            # display header and text content
            print("Header: {}\nText content: {}\n\n".format(header, text_content.get_text()))
            
            # store accepted headers and text content
            page_headers.append(header)
            page_text_content.append(text_content.get_text())

            # append if no error is raised
            accepted.append(link)
            
        # raise a URLError or HTTPError if url pattern is invalid
        # or if url does not exist in the server respectively
        except (URLError, HTTPError) as error:
            print("Error: {} has occured".format(error))

        except ValueError as error:
            print("Error: {} has occured".format(error))
            rejects.append(link)

        finally:
            print("will go to next link")

    print("number of total links: {}\nnumber of accepted links: {}\nnumber of reject links: {}\n".format(len(links), len(accepted), len(rejects)))
    print("accepted links: ", accepted, end='\n')
    print("rejected links: ", rejects, end='\n')

    # place text in data frame if no error is raised
    return pd.DataFrame({'page_link': accepted, 'page_header': page_headers, 'page_text_content': page_text_content})


# collect content individually
def collect_content_individually_bs(content: str) -> str:
    return BeautifulSoup(content, 'lxml').get_text()


def get_page_text_content_length(page_details: pd.DataFrame) -> list[tuple]:
    return [(index, len(page_text_content)) for index, page_text_content in enumerate(page_details['page_text_content'])]