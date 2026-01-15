import config
import re

def test_MO_prospecting_quickview_contact_view_contacts_check(mobile_page):
    print("----- 26번 - MO 탐색하기 > 퀵뷰(연락처) > 연락처 확인 시 동작 여부 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    # Free plan의 pa25 계정 정보 변경 - 20250903
    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA25_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA25_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    # 검색으를 Kuwait Oil의 직급이 시니어인 직원 정보를 찾아줘 검색어 입력으로 변경 - 20250903
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("Kuwait Oil의 직급이 시니어인 직원 정보를 찾아줘")
    # 탐색하기 > 검색창 > 검색버튼 클릭하는 코드 수정 - 20250805
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    mobile_page.wait_for_timeout(7000)

    print("MO Web - 탐색하기 검색 완료 후")

    max_pages = 4
    found = False

    # 페이지별로 반복 (최대 4페이지)
    for page_number in range(1, max_pages + 1):
        max_row_count = 25
        print(f"\n===== {page_number}페이지 탐색 중 =====")
        #    page.wait_for_selector("div.table-row")

        rows = mobile_page.locator("button:has-text('연락처 확인')")

        row_count = rows.count()

        print(f"{page_number} 페이지의 연락처 확인 가능한 리드 데이터는 총 {row_count}")

        for i in range(row_count):
            row = rows.nth(i)
            row_current = max_row_count - row_count + 1
            print(f"리드 데이터 총 {row_count}개이고, 리드 {row_current} 번째부터 연락처 확인 버튼 활성화 되어 있는지 확인 중....")

            test_check = row.is_visible()
            print(f"연락처 확인 버튼 활성화 여부 : {test_check}")

            if row.is_visible():
                print(f"[->] {row_current}번째 행에서 연락처 확인 버튼 발견!")

                row_location_current = row_current - 1

                # 연락처 확인 버튼이 있는 리드 데이터의 담당자 위치 열을 선택해서, 퀵뷰를 오픈하는 로직
                # 산업군 > Oil, Gas, and Mining 선택 변경으로 인한 코드 수정 - 20250903
                if "Oil, Gas, and Mining" == mobile_page.get_by_text("Oil, Gas, and Mining").nth(
                        row_location_current).inner_text():
                    mobile_page.get_by_text("Oil, Gas, and Mining").nth(row_location_current).tap()
                    mobile_page.wait_for_timeout(3000)
                    print(f"Kuwait next : {row_location_current + 1}")

                print("[O] 해당 리드 행 클릭하여 상세정보 열기")

                # 오른쪽 팝업 대기
                try:
                    # page.wait_for_selector("div.drawer-content", timeout=5000)
                    mobile_page.wait_for_timeout(3000)
                    # popup_button = page.locator("div.drawer-content button:has-text('연락처 확인')")

                    popup_button = mobile_page.locator("section button:has-text('연락처 확인')")

                    popup_btn_count = popup_button.count()
                    print(f"퀵뷰 > 연락처 확인 버튼 개수 카운트 : {popup_btn_count}")

                    # 20250930 - 탐색하기 UI 변경으로 이메일 연락처 > 연락처 확인 버튼 위치 코드 수정
                    popup_email_view_contacts = popup_button.nth(1)

                    # 퀵뷰 > 이메일 연락처 > [연락처 확인] 버튼 활성화 확인
                    if popup_email_view_contacts.is_visible():
                        popup_email_view_contacts.tap()
                        mobile_page.wait_for_timeout(2000)

                        assert "확인됨" == mobile_page.locator("section button:has-text('확인됨')").nth(0).inner_text(), \
                            "MO Web - 퀵뷰(연락처) > 이메일 연락처 [확인됨] 변경 처리 실패 - 퀵뷰 연락처 확인 실패 1"
                        assert "1 크레딧이 사용되었습니다." == mobile_page.get_by_role("alert").filter(
                            has_text="크레딧이 사용되었습니다.").inner_text(), \
                            "MO Web - 퀵뷰(연락처) > 크레딧 소모 토스트 메시지 출력 실패 - 퀵뷰 연락처 확인 실패 2"
                        mobile_page.wait_for_timeout(2000)
                        # assert False == page.locator("section button:has-text('확인됨')").nth(0).is_visible(), \
                        #    "퀵뷰(연락처) > 확인됨 비활성화 처리 안됨 - 퀵뷰 연락처 확인 실패 3"
                        print("MO Web - [V] 팝업 내 연락처 확인 버튼 클릭 완료")
                    else:
                        print("[!] 팝업 내 버튼이 없습니다.")
                        raise Exception("퀵뷰 > 이메일 연락처 > [연락처 확인] 버튼 없음 -> 퀵뷰 연락처 확인 실패 4")
                except TimeoutError:
                    print("[X] 팝업이 열리지 않았습니다 (Timeout)")
                    raise Exception("퀵뷰가 열리지 않았음 -> 퀵뷰 연락처 확인 실패 5")
                found = True
                break  # 찾았으면 더 이상 탐색 안 함

        if found:
            break  # 전체 페이지 반복 종료

        # 다음 페이지 이동 처리 (4페이지까지만)
        try:
            print(f"다음 페이지 이동 케이스 시작 - {page_number} 페이지 확인")

            # 쿠풰이트 오일 관련 검색어 변경 후 9페이지로 변경되어 수정 - 20250903
            next_button = mobile_page.locator("div").filter(
                has_text=re.compile(fr"^9 페이지 중 {page_number} 페이지페이지 바로가기$")).get_by_role("button").nth(
                1)

            print(f"next_button count : {next_button.count()}")

            if next_button.is_visible():
                mobile_page.wait_for_timeout(2000)
                next_button.tap()
                print("[->] 다음 페이지로 이동")
                mobile_page.wait_for_timeout(3000)
            else:
                print("[X] 다음 버튼이 비활성화됨")
                break
        except:
            print("[X] 다음 버튼을 찾을 수 없습니다.")
            # continue
            break

    # 결과 처리
    if not found:
        raise Exception("[X] 테스트 실패: 4페이지 모두 확인했지만 '연락처 확인' 버튼을 찾지 못했습니다.")