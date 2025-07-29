import config


def test_dashboard_usage_activity_period_selector_and_plan_credit_check(page):
    print("----- Usage Activity에 기간별 평균 크레딧 사용 활동 노출 현재 사용중인 요금제, 크레딧 정상 노출 확인 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    page.get_by_role("button", name="로그인").click()
    # page.wait_for_timeout(1000)
    # page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="대시보드").click()
    page.wait_for_timeout(3000)
    page.get_by_text("Enterprise").click()

#    print("기간 셀렉터 확인 및 이번주 설정 후 크레딧 사용량 확인 케이스 -> 기능 없음으로 확인 불가")
#    assert "This month" in page.content(), "대시보드 > 기간 셀렉터 (This month) 출력 실패 - 기간 셀렉터 확인 실패"
#    page.get_by_text("This month").click()
#    page.wait_for_timeout(500)
#    page.get_by_text("This week").click()
#    page.wait_for_timeout(500)
#    assert "168" in page.content(), "대시보드 > 이번주 사용한 크레딧 사용량 출력 실패 - 이번주 사용한 크레딧 사용량 확인 실패"
#    page.get_by_text("This month").click()
#    page.wait_for_timeout(500)

    assert "Enterprise" in page.content(), "대시보드 > 현재 사용 중인 요금제 명 Enterprise 출력 실패 - 요금제 명 확인 실패"
    assert "168" in page.content(), "대시보드 > 현재 사용한 크레딧 사용량 출력 실패 - 크레딧 사용량 확인 실패"
