import re
import config

def test_MO_dashboard_usage_activity_period_selector_and_plan_credit_check(mobile_page):
    print("----- 9번 - MO Web Usage Activity에 기간별 평균 크레딧 사용 활동 노출 현재 사용중인 요금제, 크레딧 정상 노출 확인 테스트 시작 -----")
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    # mobile_page.wait_for_timeout(1000)
    # mobile_page.get_by_role("button", name="Start Now").click()
    # 20251230 - 대기 1초 -> 2초로 수정
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_role("button", name="Confirm").click(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("link").filter(has_text="대시보드").tap()
    mobile_page.wait_for_timeout(2000)

    print("MO Web - 대시보드 진입 완료")

    mobile_page.get_by_text("Enterprise").tap()

    #    print("기간 셀렉터 확인 및 이번주 설정 후 크레딧 사용량 확인 케이스 -> 기능 없음으로 확인 불가")
    #    assert "This month" in mobile_page.content(), "대시보드 > 기간 셀렉터 (This month) 출력 실패 - 기간 셀렉터 확인 실패"
    #    mobile_page.get_by_text("This month").click()
    #    mobile_page.wait_for_timeout(500)
    #    mobile_page.get_by_text("This week").click()
    #    mobile_page.wait_for_timeout(500)
    #    assert "168" in mobile_page.content(), "대시보드 > 이번주 사용한 크레딧 사용량 출력 실패 - 이번주 사용한 크레딧 사용량 확인 실패"
    #    mobile_page.get_by_text("This month").click()
    #    mobile_page.wait_for_timeout(500)

    assert "Enterprise" in mobile_page.content(), \
        "MO Web - 대시보드 > 현재 사용 중인 요금제 명 Enterprise 출력 실패 - 요금제 명 확인 실패 1"
    assert "사용한 크레딧" in mobile_page.content(), \
        "MO Web - 대시보드 > 사용내역 > 사용한 크레딧 문구 확인 실패 2"
    assert "353" in mobile_page.content(), \
        "MO Web - 대시보드 > 현재 사용한 크레딧 사용량 출력 실패 - 크레딧 사용량 확인 실패 3"

    print("----- 9번 - MO Web Usage Activity에 기간별 평균 크레딧 사용 활동 노출 현재 사용중인 요금제, 크레딧 정상 노출 확인 테스트 시작 -> 성공 -----")
