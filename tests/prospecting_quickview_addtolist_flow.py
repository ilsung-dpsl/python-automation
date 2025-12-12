import re
from asyncio import timeout

import config

def test_prospecting_quickview_addtolist_flow(page):
    print("----- 32번 - 퀵뷰 > 리스트에 추가 시 정상 동작 여부 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("일본의 여행 가이드 업체의 직급이 매니저인 사람")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    #20251212 - 탐색하기 검색 후 이전 대기 시간 7초로 재변경
    page.wait_for_timeout(7000)

    print("탐색하기 > 검색 완료")

    #20251212 - 탐색하기 검색 시 로딩 길어짐으로 인한 앨리먼트 요소가 나올때까지 기다리는 timeout 50초 추가
    page.get_by_text("Ryo Hayashi세일즈 매니저연락처 확인Japan").click(timeout=50000)
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

    #20250930 - 탐색하기 UI 변경으로 인한 퀵뷰 > [X] 버튼 선택 후 퀵뷰 닫음 코드 수정
    page.get_by_role("main").get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(2000)

    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="마이 리스트").nth(1).click()
    page.wait_for_timeout(2000)

    page.get_by_text("기본1(1 미확인)백 일성").click()
    # 20251208 - 대기 시간 2초로 변경
    page.wait_for_timeout(2000)

    assert "Ryo Hayashi" == page.get_by_text("Ryo Hayashi").inner_text(), \
        "마이리스트 상세(Default) > 추가한 리드 성함 확인 실패 - 퀵뷰 > 리스트에 추가 실패 1"
    assert "Japan Travel Kk" in page.content(), \
        "마이리스트 상세(Default) > 추가한 리드 소속 회사 확인 실패 - 퀵뷰 > 리드에 추가 실패 2"

    print("마이리스트 상세 > 리스트에 추가한 데이터 확인 완료")

    page.locator("div").filter(has_text=re.compile(r"^이름 / 직함연락처회사담당자 위치산업군추가일자$")).get_by_role("checkbox").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)
    page.locator("#modal-root").get_by_role("button", name="삭제").click()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="리스트로 돌아가기").click()
    
    print("----- 퀵뷰 > 리스트에 추가 시 정상 동작 여부 확인 테스트 시작 -> 성공 -----")
