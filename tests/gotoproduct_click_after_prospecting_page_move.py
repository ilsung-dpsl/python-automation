import re

import config


def test_gotoproduct_click_after_prospecting_page_move(page):
        print("---- 7번 - 제품 이용하기 페이지 이동 확인 케이스 시작 ----")
        page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(1000)
        page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
        page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
        page.get_by_role("button", name="로그인").click()
       # page.wait_for_timeout(1000)
       # page.get_by_role("button", name="Start Now").click()
        page.wait_for_timeout(1000)

        # 20250929 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
        lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
        lnb_hover_target.hover()
        page.wait_for_timeout(2000)

        # 20250929 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
        page.get_by_role("button").first.click()
        page.wait_for_timeout(2000)

        page.get_by_role("link").filter(has_text=re.compile(r"^$")).nth(1).click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="제품 이용하기").click()

        page.wait_for_timeout(2000)
        assert "왼쪽 메뉴에서 필터를 선택하여 회사 검색을 시작하세요" in page.content(), "탐색하기 페이지 이동에 실패했습니다."

        print("---- 제품 이용하기 페이지 이동 확인 -> 성공 ----")

