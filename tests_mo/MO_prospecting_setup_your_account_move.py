import config
import re

def test_prospecting_setup_your_account_move(mobile_page):
    print("----- 14번 - MO 검색 이력이 없는 신규 가입 사용자일때 Set up your account 노출 (한글) 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PRD2_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PRD2_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="계정 설정하기").tap()

    mobile_page.wait_for_timeout(2000)

    assert "계정 및 설정" in mobile_page.content(), "계정 및 설정 페이지 이동 실패 1"
    assert "내 프로필" in mobile_page.content(), "계정 및 설정 > 내 프로필 이동 실패 2"
    assert "업로드" in mobile_page.content(), "계정 및 설정 > 내 프로필 > 프로필 영역 노출 실패 3"
    assert "최초 등록일 : 2025년 07월 11일" in mobile_page.content(), "계정 및 설정 > 내 프로필 > 최초 등록일 노출 실패 4"

    print("----- 14번 - MO 검색 이력이 없는 신규 가입 사용자일때 Set up your account 노출 (한글) 테스트 시작 -> 성공 -----")