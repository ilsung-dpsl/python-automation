import config
import re

def test_mylist_team_share_detail_delete_not_displayed_check(page):
    print("----- 마이리스트 상세(팀공유) > 삭제 버튼 미노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)

    print("마이리스트 페이지 진입 완료")

    page.get_by_text("마이리스트 팀멤버 공유 폴더").click()
    page.wait_for_timeout(1000)

    delete_button = page.query_selector("button#삭제")

    assert delete_button is None, \
        "마이리스트 상세(팀공유) 진입 후 삭제 버튼 미노출 확인 실패 1"

    page.wait_for_timeout(1000)

    page.locator(".flex.items-center.space-x-3").first.click()

    assert delete_button is None, \
        "마이리스트 상세(팀공유) > 연락처 체크 후 삭제 버튼 미노출 확인 실패 2"

    print("----- 마이리스트 상세(팀공유) > 삭제 버튼 미노출 확인 테스트 시작 -> 성공 -----")
