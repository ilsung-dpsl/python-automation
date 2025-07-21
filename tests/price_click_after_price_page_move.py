def test_price_click_after_price_page_move(page):
    print("---- 요금제 및 결제 페이지 이동 확인 케이스 시작 ----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=50000)
    page.wait_for_timeout(1000)
    page.get_by_role("banner").get_by_role("link", name="가격").click()
    page.wait_for_timeout(3000)

    assert "요금제 및 가격" in page.content(), "요금제 및 가격 페이지 이동 실패 - 요금제 및 가격 타이틀 확인 x"
    assert "Free" in page.content(), "요금제 및 가격 페이지 이동 실패 - Free 플랜 영역 확인 x"
    assert "Pro" in page.content(), "요금제 및 가격 페이지 이동 실패 - Pro 플랜 영역 확인 x"
    assert "Elite" in page.content(), "요금제 및 가격 페이지 이동 실패 - Elite 플랜 영역 확인 x"
    assert "Enterprise" in page.content(), "요금제 및 가격 페이지 이동 실패 - Enterprise 플랜 영역 확인 x"

    print("---- 요금제 및 결제 페이지 정상 이동 -> 성공 ----")
