import pytest
from selene import browser


# test_fixtures.py

@pytest.fixture()
def browser_management_desktop():
    browser.config.window_width = 1600
    browser.config.window_height = 900

    yield

    browser.quit()


@pytest.fixture()
def browser_management_mobile():
    browser.config.window_width = 360
    browser.config.window_height = 800

    yield

    browser.quit()


# test_parametrize.py & test_skip.py
'''
В фикстуре заданы все разрешения, но в test_parametrize indirect параметризация их перезаписывает
При этом в test_skip используются все разрешения фикстуры, но в зависимости от ширины возвращается значение, 
позволяющее пропустить неподходящий тест
'''
@pytest.fixture(params=[(1600, 900), (1900, 1000), (300, 800), (400, 900)])
def browser_management(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width <= 1010:
        yield "mobile"

        browser.quit()
    else:
        yield 'desktop'

        browser.quit()
