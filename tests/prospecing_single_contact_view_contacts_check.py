import re

import config


def test_prospecing_single_contact_view_contacts_check(page):
    print("----- 탐색하기 > 단일 연락처 > 연락처 확인 동작 확인 테스트 시작 (미완성 > 위치 파악하기가 너무 어려움)-----")

    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD3_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD3_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("구글 회사의 정보를 알려줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    if page.locator("div:nth-child(3) > .flex.gap-2 > .flex.justify-center").inner_text() == "확인됨":
        print("리드 1번째 > 확인됨")
        ㄴ
    if page.locator("div:nth-child(2) > div:nth-child(3) > .flex.gap-2 > .flex.justify-center").inner_text() == "확인됨":
       print("리드 2번째 > 연락처 확인")

    if page.locator("div:nth-child(3) > div:nth-child(3) > .flex.gap-2 > .flex.justify-center").inner_text() == "연락처 확인":
        print("리드 3번째 > 연락처 확인")

    if page.locator("div:nth-child(4) > div:nth-child(3) > .flex.gap-2 > .flex.justify-center").inner_text() == "연락처 확인":
        print("리드 4번째 > 연락처 확인")

    print("리드 2번째 > 연락처 확인 -> 확인됨 으로 출력됨")

    #page.locator("div:nth-child(2) > div:nth-child(3) > .flex.gap-2").click()
#15 크래딧이 사용되었습니다.
