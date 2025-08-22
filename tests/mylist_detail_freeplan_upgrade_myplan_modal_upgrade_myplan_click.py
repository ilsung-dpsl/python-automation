import config
import re

def test_mylist_detail_freeplan_upgrade_myplan_modal_upgrade_myplan_click(page):
    print("----- 마이 리스트 상세 > csv 내보내기 시 요금제 업그레이드 모달 > 요금제 업그레이드 선택 시 플랜 페이지 이동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)

    print("마이리스트 메인 페이지 진입 완료")
    page.get_by_text("cosmetic test 2", exact=True).click()
    page.wait_for_timeout(1000)

    page.locator("div").filter(has_text=re.compile(r"^Emily CohenMarketer확인됨Benefit CosmeticsUnited StatesWholesale2025\.05\.02 15:20$")).get_by_role("checkbox").click()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="내보내기").click()
    page.wait_for_timeout(500)

    page.get_by_role("menuitem", name="CSV 내보내기").click()
    page.wait_for_timeout(1000)

    print("요금제 업그레이드 모달 출력 완료")

    page.get_by_role("button", name="요금제 업그레이드").click()
    page.wait_for_timeout(1000)

    assert "당신의 세일즈를 위한 맞춤형 요금제" == page.get_by_role("heading", name="당신의 세일즈를 위한 맞춤형 요금제").inner_text(), \
        "업그레이드 모달 > 요금제 업그레이드 선택 후 플랜페이지 > 타이틀 문구 확인 실패 - 플랜페이지 이동 실패 1"
    assert "플랜 변경하기" in page.locator("div").filter(has_text=re.compile(r"^Pro\$39플랜 변경하기$")).get_by_role("button").inner_text(), \
        "업그레이드 모달 > 요금제 업그레이드 선택 후 플랜페이지 > Pro > [플랜 변경하기] 버튼 확인 실패 - 플랜페이지 이동 실패 1"

    print("----- 마이 리스트 상세 > csv 내보내기 시 요금제 업그레이드 모달 > 요금제 업그레이드 선택 시 플랜 페이지 이동 확인 테스트 시작 -> 성공 -----")


