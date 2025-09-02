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

    page.get_by_placeholder("이름").fill("이성")
    page.wait_for_timeout(500)
    page.get_by_placeholder("성").fill("백")
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
    page.wait_for_timeout(2000)

#    page.get_by_text("Product").click()
    page.get_by_role("option", name="Product").locator("div").click()
    page.wait_for_timeout(1000)

#    page.locator(".css-b62m3t-container > .border > .text-base > div:nth-child(2)").first.click()
#    page.wait_for_timeout(2000)

#    page.get_by_role("option", name="Product").locator("div").click(force=True)
#    page.wait_for_timeout(1000)

    print("내 프로필 > 부서 > Product 설정 완료")

    page.locator("[id=\":r1f:-form-item\"] > .css-b62m3t-container > .border > .text-base > .text-FG-Primary.css-124rwol").click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-5-input").fill("매니저")
    page.wait_for_timeout(500)

    page.locator("#react-select-5-input").press("Enter")
    page.wait_for_timeout(1000)

    print("내 프로필 > 직급 > 매니저 설정 완료")
    page.locator("[id=\"\\:r1f\\:-form-item\"] > .css-b62m3t-container > .border > .text-base > div:nth-child(2)").click()
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

    page.locator(
        ".border.rounded-\\[6px\\].bg-\\[\\#ffffff\\].hover\\:cursor-pointer.\\!min-h-10.border-Border-Inversed > .text-base > .text-FG-Primary.css-124rwol").click()
    page.wait_for_timeout(1000)

    page.locator("#react-select-8-input").fill("일본")
    page.wait_for_timeout(1000)


    page.get_by_text("일본", exact=True).click()
    page.wait_for_timeout(1000)

    print("내 프로필 > 나라(국적) > 일본 설정 완료")

    #기존에 설정된 언어 삭제 후 재설정 - 20250830
    page.locator("[id=\"\\:r1r\\:-form-item\"] > .css-b62m3t-container > .border > div:nth-child(2) > div").first.click()
    page.wait_for_timeout(1000)

    page.locator("[id=\":r1r:-form-item\"] > .css-b62m3t-container > .border > .text-base > .text-FG-Primary").click()
    page.wait_for_timeout(1000)

    page.get_by_role("option", name="한국어").get_by_role("checkbox").click()
    page.wait_for_timeout(1000)

    page.locator("form div").filter(has_text="언어 추가*option 한국어, selected.").locator("svg").nth(1).click()
    page.wait_for_timeout(1000)

