from selene import have
from selene.support.shared import browser

# 1
def select_radiobutton(element, option):
    return browser.all(element).by(have.exact_text(option))

#2
# def select_radiobutton(self, option):
#         browser.all('[for^=gender-radio]').by(have.exact_text(option)).first.click()
#         return self

#3
# def select_radiobutton(option):
#     browser.all('[for^=gender-radio]').by(have.exact_text(option)).first.click()