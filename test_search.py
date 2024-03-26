import pytest
from selene import browser, have, be


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://google.com'
    browser.driver.set_window_size(1080, 800)
    browser.open('/')


def test_valid_search():
    browser.element('[name="q"]').should(be.blank).type('qaguru').press_enter()
    browser.element('[id="search"]').should(have.text('QA.GURU'))


def test_invalid_search():
    browser.element('[name="q"]').should(be.blank).type('123sqdfqsdf&^*%*').press_enter()
    browser.element('[id="center_col"]').should(have.text('ничего не найдено.'))
