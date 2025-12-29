import re
import config

def test_salesagent_starter_toss_payments_1_2page_input_check(page):
    print("---- 86번 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 ----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("banner").get_by_role("link", name="세일즈 에이전트").click()
    page.wait_for_timeout(1000)

    print("세일즈 에이전트 페이지 진입 완료 ")

    # 20251202 - 세일즈 에이전트 > 상단 > [시작하기] -> [플랜 확인하기] 버튼으로 변경되어 코드 수정
    page.get_by_role("button", name="플랜 확인하기").click()
    page.wait_for_timeout(1000)

    # 20251202 - 세일즈 에이전트 > Starter > [시작하기] 버튼 선택 위치 변경으로 인해 코드 수정
    page.get_by_role("button", name="시작하기").nth(1).click()
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
    page.wait_for_timeout(500)

    # 20251202 - 주민등록번호 입력 부분이 본인인증 창에서 노출되는 것으로 확인되어 코드 주석 처리
    #page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 생년월일").fill(config.CARD1_RRN_BIRTH)
    #page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 성별").fill(config.CARD1_RRN_GENDER)
    #page.wait_for_timeout(500)

    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("checkbox", name="[필수] 서비스 이용 약관, 개인정보 처리 동의").check()
    page.wait_for_timeout(1000)

    assert "4033" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 1 ~ 4 자리").input_value(), \
        "토스페이먼츠 결제창 1 > 카드번호 1~4자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 1"
    assert "0201" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 5 ~ 8 자리").input_value(), \
        "토스페이먼츠 결제창 1 > 카드번호 5~8자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 2"
    assert "6000" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 9 ~ 12 자리").input_value(), \
        "토스페이먼츠 결제창 1 > 카드번호 9~12자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 3"
    assert "0000" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드번호 13 ~ 16 자리").input_value(), \
        "토스페이먼츠 결제창 1 > 카드번호 13~16자리 번호 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 4"
    assert "12/26" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="카드 유효기간").input_value(), \
        "토스페이먼츠 결제창 1 > 카드 유효기간 확인 실패 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 5"

    # 20251202 - 토스페이먼츠 심사 완료 후 운영 실결제로 변경되어, 본인인증 프로세스가 추가되어 테스트 스크립트 코드 추가 및 수정
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("button", name="다음").click()
    page.wait_for_timeout(1000)
    
    print("토스페이먼츠 결제창2 본인 인증 창 노출 확인")

    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="이름 -").fill(config.CARD1_AUTH_NAME)
    page.wait_for_timeout(500)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 생년월일").fill(config.CARD1_RRN_BIRTH)
    page.wait_for_timeout(500)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 성별").fill(config.CARD1_RRN_GENDER)
    page.wait_for_timeout(500)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("combobox", name="통신사 선택").click()
    page.wait_for_timeout(1000)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("option", name="KT", exact=True).click()
    page.wait_for_timeout(1000)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="휴대폰번호 -").fill(config.CARD1_AUTH_PHONE)
    page.wait_for_timeout(500)
    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("button", name="인증번호 받기").click()
    page.wait_for_timeout(3000)


    assert "백일성" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="이름 -").input_value(), \
        "토스페이먼츠 결제창 2 (본인인증) > 이름 확인 실패 - 세일즈 에이전트 > Starer > 구독 결제 완료 전까지 동작 확인 6"
    assert "870724" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 생년월일").input_value(), \
        "토스페이먼츠 결제창 2 (본인인증) > 주민등록번호 생년월일 확인 실패 - 세일즈 에이전트 > Starer > 구독 결제 완료 전까지 동작 확인 7"
    assert "1" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 성별").input_value(), \
        "토스페이먼츠 결제창 3 (본인인증) > 주민등록번호 성별 확인 실패 - 세일즈 에이전트 > Starer > 구독 결제 완료 전까지 동작 확인 8"
    assert "01041342385" == page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="휴대폰번호 -").input_value(), \
        "토스페이먼츠 결제창 4 (본인인증) > 휴대폰번호 확인 실패 - 세일즈 에이전트 > Starer > 구독 결제 완료 전까지 동작 확인 9"

    page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("button", name="결제 취소").click()
    page.wait_for_timeout(1000)

    print("---- 84번 - 세일즈 에이전트 > Starter > 구독 결제 완료 전까지 동작 확인 -> 성공 ----")
