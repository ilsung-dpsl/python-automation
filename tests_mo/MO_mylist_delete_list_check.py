import config
import re
#20260203 - expect 패키지 import 추가
from playwright.sync_api import expect

def test_MO_mylist_delete_list_check(mobile_page):
    print("----- 27번 - MO 마이리스트 > 리스트 삭제 확인 테스트 시작 -----")

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

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 마이리스트 페이지 진입 완료")

    # 20260113 - 타임아웃 대기 코드 추가
    mobile_page.get_by_role("button", name="리스트 만들기").tap(timeout=10000)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("textbox", name="/50").fill("test 1")
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("button", name="확인").tap(timeout=10000)
    # 20260107 - 리스트 생성 후 3초 -> 4초로 수정
    mobile_page.wait_for_timeout(4000)

    print("MO Web - 리스트 생성 완료 후")

    # 20260107 - 새로 생성한 일반 폴더 리스트 > 더보기 버튼 선택 코드 -> 타임아웃 10초 추가
    mobile_page.locator("div:nth-child(3) > div:nth-child(6) > div").tap(timeout=10000)
    # 20260107 - 대기 시간 3초 -> 4초로 수정
    mobile_page.wait_for_timeout(4000)

    # 20260107 - 앨리먼트 나타날 때까지 타임아웃 대기 10초 추가 / 2초 -> 2.5초로 대기 수정
    mobile_page.get_by_role("menuitem", name="리스트 삭제").tap(timeout=10000)
    # 20250113 - 3초 -> 2초로 변경
    mobile_page.wait_for_timeout(2000)

    # 20260304 - [검증 1] 삭제 성공 토스트 메시지 확인 (서버 응답 확인)
    toast_msg = mobile_page.locator("div").filter(has_text=re.compile(r"^리스트가 삭제되었습니다\.$")).nth(1)
    expect(toast_msg).to_be_visible(timeout=10000)

    assert "리스트가 삭제되었습니다." == mobile_page.locator("div").filter(has_text=re.compile(r"^리스트가 삭제되었습니다\.$")).nth(1).inner_text(), \
        "MO Web - 리스트 삭제 후 리스트 삭제 토스트 메시지 확인 실패 - 리스트 삭제 실패 1"

    #20260212 - 대기사간 2초 -> 3초로 변경
    mobile_page.wait_for_timeout(3000)

    #mobile_page.reload()
    #mobile_page.wait_for_timeout(2000)

    # 2026.03.04 - [최종 해결책] 가시성 검증을 넘어선 물리적 제거 대기
    # 단순히 텍스트만 찾는 것이 아니라, 리스트 아이템이 속한 구체적인 p 태그를 타겟팅
    list_item = mobile_page.locator("p").filter(has_text=re.compile(r"^test 1$"))

    # [핵심] 삭제 후 DOM이 꼬였을 경우를 대비해, 텍스트가 "사라질 때까지(hidden)" 먼저 기다림
    # to_be_hidden은 요소가 숨겨지거나, 아예 없어지는 두 상황을 모두 체크합니다.
    try:
        expect(list_item).to_be_hidden(timeout=15000)
    except AssertionError:
        print("DEBUG: 요소가 숨겨지지 않음. 강제로 count 체크 진입")

    # [최후의 보루] 1초마다 count를 체크하며 '물리적으로 0개'가 될 때까지 루프
    # Jenkins 및 로컬 간헐적 이슈를 방어하기 위해 가장 보수적으로 접근
    is_deleted = False
    for i in range(10):
        # count()는 호출 시점의 라이브 상태를 즉시 반환합니다.
        if list_item.count() == 0:
            is_deleted = True
            break
        print(f"DEBUG: 삭제 대기 중... ({i + 1}/10)")
        mobile_page.wait_for_timeout(1000)

    # 최종 결과 보고
    assert is_deleted is True, \
        f"MO Web - 리스트 정상 삭제 실패 - 여전히 {list_item.count()}개의 요소가 존재함"

    # 20260113 - 마이리스트 페이지의 test 1 폴더가 남아있는 것처럼 파악되는 경우가 있어 해당 div가 있는지 확인하는 것으로 변경
    #assert mobile_page.locator("div").filter(has_text=re.compile(r"^test 1$")).count() == 0, \
    #    "리스트 정상 삭제 실패 - 리스트 삭제 실패 2"

    print("----- 27번 - MO 마이리스트 > 리스트 삭제 확인 테스트 시작 -> 성공 -----")
