import re
import config

def test_MO_price_upgrade_to_the_pro_plan_payment_check(mobile_page):
    print("---- 8번 - MO 요금제 업그레이드 결제 > 결제 전까지 동작 확인 테스트 시작 ----")

    # 20251125 - 할인 가격 페이지 삭제로 인해, 일반 가격 페이지 url 변경되어 코드 수정
    mobile_page.goto("https://deepsales.com/ko/pricing", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA45_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA45_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").click(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 가격 페이지 진입 완료")

    # 20251125 - 일반 가격 페이지 > Pro > [플랜 변경하기] 버튼 선택 엘리먼트 코드로 수정
    mobile_page.locator("div").filter(has_text=re.compile(r"^Pro\$39플랜 변경하기$")).get_by_role("button").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - Pro로 업그레이드 결제 페이지 진입 완료")

    mobile_page.get_by_placeholder("카드 번호").tap()
    mobile_page.wait_for_timeout(500)
    mobile_page.keyboard.type(config.CARD2_CARD_NO, delay=100)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_placeholder("MM/YY").fill(config.CARD2_VALID_THRU)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_placeholder("CVC를 입력하세요").fill(config.CARD2_CVC_NO)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_placeholder("카드 소지자명을 입력하세요").fill(config.CARD2_CONSUMER_NAME)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_text("결제를 진행하는 모든 조건들에 동의합니다").tap()
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("checkbox", name="결제를 진행하는 모든 조건들에 동의합니다").tap()
    mobile_page.wait_for_timeout(1000)

    assert "4242 - 4242 - **** - ****" == mobile_page.get_by_placeholder("카드 번호").input_value(), \
        "MO Web - Pro 업그레이드 > 입력한 카드 번호 일부 마스킹 처리 노출 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 1"
    assert "12/30" == mobile_page.get_by_placeholder("MM/YY").input_value(), \
        "MO Web - Pro 업그레이드 > 월/년 정상 입력 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 2"
    assert "123" == mobile_page.get_by_placeholder("CVC를 입력하세요").input_value(), \
        "MO Web - Pro 업그레이드 > CVC 정상 입력 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 3"
    assert "BAEKILSUNG" == mobile_page.get_by_placeholder("카드 소지자명을 입력하세요").input_value(), \
        "MO Web - Pro 업그레이드 > 카드 소지자명 입력 확인 실패 - 요금제 업그레이드 결제 > 결제 전까지 동작 확인 4"

    print("MO Web - Pro 업그레이드 > 입력값 확인 완료")
    print("---- 8번 - MO 요금제 업그레이드 결제 > 결제 전까지 동작 확인 테스트 시작 -> 성공 ----")