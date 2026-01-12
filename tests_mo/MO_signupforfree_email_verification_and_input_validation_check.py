import re
from pydoc import pager

import config
from config import read_counter, write_counter

# Gmail API를 위한 OAuth 범위
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def extract_code_from_email(page):
    """
    Gmail 페이지에서 인증번호가 포함된 이메일을 열고 코드 추출
    """
    # Gmail '받은편지함' 대기
    page.wait_for_selector("table[role='grid']")

    # 가장 위쪽 메일 클릭
    page.locator("table[role='grid'] tr").first.click()

    # 메일 본문 내용 로딩 대기
    page.wait_for_timeout(2000)

    # 본문 텍스트 가져오기
    items = page.locator("div[role='listitem']")
    count = items.count()

    if count == 0:
        raise Exception("메일 본문(listitem)을 찾을 수 없습니다.")

        # 가장 마지막 listitem의 텍스트 추출
    last_item_text = items.nth(count - 1).inner_text()

    # 인증번호 찾기 (숫자 6자리)
    match = re.search(r"\b\d{6}\b", last_item_text)
    if match:
        return match.group(0)
    else:
        raise Exception("인증번호를 찾을 수 없습니다.")


def test_MO_signupforfree_email_verification_and_input_validation_check(mobile_page):
    """
    :type page: object
    """
    print("----- 2번 - MO 회원가입 완료 전까지 프로세스 확인 스크립트 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    print("세일즈 에이전트 페이지 진입 완료")

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="세일즈 에이전트 바우처").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="플랜 확인하기").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="시작하기").nth(1).tap()
    mobile_page.wait_for_timeout(1000)

    print("회원가입 페이지 진입 완료")

    count = read_counter()
    mobile_page.get_by_placeholder("예) deepsales@deepsales.com").fill(f"ilsung.baek+pa{count}@deepsales.com")
    mobile_page.get_by_role("button", name="전송").tap()
    mobile_page.wait_for_timeout(10000)

    # 3. 새 탭 열어 Gmail 로그인
    browser = mobile_page.context.browser
    pc_context = browser.new_context(
        viewport={"width": 1440, "height": 800},
        user_agent="Chrome/143.0.7499.170"
    )

    new_tab = pc_context.new_page()
    new_tab.goto("https://mail.google.com")

    # Gmail 로그인
    new_tab.get_by_label("이메일 또는 휴대전화").fill(config.GMAIL_EMAIL)
    new_tab.get_by_role("button", name="다음").click()
    new_tab.wait_for_timeout(3000)
    new_tab.get_by_label("비밀번호 입력").fill(config.GMAIL_EMAIL_PW)
    new_tab.get_by_role("button", name="다음").click()
    new_tab.wait_for_timeout(3000)

    # Gmail 앱 사용 안내 페이지 > 웹 버전 사용 버튼 선택 코드
    #new_tab.get_by_text("웹 버전 사용").click()

    # 4. 이메일에서 인증번호 추출
    new_tab.wait_for_timeout(10000)  # Gmail 로딩 대기
    code = extract_code_from_email(new_tab)

    print("인증번호:", code)

    new_tab.close()

    # 5. 원래 페이지로 돌아와 인증번호 입력
    mobile_page.bring_to_front()

    mobile_page.get_by_placeholder("인증번호를 입력해주세요").tap()
    print(f"[Verification number] {code}")
    mobile_page.wait_for_timeout(2000)
    mobile_page.get_by_placeholder("인증번호를 입력해주세요").fill(code)
    mobile_page.get_by_role("button", name="확인").tap()

    print("회원가입 > 인증번호 입력 완료")

    mobile_page.get_by_placeholder("성 (영문 입력)").fill("백")
    mobile_page.get_by_placeholder("이름 (영문 입력)").fill("일성")
    mobile_page.locator(".text-base > .text-FG-Primary").first.tap()
    mobile_page.locator("#react-select-2-input").fill("대한민국")
    mobile_page.get_by_text("대한민국", exact=True).tap()
    mobile_page.get_by_placeholder("비밀번호 생성").fill(config.COMMON_PW)
    mobile_page.get_by_role("checkbox", name="이용약관 전체 동의하기").tap()

    mobile_page.wait_for_timeout(7000)

    assert "이메일 인증이 완료되었습니다." == mobile_page.get_by_text("이메일 인증이 완료되었습니다").inner_text(), \
        "인증번호 완료 후 이메일 인증 완료 안내 문구 확인 실패 - 회원가입 완료 전 프로세스 확인 실패 1"
    assert "백" == mobile_page.get_by_placeholder("성 (영문 입력)").input_value(), \
        "회원가입 > 성 > 입력값 확인 실패 - 회원가입 완료 전 프로세스 확인 실패 2"
    assert "일성" == mobile_page.get_by_placeholder("이름 (영문 입력)").input_value(), \
        "회원가입 > 이름 > 입력값 확인 실패 - 회원가입 완료 전 프로세스 확인 실패 3"
    button = mobile_page.get_by_role("button", name="가입하기")
    assert button.is_enabled(), \
        "회원가입 > 가입하기 버튼 활성화 노출 확인 실패 - 회원가입 완료 전 프로세스 확인 실패 4"

    print("----- 2번 - MO 회원가입 완료 전까지 프로세스 확인 스크립트 테스트 시작 -> 성공 -----")