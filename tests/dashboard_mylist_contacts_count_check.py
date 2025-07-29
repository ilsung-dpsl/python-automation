import config


def test_dashboard_mylist_contacts_count_check(page):
    print("----- My lists 영역에 저장한 연락처, 미확인 연락처 표시 확인 테스트 시작-----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=60000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    page.get_by_role("button", name="로그인").click()
  #  page.wait_for_timeout(1000)
  #  page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="대시보드").click()

    page.wait_for_timeout(5000)

    assert "마이 리스트" in page.content(), "대시보드 > 마이리스트 영역 > 타이틀 문구 노출 확인 실패 1"
    assert "저장" in page.content(), "대시보드 > 마이리스트 영역 > 저장 문구 노출 확인 실패 2"
    assert "6,578" in page.content(), "대시보드 > 마이리스트 영역 > 저장 카운트 개수 확인 실패 3"
    assert "확인되지 않은" in page.content(), "대시보드 > 마이리스트 영역 > 미확인된 문구 노출 확인 실패 4"
    assert "6,377" in page.content(), "대시보드 > 마이리스트 영역 > 미확인된 연락처 카운트 개수 확인 실패 5"

#    print("대시보드 > 마이리스트 > 팀공유 연락처 개수 영역 미출력됨 -> 해당 항목 주석 처리 -> 추후 수정 시 재추가 및 수정")
#    assert "팀 공유" in page.content(), "대시보드 > 마이리스트 영역 > 팀 공유 문구 노출 확인 실패 6"


    print("----- My lists 영역에 저장한 연락처, 미확인 연락처 표시 확인 테스트 종료 -> 성공 -----")
