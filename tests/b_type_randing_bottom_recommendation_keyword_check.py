
def test_b_type_randing_bottom_recommendation_keyword_check(page):
    print("----- B안 랜딩페이지 > 하단 > 추천 검색어 3 선택 시 프롬프트 입력 확인 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/search",wait_until="load", timeout=30000)
    page.get_by_text("일본의 패션 브랜드 상품기획자에 대해 알려줘").click()
    page.get_by_role("textbox").click()
    page.wait_for_timeout(1000)

    assert "추천 검색어" in page.content(), "프롬프트 내 추천 검색어 타이틀 문구 출력 실패"
#    assert "일본의 패션 브랜드 상품기획자에 대해 알려줘" in page.content(), "프롬프트 하단 > 추천 검색어 3 설정 후 프롬프트 자동 입력 실패"
    assert "일본의 패션 브랜드 상품기획자에 대해 알려줘" == page.get_by_role("textbox").input_value(), "fail"

    page.get_by_role("textbox").click()
    page.wait_for_timeout(1000)

    print("----- B안 랜딩페이지 > 하단 > 추천 검색어 3 선택 시 프롬프트 입력 확인 테스트 시작 -> 성공 -----")