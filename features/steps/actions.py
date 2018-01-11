from behave import *

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
    pass


@then("Проверили, что появилось поле поиска")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('В поле "{field_name}" ввели "{text}"')
def step_impl(context, field_name, text):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Нажали кнопку "{button_text}"')
def step_impl(context, button_text):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Нажали на первую ссылку")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Проверили, что открылась страница "{title}"')
def step_impl(context, title):
    """
    :type context: behave.runner.Context
    """
    pass


@then('Нажали на ссылку "{link_text}"')
def step_impl(context, link_text):
    """
    :type context: behave.runner.Context
    """
    pass


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