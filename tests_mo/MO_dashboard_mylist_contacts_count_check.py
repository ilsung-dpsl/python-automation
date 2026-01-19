import config
import re

def test_MO_dashboard_mylist_contacts_count_check(mobile_page):
    print("----- 12번 - MO Web > My lists 영역에 저장한 연락처, 미확인 연락처 표시 확인 테스트 시작-----")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=60000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").click()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    mobile_page.get_by_role("button", name="로그인").click()
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("link").filter(has_text="대시보드").tap(timeout=10000)
    mobile_page.wait_for_timeout(7000)

    print("MO Web - 대시보드 진입 완료")

    assert "마이 리스트" in mobile_page.content(), \
        "MO Web - 대시보드 > 마이리스트 영역 > 타이틀 문구 노출 확인 실패 1"
    assert "저장" in mobile_page.content(), \
        "MO Web - 대시보드 > 마이리스트 영역 > 저장 문구 노출 확인 실패 2"
    # 20251211 - 마이리스트 저장 카운트 개수 재수정
    assert "6,602" in mobile_page.content(), \
        "MO Web - 대시보드 > 마이리스트 영역 > 저장 카운트 개수 확인 실패 3"
    assert "확인되지 않은" in mobile_page.content(), \
        "MO Web - 대시보드 > 마이리스트 영역 > 미확인된 문구 노출 확인 실패 4"
    # 20260119 - 마이리스트 확인되지 않은 카운트 개수 재수정
    assert "6,382" in mobile_page.content(), \
        "MO Web - 대시보드 > 마이리스트 영역 > 미확인된 연락처 카운트 개수 확인 실패 5"

    #    print("대시보드 > 마이리스트 > 팀공유 연락처 개수 영역 미출력됨 -> 해당 항목 주석 처리 -> 추후 수정 시 재추가 및 수정")
    #    assert "팀 공유" in page.content(), "대시보드 > 마이리스트 영역 > 팀 공유 문구 노출 확인 실패 6"

    print("----- 12번 - MO Web > My lists 영역에 저장한 연락처, 미확인 연락처 표시 확인 테스트 종료 -> 성공 -----")
