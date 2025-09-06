import config
import re

def test_account_and_settings_team_owner_payment_and_plan_charging_credit_payment_infor_display_check(page):
    print("----- 유료 회원(팀오너) > 결제 및 요금제 > 크레딧 충전하기 / 결제 정보 영역 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.TEAM_OWNER_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.TEAM_OWNER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("탐색하기 페이지 진입 완료")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("결제 및 요금제").click()
    page.wait_for_timeout(1000)

    print("결제 및 요금제 페이지 진입 완료")

    assert "크레딧 충전하기" == page.get_by_text("크레딧 충전하기").inner_text() , \
        "결제 및 요금제 > 크레딧 충전하기 타이틀 문구 노출 확인 실패 - 결제 및 요금제 > 유료 회원(팀오너) > 크레딧 충전하기 영역 출력 확인 실패 1"
    assert True == page.get_by_role("button", name="크레딧 충전").is_visible(), \
        "결제 및 요금제 > [크레딧 충전하기] 버튼 확인 실패 - 결제 및 요금제 > 유료 회원(팀오너) > 크레딧 충전하기 영역 출력 확인 실패 2"
    assert "결제 정보" == page.get_by_text("결제 정보").inner_text(), \
        "결제 및 요금제 > 결제 정보 타이틀 문구 노출 확인 실패 - 결제 및 요금제 > 유료 회원(팀오너) > 결제 정보 영역 출력 확인 실패 3"
    assert "카드 등록하기" == page.get_by_text("카드 등록하기").inner_text(), \
        "결제 및 요금제 > 결제 정보 > 카드 등록하기 문구 노출 확인 실패 - 결제 및 요금제 > 유료 회원(팀오너) > 결제 정보 영역 출력 확인 실패 4"

    print("결제 및 요금제 > 크레딧 충전하기 / 결제 정보 영역 노출 확인 완료")
    print("----- 유료 회원(팀오너) > 결제 및 요금제 > 크레딧 충전하기 / 결제 정보 영역 노출 확인 테스트 시작 -> 성공 -----")