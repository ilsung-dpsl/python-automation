import config
import re

def test_prospecting_addtolist_flow_check(page):
    print("----- 탐색하기 > 리스트에 추가 동작 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
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

    #page.locator(".w-\\[32px\\] > .w-fit > .p-\\[2px\\]").first.click()
    page.locator(".w-\\[32px\\].h-\\[48px\\] > .flex").first.click()
    page.wait_for_timeout(1000)
    #page.locator("div:nth-child(2) > div > .w-\\[32px\\] > .w-fit > .p-\\[2px\\]").click()
    page.locator("div:nth-child(2) > div > .w-\\[32px\\] > .flex").click()
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
    page.get_by_role("link").filter(has_text="마이 리스트").click()
    page.wait_for_timeout(3000)
    page.get_by_role("link").filter(has_text="마이 리스트").click()
    page.wait_for_timeout(3000)

    page.get_by_text("기본2(2 미확인)백 일성").click()
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
