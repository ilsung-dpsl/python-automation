import config


def test_dashboard_gotomyaccount_move(page):
    print("----- Go to my account 버튼 클릭 시, Account & Setting > My account로 이동 테스트 시작 (한글) -----")
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="대시보드").click()
    page.wait_for_timeout(3000)
    page.get_by_text("내 계정으로 이동하기 >").click()

    page.wait_for_timeout(2000)

    assert "계정 및 설정" in page.content(), "계정 및 설정 페이지 이동 실패 1"
    assert "내 프로필" in page.content(), "계정 및 설정 > 내 프로필 이동 실패 2"
    assert "업로드" in page.content(), "계정 및 설정 > 내 프로필 > 프로필 영역 노출 실패 3"
    assert "최초 등록일 : 2025년 03월 24일" in page.content(), "계정 및 설정 > 내 프로필 > 최초 등록일 노출 실패 4"

    print("----- Go to my account 버튼 클릭 시, Account & Setting > My account로 이동 테스트 시작 (한글) -> 성공 -----")
