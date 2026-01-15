import config
import re

def test_MO_mylist_create_list_check(mobile_page):
    print("----- 42번 - MO 마이리스트 > 리스트 생성 확인 테스트 시작 -----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA8_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA8_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 마이리스트 페이지 진입 완료")

    mobile_page.get_by_role("button", name="리스트 만들기").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("textbox", name="/50").fill("마이리스트 test 생성 1")
    #20250930 - 대기 시간 1초 코드 추가
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="확인").tap()
    mobile_page.wait_for_timeout(1000)

    assert "선택한 연락처가 추가되었습니다." == mobile_page.locator("div").filter(has_text=re.compile(r"^선택한 연락처가 추가되었습니다\.$")).nth(1).inner_text(), \
        "MO Web - 리스트 생성 추가 토스트 메시지 출력 실패 - 리스트 생성 실패 1"

    mobile_page.wait_for_timeout(1000)

    assert "마이리스트 test 생성 1" == mobile_page.get_by_text("마이리스트 test 생성").inner_text(), \
        "MO Web - 마이리스트 생성 후 생성한 일반 폴더명 확인 실패 - 리스트 생성 실패 2"

    assert "0" == mobile_page.get_by_text("0", exact=True).nth(1).inner_text(), \
        f"MO Web - 마이리스트 생성 후 생성한 일반 폴더 > 연락처 '0' 확인 실패 - 리스트 생성 실패 3"

    mobile_page.wait_for_timeout(2000)

    print("MO Web - 마이리스트 생성 후 확인 완료")

    # 20250930 - 새로 생성한 일반 폴더 리스트 > 더보기 버튼 선택 코드 수정
    mobile_page.locator("div:nth-child(3) > div:nth-child(6) > div").tap()
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_role("menuitem", name="리스트 삭제").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 생성한 일반 폴더 삭제 완료")
    print("----- 42번 - MO 마이리스트 > 리스트 생성 확인 테스트 시작 -> 성공 -----")
