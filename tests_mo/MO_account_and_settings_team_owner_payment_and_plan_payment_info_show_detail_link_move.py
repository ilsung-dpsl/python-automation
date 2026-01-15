import config
import re

def test_MO_account_and_settings_team_owner_payment_and_plan_payment_info_show_detail_link_move(mobile_page):
    print("----- 61번 - MO 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 상세정보 표시 선택 시 결제 정보 페이지 이동 확인 테스트 시작 -----")

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

    print("MO Web - 탐색하기 페이지 진입 완료")

    # 20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    mobile_page.get_by_role("button").nth(2).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_text("결제 및 요금제").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 결제 및 요금제 페이지 진입 완료")

    mobile_page.get_by_text("상세정보 표시 >").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 결제 정보 페이지 진입 완료")

    assert "결제 정보" == mobile_page.locator("div").filter(has_text=re.compile(r"^결제 정보$")).inner_text(), \
        "MO Web - 결제 정보 페이지 > '결제 정보' 타이틀 문구 확인 실패 - 결제 정보 > 상세정보 표시 링크 연동 실패 1"
    assert "카드 등록하기" == mobile_page.get_by_role("button", name="카드 등록하기").inner_text(), \
        "MO Web - 결제 정보 페이지 > '카드 등록하기' 버튼 문구 확인 실패 - 결제 정보 > 상세정보 표시 링크 연동 실패 2"
    assert ("저장된 카드로 결제 시 각 카드마다 최대 3회까지 결제를 시도합니다. 결제 실패 후 1일, 3일, 5일 후에 다시 결제를 시도합니다. 모두 실패하면 무료 요금제로 전환됩니다." ==
            mobile_page.get_by_text("저장된 카드로 결제 시 각 카드마다 최대 3").inner_text()), \
        "MO Web - 결제 정보 페이지 > 하단 안내 문구 확인 실패 - 결제 정보 > 상세정보 표시 링크 연동 실패 3"

    print("MO Web -결제 정보 페이지 확인 완료")
    print("----- 61번 - MO 유료회원 (팀오너) > 결제 및 요금제 > 결제 정보 > 상세정보 표시 선택 시 결제 정보 페이지 이동 확인 테스트 시작 -> 성공 -----")