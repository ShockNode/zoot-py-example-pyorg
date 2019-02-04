from pages import home
from env import automation
 
from zoot.bdd.decorators import step, given, when, then

import time

@given("I navigate to (?P<page>.*)")
def navigation(**kwargs):

    if kwargs['page'] == "Python homepage":
        err = home.to(automation.get_driver())
        if err: raise err
        automation.set_current_page(home)

@given("I wait (?P<seconds>\d+) second\(s\)")
def wait(**kwargs):
    if int(kwargs['seconds']) >= 0:
        time.sleep(int(kwargs['seconds']))

@then("I close the driver")
def close(**kwargs):
    automation.get_driver().close()








