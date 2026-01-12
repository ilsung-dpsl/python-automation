import re
import config
from conftest import mobile_page


def test_salesagent_scale_toss_payments_1_2page_input_check(mobile_page):
    print("---- 67번 - MO 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 ----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="세일즈 에이전트 바우처").tap()
    mobile_page.wait_for_timeout(1000)

    print("세일즈 에이전트 페이지 진입 완료 ")

    # 20251202 - 세일즈 에이전트 > 상단 > [시작하기] -> [플랜 확인하기] 버튼으로 변경되어 코드 수정
    mobile_page.get_by_role("button", name="플랜 확인하기").tap()
    mobile_page.wait_for_timeout(1000)

    # 20260113 - PC의 경우, 아래의 위치가 Starter 위치이지만 MO의 경우에는 Scale 위치를 가리킴
    mobile_page.get_by_role("button", name="시작하기").nth(1).tap()
    mobile_page.wait_for_timeout(2000)

    print("회원가입 페이지 진입 완료")

    # 20251125 - 회원가입 페이지 > 로그인 선택 코드 추가
    mobile_page.get_by_text("로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA46_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA46_PW)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("로그인 완료 후 세일즈 에이전트 랜딩페이지 진입")

    mobile_page.get_by_role("button", name="시작하기").nth(1).tap()
    mobile_page.wait_for_timeout(1000)

    print("토스페이먼츠 결제창 출력 상태 완료")

    mobile_page.get_by_role("textbox", name="카드번호 1 ~ 4 자리").fill(config.CARD1_1_4_NO)
    mobile_page.get_by_role("textbox", name="카드번호 5 ~ 8 자리").fill(config.CARD1_5_8_NO)
    mobile_page.get_by_role("textbox", name="카드번호 9 ~ 12 자리").fill(config.CARD1_9_12_NO)
    mobile_page.wait_for_timeout(500)
    #mobile_page.get_by_role("textbox", name="카드번호 13 ~ 16 자리").fill(config.CARD1_13_16_NO)

    for i in range(1, 5, 1):
        mobile_page.get_by_role("button", name="0").tap()
        mobile_page.wait_for_timeout(500)
        print(f"토스페이먼츠 결제창 1 > 카드번호 마지막 뒷자리 입력 카운트 : {i}")

    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("textbox", name="카드 유효기간").fill(config.CARD1_VALID_THRU)
    mobile_page.wait_for_timeout(500)

    # 20251202 - 주민등록번호 입력 부분이 본인인증 창에서 노출되는 것으로 확인되어 코드 주석 처리
    # page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 생년월일").fill(config.CARD1_RRN_BIRTH)
    # page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("textbox", name="주민등록번호 성별").fill(config.CARD1_RRN_GENDER)
    # page.wait_for_timeout(500)

    mobile_page.get_by_label("[필수] 서비스 이용 약관, 개인정보 처리 동의").first.tap()
    mobile_page.wait_for_timeout(1000)

    assert "4033" == mobile_page.get_by_role("textbox", name="카드번호 1 ~ 4 자리").input_value(), \
        "토스페이먼츠 결제창 1 > 카드번호 1~4자리 번호 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 1"
    assert "0201" == mobile_page.get_by_role("textbox", name="카드번호 5 ~ 8 자리").input_value(), \
        "토스페이먼츠 결제창 1 > 카드번호 5~8자리 번호 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 2"
    assert "6000" == mobile_page.get_by_role("textbox", name="카드번호 9 ~ 12 자리").input_value(), \
        "토스페이먼츠 결제창 1 > 카드번호 9~12자리 번호 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 3"
    #assert "0000" == mobile_page.get_by_placeholder("****").inner_text(), \
    #    "토스페이먼츠 결제창 1 > 카드번호 13~16자리 번호 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 4"

    assert "12/26" == mobile_page.get_by_role("textbox", name="카드 유효기간").input_value(), \
        "토스페이먼츠 결제창 1 > 카드 유효기간 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 4"

    # 20251202 - 토스페이먼츠 심사 완료 후 운영 실결제로 변경되어, 본인인증 프로세스가 추가되어 테스트 스크립트 코드 추가 및 수정
    mobile_page.get_by_role("button", name="다음").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("토스페이먼츠 결제창2 본인 인증 창 노출 확인")

    mobile_page.get_by_role("textbox", name="이름").fill(config.CARD1_AUTH_NAME)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("button", name="확인").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("textbox", name="주민등록번호 생년월일").fill(config.CARD1_RRN_BIRTH)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("textbox", name="주민등록번호 성별").fill(config.CARD1_RRN_GENDER)
    mobile_page.wait_for_timeout(500)

    #mobile_page.locator("iframe[name=\"__tosspayments_payment-gateway_iframe__\"]").content_frame.get_by_role("combobox",
    #                                                                                                   name="통신사 선택").click()

    mobile_page.get_by_role("listitem").filter(has_text=re.compile(r"^KT$")).locator("div").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("휴대폰번호").fill(config.CARD1_AUTH_PHONE)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("button", name="다음").tap(timeout=10000)
    mobile_page.wait_for_timeout(5000)

    mobile_page.get_by_role("textbox", name="인증번호").fill("000000")
    mobile_page.wait_for_timeout(1000)

    assert "000000" == mobile_page.get_by_role("textbox", name="인증번호").input_value(), \
        "토스페이먼츠 결제창 2-2 (본인인증) > 인증번호 인증창 > 인증번호 입력값 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 5"

    mobile_page.get_by_role("button", name="뒤로가기").tap()
    mobile_page.wait_for_timeout(2000)

    assert "백일성" == mobile_page.get_by_role("textbox", name="이름").input_value(), \
        "토스페이먼츠 결제창 2-1 (본인인증) > 이름 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 6"
    assert "870724" == mobile_page.get_by_role("textbox", name="주민등록번호 생년월일").input_value(), \
        "토스페이먼츠 결제창 2-1 (본인인증) > 주민등록번호 생년월일 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 7"
    assert "1" == mobile_page.get_by_role("textbox", name="주민등록번호 성별").input_value(), \
        "토스페이먼츠 결제창 2-1 (본인인증) > 주민등록번호 성별 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 8"
    assert "01041342385" == mobile_page.get_by_placeholder("휴대폰번호").input_value(), \
        "토스페이먼츠 결제창 2-1 (본인인증) > 휴대폰번호 확인 실패 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 9"

    mobile_page.wait_for_timeout(1000)

    print("---- 67번 - MO 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인 -> 성공 ----")
