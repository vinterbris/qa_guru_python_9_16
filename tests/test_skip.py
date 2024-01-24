"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


@pytest.fixture()
def desktop():
    return 1920, 1080


@pytest.fixture()
def mobile():
    return 360, 800


@pytest.fixture()
def browser_management(request):
    if request.param == "desktop":
        return request.getfixturevalue("desktop")
    if request.param == "mobile":
        return request.getfixturevalue("mobile")

@pytest.mark.parametrize("browser_management",
                         [
                             pytest.param("desktop"),
                             pytest.param("mobile", marks=[pytest.mark.skip(reason="not testing mobile")]),
                         ],
                         indirect=True)
def test_github_desktop(browser_management):
    browser.config.window_width = browser_management[0]
    browser.config.window_height = browser_management[1]
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in')

@pytest.mark.parametrize("browser_management",
                         [
                             pytest.param("desktop", marks=[pytest.mark.skip(reason="not testing desktop")]),
                             pytest.param("mobile"),
                         ],
                         indirect=True)
def test_github_mobile(browser_management):
    browser.config.window_width = browser_management[0]
    browser.config.window_height = browser_management[1]
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in')
