def test_signupforfree_move(page):
    print("--- 1번 - 회원가입 페이지 이동 테스트 시작 ---")

    #20251030 - 회원가입 페이지로 바로 이동 코드로 수정
    page.goto("https://deepsales.com/ko/login?page=signup",wait_until="load", timeout=60000)
    #page.locator("button:has-text('무료로 시작하기')").nth(1).click()
    #page.wait_for_timeout(5000)
    # 20251208 - 페이지 이동 후 대기 2초 -> 3초로 변경
    page.wait_for_timeout(3000)

    page.wait_for_selector("text=DeepSales에 오신 것을 환영합니다!", timeout=3000)

    assert "딥세일즈 | 가입하기" in page.title(), "회원가입 페이지 타이틀 확인 실패 - 회원가입 페이지 이동 실패 1"
    print("--- 회원가입 페이징 이동 완료 -> 성공")
