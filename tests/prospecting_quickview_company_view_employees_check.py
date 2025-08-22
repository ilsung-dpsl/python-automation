import config

def test_prospecting_quickview_company_view_employees_check(page):
    print("----- 퀵뷰(회사) > 직원 정보 확인 선택 시 탐색결과 반영 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("일본 화장품 제조사 세일즈 매니저")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    print("탐색하기 > 검색 완료")

    # 최근 1개월 이내 데이터 중복 노출 이슈로 인해 아래의 코드 주석처리 - 20250819 -> 20일 수정됨
    page.get_by_role("tab", name="회사(3)").click()

    # 최근 1개월 이내 데이터 중복 노출 이슈로 인해 아래의 코드로 수정 - 20250819
    #page.get_by_role("tab", name="회사(4)").click()

    page.wait_for_timeout(1000)
    # 최근 1개월 이내 데이터 중복 노출 이슈로 인해 아래의 코드 주석처리 - 20250819 -> 20일 수정됨
    page.get_by_text("Japan").nth(2).click()

    # 최근 1개월 이내 데이터 중복 노출 이슈로 인해 아래의 코드로 수정 - 20250819
    #page.get_by_text("Japan").nth(3).click()

    page.wait_for_timeout(1000)
    page.get_by_role("article").get_by_role("button", name="직원 정보 확인").click()
    page.wait_for_timeout(1000)

    assert "Wave Corporation Co.,Ltd." == page.get_by_text("Wave Corporation Co.,Ltd.").first.inner_text(), \
        "탐색하기 > 필터 > 회사 > 'Wave Corporation Co.,Ltd.' 키워드 추가 실패 - 직원 정보 확인 시 탐색결과 반영 실패 1"
    assert "Ishii Takehiro" == page.get_by_text("Ishii Takehiro").inner_text(), \
        "탐색하기 > 리드 결과 > 리드 첫번째 > 성함 확인 실패 - 직원 정보 확인 시 탐색결과 반영 실패 2"
    assert "Japan" == page.locator("[id=\"__next\"]").get_by_text("Japan").inner_text(), \
        "탐색하기 > 리드 결과 > 리드 첫번쨰 > 담당자 위치 확인 실패 - 직원 정보 확인 시 탐색결과 반영 실패 3"

    print("----- 퀵뷰(회사) > 직원 정보 확인 선택 시 탐색결과 반영 확인 테스트 시작 -> 성공 -----")

