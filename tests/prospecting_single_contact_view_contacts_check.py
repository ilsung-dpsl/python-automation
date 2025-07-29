import re
import config

def test_prospecing_single_contact_view_contacts_check(page):
    print("----- 탐색하기 > 단일 연락처 > 연락처 확인 동작 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD3_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD3_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(500)
 #   page.get_by_role("button", name="Start Now").click()
 #   page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("구글 회사의 정보를 알려줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    count = page.locator("button:has-text('연락처 확인')").count()

    # Free 플랜 최대 열람 페이지 4까지 확인 - 최대 100명까지만 열람이 가능 하기 때문임
    max_pages = 4
    current_page = 1

    # 1~4 페이지 까지 연락처 확인 버튼 체크 > 연락처 확인 가능한 리드 확인 처리
    while current_page <= max_pages:
        page.wait_for_timeout(5000)

        print(f"🔍 탐색하기 {current_page} 페이지에서 '연락처 확인' 버튼 찾는 중...")
        buttons = page.locator("button:has-text('연락처 확인')")
        found = False
        print(f"연락처 확인 count : {buttons.count()}")

        # 해당 페이지 > 연락처 확인 버튼 총 개수를 파악해서, 가장 위에 있는 연락처 부터 확인하는 로직
        for i in range(buttons.count()):
            btn = buttons.nth(i)
            view_contacts_text = btn.inner_text().strip()

            page.wait_for_timeout(1000)

            # 연락처 확인 버튼의 "연락처 확인" 문구 인지 확인 후 클릭
            if view_contacts_text == "연락처 확인":
                print(f"연락처 확인 {i+1} 버튼 : {view_contacts_text} -> 버튼 클릭")
                btn.click()
                found = True

                page.wait_for_timeout(2000)

                # 확인됨 버튼 변경 및 크레딧 사용 토스트 메시지 확인 후 for 종료
                assert "확인됨" == page.locator("button:has-text('확인됨')").nth(i).inner_text(), f"연락처 확인 버튼 클릭 하지 못했거나, 클릭 했음에도 확인됨 변경 실패 1 > 연락처 확인 버튼 {i+1}"
                assert "1 크래딧이 사용되었습니다." == page.get_by_role("alert").filter(has_text="크래딧이 사용되었습니다.").inner_text(), "크레딧 소모 토스트 메시지 출력 실패 - 연락처 확인 실패 2"
                print("----- 탐색하기 > 단일 연락처 > 연락처 확인 동작 확인 테스트 시작 -> 성공 -----")
                break
        # 버튼을 찾고 클릭했으면 반복 종료
        if found:
            break

        # 해당 페이지 내 연락처 확인 버튼이 없으면, 탐색하기 > 다음 페이지 버튼 찾기 및 클릭
        next_button = page.locator("div").filter(has_text=re.compile(fr"^401 페이지 중 {current_page} 페이지페이지 바로가기$")).get_by_role("button").nth(1)

        # 해당 페이지 > 다음 페이지 버튼 활성화 체크
        if next_button.is_visible() and next_button.is_enabled():
            # 다음 페이지 이동 버튼 클릭 후 현재 페이지 + 1을 하여, 현재 페이지 위치를 기억
            print("탐색하기 [>] 다음 페이지로 이동")
            next_button.click()
            page.wait_for_timeout(1000)
            current_page += 1
        else:
            print("다음 페이지 버튼이 없거나 비활성화되어 클릭 실패. 종료")
            break

        #마지막 4페이지까지도 연락처 확인 버튼이 없을 경우, 테스트 실패 체크
        if(current_page == 4 and found == False):
            assert "연락처 확인" in page.content(), "4페이지까지 연락처 확인 버튼 없음 -> 확인할 수 있는 연락처 없어서 실패"
