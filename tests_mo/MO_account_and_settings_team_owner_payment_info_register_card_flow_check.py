import config
import re

def test_MO_account_and_settings_team_owner_payment_info_register_card_flow_check(mobile_page):
    print("----- 37번 - MO 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 카드 등록하기 플로우 확인 테스트 시작 (등록 전까지만) 확인 -----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # 20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    mobile_page.get_by_role("button").nth(2).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_text("결제 및 요금제").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 결제 및 요금제 진입 완료")

    mobile_page.locator(".rounded-\\[8px\\].p-2.bg-Surface-Default-a").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 카드 등록하기 모달 노출 완료")

    mobile_page.get_by_placeholder("카드 번호").tap()
    mobile_page.keyboard.type("4242424242424242", delay=100)

    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("MM/YY").tap()
    mobile_page.get_by_placeholder("MM/YY").fill("12/30")
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_placeholder("CVC를 입력하세요").tap()
    mobile_page.get_by_placeholder("CVC를 입력하세요").fill("169")
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_placeholder("카드 소지자명을 입력하세요").tap()
    mobile_page.get_by_placeholder("카드 소지자명을 입력하세요").fill("BAEKILSUNG")
    mobile_page.wait_for_timeout(500)

    button = mobile_page.locator("button:has-text('등록')")
    pointer_events = button.evaluate("el => getComputedStyle(el).pointerEvents")

    assert "4242 - 4242 - **** - ****" == mobile_page.get_by_placeholder("카드 번호").input_value(), \
        "MO Web - 카드 등록하기 모달 > 카드 번호 입력 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 1"
    assert "12/30" == mobile_page.get_by_placeholder("MM/YY").input_value(), \
        "MO Web - 카드 등록하기 모달 > 유효 기간 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 2"
    assert "169" == mobile_page.get_by_placeholder("CVC를 입력하세요").input_value(), \
        "MO Web - 카드 등록하기 모달 > CVC 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 3"
    assert "BAEKILSUNG" == mobile_page.get_by_placeholder("카드 소지자명을 입력하세요").input_value(), \
        "MO Web - 카드 등록하기 모달 > 카드 소지자명 확인 실패 - 유료 회원(팀오너) > 카드 등록하ㅣㄱ 플로우 실패 4"
    assert "none" != pointer_events, \
        "MO Web - 카드 등록하기 모달 > 등록 클릭 가능 확인 실패 - 유료 회원(팀오너) > 카드 등록하기 플로우 실패 5"

    print("MO Web - 카드 등록하기 모달 > 입력값 확인 완료")

    mobile_page.get_by_role("button", name="취소").tap()
    mobile_page.wait_for_timeout(1000)

    print("----- 37번 - MO 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 카드 등록하기 플로우 확인 테스트 시작 (등록 전까지만 확인 -----")

