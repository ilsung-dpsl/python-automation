import config
import re

def test_team_management_team_owner_delete_member(page):
    print("----- 팀관리 > 팀오너 계정에서, 팀 멤버 삭제 동작 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.TEAM_OWNER_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.TEAM_OWNER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("팀 관리").click()
    page.wait_for_timeout(1000)

    print("팀관리 페이지 진입 완료")
    page.get_by_role("button", name="맴버 초대하기").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="지금은 괜찮아요, 그냥 초대").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("여기에 이메일을 입력하세요").fill(config.FREE_PA19_ACCOUNT)
    page.wait_for_timeout(500)

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("삭제 확인할 멤버 추가 작업 완료")

    page.get_by_text("내보내기").nth(1).click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="내보내기").click()
    page.wait_for_timeout(2000)

    assert "멤버가 삭제되었습니다." == page.locator("div").filter(has_text=re.compile(r"^멤버가 삭제되었습니다\.$")).nth(1).inner_text(), \
        "팀 관리 > 팀 멤버 삭제 시 멤버 삭제 완료 토스트 메시지 출력 실패 - 팀 멤버 삭제 실패 1"

    print("----- 팀관리 > 팀오너 계정에서, 팀 멤버 삭제 동작 확인 테스트 시작 -> 성공 -----")

