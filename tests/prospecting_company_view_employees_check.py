import re
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
#    page.get_by_role("button", name="Start Now").click()
#    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("삼성 sds 직원 정보를 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")
    page.wait_for_timeout(5000)

    page.get_by_role("tab", name="회사(2)").click()
    page.wait_for_timeout(2000)
    page.locator("div").filter(
        has_text=re.compile(r"^Samsung SDSSouth KoreaProfessional Services10,000 \+직원 정보 확인$")).get_by_role(
        "button").click()
    page.wait_for_timeout(3000)

    assert "Samsung SDS" == page.locator(".flex-1 > div:nth-child(2) > .flex").nth(0).inner_text(), "필터 > 회사 > Samsung SDS 키워드 확인 실패 1"
    assert "Jong Yoon" in page.content(), "리드 데이터 1 > 성함 확인 실패 2"
    assert "Anshu Sharma" in page.content(), "리드 데이터 6 > 성함 확인 실패 3"
    assert "연락처 확인" in page.content(), "리드 데이터 1 > 연락처 확인 버튼 출력 실패 3"

    print("----- 회사 탭 > 직원 정보 확인 후 탐색하기 검색 결과 노출 확인 테스트 시작 -> 성공 -----")
