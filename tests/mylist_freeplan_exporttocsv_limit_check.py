import config
import re

def test_mylist_freeplan_exporttocsv_limit_check(page):

    print("----- 마이리스트 > Free 플랜 사용자 csv 내보내기 시 요금제 제한 안내 모달 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA8_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA8_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(3000)

    print("마이리스트 메인 페이지 진입 완료")
    page.locator("[id=\"headlessui-menu-button-:rs:\"]").click()
    page.wait_for_timeout(2000)
    page.get_by_role("menuitem", name="CSV 내보내기").click()
    page.wait_for_timeout(2000)

    assert "이런... 연락처 내보내기 기능은 Pro 요금제 이상에만 제공됩니다." == page.get_by_text("이런... 연락처 내보내기 기능은 Pro").inner_text(), \
        "마이리스트 > CSV 내보내기 시 요금제 제한 안내 안내 타이틀 문구 확인 실패 - 마이리스트 > 요금제 제한 모달 노출 실패 1"
    assert "요금제 업그레이드" == page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "마이리스트 > CSV 내보내기 시 요금제 제한 안내 안내 > 요금제 업그레이드 버튼 확인 실패 - 마이리스트 > 요금제 제한 모달 노출 실패 2"

    print("마이리스트 > csv 내보내기 > 요금제 제한 안내 모달 노출 확인 완료")

    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    print("----- 마이리스트 > Free 플랜 사용자 csv 내보내기 시 요금제 제한 안내 모달 노출 확인 테스트 시작 -> 성공 -----")
