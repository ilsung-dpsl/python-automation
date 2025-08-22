import config
import re

def test_team_management_team_owner_other_team_member_invite_limit_check(page):
    print("----- 팀관리 > 팀오너 계정에서, 다른 팀 초대된 멤버 초대 시 팀 초대 불가 모달 노출 확인 테스트 시작-----")

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

    page.get_by_placeholder("여기에 이메일을 입력하세요").fill(config.ENTERPRISE_MEMBER_PA20_ACC)
    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    assert "초대할 수 없습니다" == page.get_by_text("초대할 수 없습니다").inner_text(), \
        "초대 불가 모달 > 타이틀 문구 확인 실패 - 다른 멤버 초대 시 초대 불가 확인 실패 1"
    assert "이 사용자는 다른 팀 또는 유료 요금제 사용자로 초대되었습니다. 다른 이메일을 입력하십시오." == page.get_by_text("이 사용자는 다른 팀 또는 유료 요금제 사용자로 초대되었습니다. 다른 이메일을 입력하십시오").inner_text(), \
        "초대 불가 모달 > 가이드 문구 확인 실패 - 다른 멤버 초대 시 초대 불가 확인 실패 2"
    assert "확인" == page.get_by_role("button", name="확인").inner_text(), \
        "초대 불가 모달 > [확인[ 실패 - 다른 멤버 초대 시 초대 불가 확인 실패 3"

    print("----- 팀관리 > 팀오너 계정에서, 다른 팀 초대된 멤버 초대 시 팀 초대 불가 모달 노출 확인 테스트 시작 -> 성공 -----")
