import config
import re

def test_mylist_delete_list_check(page):

    print("----- 46번 - 마이리스트 > 리스트 삭제 확인 테스트 시작 -----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    # 20260119 - PA18 일반 무료 계정으로 변경
    page.get_by_placeholder("이메일").fill(config.FREE_PA18_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA18_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="마이 리스트").nth(1).click()
    page.wait_for_timeout(5000)

    print("마이리스트 페이지 진입 완료")

    #20250930 - 대기 시간 0.5초 코드 추가
    page.get_by_role("button", name="리스트 만들기").click()
    page.wait_for_timeout(500)
    page.get_by_role("textbox", name="/50").fill("test 1")
    page.wait_for_timeout(500)
    page.get_by_role("button", name="확인").click()
    #20260107 - 리스트 생성 후 3초 -> 4초로 수정
    page.wait_for_timeout(4000)

    print("리스트 생성 완료 후")

    #20260107 - 새로 생성한 일반 폴더 리스트 > 더보기 버튼 선택 코드 -> 타임아웃 10초 추가
    page.locator("div:nth-child(3) > div:nth-child(6) > div").click(timeout=10000)
    #20260107 - 대기 시간 3초 -> 4초로 수정
    page.wait_for_timeout(4000)

    #20260107 - 앨리먼트 나타날 때까지 타임아웃 대기 10초 추가 / 2초 -> 2.5초로 대기 수정
    page.get_by_role("menuitem", name="리스트 삭제").click(timeout=10000)
    #20260113 - 2.5초 -> 2초로 변경
    page.wait_for_timeout(2000)

    assert "리스트가 삭제되었습니다." == page.locator("div").filter(has_text=re.compile(r"^리스트가 삭제되었습니다\.$")).nth(1).inner_text(), \
        "리스트 삭제 후 리스트 삭제 토스트 메시지 확인 실패 - 리스트 삭제 실패 1"
    #20260113 - 리스트 삭제 후 3초 대기 (test 1의 tag 코드가 남아있을 수 있음)
    page.wait_for_timeout(3000)

    assert "test 1" not in page.content(), "리스트 정상 삭제 실패 - 리스트 삭제 실패 2"

    print("----- 46번 - 마이리스트 > 리스트 삭제 확인 테스트 시작 -> 성공 -----")

