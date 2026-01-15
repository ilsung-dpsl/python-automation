import config
import re

def test_MO_discover_industry_and_title_search(mobile_page):
    print("----- 37번 - MO 발견하기 > 산업군 + 타이틀 문구 키워드 검색 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    # 20250930 - LNB > 발견하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="발견하기").tap()
    mobile_page.wait_for_timeout(3000)

    print("MO Web - 발견하기 페이지 진입 완료")
    mobile_page.get_by_text("고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").tap()
    mobile_page.wait_for_timeout(1000)

    # 페르소나 설정 안내 모달 > 나중에 하기 버튼 선택으로 모달을 닫는다.
    mobile_page.get_by_role("button", name="나중에 하기").tap()
    mobile_page.wait_for_timeout(2000)

    print("MO Web - 페르소나 설정 안내 모달 닫은 후 발견하기 페이지 노출")

    # 산업군 필터 > 모든 산업 입력 후 설정
    mobile_page.locator(".text-FG-Primary.css-124rwol").tap()
    mobile_page.wait_for_timeout(500)

    mobile_page.keyboard.type("모든 산업")
    mobile_page.wait_for_timeout(500)
    mobile_page.locator("#react-select-2-input").press("Enter")
    mobile_page.wait_for_timeout(500)

    #mobile_page.get_by_role("option", name="모든 산업").locator("div").tap(timeout=10000)
    #mobile_page.wait_for_timeout(1000)

    print("MO Web - 발견하기 > 산업군 > 모든 산업군 설정 완료")
    mobile_page.get_by_placeholder("제목으로 찾기").fill("직원 수 200명 규모")
    mobile_page.get_by_placeholder("제목으로 찾기").press("Enter")

    print("MO Web - 발견하기 > 산업군 + 검색 설정 완료")
    mobile_page.wait_for_timeout(2000)

    assert "숙박 서비스" == mobile_page.get_by_text("숙박 서비스").inner_text(), \
        "MO Web - 발견하기 > 검색된 카드 > 산업군 키워드 확인 실패 - 산업군 + 타이틀 검색 실패 1"
    assert "직원 수 200명 규모의 럭셔리 호스피탈리티 서비스 제공 업체 리스트" == mobile_page.get_by_role("heading", name="직원 수 200").inner_text(), \
        "MO Web - 발견하기 > 검색된 카드 > 타이틀 문구 확인 실패 - 산업군 + 타이틀 검색 실패 2"
    assert "Hospitality, 50 - 200" == mobile_page.locator("[id=\"__next\"]").get_by_text("Hospitality, 50 -").inner_text(), \
        "MO Web - 발견하기 > 검색된 카드 > 키워드 문구 확인 실패 - 산업군 + 타이틀 검색 실패 3"

    print("----- 37번 - MO 발견하기 > 산업군 + 타이틀 문구 키워드 검색 테스트 시작 -> -----")