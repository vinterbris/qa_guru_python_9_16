"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture()
def browser_managment_desktop():
    browser.config.window_width = 1600
    browser.config.window_height = 900


@pytest.fixture()
def browser_managment_mobile():
    browser.config.window_width = 360
    browser.config.window_height = 800


def test_github_desktop(browser_managment_desktop):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in')


def test_github_mobile(browser_managment_mobile):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in')
