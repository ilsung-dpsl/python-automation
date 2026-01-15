import config
import re

def test_MO_signupforfree_change_email_register_check(mobile_page):
    print("----- 4번 - MO 회원가입 변경 > 이메일 등록 확인 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("banner").get_by_role("img").first.tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="무료로 이용해보세요").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 회원가입 변경 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일 주소").fill(config.ENTERPRISE_TEAM_MEMBER_AC)
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="알림 등록").tap()
    mobile_page.wait_for_timeout(1000)

    assert "알림" == mobile_page.get_by_text("알림", exact=True).inner_text(), \
        "MO Web - 회원가입 변경 > 완료 모달 > 타이틀 문구 확인 실패 - 회원가입 변경 > 이메일 등록 확인 실패 1"
    assert "메일이 등록되었습니다." == mobile_page.get_by_text("메일이 등록되었습니다").inner_text(), \
        "MO Web - 회원가입 변경 > 완료 모달 > 가이드 문구 확인 실패 - 회원가입 변경 > 이메일 등록 확인 실패 2"
    assert "확인" == mobile_page.get_by_role("button", name="확인").inner_text(), \
        "MO Web - 회원가입 변경 > 완료 모달 > 확인 버튼 확인 실패 - 회원가입 변경 > 이메일 등록 확인 실패 3"

    print("MO Web - 이메일 등록 완료")

    mobile_page.get_by_role("button", name="확인").tap()
    mobile_page.wait_for_timeout(1000)

    print("----- 4번 - MO 회원가입 변경 > 이메일 등록 확인 테스트 시작 -> 성공-----")