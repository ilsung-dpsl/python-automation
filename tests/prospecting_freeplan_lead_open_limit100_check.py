import re

import config


def test_prospecting_freeplan_lead_open_limit100_check(page):
    print("----- 무료 회원이 검색 결과 리스트에서 100개 이상 연락처 탐색 시 업그레이드 모달 노출 확인 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("미국에서 화장품 수입하는 회사 찾아줘")
    page.locator("#desktop-header-slot").get_by_role("img").nth(2).click()
    page.wait_for_timeout(5000)

    for i in range(1, 5, 1):
        page.locator("div").filter(has_text=re.compile(fr"^162 페이지 중 {i} 페이지페이지 바로가기$")).get_by_role("button").nth(1).click()
        print(f"{i} 페이지 체크 확인 ")
        page.wait_for_timeout(500)

    page.wait_for_timeout(2000)

    assert "이런... Free 요금제는 최대 100" in page.content(), "Free 열람 100명 제한 모달 > 타이틀 문구 출력 실패 - 요금제 최대 100명 열람 제한 모달 출력 실패 1"
    assert "Plan을 변경하고 더 많은 잠재고객을 만나보세요." in page.content(), "Free 열람 100명 제한 모달 > 가이드 문구 출력 실패 - 요금제 최대 100명 열람 제한 모달 출력 실패 2"
    assert "요금제 업그레이드" in page.content(), "Free 열람 100명 제한 모달 > [요금제 업그레이드] 버튼 출력 실패 - 요금제 최대 100명 열람 제한 모달 출력 실패"

    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    print("----- 무료 회원이 검색 결과 리스트에서 100개 이상 연락처 탐색 시 업그레이드 모달 노출 확인 테스트 시작 -> 성공 -----")