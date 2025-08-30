from pyasn1.debug import Printer

import config
import re

def test_team_management_team_owner_invite_member_flow_check(page):
    print("----- 팀관리 > Team 오너 > 멤버 초대 Flow 확인 테스트 시작 -----")

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

    print("팀 관리 페이지 진입 완료")
    page.get_by_role("button", name="맴버 초대하기").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="지금은 괜찮아요, 그냥 초대").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("여기에 이메일을 입력하세요").fill(config.FREE_PA19_ACCOUNT)
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(2000)

    assert "초대되었습니다."== page.locator("div").filter(has_text=re.compile(r"^초대되었습니다\.$")).nth(1).inner_text(), \
        "팀관리 > 팀오너 계정으로 팀 초대 완료 후 초대 완료 메시지 출력 실패 - 팀 초대 요청 실패 1"
    assert "ilsung.baek+pa19@deepsales.com" == page.get_by_text(config.FREE_PA19_ACCOUNT).first.inner_text(), \
        "팀관리 > 팀오너 계정으로 팀 초대 완료 후 멤버 > 이메일 추가 실패 - 팀 초대 요청 실패 2"
    assert "멤버" == page.get_by_text("멤버").nth(1).inner_text(), \
        "팀관리 > 팀오너 계정으로 팀 초대 완료 후 멤버 > 멤버 노출 실패 - 팀 초대 요청 실패 3"
    #대기중 버튼 위치 인덱스 없이 누르는 것으로 코드 수정 - 20250827
    assert "대기중" == page.get_by_text("대기중").inner_text(), \
        "팀관리 > 팀오너 계정으로 팀 초대 완료 후 멤버 > 상태 > 대기중 노출 실패 - 팀 초대 요청 실패 4"

    print("팀 관리 > 팀오너 멤버 초대 요청 완료")
    page.get_by_text("내보내기").nth(1).click()

    page.wait_for_timeout(1000)

    page.get_by_role("button", name="내보내기").click()
    page.wait_for_timeout(1000)

    print("팀 관리 > 팀오너 > 초대 요청한 팀멤버 내보내기 완료")
    print("----- 팀관리 > Team 오너 > 멤버 초대 Flow 확인 테스트 시작 -> 성공 -----")
