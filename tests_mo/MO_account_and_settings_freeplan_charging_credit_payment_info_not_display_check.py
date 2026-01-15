import config
import re

def test_MO_account_and_settings_freeplan_charging_credit_payment_info_not_display_check(mobile_page):
    print("----- 58번 - MO 무료회원(유료 결제 내역 있음) > 크레딧 충전하기 / 결제정보 미노출 확인 테스트 시작 -----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 페이지 진입 완료")

    #20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    mobile_page.get_by_role("button").nth(2).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_text("결제 및 요금제").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 결제 및 요금제 진입 완료")

    assert "크레딧 충전하기" not in mobile_page.content(), \
        "MO Web - 결제 및 요금제 > 크레딧 충전하기 타이틀 문구 미노출 확인 실패 - 결제 및 요금제 > 무료 회원 > 크레딧 충전하기 미출력 확인 실패 1"
    assert "결제 정보" not in mobile_page.content(), \
        "MO Web - 결제 및 요금제 > 결제 정보 타이틀 문구 미노출 확인 실패 - 결제 및 요금제 > 무료 회원 > 결제 정보 미출력 확인 실패 2"

    print("MO Web - 결제 및 요금제 > 크레딧 충전하기 / 결제 정보 영역 미노출 확인 완료")
    print("----- 58번 - MO 무료회원(유료 결제 내역 있음) > 크레딧 충전하기 / 결제정보 미노출 확인 테스트 시작 -----")
