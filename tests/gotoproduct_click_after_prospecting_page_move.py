import re

import config


def test_gotoproduct_click_after_prospecting_page_move(page):
        print("---- 제품 이용하기 페이지 이동 확인 케이스 시작 ----")
        page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(1000)
        page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
        page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Start Now").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
        page.get_by_role("button", name="제품 이용하기").click()

        page.wait_for_timeout(2000)
        assert "왼쪽 메뉴에서 필터를 선택하여 회사 검색을 시작하세요" in page.content(), "탐색하기 페이지 이동에 실패했습니다."

        print("---- 제품 이용하기 페이지 이동 확인 -> 성공 ----")

