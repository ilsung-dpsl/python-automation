import config
import re

def test_team_management_free_team_owner_addseat_click(page):
    print("---- 57번 - 팀 관리 > Free / Team 오너 계정으로 [좌석 추가] 선택 시 요금 페이지 이동 확인 테스트 시작 ----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    #20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    #page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.get_by_role("button").nth(3).click(timeout=10000)
    page.wait_for_timeout(1000)

    page.get_by_text("팀 관리").click(timeout=10000)
    #20260316 - 대기 시간 1초 -> 2초 변경
    page.wait_for_timeout(2000)

    print("팀관리 페이지 진입 완료")
    #20260316 - 타임아웃 추가 및 대기 시간 1초 -> 2초 변경
    page.get_by_text("좌석 추가").click(timeout=10000)
    page.wait_for_timeout(2000)

    assert "당신의 세일즈를 위한 맞춤형 요금제" == page.get_by_role("heading", name="당신의 세일즈를 위한 맞춤형 요금제").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 타이틀 문구 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 1"
    assert "누구에게 팔지 막막할 때, 딥세일즈가 도와줄게요." == page.get_by_text("누구에게 팔지 막막할 때, 딥세일즈가 도와줄게요").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 타이틀 하단 > 가이드 문구 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 2"
    assert "월간" == page.get_by_role("button", name="월간").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 요금제 토글 버튼 '월간' 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 3"
    assert "연간\n-25%" == page.get_by_role("button", name="연간 -25%").inner_text(), \
        "팀관리 > Free > 좌석 추가 선택 시 요금제 페이지 > 요금제 토글 버튼 '연간 -25%' 확인 실패 - Free 계정의 요금제 결제 페이지 이동 실패 4"

    print("Free > 요금제 페이지 진입 완료")

    #20251024 - 헤더 > 탐색하기 삭제로 인해 제품 이용하기 버튼 이동으로 변경
    page.get_by_role("button", name="제품 이용하기").click()
    page.wait_for_timeout(2000)

    #20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정 (이전에 코드 블락처리)
    #page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    #20251215 - 상단 우측 마이페이지 버튼 선택 시 앨리먼트 요소가 나타낼때까지 기다리는 timeout 10초 추가
    page.get_by_role("button").nth(3).click(timeout=10000)
    #20251231 - 대기 1초 -> 2초로 수정
    page.wait_for_timeout(2000)

    #20251231 - 로그아웃 버튼 선택 전 앨리먼트 나올때까지 timeout 10초 코드 추가
    page.get_by_text("로그아웃").click(timeout=10000)
    page.wait_for_timeout(1000)

    print("Free 계정 로그아웃 후 로그인 페이지 진입 완료")
    page.get_by_placeholder("이메일").fill(config.TEAM_OWNER_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.TEAM_OWNER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    #20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    #page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.get_by_role("button").nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("팀 관리").click()
    page.wait_for_timeout(1000)

    print("Team 오너 계정 로그인 후 팀관리 페이지 진입 완료")
    page.get_by_text("좌석 추가").click()
    page.wait_for_timeout(1000)

    assert "플랜 변경하기" in page.locator("div").filter(has_text=re.compile(r"^Free\$0잠재고객을 처음 찾을 때, 부담 없이 시작하세요\.플랜 변경하기$")).get_by_role("button").inner_text(), \
        "팀관리 > Team owner > 좌석 추가 선택 후 요금제 페이지 > Elite > [플랜 변경하기] 버튼 확인 실패 - Team 오너 > 요금제 페이지 이동 실패 1"
    assert "요금제별 주요 기능 비교" == page.get_by_role("heading", name="요금제별 주요 기능 비교").inner_text(), \
        "팀관리 > Team owner > 좌석 추가 선택 후 요금제 페이지 > 요금제별 주요 기능 비교 영역 타이틀 문구 확인 실패 - Team 오너 > 요금제 페이지 이동 실패 2"

    print("팀 관리 > Free / Team 오너 계정으로 [좌석 추가] 선택 시 요금 페이지 이동 확인 테스트 시작 -> 성공")
