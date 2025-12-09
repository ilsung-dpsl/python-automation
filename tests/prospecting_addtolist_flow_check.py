import config
import re

def test_prospecting_addtolist_flow_check(page):
    print("----- 26번 - 탐색하기 > 리스트에 추가 동작 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD3_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD3_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
  #  page.get_by_role("button", name="Start Now").click()
  #  page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    #검색어 변경 - 20250805
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("let's travel 회사의 직원 정보를 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")
    page.wait_for_timeout(6000)

    #20240930 - 탐색하기 ui 변경으로 인한 리드 > 1번, 2번 체크 동작 코드 수정
    page.locator("div > .w-8 > .flex").first.click()
    page.wait_for_timeout(1000)

    page.locator("div:nth-child(2) > div > .w-8 > .flex").click()
    page.wait_for_timeout(1000)


    page.get_by_role("button", name="리스트에 추가").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="새 리스트 생성").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="/50").fill("test 1")
    page.wait_for_timeout(500)
    page.get_by_role("button", name="생성하기").click()
    page.wait_for_timeout(2000)

    assert "test 1" in page.content(), "마이리스트 폴더 생성 실패 - 리스트 생성 실패"

    page.locator("div").filter(has_text=re.compile(r"^default$")).first.click()
    page.locator("div").filter(has_text=re.compile(r"^test 1$")).first.click()


    #page.get_by_role("checkbox", name="default").click()
    #page.get_by_role("checkbox", name="test").click()

    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(5000)

    #20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    #20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    #20250930 - LNB > 대시보드 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="마이 리스트").nth(1).click()
    page.wait_for_timeout(3000)

    #20250930 - 기본 폴더 선택 동작 코드 수정
    page.locator("div").filter(has_text=re.compile(r"^기본$")).nth(1).click()
    page.wait_for_timeout(3000)

    #Default 폴더 > 데이터 위치 변경으로 인한 리드 데이터 정보 수정 - 20250829
    assert "Gayle Botti" in page.content(), "Default 폴더 test 1의 리드 1번 성함 확인 실패 - 리스트에 추가 실패 1"
    assert "Stalin Stalinsjc" in page.content(), "Default 폴더 test 1의 리드 2번 성함 확인 실패 - 리스트에 추가 실패 1"
    page.get_by_role("button", name="리스트로 돌아가기").click()

    page.wait_for_timeout(3000)
    page.locator("div").filter(has_text=re.compile(r"^test 1$")).nth(1).click()
    page.wait_for_timeout(3000)

    #test 폴더 > 데이터 위치 변경으로 인한 리드 데이터 정보 수정 - 20250829
    assert "Gayle Botti" in page.content(), "일반 폴더 test 1의 리드 1번 성함 확인 실패 - 리스트에 추가 실패 2"
    assert "Stalin Stalinsjc" in page.content(), "일반 폴더 test 1의 리드 2번 성함 확인 실패 - 리스트에 추가 실패 2"

    page.get_by_role("button", name="리스트로 돌아가기").click()

    page.wait_for_timeout(3000)

    #20250930 - 기본 폴더 선택 동작 코드 수정
    page.locator("div").filter(has_text=re.compile(r"^기본$")).nth(1).click()

    #Default 폴더 > 리스트 1, 2 체크 동작 코드 수정 - 20250805
    page.locator(".ml-\\[2px\\] > .flex").first.click()
    page.locator("div:nth-child(2) > div > .ml-\\[2px\\] > .flex").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)
    page.locator("#modal-root").get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="리스트로 돌아가기").click()
    page.wait_for_timeout(1000)
    page.locator("div").filter(has_text=re.compile(r"^test 1$")).nth(1).click()

    #test 1 폴더 > 리스트 1, 2 체크 동작 코드 수정 - 20250805
    page.locator(".ml-\\[2px\\] > .flex").first.click()
    page.locator("div:nth-child(2) > div > .ml-\\[2px\\] > .flex").click()

    page.wait_for_timeout(1000)

    page.get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)
    page.locator("#modal-root").get_by_role("button", name="삭제").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="리스트로 돌아가기").click()
    page.wait_for_timeout(3000)
    page.locator("div:nth-child(3) > div:nth-child(6) > div").click()
    page.wait_for_timeout(1000)
    page.get_by_role("menuitem", name="리스트 삭제").click()
    page.wait_for_timeout(3000)

    print("----- 탐색하기 > 리스트에 추가 동작 확인 테스트 시작 -> 성공 -----")
