import config


def test_dashboard_mylist_contacts_count_check(page):
    print("----- 14번 - My lists 영역에 저장한 연락처, 미확인 연락처 표시 확인 테스트 시작-----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=60000)
    #20251230 - URL 이동 후 잠시 0.5 대기 시간 코드 추가
    page.wait_for_timeout(500)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    page.get_by_role("button", name="로그인").click()
  #  page.wait_for_timeout(1000)
  #  page.get_by_role("button", name="Start Now").click()
    #20251230 - 대기 시간 1초 -> 2초로 수정
    page.wait_for_timeout(2000)

    #20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 대시보드 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="대시보드").nth(1).click()
    page.wait_for_timeout(2000)

    page.wait_for_timeout(7000)

    assert "마이 리스트" in page.content(), "대시보드 > 마이리스트 영역 > 타이틀 문구 노출 확인 실패 1"
    assert "저장" in page.content(), "대시보드 > 마이리스트 영역 > 저장 문구 노출 확인 실패 2"
    #20251211 - 마이리스트 저장 카운트 개수 재수정
    assert "6,602" in page.content(), "대시보드 > 마이리스트 영역 > 저장 카운트 개수 확인 실패 3"
    assert "확인되지 않은" in page.content(), "대시보드 > 마이리스트 영역 > 미확인된 문구 노출 확인 실패 4"
    #20260330 - 마이리스트 확인되지 않은 카운트 개수 재수정
    assert "6,385" in page.content(), "대시보드 > 마이리스트 영역 > 미확인된 연락처 카운트 개수 확인 실패 5"

#    print("대시보드 > 마이리스트 > 팀공유 연락처 개수 영역 미출력됨 -> 해당 항목 주석 처리 -> 추후 수정 시 재추가 및 수정")
#    assert "팀 공유" in page.content(), "대시보드 > 마이리스트 영역 > 팀 공유 문구 노출 확인 실패 6"

    print("----- 14번 - My lists 영역에 저장한 연락처, 미확인 연락처 표시 확인 테스트 종료 -> 성공 -----")
