import config
import re

def test_MO_mylist_detail_contact_view_contacts_check(mobile_page):
    print("----- 46번 - MO 마이리스트 상세 > 임의 연락처 > 연락처 확인 시 동작 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 마이리스트 메인 페이지 진입 완료")

    mobile_page.get_by_text("test 2").tap()
    mobile_page.wait_for_timeout(1000)

    # 20251001 - 첫번째 체크박스
    mobile_page.get_by_role("checkbox").nth(1).tap()
    # page.locator("button.peer.size-5").nth(1).click(force=True)
    mobile_page.wait_for_timeout(1000)

    mobile_page.locator("div").filter(has_text=re.compile(r"^1 선택됨삭제연락처 확인내보내기리스트로 이동선택 해제$")).get_by_role("button").nth(
        1).tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 마이리스트 상세 > 1번 리드 체크 완료")

    # 20251217 - 앨리먼트 나올 때까지 timeout 10초 추가
    mobile_page.get_by_role("menuitem", name="이메일 및 전화번호 보기").click(timeout=10000)
    mobile_page.wait_for_timeout(1000)
    # 20251217 - 앨리먼트 나올 때까지 timeout 10초 추가
    mobile_page.get_by_role("button", name="확인", exact=True).click(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    assert "4 크레딧이 사용되었습니다." == mobile_page.locator("div").filter(has_text=re.compile(r"^4 크레딧이 사용되었습니다\.$")).nth(
        1).inner_text(), \
        "MO Web - 크레딧 사용 토스트 메시지 출력 - 엔터프라이즈 연락처 확인 실패 1"

    print("MO Web - 마이 리스트 상세 (일반) > 연락처 > 이메일 & 전화번호 보기 연락처 확인 성공")
    mobile_page.wait_for_timeout(3000)

    # 20251001 - 한번에 체크되지 않아 첫번째 리드 선택 -> 다른 리드체크 선택/해제 후 다시 첫번째 리드 선택하는 동작으로 코드 수정 - 동작상에 문제로 인해 수정)
    mobile_page.get_by_role("checkbox").nth(1).tap(force=True)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("checkbox").nth(2).dblclick(force=True)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("checkbox").nth(1).tap(force=True)
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_role("button", name="삭제").tap()
    # 20251230 - 대기 시간 1초 -> 2초 코드 변경
    mobile_page.wait_for_timeout(2000)

    mobile_page.locator("#modal-root").get_by_role("button", name="삭제").tap()
    # 20251230 - 대기 시간 1초 -> 2초 코드 변경
    mobile_page.wait_for_timeout(2000)

    print("MO Web - 마이 리스트 상세 (일반) > 확인된 연락처 삭제 성공")

    mobile_page.get_by_role("banner").get_by_role("button").nth(3).tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_text("로그아웃").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 크레딧 성공한 계정 로그아웃 후 로그인 페이지 진입")

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PRD4_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PRD4_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 재진입 완료")

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 마이리스트 메인 페이지 재진입 완료")

    mobile_page.get_by_text("test").tap()
    mobile_page.wait_for_timeout(1000)

    # 20251001 - 첫번째 리드 체크 코드 수정
    mobile_page.get_by_role("checkbox").nth(1).tap(force=True)
    mobile_page.wait_for_timeout(500)

    mobile_page.locator("div").filter(has_text=re.compile(r"^1 선택됨삭제연락처 확인내보내기리스트로 이동선택 해제$")).get_by_role("button").nth(
        1).tap()

    print("MO Web - 마이리스트 상세 (test) > 1번 리드 체크 완료")

    # 20251217 - 앨리먼트 나올 때까지 timeout 10초 추가
    mobile_page.get_by_role("menuitem", name="이메일 및 전화번호 보기").tap(timeout=10000)
    mobile_page.wait_for_timeout(500)
    # 20251217 - 앨리먼트 나올 때까지 timeout 10초 추가
    mobile_page.get_by_role("button", name="확인", exact=True).tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    assert "이런... 크레딧이 부족해요." == mobile_page.get_by_text("이런... 크레딧이 부족해요").inner_text(), \
        "MO Web - 크레딧 부족 계정 > 마이리스트 상세 (일반) > 연락처 확인 시 크레딧 부족 모달 > 타이틀 문구 노출 실패 - 크레딧 부족 모달 확인 실패 1"
    assert "요금제 업그레이드" == mobile_page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "MO Web - 크레딧 부족 계정 > 마이리스트 상세 (일반) > 연락처 확인 시 크레딧 부족 모달 > 요금제 업그레이드 버튼 노출 실패 - 크레딧 부족 모달 확인 실패 1"

    print("MO Web - 크레딧 부족 모달 노출 확인 완료")
    print("----- 46번 - MO 마이리스트 상세 > 임의 연락처 > 연락처 확인 시 동작 확인 테스트 시작 -> 성공 -----")
