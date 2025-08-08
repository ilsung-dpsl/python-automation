def test_signupforfree_move(page):
    print("--- 회원가입 페이지 이동 테스트 시작 ---")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=60000)
    page.locator("button:has-text('무료로 시작하기')").nth(1).click()

    page.wait_for_timeout(5000)

    page.wait_for_selector("text=DeepSales에 오신 것을 환영합니다!", timeout=3000)

    assert "딥세일즈 | 가입하기" in page.title(), "회원가입 페이지 타이틀 확인 실패 - 회원가입 페이지 이동 실패 1"
    assert "가입하기" in page.title(), "가입하기 버튼 확인 실패 - 회원가입 페이지 이동 실패 2"
    print("--- 회원가입 페이징 이동 완료 -> 성공")
