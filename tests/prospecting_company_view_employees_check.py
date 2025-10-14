import re
import config


def test_prospecting_company_view_employees_check(page):
    print("----- 28번 - 회사 탭 > 직원 정보 확인 후 탐색하기 검색 결과 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD5_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD5_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    #page.get_by_role("button", name="Start Now").click()
    #page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("삼성 sds 직원 정보를 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")
    page.wait_for_timeout(5000)

    #20251014 - 회사 1개만 노출로 변경되어 코드 수정
    page.get_by_role("tab", name="회사 (1)").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="직원 정보 확인").click()
    page.wait_for_timeout(3000)

    assert "Samsung SDS" == page.locator(".flex-1 > div:nth-child(2) > .flex").nth(0).inner_text(), "필터 > 회사 > Samsung SDS 키워드 확인 실패 1"
    #20251014 - 리드 데이터 위치 변경으로 인해, 데이터 성함 확인 코드 변경
    assert "Katie Han" in page.content(), "리드 데이터 1 > 성함 확인 실패 2"
    assert "Jordi Teruel" in page.content(), "리드 데이터 6 > 성함 확인 실패 3"
    assert "연락처 확인" in page.content(), "리드 데이터 > 연락처 확인 버튼 출력 여부 실패 4"

    print("----- 회사 탭 > 직원 정보 확인 후 탐색하기 검색 결과 노출 확인 테스트 시작 -> 성공 -----")
