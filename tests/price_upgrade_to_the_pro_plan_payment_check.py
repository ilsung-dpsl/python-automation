import re
import config

def test_price_upgrade_to_the_pro_plan_payment_check(page):
    print("---- 9번 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 테스트 시작 ----")

    page.goto("https://deepsales.com/ko/pricing/sale")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA45_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA45_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.locator("div").filter(has_text=re.compile(r"^Pro\$39\$19\.5-50%플랜 변경하기$")).get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("카드 번호").click()
    page.wait_for_timeout(500)
    page.keyboard.type("4242424242424242", delay=100)
    page.wait_for_timeout(500)
    page.get_by_placeholder("MM/YY").fill("12/30")
    page.wait_for_timeout(500)
    page.get_by_placeholder("CVC를 입력하세요").fill("123")
    page.wait_for_timeout(500)
    page.get_by_placeholder("카드 소지자명을 입력하세요").fill("BAEKILSUNG")
    page.wait_for_timeout(500)
    page.get_by_text("결제를 진행하는 모든 조건들에 동의합니다").click()
    page.wait_for_timeout(500)
    page.get_by_role("checkbox", name="결제를 진행하는 모든 조건들에 동의합니다").click()
    page.wait_for_timeout(500)

    assert "4242 - 4242 - **** - ****" == page.get_by_placeholder("카드 번호").input_value(), \
        "Pro 업그레이드 > 입력한 카드 번호 일부 마스킹 처리 노출 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 1"
    assert "12/30" == page.get_by_placeholder("MM/YY").input_value(), \
        "Pro 업그레이드 > 월/년 정상 입력 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 2"
    assert "123" == page.get_by_placeholder("CVC를 입력하세요").input_value(), \
        "Pro 업그레이드 > CVC 정상 입력 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 3"
    assert "BAEKILSUNG" == page.get_by_placeholder("카드 소지자명을 입력하세요").input_value(), \
        "Pro 업그레이드 > 카드 소지자명 입력 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 4"

    print("Pro 업그레이드 > 입력값 확인 완료")

    print("---- 9번 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 테스트 시작 -> 성공 ----")