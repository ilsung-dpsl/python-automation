import config
import re

def test_account_and_settings_team_member_go_to_team_management_link_move(page):
    print("----- 팀멤버 > 결제 및 요금제 > 팀 관리로 이동 노출 및 링크 이동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.TEAM_MEMBER_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.TEAM_MEMBER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("탐색하기 페이지 진입 완료")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("결제 및 요금제").click()
    page.wait_for_timeout(1000)

    print("결제 및 요금제 페이지 진입 완료")

    assert "팀 관리로 이동" == page.get_by_text("팀 관리로 이동").inner_text(), \
        "결제 및 요금제 > 팀 관리로 이동 링크 노출 실패 - 팀 멤버 > 결제 및 요금제 > 팀 관리로 이동 링크 노출 및 이동 확인 실패 1"

    page.get_by_text("팀 관리로 이동").click()
    page.wait_for_timeout(1000)

    print("팀 관리 페이지 진입 완료")

    assert "팀 관리" == page.get_by_text("팀 관리", exact=True).inner_text(), \
        "팀 관리 > '팀관리' 타이틀 문구 노출 실패 - 팀 멤버 > 결제 및 요금제 > 팀 관리로 이동 링크 노출 및 이동 확인 실패 2"
    assert False == page.get_by_role("button", name="맴버 초대하기").is_visible(), \
        "팀 관리 > [맴버 초대하기] 버튼 활성화 확인 실패 - 팀 멤버 > 결제 및 요금제 > 팀 관리로 이동 링크 노출 및 이동 확인 실패 3"
    assert "ilsung.baek+pa14@deepsales.com" == page.get_by_text("ilsung.baek+pa14@deepsales.com").inner_text(), \
        "팀 관리 > 멤버 > 팀 멤버 이메일 확인 실패 - 팀 멤버 > 결제 및 요금제 > 팀 관리로 이동 링크 노출 및 이동 확인 실패 4"

    print("팀 관리 페이지 이동 확인 완료")
    print("----- 팀멤버 > 결제 및 요금제 > 팀 관리로 이동 노출 및 링크 이동 확인 테스트 시작 -> 성공 -----")
