import pytest


def Chrome_MO_Web_Run():
    test_files = [
        # MO Web 1번 - 회원가입 페이지 이동 여부 확인
        #"tests_mo/MO_signupforfree_move.py",
        # MO Web 2번 - 회원가입 > 이메일 인증 및 입력값 확인
        #"tests_mo/MO_signupforfree_email_verification_and_input_validation_check.py",

        # MO Web 3번 - 회원가입 완료 (1달에 1번만 돌려야 하는 항목 -> 20260116 실행 -> 20260215 재실행 필요)
        ###"tests_mo/MO_signupforfree_complete.py",

        # MO Web 4번 - 회원가입 변경 > 이메일 등록 확인
        #"tests_mo/MO_signupforfree_change_email_register_check.py",
        # MO Web 5번 - 로그인 완료
        #"tests_mo/MO_login.py",
        # MO Web 6번 - 제품 이용하기 버튼 선택 시, 탐색 페이지 이동 확인
        #"tests_mo/MO_gotoproduct_click_after_prospecting_page_move.py",
        # MO Web 7번 - 요금제 및 결제 안내 페이지로 이동
        #"tests_mo/MO_price_click_after_price_page_move.py",
        # MO Web 8번 - 요금제 결제 전 동작 확인
        #"tests_mo/MO_price_upgrade_to_the_pro_plan_payment_check.py",
        # MO Web 9번 - 사용 내역에 기간별 평균 크레딧 사용 활동 노출 -> 현재 사용중인 요금제, 크레딧 정상 노출 확인
        #"tests_mo/MO_dashboard_usage_activity_period_selector_and_plan_credit_check.py",
        # MO Web 10번 - 사용 현황 분석에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 확인
        #"tests_mo/MO_usageanalysis_section_check.py",
        # MO Web 11번 - 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 확인
        #"tests_mo/MO_dashboard_discover_link_move.py",
        # MO Web 12번 - My lists 영역에 저장한 연락처, 미확인 연락처, 팀 공유 연락처 개수 확인
        #"tests_mo/MO_dashboard_mylist_contacts_count_check.py",
        # MO Web 13번 - 내 계정으로 이동하기 버튼 선택 시, 계정 및 설정 > 내 프로필로 이동
        "tests_mo/MO_dashboard_gotomyaccount_move.py",
        # MO Web 14번 - 검색 이력이 없는 신규 가입 사용자일때 계정 설정하기 노출 및 이동
        #"tests_mo/MO_prospecting_setup_your_account_move.py",
        # MO Web 15번 - AI 키워드 검색 후, Industry 필터에 산업군 추천 태그 노출, 필터 값, 결과 값 정상 작동 확인
        #"tests_mo/MO_prospecting_search_and_tag_data_print_check.py",
        # MO Web 21번 - 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Upgrade my plan 버튼 클릭 시 플랜 페이지로 이동
        #"tests_mo/MO_prospecting_insufficient_credit_modal_upgrade_my_plan_click.py",
        # MO Web 22번 - 리스트에 추가 정상 동작 확인
        #"tests_mo/MO_prospecting_addtolist_flow_check.py",
        # MO Web 24번 - Contact 리스트 중 담당자 이름 클릭 시 담당자 상세 페이지로 이동
        #"tests_mo/MO_prospecting_contacts_name_click_and_contact_detail_check.py",

        # MO Web 26번 - 퀵뷰(Quick view_contact) > view contact 정상 작동 여부 확인 (단, 모바일의 경우 1달에 1번만 확인하는 것으로 진행 -> 20260116 실행 -> 20260215 재실행 필요)
        ###"tests_mo/MO_prospecting_quickview_contact_view_contacts_check.py",

        # MO Web 31번 - Quick view_company 정상 노출
        #"tests_mo/MO_prospecting_quickview_company_check.py",
        # MO Web 35번 - Free plan 사용자가 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출
        #"tests_mo/MO_discover_freeplan_industry_or_keyword_search_limit_check.py",
        # MO Web 36번 - Free plan 사용자가 더보기(view more) 버튼 클릭 시 요금제 업그레이드 모달 노출
        #"tests_mo/MO_discover_freeplan_viewmore_click.py",
        # MO Web 37번 - 산업군 필터와 타이틀 검색 정상 작동
        #"tests_mo/MO_discover_industry_and_title_search.py",
        # MO Web 38번 - Prospecting resoure > Prospecting now 버튼 클릭 시 탐색 메뉴로 이동 해당항목 표시(항목 타이틀 포함)
        #"tests_mo/MO_discover_card_prospecting_now_check.py",
        # MO Web 39번 - Free 플랜 사용자 Export to Csv 클릭 시 모달 노출
        #"tests_mo/MO_mylist_freeplan_exporttocsv_limit_check.py",
        # MO Web 40번 - 제목 편집(Edit title) 클릭 시 제목 변경 플로우 진행
        #"tests_mo/MO_mylist_edittitle_change_check.py",
        # MO Web 41번 - 리스트 삭제(Delete list) 클릭 시 리스트 삭제 플로우 진행
        #"tests_mo/MO_mylist_delete_list_check.py",
        # MO Web 42번 - 리스트 만들기(Create List) 클릭 시 리스트 생성 플로우 진행
        #"tests_mo/MO_mylist_create_list_check.py",
        # MO Web 45번 - 마이리스트에서 연락처 삭제 시 연락처 삭제(Delete contacts) 모달, 삭제 완료 토스트 노출
        #"tests_mo/MO_mylist_detail_contact_delete_check.py",
        # MO Web 46번 - 확인하고자하는 리스트 항목 선택 후 view contacts 버튼 클릭 시 연락처 확인 Flow 진행 
        #"tests_mo/MO_mylist_detail_contact_view_contacts_check.py",
        # MO Web 50번 - 회사 정보(company) 탭 최초 클릭시 회사 정보를 입력하지 않은 경우 설정하기(set up) 노출, Company set up_Main 화면 노출
        #"tests_mo/MO_company_setup_and_main_page_check.py",
        # MO Web 51번 - 회사 정보 메인 (company_main) 화면에서 회사 검색 후 선택 시, Register modal 노출 및 등록 시, 회사 정보(Company) 탭 클릭 시 해당 회사 노출
        #"tests_mo/MO_company_register_flow_check.py",
        # MO Web 54번 - 회원 탈퇴 플로우 확인
        #"tests_mo/MO_account_and_settings_my_profile_membership_withdrawal_flow_check.py",
        # MO Web 55번 - 소속된 회사가 있을 때 Leave company 클릭 시 소속 회사 떠나기 모달 노출_팀오너일 경우
        #"tests_mo/MO_account_and_settings_team_owner_my_profile_leave_company_flow_check.py",
        # MO Web 57번 - 소속된 회사가 없을 때 설정하기(set up) 버튼 노출, 설정하기(set up) 버튼 클릭 시 회사 정보 페이지(company_set up) 페이지로 이동
        #"tests_mo/MO_account_and_settings_company_info_no_company_affiliation_setup_check.py",
        # MO Web 58번 - 유료 회원(팀오너) : charging credit, payment information 노출
        #"tests_mo/MO_account_and_settings_freeplan_charging_credit_payment_info_not_display_check.py",
        # MO Web 60번 - Payment information에 Register a card 클릭 시, 카드 등록 플로우 진행
        #"tests_mo/MO_account_and_settings_team_owner_payment_info_register_card_flow_check.py",
        # MO Web 61번 - Payment information > show detail 클릭 시 Payment information 페이지로 이동
        #"tests_mo/MO_account_and_settings_team_owner_payment_and_plan_payment_info_show_detail_link_move.py",
        # MO Web 62번 - 에디터픽 메인 카드 노출 확인
        #"tests_mo/MO_editorspick_card_check.py",
        # MO Web 64번 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인
        #"tests_mo/MO_editorspick_detail_enterpriseplan_all_contact_open_check.py",
        # MO Web 66번 - 세일즈 에이전트 노출 확인 
        #"tests_mo/MO_salesagent_ui_check.py",
        # MO Web 67번 - 세일즈 에이전트 > Scale > 구독 결제 완료 전까지 동작 확인
        #"tests_mo/MO_salesagent_scale_toss_payments_1_2page_input_check.py",
        # MO Web 69번 - 세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인
        #"tests_mo/MO_salesagent_boucher_modal_ui_check.py",
        # MO Web 70번 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인
        #"tests_mo/MO_salesagent_boucher_modal_link_move_check.py"

    ]

    exit_code = pytest.main(
        test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml", "--alluredir=allure-results"])
    #exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml"])

    if exit_code == 0:
        print("모든 테스트 성공")
    else:
        print(f"X 테스트 실패: 종료 코드 {exit_code}")


if __name__ == "__main__":
    Chrome_MO_Web_Run()
