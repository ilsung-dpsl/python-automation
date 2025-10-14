import config
import re

def test_login(page):
    print("--- 3번 - 로그인 테스트 시작 ---")
    page.goto("https://deepsales.com/ko/search",wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(5000)
  #  page.get_by_role("button", name="Start Now").click()
  #  page.wait_for_timeout(1000)

    assert "왼쪽 메뉴에서 필터를 선택하여 회사 검색을 시작하세요." in page.content(), "로그인 후 탐색하기 페이지 이동 실패 - 로그인 실패 1"

    #20250926 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    #20250926 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    #20250926 - LNB > 대시보드 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="대시보드").nth(1).click()
    page.wait_for_timeout(2000)

    page.get_by_text("BAEK ILSUNG님 환영합니다!").click()

    assert "BAEK ILSUNG님" in page.content(), "대시보드: 환영문구 확인 -> 로그인 실패"
    print("--- 로그인 테스트 완료 -> 성공 ---")




