import re
import config

def test_salesagent_start_counseling_register_check(page):
    print("---- 84번 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 ----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("banner").get_by_role("link", name="세일즈 에이전트").click()
    page.wait_for_timeout(1000)

    print("세일즈 에이전트 페이지 진입 완료 ")

    # 20251125 - 세일즈 에이전트 > 상단 > [시작하기] 버튼 선택 코드 추가
    page.get_by_role("button", name="시작하기").nth(1).click()
    page.wait_for_timeout(1000)

    # 20251125 - 세일즈 에이전트 > Starter > [시작하기] 버튼 선택 코드 추가
    page.get_by_role("button", name="시작하기").nth(2).click()
    page.wait_for_timeout(2000)

    print("회원가입 페이지 진입 완료")

    # 20251125 - 회원가입 페이지 > 로그인 선택 코드 추가
    page.get_by_text("로그인").click()
    page.wait_for_timeout(1000)

    print("로그인 페이지 진입 완료")

    page.get_by_placeholder("이메일").fill(config.FREE_PA46_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA46_PW)
    page.wait_for_timeout(500)

    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("로그인 완료 후 세일즈 에이전트 랜딩페이지 진입")

    page.get_by_role("button", name="시작하기").nth(2).click()
    page.wait_for_timeout(1000)

    print("토스페이먼츠 결제창 출력 상태 완료")

    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 1 ~ 4 자리").fill(config.CARD1_1_4_NO)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 5 ~ 8 자리").fill(config.CARD1_5_8_NO)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 9 ~ 12 자리").fill(config.CARD1_9_12_NO)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 13 ~ 16 자리").fill(config.CARD1_13_16_NO)
    page.wait_for_timeout(500)

    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드 유효기간").fill(config.CARD1_VALID_THRU)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 생년월일").fill(config.CARD1_RRN_BIRTH)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 성별").fill(config.CARD1_RRN_GENDER)
    page.wait_for_timeout(500)

    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("checkbox", name="[필수] 서비스 이용 약관, 개인정보 처리 동의").check()
    page.wait_for_timeout(1000)


    assert "4033" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 1 ~ 4 자리").input_value(), \
        "토스페이먼츠 결제창 > 카드번호 1~4자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인"
    assert "0201" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 5 ~ 8 자리").input_value(), \
        "토스페이먼츠 결제창 > 카드번호 5~8자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인"
    assert "6000" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 9 ~ 12 자리").input_value(), \
        "토스페이먼츠 결제창 > 카드번호 9~12자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인"
    assert "0000" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 13 ~ 16 자리").input_value(), \
        "토스페이먼츠 결제창 > 카드번호 13~16자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인"
    assert "12/26" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드 유효기간").input_value(), \
        "토스페이먼츠 결제창 > 카드 유효기간 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인"
    assert "870724" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 생년월일").input_value(), \
        "토스페이먼츠 결제창 > 주민등록번호 앞자리 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인"
    assert "1" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 성별").input_value(), \
        "토스페이먼츠 결제창 > 주민등록번호 뒷자리 중 첫번째 성별 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인"


    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("button", name="결제 취소").click()
    page.wait_for_timeout(1000)

    print("---- 84번 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 -> 성공 ----")
