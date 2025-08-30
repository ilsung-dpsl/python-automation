import config
import re

def test_company_setup_and_main_page_check(page):
    print("----- 회사 정보 > setup 버튼 및 메인 페이지 진입 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.FREE_PA24_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA24_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("로그인 후 탐색하기 페이지 진입 완료")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    assert "설정하기" == page.get_by_text("설정하기", exact=True).inner_text(), \
        "프로필 하단 > 회사 정보 > 우측 > 설정하기 버튼 확인 실패 - 회사 정보 > setup 버튼 확인 실패 1"

    print("프로필 하단 > 회사 정보 우측 > [설정하기] 버튼 확인 완료")

    page.get_by_text("회사 정보 설정하기").click()
    page.wait_for_timeout(2000)

    assert ("회사 설정을 시작하세요.\n귀사의 정보를 글로벌 고객과 공유하고 새로운 기회를 만들어 보세요.") == page.get_by_text("회사 설정을 시작하세요. 귀사의 정보를 글로벌 고객과 공유하고 새로운 기회를 만들어 보세요").inner_text(), \
        "회사 정보 메인 페이지 > 타이틀 문구 출력 실패 - 회사 정보 > 메인 페이지 진입 실패 2"
    assert "새로운 회사를 등록하시겠습니까?" in page.get_by_text("새로운 회사를 등록하시겠습니까?").inner_text(), \
        "회사 정보 메인 페이지 > 하단 가이드 문구 출력 실패 - 회사 정보 > 메인 페이지 진입 실패 3"
    assert "등록하기" == page.get_by_text("등록하기").inner_text(), \
        "회사 정보 메인 페이지 > [등록하기] 버튼 출력 실패 - 회사 정보 > 메인 페이지 진입 실패 4"

    print("회사 정보 메인 페이지 진입 완료")
    print("----- 회사 정보 > setup 버튼 및 메인 페이지 진입 테스트 시작 -> 성공 -----")
