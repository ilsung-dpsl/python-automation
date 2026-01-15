import config
import re

def test_MO_login(mobile_page):
    print("--- 5번 - MO 로그인 테스트 시작 ---")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    # mobile_page.locator("iframe[name=\"intercom-notification-stack-frame\"]").content_frame.locator("html").tap()

    # mobile_page.get_by_role("button", name="로그인").tap()
    # mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(5000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 페이지 진입 완료")

    assert "왼쪽 메뉴에서 필터를 선택하여 회사 검색을 시작하세요." in mobile_page.content(), \
        "MO Web - 로그인 후 탐색하기 페이지 이동 실패 - 로그인 실패 1"

    #lnb_hover_target = mobile_page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    #lnb_hover_target.hover()
    #mobile_page.wait_for_timeout(2000)

    # 20250926 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    #mobile_page.get_by_role("button").first.tap()
    #mobile_page.wait_for_timeout(2000)

    # 20250926 - LNB > 대시보드 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    #mobile_page.get_by_role("link", name="대시보드").nth(1).tap()
    mobile_page.get_by_role("link").filter(has_text="대시보드").tap()
    mobile_page.wait_for_timeout(2000)

    print("MO Web - 대시보드 진입 완료")

    mobile_page.get_by_text("BAEK ILSUNG님 환영합니다!").tap(timeout=10000)

    assert "BAEK ILSUNG님" in mobile_page.content(), \
        "MO Web - 대시보드: 환영문구 확인 -> 로그인 실패"
    print("--- 5번 - MO 로그인 테스트 완료 -> 성공 ---")

