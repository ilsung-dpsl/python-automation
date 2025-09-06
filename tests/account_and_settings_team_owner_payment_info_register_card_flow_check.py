import config
import re

def test_account_and_settings_team_owner_payment_info_register_card_flow_check(page):
    print("----- 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 카드 등록하기 플로우 확인 테스트 시작 (등록 전까지만 확인 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("결제 및 요금제").click()
    page.wait_for_timeout(1000)

    page.locator(".rounded-\\[8px\\].p-2.bg-Surface-Default-a").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("카드 번호").click()
    page.keyboard.type("4242424242424242", delay=100)

    page.wait_for_timeout(1000)

    page.get_by_placeholder("MM/YY").click()
    page.get_by_placeholder("MM/YY").fill("12/30")
    page.wait_for_timeout(500)

    page.get_by_placeholder("CVC를 입력하세요").click()
    page.get_by_placeholder("CVC를 입력하세요").fill("169")
    page.wait_for_timeout(500)

    page.get_by_placeholder("카드 소지자명을 입력하세요").click()
    page.get_by_placeholder("카드 소지자명을 입력하세요").fill("BAEKILSUNG")
    page.wait_for_timeout(500)

    button = page.locator("button:has-text('등록')")
    pointer_events = button.evaluate("el => getComputedStyle(el).pointerEvents")

    assert "4242 - 4242 - **** - ****" == page.get_by_placeholder("카드 번호").input_value(), \
        "카드 등록하기 모달 > 카드 번호 입력 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 1"
    assert "12/30" ==  page.get_by_placeholder("MM/YY").input_value(), \
        "카드 등록하기 모달 > 유효 기간 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 2"
    assert "169" == page.get_by_placeholder("CVC를 입력하세요").input_value(), \
        "카드 등록하기 모달 > CVC 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 3"
    assert "BAEKILSUNG" == page.get_by_placeholder("카드 소지자명을 입력하세요").input_value(), \
        "카드 등록하기 모달 > 카드 소지자명 확인 실패 - 유료 회원(팀오너) > 카드 등록하ㅣㄱ 플로우 실패 4"
    assert "none" != pointer_events, \
        "카드 등록하기 모달 > 등록 클릭 가능 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 5"

    print("카드 등록하기 모달 > 입력값 확인 완료")

    page.get_by_role("button", name="취소").click()
    page.wait_for_timeout(1000)

    print("----- 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 카드 등록하기 플로우 확인 테스트 시작 (등록 전까지만 확인 -----")

