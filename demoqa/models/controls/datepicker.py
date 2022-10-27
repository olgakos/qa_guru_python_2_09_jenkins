from selene.support.shared import browser
from selenium.webdriver import Keys

# v1 (ok)
def select_date_of_bday_1(date):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type(date).press_enter()

# v2
def select_date_of_bday_2():
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').element('[value="2022"]').click()
    browser.element('.react-datepicker__month-select').element('[value="9"]').click() #<option value="9">October</option>
    browser.element('.react-datepicker__day--020').click()
    return select_date_of_bday_2()

# v3
# def select_date_of_bday_3(date):
#     browser.element('#dateOfBirthInput').type(date).press_enter()