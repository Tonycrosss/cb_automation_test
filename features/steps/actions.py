from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

use_step_matcher("parse")


@step('Поставили галочку "{text}"')
def step_impl(context, text):
    pass


@given('Зашли на сайт "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@then("Проверили, что появилось поле поиска")
def step_impl(context):
    try:
        context.driver.find_element_by_id("lst-ib")
        print('Поле поиска найдено!')
    except Exception:
        raise Exception('Not found!!')


@step('В поле "{field_name}" ввели "{text}"')
def step_impl(context, field_name, text):
    if field_name.lower() == 'поиск':
        element = context.driver.find_element_by_id("lst-ib")
        element.send_keys(text)


@then('Нажали кнопку "{button_text}"')
def step_impl(context, button_text):
    if button_text.lower() == 'enter':
        element = context.driver.find_element_by_id("lst-ib")
        element.send_keys(Keys.RETURN)


@then('Проверили, что открылась страница "{title}"')
def step_impl(context, title):
    title = context.driver.title
    print(title)
    assert 'Центральный банк' in title


@then('Нажали на ссылку "{link_text}"')
def step_impl(context, link_text):
    element = context.driver.find_element_by_xpath("//a[contains(text(),"
                                                   " '{}')]".format(link_text))
    element.click()


@step("Сделали скриншот")
def step_impl(context):
    pass


@then('Отправили скриншот на почту "{email}"')
def step_impl(context, email):
    pass
