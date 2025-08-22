import config
import re

def test_team_management_enterprise_seat_full_charge_and_invite_member_limit_check(page):
    print("팀관리 > Enterprise 계정 (4명 좌석 만석) > 팀멤버 초대 시 초대 불가 모달 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()

    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)
    page.get_by_text("팀 관리").click()
    page.wait_for_timeout(2000)

    print("팀관리 페이지 진입 완료")

    page.get_by_role("button", name="맴버 초대하기").click()
    page.wait_for_timeout(1000)

    assert "팀 멤버 추가 가능 인원을 초과했습니다." == page.get_by_text("팀 멤버 추가 가능 인원을 초과했습니다").inner_text(), \
        "팀관리 > Enterprise (4명 좌석 만석) > 멤버 초대하기 시 초대 제한 모달 > 타이틀 문구 확인 실패 - 초대 제한 모달 노출 실패 1"
    assert "확인" == page.get_by_role("button", name="확인").inner_text(), \
                "팀관리 > Enterprise (4명 좌석 만석) > 멤버 초대하기 시 초대 제한 모달 > [확인] 버튼 확인 실패 - 초대 제한 모달 노출 실패 2"

    print("팀관리 > Enterprise 계정 (4명 좌석 만석) > 팀멤버 초대 시 초대 불가 모달 노출 확인 테스트 시작 -> 성공 -----")