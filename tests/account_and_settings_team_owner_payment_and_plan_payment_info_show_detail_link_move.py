import config
import re

def test_account_and_settings_team_owner_payment_and_plan_payment_info_show_detail_link_move(page):
    print("----- 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 상세정보 표시 선택 시 결제 정보 페이지 이동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("탐색하기 페이지 진입 완료")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("결제 및 요금제").click()
    page.wait_for_timeout(1000)

    print("결제 및 요금제 페이지 진입 완료")

    page.get_by_text("상세정보 표시 >").click()
    page.wait_for_timeout(1000)

    print("결제 정보 페이지 진입 완료")

    assert "결제 정보" == page.locator("div").filter(has_text=re.compile(r"^결제 정보$")).inner_text(), \
        "결제 정보 페이지 > '결제 정보' 타이틀 문구 확인 실패 - 결제 정보 > 상세정보 표시 링크 연동 실패 1"
    assert "카드 등록하기" == page.get_by_role("button", name="카드 등록하기").inner_text(), \
        "결제 정보 페이지 > '카드 등록하기' 버튼 문구 확인 실패 - 결제 정보 > 상세정보 표시 링크 연동 실패 2"
    assert ("저장된 카드로 결제 시 각 카드마다 최대 3회까지 결제를 시도합니다. 결제 실패 후 1일, 3일, 5일 후에 다시 결제를 시도합니다. 모두 실패하면 무료 요금제로 전환됩니다." ==
            page.get_by_text("저장된 카드로 결제 시 각 카드마다 최대 3").inner_text()), \
        "결제 정보 페이지 > 하단 안내 문구 확인 실패 - 결제 정보 > 상세정보 표시 링크 연동 실패 3"

    print("결제 정보 페이지 확인 완료")
    print("----- 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 상세정보 표시 선택 시 결제 정보 페이지 이동 확인 테스트 시작 -> 성공 -----")
