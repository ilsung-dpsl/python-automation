import pytest
from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import device


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1440, "height": 900},  # 원하는 뷰포트 크기
    }

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=300)
    yield browser
    browser.close()

@pytest.fixture
def page(browser, browser_context_args):
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    context.close()

# 2026.1.6 - MO_Web 테스트를 위한 안드로이드 모바일용 셋팅
@pytest.fixture
def mobile_page(browser, playwright_instance):
    device = playwright_instance.devices["Galaxy S24"]

    context = browser.new_context(
        **device,
        locale="ko-KR"
    )

    page = context.new_page()
    page.set_default_timeout(10_000)

    yield page
    context.close()
