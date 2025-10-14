import config

def test_prospecting_quickview_contact_check(page):
    print("----- 30번 - 탐색하기 > 임의 리드 > 퀵뷰 (Quick view contact) 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
   # page.get_by_role("button", name="Start Now").click()
   # page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("미국의 화장품 유통회사 중 세일즈 담당자를 찾아줘")
    #20250930 - 탐색하기 UI 변경으로 프롬프트 창 > 검색 버튼 코드 수정
    page.locator("label").get_by_role("img").nth(1).click()

    page.wait_for_timeout(5000)
    #20250930 - 탐색하기 UI 변경으로 인한 해당 리드 선택 코드 수정
    page.get_by_text("Claudia Ramos내부 영업 담당자확인됨").click()

    page.wait_for_timeout(2000)
    assert "Claudia Ramos" == page.get_by_role("article").get_by_text("Claudia Ramos").inner_text(), \
        "퀵뷰(연락처) > 성함 확인 실패 - 퀵뷰(연락처) 노출 실패 1"
    #20250930 - 탐색하기 ui 변경 및 해당 리드 직함 변경으로 인한 코드 수정
    assert "내부 영업 담당자" == page.get_by_role("article").get_by_text("내부 영업 담당자").inner_text(), \
        "퀵뷰(연락처) > 직함 확인 실패 - 퀵뷰(연락처) 노출 실패 2"
    assert "ramos6@google.com" in page.content(), \
        "퀵뷰(연락처) > 연락처 > 확인된 연락처(이메일) 확인 실패 - 퀵뷰(연락처) 노출 실패 3"
    #assert "****@google.com" in page.content(), \
    #    "퀵뷰(연락처) > 연락처 > 미확인된 연락처(이메일) 확인 실패 - 퀵뷰(연락처) 노출 실패 3"
    assert "Sally Beauty" == page.get_by_text("Sally Beauty").nth(2).inner_text(), \
        "퀵뷰(연락처) > 회사 > 소속 회사명 확인 실패 - 퀵뷰(연락처) 노출 실패 4"

    print("----- 탐색하기 > 임의 리드 > 퀵뷰 (Quick view contact) 노출 확인 테스트 시작 -> 성공 -----")