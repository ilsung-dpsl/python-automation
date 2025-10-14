import config

def test_mylist_team_share_detail_move_to_list_not_displayed_check(page):
    print("----- 50번 - 마이리스트 상세 (팀공유) > 리스트로 이동 버튼 미노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_TEAM_MEMBER_AC)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_TEAM_MEMBER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="마이 리스트").nth(1).click()
    page.wait_for_timeout(1000)

    print("마이리스트 진입 완료")

    page.get_by_text("테스트용").click()
    page.wait_for_timeout(3000)

    assert "리스트에 이동" not in page.content(), \
        "팀공유 폴더 상세 진입 후 리스트에 이동 버튼 비활성화 확인 실패 - 팀공유 폴더의 리스트에 이동 비활성화 실패 1"

    print("----- 마이리스트 상세 (팀공유) > 리스트로 이동 비활성화 확인 테스트 시작 -> 성공 -----")