# coding=utf-8
import pytest

from seleniumwrapper import create

@pytest.yield_fixture
def browser():
    driver = create("chrome", executable_path=r'C:\Users\LubovKuznetsova\Desktop\test\chromedriver')
    yield driver
    driver.quit()






