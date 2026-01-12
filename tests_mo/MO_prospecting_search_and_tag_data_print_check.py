import config
import re

def test_MO_prospecting_search_and_tag_data_print_check(mobile_page):
    print("----- 15번 - MO Web > AI 키워드 검색 후, Industry 필터에 산업군 추천 태그 노출, 필터 값, 결과 값 정상 작동 확인 (한글) 테스트 시작 ------")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # 20250930 - 탐색하기 UI 변경으로 인해, 탐색하기 > 프롬프트 창 선택 및 검색 버튼 선택 코드 수정
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").tap()
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("한국 화장품 유통회사를 찾아줘")
    mobile_page.locator("label").get_by_role("img").nth(1).tap()

    # 20250930 - 리드 데이터 대기 시간 10초 -> 12초로 코드 수정
    mobile_page.wait_for_timeout(12000)

    assert "도매 화장품" in mobile_page.content(), "탐색하기 > AI 산업군 > 키워드 1 노출 실패"
    #    assert "도매 의약품 및 잡화" in page.content(), "탐색하기 > AI 산업군 > 키워드 2 노출 실패"
    assert "소매 화장품" in mobile_page.content(), "탐색하기 > AI 산업군 > 키워드 3 노출 실패"

    assert "대한민국" in mobile_page.content(), "탐색하기 > 위치 필터 > 위치 키워드 1 노출 실패"

    assert "Wholesale" in mobile_page.content(), "탐색하기 > 리드 데이터 > 산업군 1 - Wholesale 확인 실패"
    assert "Retail" in mobile_page.content(), "탐색하기 > 리드 데이터 > 산업군 2 - Retail 확인 실패"

    assert "창준 백" in mobile_page.content(), "탐색하기 > 리드 데이터 1 성함 확인 실패"
    assert "준용 안" in mobile_page.content(), "탐색하기 > 리드 데이터 2 성함 확인 실패"

    print("----- 15번 - MO Web > AI 키워드 검색 후, Industry 필터에 산업군 추천 태그 노출, 필터 값, 결과 값 정상 작동 확인 (한글) 테스트 시작 -> 성공 ------")