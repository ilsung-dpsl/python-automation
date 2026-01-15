import re
import config

def test_MO_gotoproduct_click_after_prospecting_page_move(mobile_page):
    print("---- 6번 - MO 제품 이용하기 페이지 이동 확인 케이스 시작 ----")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.get_by_role("banner").get_by_role("img").first.tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap()
    mobile_page.wait_for_timeout(1000)

    # 20250929 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    #lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    #lnb_hover_target.hover()
    #page.wait_for_timeout(2000

    # 20250929 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    #page.get_by_role("button").first.click()
    #page.wait_for_timeout(2000)

    mobile_page.get_by_role("link").filter(has_text=re.compile(r"^$")).tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="제품 이용하기").tap(timeout=10000)
    mobile_page.wait_for_timeout(2000)

    print("MO Web - 제품 이용하기 페이지 진입 완료")

    assert "예: 일본 화장품 제조사 세일즈 매니저" == mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").get_attribute("placeholder"), \
        "MO Web - 제품 이용하기 선택 후 탐색하기 > 프롬프트 > placeholder 확인 실패 - 제품 이용하기 선택 후 탐색하기 이동 실패 1"
    assert "필터" == mobile_page.get_by_text("필터", exact=True).inner_text(), \
        "MO Web - 제품 이용하기 선택 후 탐색하기 > 필터 > 필터 타이틀 문구 확인 실패 - 제품 이용하기 선택 후 탐색하기 이동 실패 2"
    assert "왼쪽 메뉴에서 필터를 선택하여 회사 검색을 시작하세요" in mobile_page.content(), \
        ("MO Web - 탐색하기 페이지 이동에 실패했습니다. - 제품 이용하기 선택 후 탐색하기 이동 실패 3")

    print("---- 6번 - MO 제품 이용하기 페이지 이동 확인 -> 성공 ----")