import re

def test_b_type_randing_prompt_print(page):
    print("----- B안 랜딩페이지 > 프롬프트 영역 확인 테스트 시작 ------")
    page.goto("https://deepsales.com/ko/search",wait_until="load", timeout=30000)


    assert "담당자 이름, 이메일, 전화번호까지" in page.content(), "B안 랜딩페이지 > 타이틀 문구 1 출력 실패 - B안 랜딩페이지 확인 실패"
    assert "글로벌 바이어 연락처 모음" in page.content(), "B안 랜딩페이지 > 타이틀 문구 2 출력 실패 - B안 랜딩페이지 확인 실패"
    assert "미국의 화장품 회사 마케터 찾아줘" in page.content(), "B안 랜딩페이지 > 하단 > 추천 검색어 1 출력 실패 - B안 랜딩페이지 확인 실패"
    assert "프랑스의 여행 매니저를 찾아줘" in page.content(), "B안 랜딩페이지 > 하단 > 추천 검색어 5 출력 실패 - B안 랜딩페이지 확인 실패"

    page.wait_for_timeout(2000)

    print("----- B안 랜딩페이지 > 프롬프트 영역 확인 테스트 시작 -> 성공 ------")
