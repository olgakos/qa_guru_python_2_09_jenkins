from selene import have
from selene.support.shared import browser


def select_checkbox(element, option):
    return browser.all(element).by(have.exact_text(option))