import config
import re

def test_account_and_settings_team_member_payment_and_plan_charging_credit_payment_info_not_display_check(page):
    print("----- 유료 회원(팀멤버) > 결제 및 요금제 > 크레딧 충전하기 / 결제 정보 영역 미노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.TEAM_MEMBER_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.TEAM_MEMBER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("탐색하기 페이지 진입 완료")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("결제 및 요금제").click()
    page.wait_for_timeout(1000)

    assert "크레딧 충전하기" not in page.content(), \
        "결제 및 요금제 > 크레딧 충전하기 타이틀 문구 미노출 확인 실패 - 결제 및 요금제 > 유료 회원(팀멤버) > 크레딧 충전하기 미출력 확인 실패 1"
    assert "결제 정보" not in page.content(), \
        "결제 및 요금제 > 결제 정보 타이틀 문구 미노출 확인 실패 - 결제 및 요금제 > 유료 회원(팀멤버) > 결제 정보 미출력 확인 실패 2"

    print("결제 및 요금제 > 크레딧 충전하기 / 결제 정보 영역 미노출 확인 완료")
    print("----- 유료 회원(팀멤버) > 결제 및 요금제 > 크레딧 충전하기 / 결제 정보 영역 미노출 확인 테스트 시작 -> 성공 -----")
