from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

use_step_matcher("parse")


@step('Поставили галочку "{text}"')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    pass


@given('Зашли на сайт "{url}"')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@then("Проверили, что появилось поле поиска")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.driver.find_element_by_id("lst-ib")
        print('Поле поиска найдено!')
    except Exception:
        raise Exception('Not found!!')


@step('В поле "{field_name}" ввели "{text}"')
def step_impl(context, field_name, text):
    """
    :type context: behave.runner.Context
    """
    if field_name.lower() == 'поиск':
        element = context.driver.find_element_by_id("lst-ib")
        element.send_keys(text)


@then('Нажали кнопку "{button_text}"')
def step_impl(context, button_text):
    """
    :type context: behave.runner.Context
    """
    if button_text.lower() == 'enter':
        element = context.driver.find_element_by_id("lst-ib")
        element.send_keys(Keys.RETURN)


@then('Проверили, что открылась страница "{title}"')
def step_impl(context, title):
    """
    :type context: behave.runner.Context
    """
    title = context.driver.title
    print(title)
    assert 'Центральный банк' in title


@then('Нажали на ссылку "{link_text}"')
def step_impl(context, link_text):
    """
    :type context: behave.runner.Context
    """
    element = context.driver.find_element_by_xpath("//a[contains(text(), 'Центральный банк Российской Федерации')]")
    element.click()


@step("Сделали скриншот")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Отправили скриншот на почту "{email}"')
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """
    pass