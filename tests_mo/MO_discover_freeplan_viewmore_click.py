import config
import re

def test_MO_discover_freeplan_viewmore_click(mobile_page):
    print("----- 36번 - MO Web > Free plan 사용자가 발견하기 > 더보기 선택 시 요금제 업그레이드 모달 노출 테스트 시작  -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)
    # 20260119 - PA18 일반 무료 계정으로 변경
    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA18_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA18_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # 20250930 - LNB > 발견하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="발견하기").tap()
    mobile_page.wait_for_timeout(3000)

    print("MO Web - 발견하기 페이지 진입 완료")

    mobile_page.get_by_text("고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").tap()
    mobile_page.wait_for_timeout(1000)

    # 페르소나 설정 안내 모달 > 나중에 하기 버튼 선택으로 모달을 닫는다.
    mobile_page.get_by_role("button", name="나중에 하기").tap()
    mobile_page.wait_for_timeout(2000)

    print("MO Web - 페르소나 설정 모달 닫기 후 발견하기 페이지 진입")

    mobile_page.get_by_role("button", name="더보기").tap()
    mobile_page.wait_for_timeout(1000)

    assert "이런! 무료 플랜에서는 추가 탐색이\n제한됩니다." == mobile_page.get_by_text("이런! 무료 플랜에서는 추가 탐색이 제한됩니다").inner_text(), \
        "MO Web - 요금제 업그레이드 모달 > 타이틀 문구 노출 실패 - 발견하기 > 더보기 선택 후 요금제 업그레이드 모달 노출 실패 1"
    assert "요금제 업그레이드" == mobile_page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "MO Web - 요금제 업그레이드 모달 > 요금제 업그레이드 버튼 노출 실패 - 발견하기 > 더보기 선택 후 요금제 업그레이드 모달 노출 실패 2"

    print("----- 36번 - MO Web > Free plan 사용자가 발견하기 > 더보기 선택 시 요금제 업그레이드 모달 노출 테스트 시작 -> 성공 -----")