import re

import config


def test_prospecting_insufficient_credit_modal_upgrade_my_plan_click(page):
    print("----- 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Upgrade my plan 버튼 클릭 시 플랜 페이지로 이동 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD4_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD4_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(500)
    #page.get_by_role("button", name="Start Now").click()
   # page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("walmart 회사의 직원정보를 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    page.locator("div").filter(has_text=re.compile(r"^Aparna KulkarniSoftware Engineer연락처 확인WalmartUnited StatesRetail$")).get_by_role("button").click()
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="요금제 업그레이드").click()
    page.wait_for_timeout(3000)

    assert "당신의 세일즈를 위한 맞춤형 요금제" in page.content(), "요금제 및 가격 페이지 > 타이틀 문구 출력 실패 - 플랜 페이지 이동 실패 1"
    #assert "플랜 변경하기" in page.content(), "요금제 및 가격 페이지 > 플랜 변경 버튼 출력 실패 - 플랜 페이지 이동 실패 2"
    #요금제 및 가격 페이지 > Elite 영역 > [플랜 변경하기] 버튼 확인으로 변경 - 20250805
    assert "플랜 변경하기" in page.locator("div").filter(has_text=re.compile(r"^Elite인기 상품\$96플랜 변경하기$")).get_by_role("button").inner_text(), "요금제 및 가격 페이지 > ELite > 플랜 변경하기 버튼 출력 실패 - 플랜 페이지 이동 실패 2"

    print("----- 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Upgrade my plan 버튼 클릭 시 플랜 페이지로 이동 테스트 시작 -> 성공 -----")
