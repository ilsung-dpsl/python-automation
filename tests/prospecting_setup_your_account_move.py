import config


def test_prospecting_setup_your_account_move(page):
    print("----- 검색 이력이 없는 신규 가입 사용자일때 Set up your account 노출 (한글) 테스트 시작 -----")
    print("계정 정보: ilsung.baek+prd2@deepsales.com, PW: !deepsales@36")

    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)

    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD2_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD2_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    #page.get_by_role("button", name="Start Now").click()
    #page.wait_for_timeout(1000)
    page.get_by_role("button", name="계정 설정하기").click()

    page.wait_for_timeout(2000)

    assert "계정 및 설정" in page.content(), "계정 및 설정 페이지 이동 실패 1"
    assert "내 프로필" in page.content(), "계정 및 설정 > 내 프로필 이동 실패 2"
    assert "업로드" in page.content(), "계정 및 설정 > 내 프로필 > 프로필 영역 노출 실패 3"
    assert "최초 등록일 : 2025년 07월 11일" in page.content(), "계정 및 설정 > 내 프로필 > 최초 등록일 노출 실패 4"

    print("----- 검색 이력이 없는 신규 가입 사용자일때 Set up your account 노출 (한글) 테스트 시작 -> 성공 -----")