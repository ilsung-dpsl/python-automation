import config

def test_prospecting_company_companyname_click_and_company_info_move(page):
    print("----- 회사 리스트 중 회사 이름 선택 시 회사 상세페이지 이동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("일본 화장품 제조사 세일즈 매니저")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    print("탐색하기 > 검색 완료")

    page.get_by_role("tab", name="회사(3)").click()
    page.wait_for_timeout(1000)

    with page.expect_popup() as page1_info:
        page.locator("[id=\"__next\"]").get_by_text("Nikko Chemicals").click()
    page1 = page1_info.value

    page.wait_for_timeout(3000)

    assert "Nikko Chemicals" == page1.locator(".text-\\[18px\\]").first.inner_text(), \
        "회사정보 페이지 > 회사명칭 확인 실패 - 회사리스트 > 회사명 선택 후 회사 정보 페이지 이동 실패 1"
    assert "Japan" == page1.get_by_text("Japan").inner_text(), \
        "회사정보 페이지 > 위치 > Japan 확인 실패 - 회사리스트 > 회사명 선택 후 회사 정보 페이지 이동 실패 2"
    assert ("NIKKOL is a company that manufactures chemical products, including cosmetics and other personal care items. "
            "The company has a strong focus on corporate social responsibility (CSR) and sustainability, "
            "with goals aligned with the United Nations' Sustainable Development Goals (SDGs).") == page1.get_by_text("NIKKOL is a company that").inner_text(), \
        "회사정보 페이지 > 설명 > 설명 내용 확인 실패 - 회사리스트 > 회사명 선택 후 회사 정보 페이지 이동 실패 3"
    assert "18" == page1.get_by_text("18").inner_text(), \
        "회사정보 페이지 > 직원 통계 > 기타 > 직원 수 확인 실패 - 회사리스트 > 회사명 선택 후 회사 정보 페이지 이동 실패 4"

    print("----- 회사 리스트 중 회사 이름 선택 시 회사 상세페이지 이동 확인 테스트 시작 -> 성공 -----")