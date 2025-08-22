import config
import re

def test_team_management_free_team_owner_addseat_click(page):
    print("팀 관리 > Free / Team 오너 계정으로 [좌석 추가] 선택 시 요금 페이지 이동 확인 테스트 시작")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("팀 관리").click()
    page.wait_for_timeout(1000)

    print("팀관리 페이지 진입 완료")
    page.get_by_text("좌석 추가").click()
    page.wait_for_timeout(1000)

    assert "당신의 세일즈를 위한 맞춤형 요금제" == page.get_by_role("heading", name="당신의 세일즈를 위한 맞춤형 요금제").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 타이틀 문구 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 1"
    assert "누구에게 팔지 막막할 때, 딥세일즈가 도와줄게요." == page.get_by_text("누구에게 팔지 막막할 때, 딥세일즈가 도와줄게요").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 타이틀 하단 > 가이드 문구 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 2"
    assert "월간" == page.get_by_role("button", name="월간").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 요금제 토글 버튼 '월간' 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 3"
    assert "연간\n-25%" == page.get_by_role("button", name="연간 -25%").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 요금제 토글 버튼 '연간 -25%' 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 4"

    print("Free > 요금제 페이지 진입 완료")

    page.get_by_role("banner").get_by_role("link", name="탐색하기").click()
    page.wait_for_timeout(2000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("로그아웃").click()
    page.wait_for_timeout(1000)

    print("Free 계정 로그아웃 후 로그인 페이지 진입 완료")
    page.get_by_placeholder("이메일").fill(config.TEAM_OWNER_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.TEAM_OWNER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("팀 관리").click()
    page.wait_for_timeout(1000)

    print("Team 오너 계정 로그인 후 팀관리 페이지 진입 완료")
    page.get_by_text("좌석 추가").click()
    page.wait_for_timeout(1000)

    assert "플랜 변경하기" in page.locator("div").filter(has_text=re.compile(r"^Elite인기 상품\$96플랜 변경하기$")).get_by_role("button").inner_text(), \
        "팀관리 > Team owner > 좌석 추가 선택 후 요금제 페이지 > Elite > [플랜 변경하기] 버튼 확인 실패 - Team 오너 > 요금제 페이지 이동 실패 1"
    assert "요금제별 주요 기능 비교" == page.get_by_role("heading", name="요금제별 주요 기능 비교").inner_text(), \
        "팀관리 > Team owner > 좌석 추가 선택 후 요금제 페이지 > 요금제별 주요 기능 비교 영역 타이틀 문구 확인 실패 - Team 오너 > 요금제 페이지 이동 실패 2"

    print("팀 관리 > Free / Team 오너 계정으로 [좌석 추가] 선택 시 요금 페이지 이동 확인 테스트 시작 -> 성공")
