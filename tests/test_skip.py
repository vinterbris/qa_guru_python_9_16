"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)

3. Параметризовать всеми возможными ситуациями и в тесте если получили не подходящее сочетание,
то пропускаем тест
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1600, 900), (1900, 1000), (300, 800), (400, 900)])
def bparam(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


def test_github_desktop(browser_management):
    if browser_management == 'mobile':
        pytest.skip('Not a mobile resolution')
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_management):
    if browser_management == 'desktop':
        pytest.skip('Not a desktop resolution')
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
