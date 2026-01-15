import config
import re

def test_MO_prospecting_insufficient_credit_modal_upgrade_my_plan_click(mobile_page):
    print("----- 21번 - MO 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Upgrade my plan 버튼 클릭 시 플랜 페이지로 이동 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PRD4_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PRD4_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").tap()
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("walmart 회사의 직원정보를 찾아줘")
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    mobile_page.wait_for_timeout(5000)

    print("MO Web - 탐색하기 검색 완료 후")

    # 202511125 - 연락처 확인 리드 재변경 > 첫번째 페이지 > 4번째 리드로 변경
    mobile_page.locator("div").filter(
        has_text=re.compile(r"^Anton Kramarenko소프트웨어 엔지니어연락처 확인WalmartUnited StatesRetail$")).get_by_role(
        "button").tap()
    mobile_page.wait_for_timeout(4000)

    print("MO Web - 크레딧 부족 모달 출력 완료")

    mobile_page.get_by_role("button", name="요금제 업그레이드").tap()
    mobile_page.wait_for_timeout(3000)

    assert "당신의 세일즈를 위한 맞춤형 요금제" in mobile_page.content(), \
        "MO Web - 요금제 및 가격 페이지 > 타이틀 문구 출력 실패 - 플랜 페이지 이동 실패 1"
    # assert "플랜 변경하기" in page.content(), "요금제 및 가격 페이지 > 플랜 변경 버튼 출력 실패 - 플랜 페이지 이동 실패 2"
    # 요금제 및 가격 페이지 > Elite 영역 > [플랜 변경하기] 버튼 확인으로 변경 - 20250805
    assert "컨설팅 받기" in mobile_page.locator("div").filter(has_text=re.compile(r"^Enterprise별도 문의컨설팅 받기$")).get_by_role(
        "button").inner_text(), \
        "MO Web - 요금제 및 가격 페이지 > Enterprise > 컨설팅 받기 버튼 출력 실패 - 플랜 페이지 이동 실패 2"

    print("----- 21번 - MO 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Upgrade my plan 버튼 클릭 시 플랜 페이지로 이동 테스트 시작 -> 성공 -----")