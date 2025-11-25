import re

import config


def test_unabletochangetheplan_modal_check(page):
    print("------ 10번 - 요금제 변경 불가 모달 출력 확인 및 팀오너 권한 확인 테스트 시작 ------")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_TEAM_MEMBER_AC)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_TEAM_MEMBER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
  #  page.get_by_role("button", name="Start Now").click()
  #  page.wait_for_timeout(1000)

    # 20250929 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250929 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    page.get_by_role("link").filter(has_text=re.compile(r"^$")).nth(1).click()
    page.wait_for_timeout(1000)

    # 20251125 - 가격 할인 페이지 삭제로 인해, 일반 가격 페이지 url 변경되어 코드 수정
    page.goto("https://deepsales.com/ko/pricing", wait_until="load", timeout=50000)
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="플랜 변경").nth(2).click()
    page.wait_for_timeout(1000)

    assert "요금제 변경 불가" in page.content(), "요금제 변경 불가 모달 미출력됨 1 -> 실패"""
    assert "팀오너가 아니면 요금제를 변경할 수 없습니다. 요금제를 변경하기 원하시면, 팀오너에게 요청해 주세요" in page.content(), "요금제 변경 불가 모달 미출력됨 2 -> 실패"
    assert "Okay" in page.content(), "요금제 변경 불가 모달 미출력됨 3 -> 실패"

    page.get_by_role("button", name="Okay").click()
    page.wait_for_timeout(1000)

    print("요금제 변경 불가 모달 출력 확인 및 팀오너 권한 확인 -> 성공")