import config
import re

def test_MO_mylist_detail_contact_delete_check(mobile_page):
    print("----- 29번 - MO 마이리스트 상세 (일반) > 연락처 삭제 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA17_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA17_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 마이리스트 페이지 진입 완료")

    mobile_page.get_by_text("test").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 마이리스트 상세 (일반) 페이지 진입 완료")

    # 20250930 - 첫번째 리드 체크 코드 수정
    mobile_page.locator(".ml-\\[2px\\] > .flex.items-center.space-x-3").first.tap()
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("button", name="삭제").tap()
    mobile_page.wait_for_timeout(500)

    assert "연락처 삭제 (1)" == mobile_page.get_by_text("연락처 삭제 (1)").inner_text(), \
        "MO Web - 연락처 삭제 모달 > 타이틀 문구 확인 실패 - 연락처 삭제 모달 출력 실패 1"
    assert "삭제" == mobile_page.locator("#modal-root").get_by_role("button", name="삭제").inner_text(), \
        "MO Web - 연락처 삭제 모달 > 삭제 버튼 확인 실패 - 연락처 삭제 모달 출력 실패 2"

    print("MO Web - 연락처 삭제 모달 출력 확인 완료")

    mobile_page.locator("#modal-root").get_by_role("button", name="삭제").tap()
    mobile_page.wait_for_timeout(1000)

    assert "연락처가 삭제되었습니다." == mobile_page.locator("div").filter(has_text=re.compile(r"^연락처가 삭제되었습니다\.$")).nth(1).inner_text(), \
        "MO Web - 연락처 삭제 후 연락처 삭제 토스트 메시지 출력 실패 - 연락처 삭제 완료 실패 3"

    print("----- 29번 - MO 마이리스트 상세 (일반) > 연락처 삭제 확인 테스트 시작 -> 성공-----")