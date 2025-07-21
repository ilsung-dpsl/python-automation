import config


def test_usageanalysis_section_check(page):
    print("----- 대시보드 > Usage Analysis에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="대시보드").click()
    page.wait_for_timeout(5000)

    assert "산업" in page.content(), "Usage Analysis > 산업 체크 실패"
    assert "부서" in page.content(), "Usage Analysis > 부서 체크 실패"
    assert "직위" in page.content(), "Usage Analysis > 직위 체크 실패"
    assert "Cosmetics Manufacturing" in page.content(), "Usage Analysis > 산업 > 임의 항목 체크 실패"
    assert "General Management" in page.content(), "Usage Analysis > 부서 > 임의 항목 체크 실패"
    assert "Junior" in page.content(), "Usage Analysis > 직위 > 임의 항목 체크 실패"

    print("대시보드 > Usage Analysis에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 테스트 -> 성공")