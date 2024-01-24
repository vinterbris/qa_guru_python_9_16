"""
Переопределите параметр с помощью indirect параметризации на уровне теста

2. Есть фикстура, которая параметризована всеми возможными сочетаниями высоты и ширин экранов,
но для десктопа и мобайла переопределяются эти значения конкретными
"""
import pytest
from selene import browser, have


@pytest.mark.parametrize("browser_management", [(1600, 900), (1900, 1000)], indirect=True)
def test_github_desktop(browser_management):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_management", [(300, 800), (400, 900)], indirect=True)
def test_github_mobile(browser_management):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
