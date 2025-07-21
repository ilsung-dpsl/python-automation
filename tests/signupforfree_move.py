def test_signupforfree_move(page):
    print("--- 회원가입 페이지 이동 테스트 시작 ---")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=60000)
    page.locator("button:has-text('무료로 시작하기')").nth(1).click()

    page.wait_for_timeout(5000)

    page.wait_for_selector("text=DeepSales에 오신 것을 환영합니다!", timeout=3000)

    assert "DeepSales: Sign Up" in page.title(), "회원가입 페이지 이동 실패했습니다"
    print("--- 회원가입 페이징 이동 완료 -> 성공")
