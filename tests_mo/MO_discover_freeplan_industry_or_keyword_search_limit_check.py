import config
import re

def test_MO_discover_freeplan_industy_or_keyword_search_limit_check(mobile_page):
    print("---- 21번 - MO 발견하기 > 무료 회원 사용자 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출 확인 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA9_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA9_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # 20250930 - LNB > 발견하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="발견하기").tap()
    mobile_page.wait_for_timeout(3000)

    print("MO Web - 발견하기 페이지 진입")

    mobile_page.get_by_text("고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 페르소나 설정 안내 모달 출력 완료")

    # 페르소나 설정 안내 모달 > 나중에 하기 버튼 선택으로 모달을 닫는다.
    mobile_page.get_by_role("button", name="나중에 하기").tap()
    mobile_page.wait_for_timeout(2000)

    # 산업군 필터 선택하는 코드
    mobile_page.locator(".cursor-pointer").first.tap()
    mobile_page.wait_for_timeout(2000)

    print("MO Web - 요금제 제한 안내 모달 노출 전")

    assert "이런! 무료 플랜에서는 키워드 검색 및\n필터 사용이 제한됩니다." == mobile_page.locator("header").filter(
        has_text="이런! 무료 플랜에서는 키워드 검색 및 필터 사용이 제한됩니다").inner_text(), \
        "MO Wew - 요금제 제한 안내 모달 > 타이틀 문구 노출 실패 - 발견하기 산업군 탐색 시 요금제 제한 안내 모달 출력 실패 1"
    assert "요금제 업그레이드" == mobile_page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "MO Wew - 요금제 제한 안내 모달 > 요금제 업그레이드 버튼 노출 실패 - 발견하기 산업군 탐색 시 요금제 제한 안내 모달 출력 실패 2"

    print("MO Wew - 요금제 제한 안내 모달 노출 확인 완료")

    # 산업군 > 제목 입력창 선택하는 코드
    mobile_page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).tap()

    # 20251014 - 키워드 검색 시 제한 수정으로 인해 코드 추가
    mobile_page.get_by_placeholder("제목으로 찾기").fill("도매")
    mobile_page.get_by_placeholder("제목으로 찾기").press("Enter")

    mobile_page.wait_for_timeout(1000)

    assert "이런! 무료 플랜에서는 키워드 검색 및\n필터 사용이 제한됩니다." == mobile_page.locator("header").filter(
        has_text="이런! 무료 플랜에서는 키워드 검색 및 필터 사용이 제한됩니다").inner_text(), \
        "MO Web - 요금제 제한 안내 모달 > 타이틀 문구 노출 실패 - 발견하기 키워드 탐색 시 요금제 제한 안내 모달 출력 실패 3"
    assert "플랜을 변경하고 더 많은 잠재고객을 만나보세요." in mobile_page.get_by_text("플랜을 변경하고 더 많은 잠재고객을 만나보세요. AI").inner_text(), \
        "MO Web - 요금제 제한 안내 모달 > 안내 문구 노출 실패 - 발견하기 키워드 탐색 시 요금제 제한 안내 모달 출력 실패 4"

    mobile_page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).tap()

    print("----- 21번 - MO 발견하기 > 무료 회원 사용자 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출 확인 테스트 시작 -> 성공 -----")