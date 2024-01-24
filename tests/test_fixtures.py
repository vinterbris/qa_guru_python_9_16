"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser, have


def test_github_desktop(browser_management_desktop):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_management_mobile):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))