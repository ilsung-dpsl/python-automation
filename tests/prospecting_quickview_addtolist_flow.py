import re
import config

def test_prospecting_quickview_addtolist_flow(page):
    print("----- 퀵뷰 > 리스트에 추가 시 정상 동작 여부 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("일본의 여행 가이드 업체의 직급이 매니저인 사람을 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    print("탐색하기 > 검색 완료")

    page.locator(".truncate > .flex-1").first.click()
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="리스트에 추가").click()
    page.wait_for_timeout(1000)
    page.get_by_role("checkbox", name="default").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(1000)

    assert "선택한 연락처가 추가되었습니다." == page.get_by_text("선택한 연락처가 추가되었습니다").inner_text(), \
        "리스트에 추가 모달 > 선택한 연락처 추가 후 추가 완료 토스트 메시지 출력 실패 - 퀵뷰 > 리스트에 추가 실패 1"

    print("탐색하기 > 퀵뷰 > 리스트에 추가 완료")


    #퀵뷰 > [X] 버튼 선택 후 퀵븁 닫음
    page.get_by_role("main").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()

    #마이리스트로 이동
    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)
    page.get_by_text("기본1(1 미확인)백 일성").click()
    page.wait_for_timeout(1000)

    assert "Ryo Hayashi" == page.get_by_text("Ryo Hayashi").inner_text(), \
        "마이리스트 상세(Default) > 추가한 리드 성함 확인 실패 - 퀵뷰 > 리스트에 추가 실패 1"
    assert "Japan Travel Kk" in page.content(), \
        "마이리스트 상세(Default) > 추가한 리드 소속 회사 확인 실패 - 퀵뷰 > 리드에 추가 실패 2"

    print("마이리스트 상세 > 리스트에 추가한 데이터 확인 완료")

    page.locator("div").filter(has_text=re.compile(r"^이름 / 직함연락처회사담당자 위치산업군추가일자$")).get_by_role("checkbox").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="삭제").click()
    page.wait_for_timeout(500)
    page.locator("#modal-root").get_by_role("button", name="삭제").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="리스트로 돌아가기").click()
    
    print("----- 퀵뷰 > 리스트에 추가 시 정상 동작 여부 확인 테스트 시작 -> 성공 -----")
