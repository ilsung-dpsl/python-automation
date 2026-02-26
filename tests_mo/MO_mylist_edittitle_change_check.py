import config

def test_MO_mylist_delete_list_check(mobile_page):
    print("----- 26번 - MO 마이리스트 > 임의 폴더 제목 편집 변경 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    # 20260119 - PA18 일반 무료 계정으로 변경
    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA18_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA18_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 마이리스트 메인 페이지 진입 완료")

    mobile_page.get_by_role("button", name="리스트 만들기").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("textbox", name="/50").fill("test 1")
    mobile_page.wait_for_timeout(500)
  #  page.get_by_role("button", name="확인").click(button="right")
    mobile_page.get_by_role("button", name="확인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 마이리스트 > 일반 폴더 1 생성 완료")

    #20250930 - 마이리스트 > test 1 일반 폴더 > 더보기 버튼 선택 코드 수정
    mobile_page.locator("div:nth-child(3) > div:nth-child(6) > div").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("menuitem", name="제목 편집").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)
    print("MO Web - 마이리스트 > 제목 편집 모달 노출 완료")
    mobile_page.get_by_role("textbox", name="/50").tap()
    mobile_page.get_by_role("textbox", name="/50").fill("test 2")
    mobile_page.get_by_role("button", name="확인").tap()
    mobile_page.wait_for_timeout(2000)

    assert "list_title_changed" == mobile_page.get_by_text("list_title_changed").inner_text(), \
        "MO Web - 마이리스트 > 제목 편집 수정 후 토스트 메시지 노출 실패 - 일반 폴더 제목 수정 실패 1"

    assert "test 2" == mobile_page.get_by_text("test").inner_text(), \
        "MO Web - 마이리스트 > 일반 폴더 제목 수정 실패 - 일반 폴더 제목 수정 실패 2"

    mobile_page.get_by_text("test").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    assert "test 2" == mobile_page.get_by_role("heading", name="test").inner_text(), \
        "MO Web - 마이리스트 상세(일반폴더) > 제목 변경 수정 실패 - 일반폴더 제목 수정 실패 3"

    print("MO Web - 마이리스트 > 일반 폴더 제목 편집 완료")
    mobile_page.get_by_role("button", name="리스트로 돌아가기").tap()
    mobile_page.wait_for_timeout(1000)

    #20250930 - 마이리스트 > test 1 일반 폴더 > 더보기 버튼 선택 코드 수정
    mobile_page.locator("div:nth-child(3) > div:nth-child(6) > div").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("menuitem", name="리스트 삭제").tap()

    print("----- 26번 - MO 마이리스트 > 임의 폴더 제목 편집 변경 확인 테스트 시작 -> 성공 -----")