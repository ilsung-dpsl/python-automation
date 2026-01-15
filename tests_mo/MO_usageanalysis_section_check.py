import config
import re

def test_MO_usageanalysis_section_check(mobile_page):
    print("----- 10번 - MO 대시보드 > Usage Analysis에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 테스트 시작 -----")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    mobile_page.get_by_role("link").filter(has_text="대시보드").tap(timeout=10000)
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 대시보드 진입 완료")

    assert "산업" in mobile_page.content(), \
        "MO Web - Usage Analysis > 산업 체크 실패"
    assert "부서" in mobile_page.content(), \
        "MO Web - Usage Analysis > 부서 체크 실패"
    assert "직위" in mobile_page.content(), \
        "MO Web - Usage Analysis > 직위 체크 실패"
    assert "Wholesale Cosmetics" in mobile_page.content(), \
        "MO Web - Usage Analysis > 산업 > 임의 항목 체크 실패"
    assert "General Management" in mobile_page.content(), \
        "MO Web - Usage Analysis > 부서 > 임의 항목 체크 실패"
    assert "Junior" in mobile_page.content(), \
        "MO Web - Usage Analysis > 직위 > 임의 항목 체크 실패"

    print("---- 10번 - MO 대시보드 > Usage Analysis에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 테스트 -> 성공 ----")