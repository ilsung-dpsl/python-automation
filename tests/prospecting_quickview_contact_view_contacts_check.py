import re
from logging import exception

import config

def test_prospecting_quickview_contact_view_contacts_check(page):
    print("----- 탐색하기 > 퀵뷰(연락처) > 연락처 확인 시 동작 여부 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Start Now").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("일본 엔터테인먼트 회사 중에 직급이 매니저인 사람을 찾아줘")
    page.locator("#desktop-header-slot").get_by_role("img").nth(2).click()

    page.wait_for_timeout(7000)

    max_pages = 4
    found = False

    # 페이지별로 반복 (최대 4페이지)
    for page_number in range(1, max_pages+1):
        print(f"\n===== {page_number}페이지 탐색 중 =====")
    #    page.wait_for_selector("div.table-row")

        rows = page.locator("button:has-text('연락처 확인')")

        row_count = rows.count()

        print(f"{page_number} 페이지의 리드데이터는 총 {row_count}")

        for i in range(row_count):
            row = rows.nth(i)
            print(f"리드 데이터 {i+1} 번쨰 연락처 확인 버튼 활성화 되어 있는지 확인 중....")

            if row.locator("button:has-text('연락처 확인')").is_visible():
                print(f"👉 {i+1}번째 행에서 연락처 확인 버튼 발견!")

                # 버튼 클릭
                row.click()
                print("🟢 해당 리드 행 클릭하여 상세정보 열기")

                # 오른쪽 팝업 대기
                try:
                    page.wait_for_selector("div.drawer-content", timeout=5000)
                    popup_button = page.locator("div.drawer-content button:has-text('연락처 확인')")

                    if popup_button.is_visible():
                        popup_button.click()
                        page.wait_for_timeout(2000)
                        assert "확인됨" == page.locator("div.drawer-content button:has-text('확인됨')").inner_text(), \
                            "퀵뷰(연락처) > [확인됨] 변경 처리 실패 - 퀵뷰 연락처 확인 실패 1"
                        assert "1 크래딧이 사용되었습니다." == page.get_by_role("alert").filter(
                            has_text="크래딧이 사용되었습니다.").inner_text(), \
                            "퀵뷰(연락처) > 크레딧 소모 토스트 메시지 출력 실패 - 퀵뷰 연락처 확인 실패 2"
                        assert False == popup_button.is_visible(), \
                            "퀵뷰(연락처) > 확인됨 비활성화 처리 안됨 - 퀵뷰 연락처 확인 실패 3"
                        print("✅ 팝업 내 연락처 확인 버튼 클릭 완료")
                    else:
                        print("⚠️ 팝업 내 버튼이 없습니다.")

                except TimeoutError:
                    print("❌ 팝업이 열리지 않았습니다 (Timeout)")

                found = True
                break  # 찾았으면 더 이상 탐색 안 함

        if found:
            break  # 전체 페이지 반복 종료

        # 다음 페이지 이동 처리 (4페이지까지만)
        try:
            print(f"다음 페이지 이동 케이스 시작 - {page_number} 페이지 확인")

            next_button = page.locator("div").filter(has_text=re.compile(fr"^80 페이지 중 {page_number} 페이지페이지 바로가기$")).get_by_role("button").nth(
                1)

            print(f"next_button count : {next_button.count()}")

            if next_button.is_visible():
                page.wait_for_timeout(2000)
                next_button.click()
                print("➡️ 다음 페이지로 이동")
                page.wait_for_timeout(3000)
            else:
                print("❌ 다음 버튼이 비활성화됨")
                break
        except:
            print("❌ 다음 버튼을 찾을 수 없습니다.")
            #continue
            break

    # 결과 처리
    if not found:
        raise Exception("❌ 테스트 실패: 4페이지 모두 확인했지만 '연락처 확인' 버튼을 찾지 못했습니다.")
