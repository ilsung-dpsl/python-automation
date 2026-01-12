import config
import re

def test_MO_prospecting_addtolist_flow_check(mobile_page):
    print("----- 22번 - MO 탐색하기 > 리스트에 추가 동작 확인 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PRD3_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PRD3_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").tap()
    # 검색어 변경 - 20250805
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("let's travel 회사의 직원 정보를 찾아줘")
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")
    mobile_page.wait_for_timeout(6000)

    # 20240930 - 탐색하기 ui 변경으로 인한 리드 > 1번, 2번 체크 동작 코드 수정
    mobile_page.locator("div > .w-8 > .flex").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.locator("div:nth-child(2) > div > .w-8 > .flex").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="리스트에 추가").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="새 리스트 생성").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("textbox", name="/50").fill("test 1")
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("button", name="생성하기").tap()
    mobile_page.wait_for_timeout(2000)

    assert "test 1" in mobile_page.content(), "마이리스트 폴더 생성 실패 - 리스트 생성 실패"

    mobile_page.locator("div").filter(has_text=re.compile(r"^default$")).first.tap()
    mobile_page.locator("div").filter(has_text=re.compile(r"^test 1$")).first.tap()

    mobile_page.get_by_role("button", name="확인", exact=True).tap()
    mobile_page.wait_for_timeout(5000)

    # 20250930 - LNB > 대시보드 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(3000)

    # 20250930 - 기본 폴더 선택 동작 코드 수정
    mobile_page.locator("div").filter(has_text=re.compile(r"^기본$")).nth(1).tap()
    mobile_page.wait_for_timeout(3000)

    # Default 폴더 > 데이터 위치 변경으로 인한 리드 데이터 정보 수정 - 20250829
    assert "Gayle Botti" in mobile_page.content(), "Default 폴더 test 1의 리드 1번 성함 확인 실패 - 리스트에 추가 실패 1"
    assert "Stalin Stalinsjc" in mobile_page.content(), "Default 폴더 test 1의 리드 2번 성함 확인 실패 - 리스트에 추가 실패 1"
    mobile_page.get_by_role("button", name="리스트로 돌아가기").tap()

    mobile_page.wait_for_timeout(3000)
    mobile_page.locator("div").filter(has_text=re.compile(r"^test 1$")).nth(1).tap()
    mobile_page.wait_for_timeout(3000)

    # test 폴더 > 데이터 위치 변경으로 인한 리드 데이터 정보 수정 - 20250829
    assert "Gayle Botti" in mobile_page.content(), "일반 폴더 test 1의 리드 1번 성함 확인 실패 - 리스트에 추가 실패 2"
    assert "Stalin Stalinsjc" in mobile_page.content(), "일반 폴더 test 1의 리드 2번 성함 확인 실패 - 리스트에 추가 실패 2"

    mobile_page.get_by_role("button", name="리스트로 돌아가기").tap()

    mobile_page.wait_for_timeout(3000)

    # 20250930 - 기본 폴더 선택 동작 코드 수정
    mobile_page.locator("div").filter(has_text=re.compile(r"^기본$")).nth(1).tap()

    # Default 폴더 > 리스트 1, 2 체크 동작 코드 수정 - 20250805
    mobile_page.locator(".ml-\\[2px\\] > .flex").first.tap()
    mobile_page.locator("div:nth-child(2) > div > .ml-\\[2px\\] > .flex").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="삭제").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.locator("#modal-root").get_by_role("button", name="삭제").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="리스트로 돌아가기").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.locator("div").filter(has_text=re.compile(r"^test 1$")).nth(1).tap()

    # test 1 폴더 > 리스트 1, 2 체크 동작 코드 수정 - 20250805
    mobile_page.locator(".ml-\\[2px\\] > .flex").first.tap()
    mobile_page.locator("div:nth-child(2) > div > .ml-\\[2px\\] > .flex").tap()

    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="삭제").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.locator("#modal-root").get_by_role("button", name="삭제").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="리스트로 돌아가기").tap()
    mobile_page.wait_for_timeout(3000)
    mobile_page.locator("div:nth-child(3) > div:nth-child(6) > div").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("menuitem", name="리스트 삭제").tap()
    mobile_page.wait_for_timeout(3000)

    print("----- 22번 - MO 탐색하기 > 리스트에 추가 동작 확인 테스트 시작 -> 성공 -----")