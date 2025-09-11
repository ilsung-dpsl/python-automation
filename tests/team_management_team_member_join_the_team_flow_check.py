import config
import re

def test_team_management_team_member_join_the_team_flow_check(page):
    print("----- 팀 멤버 > 팀 합류 플로우 확인 테스트 시작 -----")

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
    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(10000)

    print("팀 관리 > 팀 멤버 초대 요청 완료")

    context = page.context
    page1 = context.new_page()
    page1.goto("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AdBytiP1SYDEMEr3CoGyQTIDKbfnmbMM9JS1E3G8teDobHL_bY6VotbPKkRuHqZ8lzYDJdli7jitEA&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-148400069%3A1756345294909753")
    page1.wait_for_timeout(1000)

    print("구글 지메일 계정 로그인 페이지 진입 완료")

    page1.get_by_role("textbox", name="이메일 또는 휴대전화").fill(config.GMAIL_EMAIL)
    page1.get_by_role("button", name="다음").click()
    page1.wait_for_timeout(1000)
    page1.get_by_role("textbox", name="비밀번호 입력").fill(config.GMAIL_EMAIL_PW)
    page1.get_by_role("button", name="다음").click()
    page1.wait_for_timeout(5000)

    print("구글 지메일 계정 로그인 완료")

    # Gmail '받은편지함' 대기
    page1.wait_for_selector("table[role='grid']")

    # 가장 위쪽 메일 클릭
    page1.locator("table[role='grid'] tr").first.click()
    page1.wait_for_timeout(7000)

    with page1.expect_popup() as page2_info:
        print("팀 멤버 초대 메일 진입 완료")
        join_the_team_btn_count = page1.get_by_role("link", name="초대된 팀 가입하기").count()
        print(f"초대된 팀 가입하기 버튼 카운트 : {join_the_team_btn_count}")
        page1.get_by_role("link", name="초대된 팀 가입하기").nth(join_the_team_btn_count - 1).click()

    page1.wait_for_timeout(2000)
    print("팀 멤버 초대 메일 > 초대된 팀에 가입하기 링크 연동 완료")

    page2 = page2_info.value
    page2.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page2.wait_for_timeout(1000)
    page2.get_by_text("로그아웃").click()
    page2.wait_for_timeout(1000)

    page2.get_by_placeholder("이메일").fill(config.FREE_PA19_ACCOUNT)
    page2.get_by_placeholder("비밀번호").fill(config.FREE_PA19_PW)
    page2.get_by_role("button", name="로그인").click()
    page2.wait_for_timeout(3000)

    assert "일성 백님의 팀에 초대되었습니다." == page2.get_by_text("일성 백님의 팀에 초대되었습니다").inner_text(), \
        "팀 멤버 로그인 후 팀에 합류 모달 > 타이틀 문구 확인 실패 - 팀에 합류 모달 노출 실패 1"

    print("팀 멤버 계정으로 로그인 후 팀에 합류 모달 노출 완료")

    page2.get_by_role("button", name="팀에 합류").click()
    page2.wait_for_timeout(3000)

    assert "TEAM" == page2.get_by_text("TEAM").inner_text(), \
        "팀 관리 > 팀 요금제 명 확인 실패 - 팀 합류 실패 2"
    assert "ilsung.baek+pa14@deepsales.com" == page2.get_by_text("ilsung.baek+pa14@deepsales.com").inner_text(), \
        "팀 관리 > 첫번째 멤버 > 이메일 확인 실패 - 팀 합류 실패 3"
    assert "팀 크레딧: 월간 600 크레딧" == page2.get_by_text("팀 크레딧: 월간 600 크레딧").inner_text(), \
        "팀 관리 > 팀 크레딧 정보 확인 실패 - 팀 합류 실패 4"
    #팀 오너 크레딧 사용으로 인한 잔여 크레딧 개수 수정 - 20250911
    assert "잔여 크레딧: 584/1184" == page2.get_by_text("잔여 크레딧: 584/").inner_text(), \
        "팀 관리 > 잔여 크레딧 정보 확인 실패 - 팀 합류 실패 5"
    assert "ilsung.baek+pa19@deepsales.com" == page2.get_by_text("ilsung.baek+pa19@deepsales.com").inner_text(), \
        "팀 관리 > 팀 합류한 이메일 정보 확인 실패 - 팀 합류 실패 6"

    page.wait_for_timeout(5000)

    print("팀 멤버 합류 정상 동작 확인 완료")

    page2.get_by_text("팀 떠나기").click()
    page2.wait_for_timeout(1000)
    page2.locator("#modal-root").get_by_text("팀 떠나기").click()
    page2.wait_for_timeout(1000)
    page2.get_by_role("button", name="떠나기").click()
    page2.wait_for_timeout(3000)

    print("팀 멤버 합류 후 팀 떠나기 처리 완료")
    print("----- 팀 멤버 > 팀 합류 플로우 확인 테스트 시작 -> 성공 -----")
