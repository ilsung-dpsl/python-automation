import config
import re

def test_mylist_detail_contact_view_contacts_check(page):

    print("----- 마이리스트 상세 > 임의 연락처 > 연락처 확인 시 동작 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()

    page.wait_for_timeout(1000)
    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)

    print("마이리스트 메인 페이지 진입 완료")
    page.get_by_text("test 2").click()
    page.wait_for_timeout(1000)

    page.locator(".ml-\\[2px\\] > .flex").first.click()

    page.locator("div").filter(has_text=re.compile(r"^1 선택됨삭제연락처 확인내보내기리스트로 이동선택 해제$")).get_by_role("button").nth(1).click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="이메일 및 전화번호 보기").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(1000)

    assert "4 크레딧이 사용되었습니다." ==     page.locator("div").filter(has_text=re.compile(r"^4 크레딧이 사용되었습니다\.$")).nth(1).inner_text(), \
        "크레딧 사용 토스트 메시지 출력 - 엔터프라이즈 연락처 확인 실패 1"

    print("마이 리스트 상세 (일반) > 연락처 > 이메일 & 전화번호 보기 연락처 확인 성공")
    page.wait_for_timeout(2000)
    page.locator(".ml-\\[2px\\] > .flex").first.click()

    page.wait_for_timeout(1000)

    page.get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)

    page.locator("#modal-root").get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)

    print("마이 리스트 상세 (일반) > 확인된 연락처 삭제 성공")

    page.get_by_role("banner").get_by_role("button").nth(3).click()
    page.wait_for_timeout(1000)
    page.get_by_text("로그아웃").click()
    page.wait_for_timeout(1000)

    print("크레딧 성공한 계정 로그아웃 후 로그인 페이이 진입")

    page.get_by_placeholder("이메일").fill(config.FREE_PRD4_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD4_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)
    print("마이리스트 메인 페이지 재진입 완료")

    page.get_by_text("test").click()
    page.wait_for_timeout(1000)
    page.locator(".ml-\\[2px\\] > .flex").first.click()
    page.wait_for_timeout(500)

    page.locator("div").filter(has_text=re.compile(r"^1 선택됨삭제연락처 확인내보내기리스트로 이동선택 해제$")).get_by_role("button").nth(
        1).click()
    page.get_by_role("menuitem", name="이메일 및 전화번호 보기").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="확인", exact=True).click()

    page.wait_for_timeout(1000)

    assert "이런... 크레딧이 부족해요." == page.get_by_text("이런... 크레딧이 부족해요").inner_text(), \
        "크레딧 부족 계정 > 마이리스트 상세 (일반) > 연락처 확인 시 크레딧 부족 모달 > 타이틀 문구 노출 실패 - 크레딧 부족 모달 확인 실패 1"
    assert "요금제 업그레이드" == page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "크레딧 부족 계정 > 마이리스트 상세 (일반) > 연락처 확인 시 크레딧 부족 모달 > 요금제 업그레이드 버튼 노출 실패 - 크레딧 부족 모달 확인 실패 1"

    print("----- 마이리스트 상세 > 임의 연락처 > 연락처 확인 시 동작 확인 테스트 시작 -> 성공 -----")