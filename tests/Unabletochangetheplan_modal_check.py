import re

import config


def test_unabletochangetheplan_modal_check(page):
    print("------ 요금제 변경 불가 모달 출력 확인 및 팀오너 권한 확인 테스트 시작 ------")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_TEAM_MEMBER_AC)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_TEAM_MEMBER_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
  #  page.get_by_role("button", name="Start Now").click()
  #  page.wait_for_timeout(1000)
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    page.get_by_role("banner").get_by_role("link", name="가격").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="플랜 변경").nth(2).click()
    page.wait_for_timeout(1000)

    assert "요금제 변경 불가" in page.content(), "요금제 변경 불가 모달 미출력됨 1 -> 실패"""
    assert "팀오너가 아니면 요금제를 변경할 수 없습니다. 요금제를 변경하기 원하시면, 팀오너에게 요청해 주세요" in page.content(), "요금제 변경 불가 모달 미출력됨 2 -> 실패"
    assert "Okay" in page.content(), "요금제 변경 불가 모달 미출력됨 3 -> 실패"

    page.get_by_role("button", name="Okay").click()
    page.wait_for_timeout(1000)

    print("요금제 변경 불가 모달 출력 확인 및 팀오너 권한 확인 -> 성공")