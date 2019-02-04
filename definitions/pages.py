from zoot.automation.elements import Locator
from zoot.automation.pages import Page, PageInfo

home = Page(PageInfo("Home", "https://python.org", True, 30), {"Logo":Locator("Logo", "xpath", "//img[@class='python-logo']", True)}, None)