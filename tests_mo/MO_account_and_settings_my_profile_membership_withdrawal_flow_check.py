import config
import re

def test_MO_account_and_settings_my_profile_membership_withdrawal_flow_check(mobile_page):
    print("----- 54번 - MO 회원 탈퇴 플로우 확인 테스트 시작 -----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA25_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA25_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # 20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    mobile_page.get_by_role("button").nth(2).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_text("계정 및 설정").tap()
    mobile_page.wait_for_timeout(1000)

    print("계정 및 설정 > 내 프로필 페이지 진입 완료")

    mobile_page.get_by_role("button", name="회원 탈퇴").tap()
    mobile_page.wait_for_timeout(1000)

    assert "회원 탈퇴" == mobile_page.locator("#modal-root").get_by_text("회원 탈퇴").inner_text(), \
        "회원 탈퇴 알림창 > 타이틀 문구 확인 실패 - 회원가입 플로우 진행 실패 1"
    assert "계속하기" == mobile_page.get_by_role("button", name="계속하기").inner_text(), \
        "회원 탈퇴 알림창 > [계속하기] 버튼 확인 실패 - 회원가입 플로우 진행 실패 2"

    print("회원 탈퇴 알림창 노출 확인 완료")

    mobile_page.get_by_role("button", name="계속하기").tap()
    mobile_page.wait_for_timeout(1000)

    assert "탈퇴하시겠습니까?" == mobile_page.locator("header").filter(has_text="탈퇴하시겠습니까?").inner_text(), \
        "탈퇴 사유 선택창 > 타이틀 문구 확인 실패 - 회원가입 플로우 진행 실패 3"
    assert "기타" == mobile_page.locator("#modal-root").get_by_text("기타").inner_text(), \
        "탈퇴 사유 선택창 > 기타 옵션 확인 실패 - 회원가입 플로우 진행 실패 4"

    print("탈퇴 사유 선택창 노출 확인 완료")

    mobile_page.get_by_role("checkbox", name="부정확한 데이터").tap()
    mobile_page.wait_for_timeout(1000)

    assert True == mobile_page.get_by_role("checkbox", name="부정확한 데이터").is_checked(), \
        "탈퇴 사유 선택창 > 부정확한 데이터 체크 확인 실패 - 회원가입 플로우 진행 실패 5"

    print("탈퇴 사유 선택창 > 부정확한 데이터 > 체크 여부 확인 완료")

    mobile_page.get_by_role("checkbox", name="부정확한 데이터").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("checkbox", name="기타").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("textbox", name="이유를 적어주세요").fill("내가 원하는 리드가 없어요.")
    mobile_page.wait_for_timeout(1000)

    assert "내가 원하는 리드가 없어요." == mobile_page.get_by_role("textbox", name="이유를 적어주세요").input_value(), \
        "탈퇴 사유 선택창 > 기타 > 사유 입력 후 확인 실패 - 회원가입 플로우 진행 실패 6"

    print("탈퇴 사유 선택창 > 기타 > 사유 내용 확인 완료")

    mobile_page.get_by_role("button", name="취소").tap()
    mobile_page.wait_for_timeout(1000)

    print("탈퇴 사유 선택창 > 취소 선택 후 알림창 닫힘 완료")

    print("----- 54번 - MO 회원 탈퇴 플로우 확인 테스트 시작 -> 성공 -----")

