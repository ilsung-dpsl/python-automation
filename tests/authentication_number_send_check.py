import config


def test_authentication_number_send_check(page):
    print("--- 인증번호 전송 체크 시작 ---")
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    page.get_by_role("button", name="무료로 시작하기").nth(1).click()
    page.get_by_placeholder("예) deepsales@deepsales.com").fill(config.FREE_ACCOUNT_CHECK)
    page.get_by_role("button", name="전송").click()

    page.wait_for_timeout(2000)
    page.get_by_placeholder("OTP를 입력해주세요").click()

    assert "OTP를 입력해주세요" in page.content(), "인증번호 입력창 노출 실패"
    assert "확인" in page.content(), "인증번호 확인 버튼 노출 실패"

    print("--- 인증번호 전송 확인 완료 -> 성공")