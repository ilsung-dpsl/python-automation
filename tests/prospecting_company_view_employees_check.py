import config


def test_prospecting_company_view_employees_check(page):
    print("----- 회사 탭 > 직원 정보 확인 후 탐색하기 검색 결과 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD5_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD5_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("cosmetic")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")
    page.wait_for_timeout(5000)

    page.get_by_role("tab", name="회사(3,159)").click()
    page.wait_for_timeout(2000)
    page.locator(".h-\\[48px\\] > div:nth-child(5) > div").first.click()
    page.wait_for_timeout(3000)

    assert "Sephora" in page.content(), "필터 > 회사 > Sephora 키워드 확인 실패 1"
    assert "Dominique Mandonnaud" in page.content(), "리드 데이터 1 > 성함 확인 실패 2"
    assert "연락처 확인" in page.content(), "리드 데이터 1 > 연락처 확인 버튼 출력 실패 3"

    print("----- 회사 탭 > 직원 정보 확인 후 탐색하기 검색 결과 노출 확인 테스트 시작 -> 성공 -----")
