import config
import re

def test_company_register_for_a_new_company_flow_check(page):
    print("----- 회사 정보 > 회사 정보 생성 페이지에서, 필수 정보 정상 입력 확인 테스트 시작 -----")

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

    page.get_by_text("회사 정보").click()
    page.wait_for_timeout(1000)

    page.get_by_text("등록하기").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("회사명을 영어로 입력해 주세요").fill("ilsung AI Corperation 1")
    page.wait_for_timeout(500)
    print("회사 정보 생성 페이지 > 회사명 입력 완료")

    page.get_by_placeholder("URL 정보를 입력해 주세요").fill("https://deepsales.com/ko")
    page.wait_for_timeout(500)
    print("회사 정보 생성 페이지 > 웹사이트 정보 입력 완료")

    page.locator(".p-5").click()
    page.wait_for_timeout(1000)

    page.get_by_text("산업 카테고리를 선택해 주세요").click()
    page.wait_for_timeout(1000)

    page.get_by_text("Accommodation Services", exact=True).nth(1).click()
    page.wait_for_timeout(1000)

    page.get_by_text("Food and Beverage Services", exact=True).click()
    page.wait_for_timeout(1000)

    page.get_by_text("Bars, Taverns, and Nightclubs", exact=True).click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="확인").click()
    page.wait_for_timeout(1000)
    print("회사 정보 생성 페이지 > 산업군 설정 완료")

    #page.get_by_text("Accommodation Services > Food").click()

    page.get_by_text("회사 위치를 검색해 주세요").click()
    page.wait_for_timeout(1000)

    #위치 정보 입력창 선택하는 코드 추가 - 20250902
    page.get_by_placeholder("귀사의 주소를 검색하세요").click()
    page.get_by_placeholder("귀사의 주소를 검색하세요").fill("송파대로 111")
    #대기 시간 3초 -> 5초로 증가 - 20250904
    page.wait_for_timeout(5000)

    page.get_by_text("Songpa District, 송파대로").click()
    page.wait_for_timeout(1000)

    page.locator("#modal-root").get_by_role("button", name="저장").click()
    page.wait_for_timeout(1000)
    print("회사 정보 생성 페이지 > 위치 설정 완료")

    page.get_by_placeholder("연간 매출(달러)을 입력해 주세요").fill("$200,000")
    page.wait_for_timeout(1000)
    print("회사 정보 생성 페이지 > 연간 매출 입력 완료")

    page.locator(".text-FG-Primary.css-124rwol").first.click()
    page.wait_for_timeout(1000)

    page.get_by_text("2020").click()
    page.wait_for_timeout(1000)
    print("회사 정보 생성 페이지 > 설립연도 설정 완료")

    page.locator(".border.rounded-\\[6px\\].bg-\\[\\#ffffff\\].hover\\:cursor-pointer.\\!min-h-10.border-Border-Default-a").first.click()
    page.wait_for_timeout(1000)

    page.get_by_role("option", name="1 -").locator("div").click()
    page.wait_for_timeout(1000)
    print("회사 정보 생성 페이지 > 직원 수 설정 완료")

    page.get_by_role("textbox", name="귀사의 제품과 서비스를 간략히 소개하는 내용을 포함하여 회사에 대한 소개를 작성해 주세요(최소 50자 이상)").fill("ilsung AI Corperation Cosmetic, Software, etc.")
    page.wait_for_timeout(3000)

    print("회사 정보 생성 페이지 > 필수 정보 입력 완료")

    assert "ilsung AI Corperation 1" == page.get_by_placeholder("회사명을 영어로 입력해 주세요").input_value(), \
        "회사 정보 생성 페이지 > 회사명 입력 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 1"
    assert "https://deepsales.com/ko" == page.get_by_placeholder("URL 정보를 입력해 주세요").input_value(), \
        "회사 정보 생성 페이지 > 웹사이트 입력 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 2"
    assert "Accommodation Services > Food" in page.get_by_text("Accommodation Services > Food").inner_text(), \
        "회사 정보 생성 페이지 > 산업군 설정 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 3"
    assert "111 Songpa-daero, Songpa" in page.get_by_text("111 Songpa-daero, Songpa").inner_text(), \
        "회사 정보 생성 페이지 > 위치 설정 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 4"
    assert "$200,000" == page.get_by_placeholder("연간 매출(달러)을 입력해 주세요").input_value(), \
        "회사 정보 생성 페이지 > 연간 매출 설정 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 5"
    assert "2020" == page.get_by_text("2020").inner_text(), \
        "회사 정보 생성 페이지 > 설립연도 설정 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 6"
    assert "1 - 10" == page.get_by_text("1 - 10").inner_text(), \
        "회사 정보 생성 페이지 > 직원 수 설정 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 7"
    assert "ilsung AI Corperation Cosmetic, Software, etc." == page.get_by_role("textbox", name="귀사의 제품과 서비스를 간략히 소개하는 내용을 포함하여 회사에 대한 소개를 작성해 주세요(최소 50자 이상)").input_value(), \
        "회사 정보 생성 페이지 > 영어 설명 입력 후 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 8"
    assert "저장" == page.get_by_role("button", name="저장").inner_text(), \
        "회사 정보 생성 페이지 > 저장 버튼 확인 실패 - 회사 생성 > 필수 입력 후 확인 실패 9"


    print("회사 정보 생성 페이지 > 필수 정보 입력 > 확인 완료")
    print("----- 회사 정보 > 회사 정보 생성 페이지에서, 필수 정보 정상 입력 확인 테스트 시작 -> 성공 -----")
