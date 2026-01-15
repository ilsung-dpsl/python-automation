import config

def test_MO_price_click_after_price_page_move(mobile_page):
    print("---- 7번 - MO 요금제 및 결제 페이지 이동 확인 케이스 시작 ----")

    mobile_page.goto("https://deepsales.com/ko/pricing", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(2000)

    assert "당신의 세일즈를 위한 맞춤형 요금제" in mobile_page.content(), \
        "MO Web - 요금제 및 가격 페이지 이동 실패 - 요금제 및 가격 타이틀 확인 x"
    assert "Free" in mobile_page.content(), \
        "MO Web - 요금제 및 가격 페이지 이동 실패 - Free 플랜 영역 확인 x"
    assert "Pro" in mobile_page.content(), \
        "MO Web - 요금제 및 가격 페이지 이동 실패 - Pro 플랜 영역 확인 x"
    assert "Elite" in mobile_page.content(), \
        "MO Web - 요금제 및 가격 페이지 이동 실패 - Elite 플랜 영역 확인 x"
    assert "Enterprise" in mobile_page.content(), \
        "MO Web - 요금제 및 가격 페이지 이동 실패 - Enterprise 플랜 영역 확인 x"

    print("---- 7번 - MO 요금제 및 결제 페이지 정상 이동 -> 성공 ----")