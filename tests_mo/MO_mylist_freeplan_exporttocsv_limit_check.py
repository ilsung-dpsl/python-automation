import config
import re

def test_MO_mylist_freeplan_exporttocsv_limit_check(mobile_page):
    print("----- 39번 - MO 마이리스트 > Free 플랜 사용자 csv 내보내기 시 요금제 제한 안내 모달 노출 확인 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA8_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA8_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="마이 리스트").tap()
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 마이리스트 메인 페이지 진입 완료")

    # 20250930 - 마이리스트 > 기본 > 더보기 버튼 코드 수정
    mobile_page.locator("div:nth-child(6) > div").first.tap()
    mobile_page.wait_for_timeout(2000)
    mobile_page.get_by_role("menuitem", name="CSV 내보내기").tap()
    mobile_page.wait_for_timeout(2000)

    assert "이런... 연락처 내보내기 기능은 Pro 요금제 이상에만 제공됩니다." == mobile_page.get_by_text("이런... 연락처 내보내기 기능은 Pro").inner_text(), \
        "MO Web - 마이리스트 > CSV 내보내기 시 요금제 제한 안내 안내 타이틀 문구 확인 실패 - 마이리스트 > 요금제 제한 모달 노출 실패 1"
    assert "요금제 업그레이드" == mobile_page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "MO Web - 마이리스트 > CSV 내보내기 시 요금제 제한 안내 안내 > 요금제 업그레이드 버튼 확인 실패 - 마이리스트 > 요금제 제한 모달 노출 실패 2"

    print("MO Web - 마이리스트 > csv 내보내기 > 요금제 제한 안내 모달 노출 확인 완료")

    mobile_page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).tap()

    print("----- 39번 - MO 마이리스트 > Free 플랜 사용자 csv 내보내기 시 요금제 제한 안내 모달 노출 확인 테스트 시작 -> 성공 -----")