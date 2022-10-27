from selene import have
from selene.support.shared import browser


def select_data(dropdown, option):
    dropdown.click()
    browser.all('[id^=react-select][id*=-option-]').by(have.exact_text(option)).first.click()