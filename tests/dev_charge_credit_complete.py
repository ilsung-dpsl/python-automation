import re

def test_charge_credit_complete(page):
    print("----- 크레딧 충전하기 > 충전 완료 테스트 시작 > DEV 기준으로 작성 -----")

    page.goto("https://dev.deepsales.io/ko/intro", wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill("ilsung.baek+devtest116@deepsales.com")
    page.get_by_placeholder("비밀번호").fill("!deepsales@36")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(500)
    page.get_by_text("결제 및 요금제").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="크레딧 충전").click()
    page.wait_for_timeout(500)
    page.locator(".text-FG-Primary.css-124rwol").click()
    page.get_by_text("300 크레딧").click()
    page.get_by_text("결제를 진행하는 모든 조건들에 동의합니다").click()
    page.get_by_role("button", name="결제하기").click()

    page.wait_for_timeout(10000)

    assert "결제 성공!" in page.content(), "결제 성공 완료 모달 > 타이틀 문구 출력 실패 - 크레딧 충전 실패 1"
    assert "결제가 완료되었으며 크레딧이 충전되었습니다" in page.content(), "결제 성공 완료 모달 > 가이드 문구 출력 실패 - 크레딧 충전 실패 2"
    page.get_by_role("button", name="Okay").click()
    page.wait_for_timeout(1000)

    assert "ELITE" in page.content(), "결제 및 요금제 페이지 > 요금제 출력 실패 - 크레딧 충전 후 페이지 유지 실패"

    print("----- 크레딧 충전하기 > 충전 완료 테스트 시작 -> 성공 -----")
