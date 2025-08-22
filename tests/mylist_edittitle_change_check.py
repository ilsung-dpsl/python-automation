import config

def test_mylist_edittitle_change_check(page):
    print("----- 마이리스트 > 임의 폴더 제목 편집 변경 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA8_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA8_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)

    print("마이리스트 메인 페이지 진입 완료")
    page.get_by_role("button", name="리스트 만들기").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="/50").fill("test 1")
  #  page.get_by_role("button", name="확인").click(button="right")
    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("마이리스트 > 일반 폴더 1 생성 완료")
    page.locator("[id=\"headlessui-menu-button-:r13:\"]").click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="제목 편집").click()
    page.wait_for_timeout(1000)
    print("마이리스트 > 제목 편집 모달 노출 완료")
    page.get_by_role("textbox", name="/50").click()
    page.get_by_role("textbox", name="/50").fill("test 2")
    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(2000)

    assert "list_title_changed" == page.get_by_text("list_title_changed").inner_text(), \
        "마이리스트 > 제목 편집 수정 후 토스트 메시지 노출 실패 - 일반 폴더 제목 수정 실패 1"

    assert "test 2" == page.get_by_text("test").inner_text(), \
        "마이리스트 > 일반 폴더 제목 수정 실패 - 일반 폴더 제목 수정 실패 2"

    page.get_by_text("test").click()
    page.wait_for_timeout(1000)

    assert "test 2" == page.get_by_role("heading", name="test").inner_text(), \
        "마이리스트 상세(일반폴더) > 제목 변경 수정 실패 - 일반폴더 제목 수정 실패 3"

    print("마이리스트 > 일반 폴더 제목 편집 완료")
    page.get_by_role("button", name="리스트로 돌아가기").click()
    page.wait_for_timeout(1000)
    page.locator("[id=\"headlessui-menu-button-:r1g:\"]").click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="리스트 삭제").click()

    print("----- 마이리스트 > 임의 폴더 제목 편집 변경 확인 테스트 시작 -> 성공 -----")