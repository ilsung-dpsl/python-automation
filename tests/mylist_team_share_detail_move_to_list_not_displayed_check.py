import config

def test_mylist_team_share_detail_move_to_list_not_displayed_check(page):
    print("----- 마이리스트 상세 (팀공유) > 리스트로 이동 버튼 미노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_TEAM_MEMBER_AC)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_TEAM_MEMBER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(6000)

    print("마이리스트 진입 완료")

    page.get_by_text("테스트용").click()
    page.wait_for_timeout(3000)

    assert "리스트에 이동" not in page.content(), \
        "팀공유 폴더 상세 진입 후 리스트에 이동 버튼 비활성화 확인 실패 - 팀공유 폴더의 리스트에 이동 비활성화 실패 1"

    print("----- 마이리스트 상세 (팀공유) > 리스트로 이동 비활성화 확인 테스트 시작 -> 성공 -----")