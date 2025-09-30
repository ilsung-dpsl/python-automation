
import config

def test_discover_freeplan_viewmore_click(page):
    print("----- Free plan 사용자가 발견하기 > 더보기 선택 시 요금제 업그레이드 모달 노출 테스트 시작  -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA8_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA8_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 발견하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="발견하기").nth(1).click()
    page.wait_for_timeout(3000)

    print("발견하기 페이지 진입 완료")

    page.locator("header").filter(has_text="고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="더보기").click()
    page.wait_for_timeout(1000)

    assert "이런! 무료 플랜에서는 추가 탐색이\n제한됩니다." == page.get_by_text("이런! 무료 플랜에서는 추가 탐색이 제한됩니다").inner_text(), \
        "요금제 업그레이드 모달 > 타이틀 문구 노출 실패 - 발견하기 > 더보기 선택 후 요금제 업그레이드 모달 노출 실패 1"
    assert "요금제 업그레이드" == page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "요금제 업그레이드 모달 > 요금제 업그레이드 버튼 노출 실패 - 발견하기 > 더보기 선택 후 요금제 업그레이드 모달 노출 실패 2"

    print("----- Free plan 사용자가 발견하기 > 더보기 선택 시 요금제 업그레이드 모달 노출 테스트 시작 -> 성공 -----")
