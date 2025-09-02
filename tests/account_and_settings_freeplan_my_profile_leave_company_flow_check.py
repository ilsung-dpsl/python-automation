import config
import re

def test_account_and_settings_freeplan_my_profile_leave_company_flow_check(page):
    print("----- 계정 및 설정 > 팀오너가 아닌 경우 > 내 프로필 > 소속회사 떠나기 플로우 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.FREE_PA24_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA24_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("회사 정보", exact=True).click()
    page.wait_for_timeout(1000)

    print("회사 정보 페이지 진입 완료")

    page.locator(".text-base > .text-FG-Primary").click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-2-input").fill("deepsales")
    page.wait_for_timeout(1000)

    page.locator("#react-select-2-option-0").get_by_text("DeepSales").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("회사 정보 > 회사 설정 완료")

    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    page.wait_for_timeout(1000)

    page.get_by_text("계정 및 설정").click()
    page.wait_for_timeout(1000)

    print("계정 및 설정 > 내 프로필 페이지 진입 완료")

    page.get_by_role("button", name="소속 회사 떠나기 >").click()
    page.wait_for_timeout(1000)

    assert "소속 회사 떠나기" == page.get_by_text("소속 회사 떠나기", exact=True).inner_text(), \
        "소속 회사 떠나기 모달 > 타이틀 문구 확인 실패 - 내 프로필 > 팀오너가 아닌 경우 소속 회사 떠나기 플로우 실패 1"
    assert "확인" == page.get_by_role("button", name="확인").inner_text(), \
        "소속 회사 떠나기 모달 > [확인] 버튼 확인 실패 - 내 프로필 > 팀오너가 아닌 경우 소속 회사 떠나기 플로우 실패 2"

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    assert "소속 회사 떠나기 완료" == page.get_by_text("소속 회사 떠나기 완료").inner_text(), \
        "소속 회사 떠나기 완료 모달 > 타이틀 문구 확인 실패 - 내 프로필 > 팀오너가 아닌 경우 소속 회사 떠나기 플로우 실패 3"

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    print("계정 및 설정 > 팀오너가 아닌 경우 > 내 프로필 > 소속된 회사 떠나기  완료")

    assert "회사를 입력해주세요." == page.locator("div").filter(has_text=re.compile(r"^회사를 입력해주세요\.$")).nth(3).inner_text(), \
        "내 프로필 > 회사 > 회사 입력창 Place내holder 확인 실패 - 내 프로필 > 팀오너가 아닌 경우 소속 회사 떠나기 플로우 실패 4"
    assert "회사 설정" == page.get_by_role("button", name="회사 설정").inner_text(), \
        "내 프로필 > 회사 > 회사 설정 링크 확인 실패 - 내 프로필 - 팀오너가 아닌 경우 소속 회사 떠나기 플로우 실패 5"

    print("계정 및 설정 > 팀오너가 아닌 경우 > 내 프로필 > 소속된 회사 떠나기 후 회사 > 설정 초기화 확인")

    page.get_by_role("button", name="저장").click()
    page.wait_for_timeout(1000)

    # page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    # page.wait_for_timeout(1000)

    page.get_by_role("tab", name="회사 정보").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="내 프로필").click()
    page.wait_for_timeout(1000)

    assert "회사를 입력해주세요." == page.locator("div").filter(has_text=re.compile(r"^회사를 입력해주세요\.$")).nth(3).inner_text(), \
        "내 프로필 > 회사 > 회사 입력창 Place내holder 확인 실패 - 내 프로필 > 팀오너가 아닌 경우 소속 회사 떠나기 플로우 실패 6"

    print("소속된 회사 떠나기 후 저장 -> 내 프로필 재진입 -> 회사 설정 초기화 확인 완료")
    print("----- 계정 및 설정 > 팀오너가 아닌 경우 > 내 프로필 > 소속회사 떠나기 플로우 확인 테스트 시작 -> 성공 -----")

