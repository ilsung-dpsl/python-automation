import re

import config


def test_b_type_randing_recommendation_keyword_search_integration(page):
    print("----- B안 랜딩페이지 > 임의 추천검색어 1 검색 후 로그인 시 탐색하기 연동 확인 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/search",wait_until="load", timeout=30000)
    page.get_by_role("textbox").click()
    page.wait_for_timeout(1000)
    page.get_by_text("기술 협력을 위한 인도 SaaS R&D 엔지니어").click()
    page.get_by_role("img", name="search button enabled").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
#    page.wait_for_timeout(1000)
#    page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(7000)

   # assert "기술 협력을 위한 인도 SaaS R&D 엔지니어" in page.get_by_role("textbox", name="search button enabled").inner_text(), "추천검색어 1 출력 실패 - 탐색하기 연동 실패 1"

    element = page.locator("input[placeholder='예: 일본 화장품 제조사 세일즈 매니저']")
    prompt_inputtext = element.input_value()

    assert "기술 협력을 위한 인도 SaaS R&D 엔지니어" == prompt_inputtext, "탐색하기 > 검색창 > 임의 추천검색어 1 출력 실패 - 탐색하기 연동 실패"
    assert "인도" in page.content(), "탐색하기 > 필터 > 위치 > 인도 키워드 출력 실패 - 탐색하기 연동 실패"
    assert "기술, 정보 및 인터넷" in page.content(), "탐색하기 > 필터 > 산업군 > 키워드 출력 실패 - 탐색하기 연동 실패"
    #리드 데이터 1 성함 변경 - 20250805
    assert "Professional Services" in page.content(), "탐색하기 > 리드 영역 > 산업군 > 'Professional Services' 출력 실패 - 탐색하기 연동 실패"

    print("---- ")
