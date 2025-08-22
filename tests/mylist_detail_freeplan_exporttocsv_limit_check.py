import config
import re

def test_mylist_detail_freeplan_exporttocsv_limit_check(page):
    print("----- 무료 회원, 마이리스트 상세 > CSV 내보내기 시 요금제 업그레이드 모달 노출 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()

    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA8_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA8_PW)
    page.get_by_role("button", name="로그인").click()

    page.wait_for_timeout(1000)
    page.get_by_role("link", name="마이 리스트").click()
    page.wait_for_timeout(1000)
    print("마이리스트 페이지 진입 완료")
    page.locator("div").filter(has_text=re.compile(r"^확인됨$")).nth(1).click()
    page.wait_for_timeout(1000)
    page.locator("[id=\":r15:\"]").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="내보내기").click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="CSV 내보내기").click()
    page.wait_for_timeout(1000)

    assert "이런... 연락처 내보내기 기능은 Pro 요금제 이상에만 제공됩니다." == page.get_by_text("이런... 연락처 내보내기 기능은 Pro").inner_text(), \
        "마이리스트 상세 > 요금제 업그레이드 모달 타이틀 문구 확인 실패 - 무료 회원 csv 내보내기 제한 확인 실패 1"
    assert "플랜을 변경하고 더 많은 잠재고객을 만나보세요. AI 잠재고객 발견을 통해 세일즈 파이프라인을 빠르게 확장하십시오." == page.get_by_text("플랜을 변경하고 더 많은 잠재고객을 만나보세요. AI").inner_text(), \
        "마이리스트 상세 > 요금제 업그레이드 모달 내용 문구 확인 실패 - 무료 회원 csv 내보내기 제한 확인 실패 2"

    print("마이리스트 상세 > CSV 내보내기 시 요금제 업그레이드 모달 노출 확인 완료")
    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    print("----- 무료 회원, 마이리스트 상세 > CSV 내보내기 시 요금제 업그레이드 모달 노출 테스트 시작 -> 성공 -----")


