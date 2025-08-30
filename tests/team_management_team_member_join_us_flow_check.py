import config
import re

def test_team_management_team_member_join_us_flow_check(page):
    print("----- 팀 멤버 초대 수신 및 합류 플로우 확인 테스트 시작 -----")

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

    page.get_by_role("button", name="맴버 초대하기").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="지금은 괜찮아요, 그냥 초대").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("여기에 이메일을 입력하세요").fill(config.FREE_PA19_ACCOUNT)
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("팀 오너 > 팀 멤버 초대 요청 완료")

    context = page.context
    page1 = context.new_page()
    page1.goto("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AdBytiMKaXv-hglpNxVK6g4rBCb2066xFBFCwAmUVlsyQa5nMYZaDD3XoLoouhtztxE9hWG6Johg1Q&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1311583840%3A1755873863287831")
    page1.get_by_role("textbox", name="이메일 또는 휴대전화").fill(config.GMAIL_EMAIL)
    page.wait_for_timeout(1000)

    page1.get_by_role("button", name="다음").click()
    page.wait_for_timeout(1000)

    page1.get_by_role("textbox", name="비밀번호 입력").fill(config.GMAIL_EMAIL_PW)
    page.wait_for_timeout(1000)

    page1.get_by_role("button", name="다음").click()
    page.wait_for_timeout(1000)

    page1.get_by_role("link", name="백 일성님이 회원님을 DeepSales").click()
    page.wait_for_timeout(3000)

    # "초대된 팀 가입하기" 링크 여러 개일 때 마지막 클릭
    links = page1.get_by_role("link", name="초대된 팀 가입하기")
    count = links.count()

    with page1.expect_popup() as page2_info:
        links.nth(count - 1).click()

    page2 = page2_info.value
    page2.wait_for_timeout(1000)
    print("팀 멤버 초대 수신 메일 연동 완료")

    page2.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page2.wait_for_timeout(1000)

    page2.get_by_text("로그아웃").click()
    page2.wait_for_timeout(1000)

    print("이전 로그인 -> 로그아웃 처리 완료")

    page2.get_by_placeholder("이메일").fill(config.FREE_PA19_ACCOUNT)
    page2.get_by_placeholder("비밀번호").fill(config.FREE_PA19_PW)
    page2.get_by_role("button", name="로그인").click()
    page2.wait_for_timeout(1000)

    print("팀 멤버 계정으로 재로그인 완료")

    page2.get_by_text("일성 백님의 팀에 초대되었습니다").click()
    page2.wait_for_timeout(1000)

    page2.get_by_role("button", name="팀에 합류").click()
    page2.wait_for_timeout(1000)

    assert "TEAM" == page2.get_by_text("TEAM").inner_text(), \
        "팀 관리 > 팀 요금제 노출 확인 실패 - 팀 합류 플로우 확인 실패 1"
    assert "ilsung.baek+pa14@deepsales.com" == page2.get_by_text("ilsung.baek+pa14@deepsales.com").inner_text(), \
        "팀 관리 > 팀 멤버 1 이메일 확인 실패 - 팀 합류 플로우 확인 실패 2"
    assert "팀 크레딧: 월간 600 크레딧" == page2.get_by_text("팀 크레딧: 월간 600 크레딧").inner_text(), \
        "팀 관리 > 팀 크레딧 노출 확인 실패 - 팀 합류 플로우 확인 실패 3"
    assert "잔여 크레딧: 600/1200" == page2.get_by_text("잔여 크레딧: 600/").inner_text(), \
        "팀 관리 > 남은 크레딧 노출 확인 실패 - 팀 합류 플로우 확인 실패 4"

    print("팀 멤버로 합류 후 팀 멤버 변경 사항 확인")

    page2.get_by_text("내보내기").nth(1).click()
    page2.wait_for_timeout(1000)

    page2.get_by_role("button", name="내보내기").click()
    page2.wait_for_timeout(1000)

    print("----- 팀 멤버 초대 수신 및 합류 플로우 확인 테스트 시작 -> 성공 -----")
