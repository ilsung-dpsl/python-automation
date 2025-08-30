import config
import re

def test_account_and_settings_my_profile_input_add_edit_flow_check(page):
    print("----- 계정 및 설정 > 내 프로필 > 모든 정보 기업 후 저장 / 추가 / 수정 확인 테스트 시작 -----")

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
    page.get_by_text("계정 및 설정").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="내 프로필").click()
    page.wait_for_timeout(1000)

    print("계정 및 설정 > 내 프로필 페이지 진입 완료")

    page.get_by_placeholder("이름").fill("백")
    page.wait_for_timeout(500)
    page.get_by_placeholder("성").fill("이성")
    page.wait_for_timeout(500)

    print("내 프로필 > 이름 / 성 완료")

    page.get_by_placeholder("LinkedIn URL을 입력해 주세요").fill("https://www.linkedin.com/in/ilsung-baek-221769363/")
    page.wait_for_timeout(500)

    print("내 프로필 > 링크드인 정보 입력 완료")

    page.locator(".text-FG-Primary.css-124rwol").first.click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-2-input").fill("deepsales")
    page.wait_for_timeout(1000)

    page.locator("#react-select-2-option-0").get_by_text("DeepSales").click()
    page.wait_for_timeout(1000)

    print("내 프로필 > 회사 > Deepsales 정보 설정 완료")

    page.locator(".border.rounded-\\[6px\\].bg-\\[\\#ffffff\\].hover\\:cursor-pointer.\\!min-h-10.border-Border-Default-a > .text-base > .text-FG-Primary.css-124rwol").first.click()
    page.wait_for_timeout(1000)

    page.get_by_text("Product").click()
    page.wait_for_timeout(1000)

    print("내 프로필 > 부서 > Product 설정 완료")

    page.locator("[id=\":r1f:-form-item\"] > .css-b62m3t-container > .border > .text-base > .text-FG-Primary.css-124rwol").click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-5-input").fill("매니저")
    page.wait_for_timeout(500)

    page.locator("#react-select-5-input").press("Enter")
    page.wait_for_timeout(1000)

    print("내 프로필 > 직급 > 매니저 설정 완료")

    page.locator("[id=\":r1g:-form-item\"] > .flex.flex-col.gap-5 > .flex.flex-col.gap-3 > div:nth-child(2) > div > .css-b62m3t-container > .border > .text-base > .text-FG-Primary.css-124rwol").click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-7-input").fill("manager")
    page.wait_for_timeout(1000)

    page.get_by_text("Manager", exact=True).click()
    page.wait_for_timeout(1000)

    print("내 프로필 > 직함 > Manager 설정 완료")

    page.get_by_role("radio", name="남성").click()
    page.wait_for_timeout(1000)

    page.locator("[id=\":r1q:-form-item\"] > .css-b62m3t-container > .border > .text-base > .text-FG-Primary.css-124rwol").dblclick()
    page.wait_for_timeout(1000)

    page.locator(".border.rounded-\\[6px\\].bg-\\[\\#ffffff\\].hover\\:cursor-pointer.\\!min-h-10.border-Border-Inversed > .text-base > .text-FG-Primary.css-124rwol").click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-8-input").fill("일본")
    page.wait_for_timeout(1000)

    page.get_by_text("일본", exact=True).click()
    page.wait_for_timeout(1000)

    print("내 프로필 > 나라(국적) > 일본 설정 완료")

    page.locator("[id=\":r1r:-form-item\"] > .css-b62m3t-container > .border > .text-base > .text-FG-Primary").click()
    page.wait_for_timeout(1000)

    page.get_by_role("option", name="한국어").get_by_role("checkbox").click()
    page.wait_for_timeout(1000)

#    page.locator("div").filter(has_text=re.compile(r"^언어\(1\)$")).first.click()

    print("내 프로필 > 언어 > 한국어 설정 완료")

    page.get_by_role("button", name="저장").click()
    page.wait_for_timeout(1000)

    assert "update completed!" == page.get_by_text("update completed!").inner_text(), \
        "내 프로필 > 필수 정보 입력 후 저장 시 토스트 메시지 확인 실패 - 내 프로필 > 입력 후 저장 실패 1"

    page.get_by_role("tab", name="회사 정보").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="내 프로필").click()
    page.wait_for_timeout(1000)

    assert "이성" == page.get_by_placeholder("이름").input_value(), \
        "내 프로필 > 이전 입력한 이름 확인 실패 - 내 프로필 저장 실패 1"
    assert "https://www.linkedin.com/in/ilsung-baek-221769363/" == page.get_by_placeholder("LinkedIn URL을 입력해 주세요").input_value(), \
        ""

    page.locator("[id=\":r7g:-form-item\"]").click()
    page.locator(".text-FG-Primary.css-124rwol").first.click()
    page.locator(".text-FG-Primary.css-124rwol").first.click()
    page.locator("div").filter(has_text=re.compile(r"^EnglishProduct언어추가$")).locator("svg").nth(1).click()
    page.locator(".border.rounded-\\[6px\\].bg-\\[\\#ffffff\\].hover\\:cursor-pointer.\\!min-h-10.border-Border-Inversed > .p-1.css-1wy0on6 > .p-1").click()
    page.locator(".border.rounded-\\[6px\\].bg-\\[\\#ffffff\\].hover\\:cursor-pointer.\\!min-h-10.border-Border-Default-a > .text-base > .text-FG-Primary.css-124rwol").first.click()
    page.locator("form div").filter(has_text="직급10 results available.Use Up").locator("svg").click()
    page.locator("[id=\":r7j:-form-item\"] > .flex.flex-col.gap-5 > .flex.flex-col > .relative > div > .css-b62m3t-container > .border > .text-base > .text-FG-Primary.css-124rwol").click()
    page.locator("form div").filter(has_text="직함1/2English21 results").locator("svg").nth(1).click()
    page.locator("[id=\":r7t:-form-item\"] > .css-b62m3t-container > .border > .text-base > .text-FG-Primary.css-124rwol").click()
    page.locator("form div").filter(has_text="나라(국적)*249 results available.").locator("svg").click()
    page.get_by_text("언어(1)").click()
    page.locator("form div").filter(has_text="언어 추가*155 results available.").locator("svg").nth(1).click()
