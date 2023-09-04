"""
Selenium steps to configure behave test scenarios
"""
import time
from selenium.webdriver.common.by import By

@when('visit url "{url}"')
def step(context, url):
    context.driver.get(url)


@when('check if title is "{title}"')
def step(context, title):
    assert context.driver.title == title


@when('field with name "First Item" is present check the box')
def step(context):
    Element_ID1 = context.driver.find_element(By.NAME, "li1").click()
   

@when('field with name "Second Item" is present check the box')
def step(context):
    context.driver.find_element(By.NAME, 'li3').click()


@when('select the textbox add "{text}" in the box')
def step(context, text):
    context.driver.find_element(By.ID, "sampletodotext").click()
    context.driver.find_element(By.ID, "sampletodotext").clear()
    context.driver.find_element(By.ID, "sampletodotext").send_keys(text)


@then('click the "{button}"')
def step(context, button):
    context.driver.find_element(By.ID, "addbutton").click()
