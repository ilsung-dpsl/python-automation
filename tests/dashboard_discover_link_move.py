import config


def test_dashboard_discover_link_move(page):
    print("----- 대시보드 > 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 테스트 시작 -----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
 #   page.wait_for_timeout(1000)
 #   page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="대시보드").click()
    page.wait_for_timeout(2000)

    #대시보드 > 발견하기 > 1번 항목 탐색하기 연동 확인
    page.get_by_text("네덜란드 종교 기관 업계의 전문가들").click()
    page.wait_for_timeout(2000)

    assert "'Religious Institutions" in page.content(), "대시보드 > 발견하기 > 1번 항목 > 탐색하기 연동 실패 1"
    assert "Leon Broeke" in page.content(), "탐색하기 연동 후 리드 데이터 출력 실패 1"

    print("--- 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 1 -> 성공")

    page.get_by_role("link", name="대시보드").click()
    page.wait_for_timeout(2000)

    page.get_by_text("미국 도매 알코올 음료 업계, 직원 수 50-200").click()
    page.wait_for_timeout(3000)

    assert "'Wholesale Alcoholic" in page.content(), "대시보드 > 발견하기 > 5번 항목 > 탐색하기 연동 실패 2"
    assert "Colin Quinn" in page.content(), "탐색하기 연동 후 리드 데이터 출력 실패 2"

    print("--- 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 2 -> 성공")
    print("--- 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 완료 -> 성공")