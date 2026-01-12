import config
import re

def test_MO_dashboard_discover_link_move(mobile_page):
    print("----- 11번 - MO 대시보드 > 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 테스트 시작 -----")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("link").filter(has_text="대시보드").tap(timeout=10000)
    mobile_page.wait_for_timeout(5000)

    # 대시보드 > 발견하기 > 1번 항목 탐색하기 연동 확인
    mobile_page.get_by_text("네덜란드 종교 기관 업계의 전문가들").tap()
    mobile_page.wait_for_timeout(5000)

    assert "잠재고객 '" in mobile_page.content(), "대시보드 > 발견하기 > 1번 항목 > 탐색하기 연동 후 잠재고객 노출 확인 실패 1"
    assert "Religious Institutions" in mobile_page.content(), "대시보드 > 발견하기 > 1번 항목 > 탐색하기 연동 후 검색결과의 카드 타이틀 문구 확인 실패 2"
    assert "Lenneke Keuning" in mobile_page.content(), "탐색하기 연동 후 리드 데이터 출력 실패 3"

    print("--- 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 1 -> 성공")

    mobile_page.get_by_role("link").filter(has_text="대시보드").tap(timeout=10000)
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_text("미국 도매 알코올 음료 업계, 직원 수 50-200").tap()
    mobile_page.wait_for_timeout(3000)

    assert "Wholesale Alcoholic" in mobile_page.content(), "대시보드 > 발견하기 > 5번 항목 > 탐색하기 연동 실패 2"
    assert "Jamie Pollack" in mobile_page.content(), "탐색하기 연동 후 리드 데이터 출력 실패 2"

    print("--- 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 2 -> 성공")
    print("--- 11번 - MO 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 완료 -> 성공")