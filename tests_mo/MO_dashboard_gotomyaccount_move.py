import config
import re

def test_MO_dashboard_gotomyaccount_move(mobile_page):
    print("----- 13번 - MO Web > Go to my account 버튼 클릭 시, Account & Setting > My account로 이동 테스트 시작 (한글) -----")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("link").filter(has_text="대시보드").tap(timeout=10000)
    mobile_page.wait_for_timeout(5000)

    mobile_page.get_by_text("내 계정으로 이동하기 >").click()
    mobile_page.wait_for_timeout(2000)

    assert "계정 및 설정" in mobile_page.content(), "계정 및 설정 페이지 이동 실패 1"
    assert "내 프로필" in mobile_page.content(), "계정 및 설정 > 내 프로필 이동 실패 2"
    assert "업로드" in mobile_page.content(), "계정 및 설정 > 내 프로필 > 프로필 영역 노출 실패 3"
    assert "최초 등록일 : 2025년 03월 24일" in mobile_page.content(), "계정 및 설정 > 내 프로필 > 최초 등록일 노출 실패 4"

    print("----- 13번 - MO Web > Go to my account 버튼 클릭 시, Account & Setting > My account로 이동 테스트 시작 (한글) -> 성공 -----")