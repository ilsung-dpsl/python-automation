import config
import re

def test_mylist_freeplan_exporttocsv_limit_check(page):
    print("----- 44번 - 마이리스트 > Free 플랜 사용자 csv 내보내기 시 요금제 제한 안내 모달 노출 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    # 20260119 - PA18 일반 무료 계정으로 변경
    page.get_by_placeholder("이메일").fill(config.FREE_PA18_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA18_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="마이 리스트").nth(1).click()
    page.wait_for_timeout(5000)

    print("마이리스트 메인 페이지 진입 완료")

    #20250930 - 마이리스트 > 기본 > 더보기 버튼 코드 수정
    page.locator("div:nth-child(6) > div").first.click()
    page.wait_for_timeout(2000)
    page.get_by_role("menuitem", name="CSV 내보내기").click()
    page.wait_for_timeout(2000)

    assert "이런... 연락처 내보내기 기능은 Pro 요금제 이상에만 제공됩니다." == page.get_by_text("이런... 연락처 내보내기 기능은 Pro").inner_text(), \
        "마이리스트 > CSV 내보내기 시 요금제 제한 안내 안내 타이틀 문구 확인 실패 - 마이리스트 > 요금제 제한 모달 노출 실패 1"
    assert "요금제 업그레이드" == page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "마이리스트 > CSV 내보내기 시 요금제 제한 안내 안내 > 요금제 업그레이드 버튼 확인 실패 - 마이리스트 > 요금제 제한 모달 노출 실패 2"

    print("마이리스트 > csv 내보내기 > 요금제 제한 안내 모달 노출 확인 완료")

    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    print("----- 44번 - 마이리스트 > Free 플랜 사용자 csv 내보내기 시 요금제 제한 안내 모달 노출 확인 테스트 시작 -> 성공 -----")
