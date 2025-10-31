import config
import re

def test_signupforfree_change_email_register_check(page):
    print("----- 79번 - 회원가입 변경 > 이메일 등록 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="무료로 시작하기").get_by_role("button").click()
    page.wait_for_timeout(1000)

    print("회원가입 변경 페이지 진입 완료")

    page.get_by_placeholder("이메일 주소").fill(config.ENTERPRISE_TEAM_MEMBER_AC)
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="알림 등록").click()
    page.wait_for_timeout(1000)

    assert "알림" == page.get_by_text("알림", exact=True).inner_text(), \
        "회원가입 변경 > 완료 모달 > 타이틀 문구 확인 실패 - 회원가입 변경 > 이메일 등록 확인 실패 1"
    assert "메일이 등록되었습니다." == page.get_by_text("메일이 등록되었습니다").inner_text(), \
        "회원가입 변경 > 완료 모달 > 가이드 문구 확인 실패 - 회원가입 변경 > 이메일 등록 확인 실패 2"
    assert "확인" == page.get_by_role("button", name="확인").inner_text(), \
        "회원가입 변경 > 완료 모달 > 확인 버튼 확인 실패 - 회원가입 변경 > 이메일 등록 확인 실패 3"

    print("이메일 등록 완료")

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("----- 79번 - 회원가입 변경 > 이메일 등록 확인 테스트 시작 -> 성공-----")



