import config

def test_discover_industry_and_title_search(page):
    print("----- 42번 - 발견하기 > 산업군 + 타이틀 문구 키워드 검색 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 발견하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="발견하기").nth(1).click()
    page.wait_for_timeout(3000)

    print("발견하기 페이지 진입 완료")
    page.locator("header").filter(has_text="고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").get_by_role("button").click()
    page.locator(".text-FG-Primary.css-124rwol").click()

    page.get_by_role("option", name="모든 산업").locator("div").click()
    print("발견하기 > 산업군 > 모든 산업군 설정 완료")
    page.get_by_placeholder("제목으로 찾기").fill("직원 수 200명 규모")
    page.get_by_placeholder("제목으로 찾기").press("Enter")

    print("발견하기 > 산업군 + 검색 설정 완료")
    page.wait_for_timeout(2000)

    assert "숙박 서비스" == page.get_by_text("숙박 서비스").inner_text(), \
        "발견하기 > 검색된 카드 > 산업군 키워드 확인 실패 - 산업군 + 타이틀 검색 실패 1"
    assert "직원 수 200명 규모의 럭셔리 호스피탈리티 서비스 제공 업체 리스트" == page.get_by_role("heading", name="직원 수 200").inner_text(), \
        "발견하기 > 검색된 카드 > 타이틀 문구 확인 실패 - 산업군 + 타이틀 검색 실패 2"
    assert "Hospitality, 50 - 200" ==     page.locator("[id=\"__next\"]").get_by_text("Hospitality, 50 -").inner_text(), \
        "발견하기 > 검색된 카드 > 키워드 문구 확인 실패 - 산업군 + 타이틀 검색 실패 3"

    print("----- 발견하기 > 산업군 + 타이틀 문구 키워드 검색 테스트 시작 -> -----")
