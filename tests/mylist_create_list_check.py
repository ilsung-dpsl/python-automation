import config
import re

def test_mylist_create_list_check(page):
    print("----- 마이리스트 > 리스트 생성 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA8_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA8_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)

    print("마이리스트 페이지 진입 완료")
    page.get_by_role("button", name="리스트 만들기").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="/50").fill("마이리스트 test 생성 1")
    page.get_by_role("button", name="확인").click()

    page.wait_for_timeout(1000)

    assert "선택한 연락처가 추가되었습니다." == page.locator("div").filter(has_text=re.compile(r"^선택한 연락처가 추가되었습니다\.$")).nth(1).inner_text(), \
        "리스트 생성 추가 토스트 메시지 출력 실패 - 리스트 생성 실패 1"

    page.wait_for_timeout(1000)

    assert "마이리스트 test 생성 1" == page.get_by_text("마이리스트 test 생성").inner_text(), \
        "마이리스트 생성 후 생성한 일반 폴더명 확인 실패 - 리스트 생성 실패 2"

    assert "0" == page.get_by_text("0", exact=True).nth(1).inner_text(), \
        f"마이리스트 생성 후 생성한 일반 폴더 > 연락처 '0' 확인 실패 - 리스트 생성 실패 3"

    page.wait_for_timeout(2000)

    print("마이리스트 생성 후 확인 완료")

    page.locator("[id=\"headlessui-menu-button-:r13:\"]").click()
    page.wait_for_timeout(2000)

    page.get_by_role("menuitem", name="리스트 삭제").click()
    page.wait_for_timeout(1000)

    print("----- 마이리스트 > 리스트 생성 확인 테스트 시작 -> 성공 -----")
