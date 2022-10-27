import allure
from allure_commons.types import Severity
from demoqa.models.controls import datepicker
from demoqa.models.pages.automation_practice_form import *
from utils import attach
from pathlib import Path

def resource(relative_path) -> str:
    path = str(Path(__file__).parent.parent.joinpath('resources').joinpath(relative_path))
    return path


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "OlgaKos")
@allure.description("demoqa")
@allure.feature("Student Registration Form")
@allure.story("Проверка формы регистрации студента")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title('Заполнение формы регистрации')
def test_practice_form():
        with allure.step('Открываем регистрационную форму студента'):
            open_page('https://demoqa.com', '/automation-practice-form')
        with allure.step('Внести анкетные данные'):
            set_first_name('Olga')
            set_last_name('Kos')
            set_email('test@test.uk')
            set_gender('Female')
            set_user_number('0123456789') #10!
            datepicker.select_date_of_bday_1('20 Oct 2022')
            #datepicker.select_date_of_bday_2()
        with allure.step('Учебные предметы и хобби'):
            set_subject('Arts', 'English')
            set_hobbies('Sports', 'Music')
        with allure.step('Добавить изображение'):
            #set_photo('../resources/siegfriedsassoon.jpg')
            #set_photo('siegfriedsassoon.jpg')
            set_photo(resource('siegfriedsassoon.jpg'))
        with allure.step('Добавить адрес'):
            set_address('Peterburg, Moskowsky 16') #simple text
            select_state('Haryana')
            select_city('Karnal')
        with allure.step('Нажать "отправить"'):
            submit()
        with allure.step('Проверить введенные данные'):
            data_verification('Olga Kos')
            data_verification('test@test.uk')
            data_verification('Female')
            data_verification('0123456789')
            data_verification('20 October,2022')
            data_verification('Arts, English')
            data_verification('Sports, Music')
            data_verification('siegfriedsassoon.jpg')
            data_verification('Peterburg, Moskowsky 16')
            data_verification('Haryana Karnal')