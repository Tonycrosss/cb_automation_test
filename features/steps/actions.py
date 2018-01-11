from behave import *

use_step_matcher("re")


@given('Зашли на сайт "www\.google\.ru"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass