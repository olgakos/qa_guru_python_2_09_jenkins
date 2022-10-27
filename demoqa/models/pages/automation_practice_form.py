import os

from selene import have, command
from selene.support.shared import browser
from demoqa.models.controls import dropdown
from demoqa.models.controls.checkbox import select_checkbox
from demoqa.models.controls.radiobutton import select_radiobutton


def open_page(url, resourses):
    browser.config.window_height, browser.config.window_width = 1000, 1000
    browser.open(url + resourses)


def set_first_name(first_name):
    browser.element('#firstName').type(first_name)


def set_last_name(last_name):
    browser.element('#lastName').type(last_name)


def set_email(email):
    browser.element('#userEmail').type(email)


def set_gender(option):
    select_radiobutton('[for^=gender-radio]', option).first.click()


def set_user_number(user_number):
    browser.element('#userNumber').type(user_number)


def set_subject(subject_1, subject_2):
    browser.element('[id="subjectsInput"]').type(subject_1).press_enter() \
        .type(subject_2).press_enter()


def set_hobbies(option, option1):
    select_checkbox('[for^=hobbies-checkbox]', option).first.click()
    select_checkbox('[for^=hobbies-checkbox]', option1).first.click().perform(command.js.scroll_into_view)


def abs_path(relative_path):
    path = os.path.abspath(relative_path)
    return path


def set_photo(photo):
    browser.element('[id="uploadPicture"]').send_keys(abs_path(photo))


def set_address(current_address):
    browser.element('[id="currentAddress"]').type(current_address)


def select_state(state):
    dropdown.select_data(browser.element('#state'), state)


def select_city(city):
    dropdown.select_data(browser.element('#city'), city)


def submit():
    browser.element('#submit').press_enter()


def data_verification(parameter_name):
    browser.element('.table-responsive').should(have.text(parameter_name))