from time import process_time_ns

import config
import re

def test_company_register_flow_check(page):
    print("----- 회사 정보 메인 > 등록하기 -> 회사 등록 후 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.FREE_PA24_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA24_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("로그인 후 탐색하기 페이지 진입 완료")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("회사 정보", exact=True).click()
    page.wait_for_timeout(3000)

    page.locator(".text-FG-Primary.css-124rwol").click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-2-input").fill("deepsales")
    page.wait_for_timeout(1000)

    page.locator("#react-select-2-option-0").get_by_text("DeepSales").click()
    page.wait_for_timeout(1000)

    page.get_by_text("회사 페이지 등록하기").click()
    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("회사 정보 메인 > 회사 정보 등록 완료")

    page.locator(".text-\\[18px\\]").first.click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("팀 관리").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("회사 정보").click()
    page.wait_for_timeout(1000)

    print("회사 정보 상세 페이지 진입 완료")

    assert "DeepSales" == page.locator(".text-\\[18px\\]").first.inner_text(), \
        "회사 정보 상세 페이지 > 회사명 출력 실패 - 회사 정보 등록 실패 1"
    assert "2021" == page.get_by_text("2021", exact=True).inner_text(), \
        "회사 정보 상세 페이지 > 설립연도 출력 실패 - 회사 정보 등록 실패 2"
    assert "Seed" == page.get_by_text("Seed").inner_text(), \
        "회사 정보 상세 페이지 > 펀딩 > 투자 단계 출력 실패 - 회사 정보 등록 실패 3"

    print("회사 정보 등록 완료 확인")

    page.get_by_text("소속된 회사에서 나가기").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(1000)

    print("회사 정보 등록 후 소속된 회사 떠니기 완료")
    print("----- 회사 정보 메인 > 등록하기 -> 회사 등록 후 확인 테스트 시작 -> 성공 -----")