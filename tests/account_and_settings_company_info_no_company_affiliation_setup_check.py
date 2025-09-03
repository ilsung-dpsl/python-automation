from httplib2 import ProxyInfo

import config
import re

def test_account_and_settings_company_info_no_company_affiliation_setup_check(page):
    print("소속된 회사가 없을 경우, 회사 정보 > [설정하기] 버튼 노출 및 선택 시 회사 설정 페이지 이동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.FREE_PA25_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA25_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("탐색하기 페이지 진입 완료")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("계정 및 설정").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="회사 정보").click()
    page.wait_for_timeout(1000)

    print("계정 및 설정 > 회사 정보 페이지 진입 완료")

    assert True == page.get_by_role("button", name="설정하기").is_visible(), \
        "계정 및 설정 > 회사 정보 > [설정하기] 버튼 활성화 노출 확인 실패 - 소속된 회사 없는 회사 정보 > 설정하기 플로우 확인 실패 1"

    page.get_by_role("button", name="설정하기").click()
    page.wait_for_timeout(1000)

    assert "회사 설정을 시작하세요.\n귀사의 정보를 글로벌 고객과 공유하고 새로운 기회를 만들어 보세요." == page.get_by_text("회사 설정을 시작하세요. 귀사의 정보를 글로벌 고객과 공유하고 새로운 기회를 만들어 보세요").inner_text(), \
        "회사 정보 페이지 > 타이틀 문구 확인 실패 - 소속된 회사 없는 회사 정보 > 설정하기 선택 후 회사 정보 페이지 이동 확인 실패 2"
    assert "회사명을 검색하세요." == page.locator("div").filter(has_text=re.compile(r"^회사명을 검색하세요\.$")).nth(2).inner_text(), \
        "회사 정보 페이지 > 회사 입력창 > Placeholder 확인 실패 - 소속된 회사 없는 회사 정보 > 설정하기 선택 후 회사 정보 페이지 이동 확인 실패 3"

    print("회사 정보 페이지 > 타이틀 / 회사 입력창 확인 완료")
    print("소속된 회사가 없을 경우, 회사 정보 > [설정하기] 버튼 노출 및 선택 시 회사 설정 페이지 이동 확인 테스트 시작 -> 성공 -----")
