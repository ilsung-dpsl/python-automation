import config
import re

def test_mylist_delete_list_check(page):

    print("----- 마이리스트 > 리스트 삭제 확인 테스트 시작 -----")

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
    page.get_by_role("textbox", name="/50").fill("test 1")
    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("리스트 생성 완료 후")

    page.locator("[id=\"headlessui-menu-button-:r13:\"]").click()
    page.get_by_role("menuitem", name="리스트 삭제").click()

    page.wait_for_timeout(2000)

    assert "리스트가 삭제되었습니다." == page.locator("div").filter(has_text=re.compile(r"^리스트가 삭제되었습니다\.$")).nth(1).inner_text(), \
        "리스트 삭제 후 리스트 삭제 토스트 메시지 확인 실패 - 리스트 삭제 실패 1"
    assert "test 1" not in page.content(), "리스트 정상 삭제 실패 - 리스트 삭제 실패 2"

    print("----- 마이리스트 > 리스트 삭제 확인 테스트 시작 -> 성공 -----")

