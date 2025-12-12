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


def test_signupforfree_complete(page):
    """
    :type page: object
    """
    print("----- 2번 - 회원가입 완료 스크립트 테스트 시작 -----")
    print("20251212 회원가입 완료 테스트 진행 -> 20250111 테스트 진행 (1달에 1번 진행되는 테스트 스크립트)")

    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)
#    page.goto("https://dev.deepsales.io/ko/intro",wait_until="load", timeout=30000)

    # 20251125 - 세일즈 에이전트 > 플랜소개 > 시작하기 -> 회원가입 변경 플로우 코드 수정
    page.wait_for_timeout(1000)

    page.get_by_role("banner").get_by_role("link", name="세일즈 에이전트").click()
    page.wait_for_timeout(1000)

    # 20251212 - 세일즈 에이전트 진입 완료 확인용 코드 추가
    print("세일즈 에이전트 페이지 진입 완료")

    # 20251203 - 세일즈 에이전트 랜딩 페이지 > 상단 > [플랜 확인하기] 선택 코드 수정
    page.get_by_role("button", name="플랜 확인하기").click()
    page.wait_for_timeout(1000)

    # 20251203 - 세일즈 에이전트 랜딩 페이지 > 플랜소개 > Scale > [시작하기] 선택 앨리먼트 요소 수정되어 코드 수정
    page.get_by_role("button", name="시작하기").nth(2).click()
    page.wait_for_timeout(1000)

    # 20251212 - 회원가입 페이지 진입 완료 확인용 코드 추가
    print("회원가입 페이지 진입 완료")

    count = read_counter()
    page.get_by_placeholder("예) deepsales@deepsales.com").fill(f"ilsung.baek+pa{count}@deepsales.com")
    page.get_by_role("button", name="전송").click()
    page.wait_for_timeout(10000)

    # 3. 새 탭 열어 Gmail 로그인
    context = page.context
    new_tab = context.new_page()
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

    # 5. 원래 페이지로 돌아와 인증번호 입력
    page.bring_to_front()

    page.get_by_placeholder("인증번호를 입력해주세요").click()
    print(f"[Verification number] {code}")
    page.wait_for_timeout(2000)
    page.get_by_placeholder("인증번호를 입력해주세요").fill(code)
    page.get_by_role("button", name="확인").click()

    # 20251212 - 회원가입 > 인증번호 입력 완료 확인용 코드 추가
    print("회원가입 > 인증번호 입력 완료")

    page.get_by_placeholder("성 (영문 입력)").fill("백")
    page.get_by_placeholder("이름 (영문 입력)").fill("일성")
    page.locator(".text-base > .text-FG-Primary").first.click()
    page.locator("#react-select-2-input").fill("대한민국")
    page.get_by_text("대한민국", exact=True).click()
    page.get_by_placeholder("비밀번호 생성").fill(config.COMMON_PW)
    page.get_by_role("checkbox", name="이용약관 전체 동의하기").click()

    page.wait_for_timeout(7000)

    ### ---- ## 주석 2개가 실제 사용 코드, # 주석 1개는 이전 사용했던 코드나 사용하지 않음 ------

    page.get_by_role("button", name="가입하기").click()
    page.wait_for_timeout(5000)

   # page.get_by_role("button", name="Start Now").click()
   # page.wait_for_timeout(1000)

    # 20251125 - 세일즈 에이전트 페이지 > 상단 > [제품 이용하기] 선택 하는 코드 추가
    page.get_by_role("button", name="제품 이용하기").click()
    page.wait_for_timeout(1000)

    #20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    #20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    #20250930 - LNB > 탐색하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="탐색하기").nth(1).click()
    page.wait_for_timeout(2000)

    #page.get_by_role("paragraph").filter(has_text=re.compile(r"^필터$")).click()

    assert "탐색하기" == page.locator("#desktop-header-slot").get_by_text("탐색하기").inner_text(), \
        "회원가입 완료 후 탐색하기 이동 > '탐색하기' 타이틀 문구 확인 실패 - 회원가입 완료 실패 1"
    assert "필터" == page.get_by_text("필터").inner_text(), \
        "회원가입 완료 후 탐색하기 이동 > 필터 > '필터' 타이틀 문구 확인 실패 - 회원가입 완료 실패 2"

    print("회원가입 완료 후 탐색하기 이동 성공")
    
    count += 1
    write_counter(count)

    print (f"counter : {count}")

    #20250930 - 탐색하기 UI 변경(LNB 레이아웃)으로 인한 대시보드 선택 코드 수정
    page.get_by_role("link", name="대시보드").nth(1).click()
    page.wait_for_timeout(6000)

    assert "백 일성님\n환영합니다!" in page.get_by_text("백 일성님 환영합니다!").inner_text(), \
        "대시보드 환영문구 확인 실패 - 회원가입 실패 3"
    assert "크레딧 15/" in page.content(), \
        "대시보드 > 크레딧 보유량 확인 실패 - 회원가입 실패 3"

    print("----- 회원가입 완료 스크립트 테스트 시작 -> 성공 -----")