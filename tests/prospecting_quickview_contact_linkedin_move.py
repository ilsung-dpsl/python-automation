import config

def test_prospecting_quickview_contact_linkedin_move(page):
    print("----- 탐색하기 > 퀵뷰 > 링크드인 선택 시 해당 링크드인 페이지 이동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("apple 회사의 프로덕트 매니저 담당자를 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    print("탐색하기 > 검색 완료")

    #첫번째 리드의 담당자 위치 열 선택
    page.locator(".truncate > .flex-1").first.click()

    page.wait_for_timeout(1000)

    #퀵뷰 > 링크드인 아이콘 선택
    with page.expect_popup() as page1_info:
        page.get_by_role("article").locator("section").filter(has_text="Camden YumoriProduct Manager").get_by_role("img").click()
    page1 = page1_info.value

    page1.wait_for_timeout(2000)

    #링크드인 페이지 로그인 절차 진행
    page1.get_by_role("button", name="로그인").click()
    page1.wait_for_timeout(1000)
    page1.get_by_role("textbox", name="이메일 또는 전화").fill(config.LINKEDIN_ACCOUNT)
    page1.get_by_role("textbox", name="비밀번호").fill(config.LINKEDIN_PW)
    page1.wait_for_timeout(1000)
    page1.locator("#base-sign-in-modal").get_by_role("button", name="로그인").click()
    page1.wait_for_timeout(5000)

    assert "https://www.linkedin.com/in/camdenyumori/" == page1.url, \
        "링크드인 페이지 url 이동 실패 - 퀵뷰 > 링크드인 페이지 이동 실패 1"
    assert "Camden Yumori " == page1.get_by_label("Camden Yumori", exact=True).inner_text(), \
        "링크드인 페이지 > 성함 확인 실패 - 퀵뷰 > 링크드인 페이지 이동 실패 2"
    assert "Product @ Gusto | Ex Google, Apple" == page1.get_by_text("Product @ Gusto | Ex Google,").nth(2).inner_text(), \
        "링크드인 페이지 > 직함 및 회사 정보 확인 실패 - 퀵뷰 > 링크드인 페이지 이동 실패 3"


    print("----- 탐색하기 > 퀵뷰 > 링크드인 선택 시 해당 링크드인 페이지 이동 확인 테스트 시작 -> 성공 -----")