#    page.locator("div").filter(has_text=re.compile(r"^언어\(1\)$")).first.click()

    print("내 프로필 > 언어 > 한국어 설정 완료")

    page.get_by_role("button", name="저장").click()
    page.wait_for_timeout(1000)

    assert "update completed!" == page.get_by_text("update completed!").inner_text(), \
        "내 프로필 > 필수 정보 입력 후 저장 시 토스트 메시지 확인 실패 - 내 프로필 > 입력 후 저장 실패 1"

    print("내 프로필 > 필수 입력 후 저장 완료")
    page.get_by_role("tab", name="회사 정보").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="내 프로필").click()
    page.wait_for_timeout(2000)

    assert "이성" == page.get_by_placeholder("이름").input_value(), \
        "내 프로필 > 이전 입력한 이름 확인 실패 - 내 프로필 저장 실패 1"
    assert "https://www.linkedin.com/in/ilsung-baek-221769363/" == page.get_by_placeholder("LinkedIn URL을 입력해 주세요").input_value(), \
        "내 프로필 > 이전 입력한 이름 확인 실패 - 내 프로필 저장 실패 2"
    assert "소속 회사 떠나기 >" == page.get_by_role("button", name="소속 회사 떠나기 >").inner_text(), \
        "내 프로필 > 이전 회사 설정 후 소속 회사 떠나기 버튼 확인 실패 - 내 프로필 저장 실패 3"
    assert "Product" == page.locator(".relative > div > .css-b62m3t-container > .border").first.inner_text(), \
        "내 프로필 > 이전 설정한 부서명 확인 실패 - 내 프로필 저장 실패 4"
    assert "매니저" == page.get_by_text("매니저").inner_text(), \
        "내 프로필 > 이전 설정한 직급 확인 실패 - 내 프로필 저장 실패 5"
    assert "Manager" == page.get_by_text("Manager").inner_text(), \
        "내 프로필 > 이전 설정한 직함 확인 실패 - 내 프로필 저장 실패 6"
    assert "일본" == page.get_by_text("일본").inner_text(), \
        "내 프로필 > 이전 설정한 나라(국적) 확인 실패 - 내 프로필 저장 실패 7"
    assert "언어(1)" == page.get_by_text("언어(1)").inner_text(), \
        "내 프로필 > 이전 설정한 언어 설정 확인 실패 - 내 프로필 저장 실패 8"

    print("내 프로필 > 필수 정보 입력 후 저장 -> 저장한 데이터 확인 완료")


    page.locator("div").filter(has_text=re.compile(r"^언어 추가\*언어\(1\)$")).locator("svg").first.click(force=True)
    page.wait_for_timeout(1000)

    page.locator("div").filter(has_text=re.compile(r"^추가할 언어를 선택해 주세요\.$")).first.click()
    page.wait_for_timeout(1000)

    page.get_by_role("option", name="영어").get_by_role("checkbox").click()
    page.wait_for_timeout(1000)

    page.get_by_role("option", name="한국어").get_by_role("checkbox").click()
    page.wait_for_timeout(1000)

    page.get_by_role("option", name="스페인어").get_by_role("checkbox").click()
    page.wait_for_timeout(1000)

    page.locator("form div").filter(has_text="언어 추가*option 스페인어, selected.").locator("svg").nth(1).click()
    page.wait_for_timeout(1000)


   # page.locator("form div").filter(has_text="언어 추가*option 스페인어, selected.").locator("svg").nth(1).click()
   # page.wait_for_timeout(1000)

    print("내 프로필 > 언어 추가 완료")

    page.get_by_role("button", name="저장").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="회사 정보").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="내 프로필").click()
    page.wait_for_timeout(2000)

    assert "언어(3)" == page.get_by_text("언어(3)").inner_text(), \
        "내 프로필 > 언어 추가 설정 후 언어 3개 설정 여부 확인 실패 - 내 프로필 추가 후 저장 실패 1"

    print("내 프로필 > 언어 추가 후 저장 반영 확인 완료")

    page.get_by_placeholder("이름").fill("일성")
    page.wait_for_timeout(500)
    page.get_by_placeholder("성").fill("백")
    page.wait_for_timeout(500)

    print("내 프로필 > 성, 이름 수정 완료")

    page.locator("div").filter(has_text=re.compile(r"^나라\(국적\)\*일본$")).locator("svg").click(force=True)
    page.wait_for_timeout(2000)

    #대한민국 옵션 선택하는 것으로 코드 수정 - 20250902
    page.get_by_text("대한민국", exact=True).click(force=True)
    page.wait_for_timeout(1000)

    print("내 프로필 > 나라(국적) > 대한민국으로 수정 완료")

    page.locator("div").filter(has_text=re.compile(r"^언어 추가\*언어\(3\)$")).locator("svg").first.click(force=True)
    page.wait_for_timeout(1000)

    page.locator("div").filter(has_text=re.compile(r"^추가할 언어를 선택해 주세요\.$")).first.click()
    page.wait_for_timeout(1000)

    page.get_by_role("option", name="영어").get_by_role("checkbox").click()
    page.wait_for_timeout(1000)

    page.locator("form div").filter(has_text="언어 추가*option 영어, selected.155").locator("svg").nth(1).click()
    page.wait_for_timeout(1000)

    print("내 프로필 > 언어 추가 > 영어 재설정 완료")

    page.get_by_role("button", name="저장").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="회사 정보").click()
    page.wait_for_timeout(1000)

    page.get_by_role("tab", name="내 프로필").click()
    page.wait_for_timeout(1000)

    assert "백" == page.get_by_placeholder("성").input_value(), \
        "내 프로필 > 이전 수정한 성 확인 실패 - 내 프로필 수정 실패 1"
    assert "일성" == page.get_by_placeholder("이름").input_value(), \
        "내 프로필 > 이전 수정한 이름 확인 실패 - 내 프로필 수정 실패 2"
    assert "대한민국" == page.get_by_text("대한민국").inner_text(),\
        "내 프로필 > 이전 수정한 이름 확인 실패 - 내 프로필 수정 실패 3"
    assert "언어(1)" == page.get_by_text("언어(1)").inner_text(), \
        "내 프로필 > 이전 수정한 언어 추가 확인 실패 - 내 프로필 수정 실패 4"

    print("내 프로필 > 수정 후 정상 수정 확인 완료")

    page.get_by_role("button", name="소속 회사 떠나기 >").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)

    #소속회사 떠나기 후 저장 클릭 코드 추가 - 20250902
    page.get_by_role("button", name="저장").click()
    page.wait_for_timeout(1000)

    print("내 프로필 > 소속된 회사 떠나기 처리 후 모든 작업 완료")
    print("----- 계정 및 설정 > 내 프로필 > 모든 정보 기업 후 저장 / 추가 / 수정 확인 테스트 시작 -> 성공 -----")