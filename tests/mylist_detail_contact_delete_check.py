import config
import re

def test_mylist_detail_contact_delete_check(page):
    print("----- 마이리스트 상세 (일반) > 연락처 삭제 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA17_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA17_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)

    print("마이리스트 페이지 진입 완료")

    page.get_by_text("test").click()
    page.wait_for_timeout(1000)

    print("마이리스트 상세 (일반) 페이지 진입 완료")

    #첫번째 리드 체크
    page.locator("[id=\":r1c:\"]").click()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="삭제").click()
    page.wait_for_timeout(500)

    assert "연락처 삭제 (1)" == page.get_by_text("연락처 삭제 (1)").inner_text(), \
        "연락처 삭제 모달 > 타이틀 문구 확인 실패 - 연락처 삭제 모달 출력 실패 1"
    assert "삭제" == page.locator("#modal-root").get_by_role("button", name="삭제").inner_text(), \
        "연락처 삭제 모달 > 삭제 버튼 확인 실패 - 연락처 삭제 모달 출력 실패 2"

    print("연락처 삭제 모달 출력 확인 완료")

    page.locator("#modal-root").get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)

    assert "연락처가 삭제되었습니다." == page.locator("div").filter(has_text=re.compile(r"^연락처가 삭제되었습니다\.$")).nth(1).inner_text(), \
        "연락처 삭제 후 연락처 삭제 토스트 메시지 출력 실패 - 연락처 삭제 완료 실패 3"

    print("----- 마이리스트 상세 (일반) > 연락처 삭제 확인 테스트 시작 -> 성공-----")

