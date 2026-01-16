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


def test_MO_signupforfree_complete(mobile_page):
    """
    :type page: object
    """
    print("----- 3번 - MO 회원가입 완료 스크립트 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 세일즈 에이전트 페이지 진입 완료")

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="세일즈 에이전트 바우처").tap()
    mobile_page.wait_for_timeout(1000)

    # 20251212 - 세일즈 에이전트 진입 완료 확인용 코드 추가
    print("MO Web - 세일즈 에이전트 페이지 진입 완료")

    # 20251203 - 세일즈 에이전트 랜딩 페이지 > 상단 > [플랜 확인하기] 선택 코드 수정
    mobile_page.get_by_role("button", name="플랜 확인하기").tap()
    mobile_page.wait_for_timeout(1000)

    # 20251203 - 세일즈 에이전트 랜딩 페이지 > 플랜소개 > Scale > [시작하기] 선택 앨리먼트 요소 수정되어 코드 수정
    mobile_page.get_by_role("button", name="시작하기").nth(1).tap()
    mobile_page.wait_for_timeout(1000)

    # 20251212 - 회원가입 페이지 진입 완료 확인용 코드 추가
    print("MO Web - 회원가입 페이지 진입 완료")

    count = read_counter()
    mobile_page.get_by_placeholder("예) deepsales@deepsales.com").fill(f"ilsung.baek+pa{count}@deepsales.com")
    mobile_page.get_by_role("button", name="전송").tap()
    mobile_page.wait_for_timeout(10000)

    # 3. 새 탭 열어 Gmail 로그인
    browser = mobile_page.context.browser
    pc_context = browser.new_context(
        viewport={"width": 1440, "height": 800},
        user_agent="Chrome/143.0.7499.193"
    )

    new_tab = pc_context.new_page()
    new_tab.goto("https://mail.google.com")

    # Gmail 로그인
    new_tab.get_by_label("이메일 또는 휴대전화").fill(config.GMAIL_EMAIL)
    new_tab.get_by_role("button", name="다음").click()
    new_tab.wait_for_timeout(3000)
    new_tab.get_by_label("비밀번호 입력").fill(config.GMAIL_EMAIL_PW)
    new_tab.get_by_role("button", name="다음").click()

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

    # 20251212 - 회원가입 > 인증번호 입력 완료 확인용 코드 추가
    print("MO Web - 회원가입 > 인증번호 입력 완료")

    mobile_page.get_by_placeholder("성 (영문 입력)").fill("백")
    mobile_page.get_by_placeholder("이름 (영문 입력)").fill("일성")
    mobile_page.locator(".text-base > .text-FG-Primary").first.tap()
    mobile_page.locator("#react-select-2-input").fill("대한민국")
    mobile_page.get_by_text("대한민국", exact=True).tap()
    mobile_page.get_by_placeholder("비밀번호 생성").fill(config.COMMON_PW)
    mobile_page.get_by_role("checkbox", name="이용약관 전체 동의하기").tap()

    mobile_page.wait_for_timeout(7000)

    ### ---- ## 주석 2개가 실제 사용 코드, # 주석 1개는 이전 사용했던 코드나 사용하지 않음 ------

    # 20260116 - 채널톡으로 인해, 가입하기 버튼 영역을 가려버림 -> 채널톡을 닫고 가입하기 버튼을 선택할 수 있도록 코드 변경
    mobile_page.locator("iframe[name=\"intercom-notification-stack-frame\"]").content_frame.get_by_test_id(
        "notification-close").tap(timeout=10000)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("button", name="가입하기").tap(timeout=10000)
    mobile_page.wait_for_timeout(5000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # page.get_by_role("button", name="Start Now").click()
    # page.wait_for_timeout(1000)

    # 20251125 - 세일즈 에이전트 페이지 > 상단 > [제품 이용하기] 선택 하는 코드 추가
    #mobile_page.get_by_role("button", name="제품 이용하기").tap()
    #mobile_page.wait_for_timeout(1000)

    # 20260116 - 회원가입 완료 후 세일즈 에이전트 페이지로 이동되어 햄버거 메뉴 -> 제품 이용하기 버튼 이동 동작 추가
    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_role("button", name="제품 이용하기").tap()

    # 20250930 - LNB > 탐색하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    #mobile_page.get_by_role("link").filter(has_text="탐색하기").tap()
    mobile_page.wait_for_timeout(2000)

    # page.get_by_role("paragraph").filter(has_text=re.compile(r"^필터$")).click()

    assert "탐색하기" == mobile_page.locator("#desktop-header-slot").get_by_text("탐색하기").inner_text(), \
        "MO Web - 회원가입 완료 후 탐색하기 이동 > '탐색하기' 타이틀 문구 확인 실패 - 회원가입 완료 실패 1"
    assert "필터" == mobile_page.get_by_text("필터").inner_text(), \
        "MO Web - 회원가입 완료 후 탐색하기 이동 > 필터 > '필터' 타이틀 문구 확인 실패 - 회원가입 완료 실패 2"

    print("MO Web - 회원가입 완료 후 제품 이용하기 -> 탐색하기 이동 성공")

    count += 1
    write_counter(count)

    print(f"counter : {count}")

    # 20250930 - 탐색하기 UI 변경(LNB 레이아웃)으로 인한 대시보드 선택 코드 수정
    mobile_page.get_by_role("link").filter(has_text="대시보드").tap(timeout=10000)
    mobile_page.wait_for_timeout(6000)

    assert "백 일성님\n환영합니다!" in mobile_page.get_by_text("백 일성님 환영합니다!").inner_text(), \
        "MO Web - 대시보드 환영문구 확인 실패 - 회원가입 실패 3"
    assert "크레딧 15/" in mobile_page.content(), \
        "MO Web - 대시보드 > 크레딧 보유량 확인 실패 - 회원가입 실패 3"

    print("----- 3번 - MO 회원가입 완료 스크립트 테스트 시작 -> 성공 -----")