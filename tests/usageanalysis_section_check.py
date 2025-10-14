import config


def test_usageanalysis_section_check(page):
    print("----- 12번 - 대시보드 > Usage Analysis에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
 #   page.get_by_role("button", name="Start Now").click()
 #   page.wait_for_timeout(1000)

    # 20250929 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250929 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250929 - LNB > 대시보드 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="대시보드").nth(1).click()
    page.wait_for_timeout(2000)

    assert "산업" in page.content(), "Usage Analysis > 산업 체크 실패"
    assert "부서" in page.content(), "Usage Analysis > 부서 체크 실패"
    assert "직위" in page.content(), "Usage Analysis > 직위 체크 실패"
    assert "Wholesale Cosmetics" in page.content(), "Usage Analysis > 산업 > 임의 항목 체크 실패"
    assert "General Management" in page.content(), "Usage Analysis > 부서 > 임의 항목 체크 실패"
    assert "Junior" in page.content(), "Usage Analysis > 직위 > 임의 항목 체크 실패"

    print("대시보드 > Usage Analysis에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 테스트 -> 성공")