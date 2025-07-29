import re
import config

def test_prospecting_contacts_name_click_and_contact_detail_check(page):
    print("----- 탐색하기 > 성함 선택 후 담당자 상세 화면 이동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
  #  page.get_by_role("button", name="Start Now").click()
  #  page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("한국 화장품 유통 회사 중 직급이 매니저인 담당자를 찾아줘")
    page.locator("#desktop-header-slot").get_by_role("img").nth(2).click()
    page.wait_for_timeout(5000)

    page.get_by_text("Danny Jung").click()
    page.wait_for_timeout(5000)

    assert "탐색하기" == page.locator("span").inner_text(), "연락처 상세 페이지 > 타이틀 문구 '탐색하기' 확인 실패 - 연락처 상세 페이지 이동 실패 1"
    assert "/ Danny Jung" in page.content(), "연락처 상세 페이지 > 타이틀 문구 '/ Danny Jung' 확인 실패 - 연락처 상세 페이지 이동 실패 2"
    assert "Manager" == page.get_by_text("Manager", exact=True).inner_text(), "연락처 상세 페이지 > 직급 - Manager 확인 실패 - 연락처 상세 페이지 이동 실패 3"
    assert "skin79 Co., Ltd." in page.content(), "연락 상세 페이지 > 회사 영역 > 소속 회사 문구 확인 실패 - 연락처 상세 페이지 이동 실패 4"
    assert "****@skin79.com" in page.content(), "연락 상세 페이지 > 연락처 상세 영역 > 미확인된 이메일 확인 실패 - 연락처 상세 페이지 이동 실패 5"

    print("----- 탐색하기 > 성함 선택 후 담당자 상세 화면 이동 확인 테스트 시작 -> 성공 -----")
