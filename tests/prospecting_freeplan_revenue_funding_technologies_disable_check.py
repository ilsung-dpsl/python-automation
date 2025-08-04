import re

import config


def test_prospecting_freeplan_revenue_funding_technologies_unavailable_check(page):
    print("----- (Free 플랜) 탐색하기 > 필터 > 연간 매출 / 펀딩 / 기술 필터 > 사용 불가 동작 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
  #  page.wait_for_timeout(1000)
  #  page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(3000)

    page.locator("div:nth-child(9) > div > div:nth-child(2) > .transition-transform").click()
    page.wait_for_timeout(1000)
    page.get_by_text("$0~$1M").click()
    page.wait_for_timeout(2000)

    assert "이런... 고급 필터는 Pro" in page.content(), "요금제 업그레이드 모달 안내 출력 실패 1 - 연간매출"
    assert "요금제 업그레이드" in page.content(), "요금제 업그레이드 모달 안내 > [요금제 업그레이드] 버튼 확인 실패 1 - 연간매출"
    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.wait_for_timeout(1000)

    page.locator("svg:nth-child(3)").first.click()
    page.wait_for_timeout(1000)
    page.get_by_role("checkbox", name="기타").click()
    page.wait_for_timeout(2000)

    assert "플랜을 변경하고 더 많은 잠재고객을 만나보세요. AI" in page.content(), "요금제 업그레이드 모달 안내 > 가이드 문구 출력 실패 2 - 펀딩"
    assert "요금제 업그레이드" in page.content(), "요금제 업그레이드 모달 안내 > [요금제 업그레이드] 버튼 확인 실패 2 - 펀딩"
    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.wait_for_timeout(1000)

    page.locator("div:nth-child(23) > div > div:nth-child(2) > .transition-transform").click()
    page.wait_for_timeout(500)
    page.locator(".pt-1 > .flex > .flex-1 > .border").click()
    page.wait_for_timeout(500)
    page.locator("#react-select-5-input").fill("google drive")
    page.wait_for_timeout(500)
    page.get_by_text("Google Drive", exact=True).click()

  #  page.locator("#react-select-4-input").fill("google drive")
  #  page.wait_for_timeout(500)
  #  page.get_by_text("Google Drive", exact=True).click()
    page.wait_for_timeout(2000)

    assert "플랜을 변경하고 더 많은 잠재고객을 만나보세요. AI" in page.content(), "요금제 업그레이드 모달 안내 > 가이드 문구 출력 실패 3 - 기술"
    assert "요금제 업그레이드" in page.content(), "요금제 업그레이드 모달 안내 > [요금제 업그레이드] 버튼 확인 실패 3 - 기술"
    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.wait_for_timeout(1000)
    
    print("----- (Free 플랜) 탐색하기 > 필터 > 연간 매출 / 펀딩 / 기술 필터 > 사용 불가 동작 확인 테스트 시작 -> 성공 -----")

#    page.get_by_text("이런... 고급 필터는 Pro").dblclick()
#    page.get_by_role("button", name="요금제 업그레이드").click()
#    page.get_by_role("banner").get_by_role("link", name="탐색하기").click()
