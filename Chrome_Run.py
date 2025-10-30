import pytest

def Chrome_Run_Main():
    test_files = [
        # 1번 - 무료로 시작하기 -> 회원가입
        "tests/signupforfree_move.py",
        # 2번 - 회원가입 완료 -> 회원가입 페이지 제거로 블락 처리
        #"tests/signupforfree_complete.py",
        # 3번 - 로그인 완료
        #"tests/login.py",
        # 4번 - B안 랜딩 페이지 > 프롬프트 영역 확인
        #"tests/b_type_randing_prompt_print.py",
        # 5번 - B안 랜딩 > 추천검색어 3 입력 확인
        #"tests/b_type_randing_bottom_recommendation_keyword_check.py",
        # 6번 - B안 래딩 > 추천검색어 1번 -> 탐색하기 연동 확인
        #"tests/b_type_randing_recommand_keyword_search_integration.py",
        # 7번 - 제품 이용하기 연동 확인
        #"tests/gotoproduct_click_after_prospecting_page_move.py",
        # 8번 - "가격" 선택 시, 결제 페이지로 이동
        #"tests/price_click_after_price_page_move.py",
        # 9번 - 요금제 결제 정상 진행 및 영수증 노출 확인 (결제 전까지로 수정 필요 / 보류)

        # 10번 - "플랜 변경" 선택 시, 팀오너 권한 확인
        #"tests/unabletochangetheplan_modal_check.py",
        # 11번 - 사용 내역에 기간별 평균 크레딧 사용 활동 노출,. 현재 사용중인 요금제, 크레딧 정상 노출 확인
        #"tests/dashboard_usage_activity_period_selector_and_plan_credit_check.py",
        # 12번 - 사용 현황 분석에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 확인
        #"tests/usageanalysis_section_check.py",
        # 13번 - 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 확인
        #"tests/dashboard_discover_link_move.py",
        # 14번 - My lists 영역에 저장한 연락처, 미확인 연락처, 팀 공유 연락처 개수 확인 (단, 팀 공유 연락처 미노출로 해당 부분은 제외)
        #"tests/dashboard_mylist_contacts_count_check.py",
        # 15번 - 내 계정으로 이동하기 버튼 선택 시, 계정 및 설정 > 내 프로필로 이동
        #"tests/dashboard_gotomyaccount_move.py",
        # 16번 - 검색 이력이 없는 신규 가입 사용자일때 게정 설정하기 노출 및 이동
        #"tests/prospecting_setup_your_account_move.py",
        # 17번 - AI 키워드 검색 후, Industry 필터에 산업군 추천 태그 노출, 필터 값, 결과 값 정상 작동 확인
        #"tests/prospecting_search_and_tag_data_print_check.py",
        # 18번 - 무료 회원에게 Revenue, Funding, Technologies 필터 Lock 아이콘 노출 확인
        #"tests/prospecting_freeplan_revenue_funding_technologies_lock_check.py",
        # 19번 - 무료 회원 Revenue, Funding, Technologies (1개 초과 생성시) 필터 사용 불가 확인
        #"tests/prospecting_freeplan_revenue_funding_technologies_disable_check.py",
        # 20번 - 무료 회원이 검색 결과 리스트에서 100개 이상 연락처 탐색 시 업그레이드 모달 노출 확인
        #"tests/prospecting_freeplan_lead_open_limit100_check.py",
        # 21번 - Enterprise 회원이 검색 결과 리스트에서 5000개 이상 연락처 탐색 시 업그레이드 모달 노출 확인
        #"tests/prospecting_enterpriseplan_lead_open_limit5000_check.py",
        # 22번 - 단일 or 복수 연락처에 대한 [연락처 확인] 버튼의 동작 확인
        #"tests/prospecting_single_contact_view_contacts_check.py",
        # 23번 - 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Upgrade my plan 버튼 클릭 시 플랜 페이지로 이동
        #"tests/prospecting_insufficient_credit_modal_upgrade_my_plan_click.py",
        # 24번 - 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Charge credit 클릭 시 크레딧 충전 모달 노출 확인 (결제 취소 지연 문제로 인해 DEV 기준으로 작성)
        #"tests/dev_prospecting_insufficient_credit_modal_charge_credit_click.py",
        # 25번 - 크레딧 정상 충전 및 결제 확인 (결제 취소 지연 문제로 인해 DEV 기준으로 작성)
        #"tests/dev_charge_credit_complete.py",
        # 26번 - 리스트에 추가 정상 동작 확인
        #"tests/prospecting_addtolist_flow_check.py",
        # 28번 - 회사 검색 후 View Employees 버튼 클릭 시 선택한 회사가 Company 필터 설정된 상태로 Prospecting 검색 결과 노출
        #"tests/prospecting_company_view_employees_check.py",
        # 29번 - Contact 리스트 중 담당자 이름 클릭 시 담당자 상세 페이지로 이동 (필터 이슈로 Fail - HOLDING 처리)
        #"tests/prospecting_contacts_name_click_and_contact_detail_check.py",
        # 30번 -퀵뷰(Quick view_contact) 정상 노출 (필터 이슈로 Fail - HOLDING 처리)
        #"tests/prospecting_quickview_contact_check.py",
        # 31번 - 퀵뷰(Quick view_contact) > view contact 정상 작동 여부 확인
        #"tests/prospecting_quickview_contact_view_contacts_check.py",
        # 32번 - 퀵뷰(Quick view_contact) > add to list 정상 작동 여부 확인
        #"tests/prospecting_quickview_addtolist_flow.py",
        # 33번 - 퀵뷰(Quick view_contact) 회사 정보에서 회사명칭 클릭 시 해당 회사 페이지로 이동 (필터 이슈로 Fail - HOLDING 처리)
        #"tests/prospecting_quickview_companyname_link_move.py",
        # 34번 - 회사 리스트 중 회사 이름 클릭 시 회사 상세 페이지로 이동 (필터 이슈로 Fail - HOLDING 처리)
        #"tests/prospecting_company_companyname_click_and_company_info_move.py",
        # 35번 - Quick view_contact Linkedin 클릭 시 연결된 링크드인 URL로 이동 (필터 이슈로 Fail - HOLDING 처리)
        #"tests/prospecting_quickview_contact_linkedin_move.py",
        # 36번 - Quick view_company 정상 노출
        #"tests/prospecting_quickview_company_check.py",
        # 37번 - 퀵뷰(Quick view_company) 회사 정보에서 회사명칭 클릭 시 해당 회사 페이지로 이동 (필터 이슈로 Fail - HOLDING 처리)
        #"tests/prospecting_quickview_company_companyname_click.py",
        # 38번 - 퀵뷰(Quick view_company) > 직원 정보 확인(View employees) 클릭 시 선택한 회사가 Company 필터 설정된 상태로 Prospecting 검색 결과 노출
        # (필터 이슈로 Fail - HOLDING 처리)
        #"tests/prospecting_quickview_company_view_employees_check.py",
        # 39번 - Discover 최초 진입 시 퍼소나 설정안내 모달 표시
        #"tests/discover_persona_setup_check.py",
        # 40번 - Free plan 사용자가 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출
        #"tests/discover_freeplan_industry_or_keyword_search_limit_check.py",
        # 41번 - Free plan 사용자가 더보기(view more) 버튼 클릭 시 요금제 업그레이드 모달 노출
        #"tests/discover_freeplan_viewmore_click.py",
        # 42번 - 산업군 필터와 타이틀 검색 정상 작동
        #"tests/discover_industry_and_title_search.py",
        # 43번 - Prospecting resoure > Prospecting now 버튼 클릭 시 탐색 메뉴로 이동 해당항목 표시(항목 타이틀 포함)
        #"tests/discover_card_prospecting_now_check.py",
        # 44번 - Free 플랜 사용자 Export to Csv 클릭 시 모달 노출
        #"tests/mylist_freeplan_exporttocsv_limit_check.py",
        # 45번 - 제목 편집(Edit title) 클릭 시 제목 변경 플로우 진행
        #"tests/mylist_edittitle_change_check.py",
        # 46번 - 리스트 삭제(Delete list) 클릭 시 리스트 삭제 플로우 진행
        #"tests/mylist_delete_list_check.py",
        # 47번 - 리스트 만들기(Create List) 클릭 시 리스트 생성 플로우 진행
        #"tests/mylist_create_list_check.py",
        # 48번 - Free 플랜 사용자 Export to CSV 클릭 시 모달 노출
        #"tests/mylist_detail_freeplan_exporttocsv_limit_check.py",
        # 49번 - 유료 플랜 사용자 Export to CSV 클릭 시 모달 노출
        #"tests/mylist_detail_enterpriseplan_exporttocsv_check.py",
        # 50번 - 팀 공유 리스트 리스트에 이동(Move to list) 미노출
        #"tests/mylist_team_share_detail_move_to_list_not_displayed_check.py",
        # 51번 - 팀 공유 리스트 삭제(Delete) 버튼 미노출
        #"tests/mylist_team_share_detail_delete_not_displayed_check.py",
        # 52번 - 마이리스트에서 연락처 삭제 시 연락처 삭제(Delete contacts) 모달, 삭제 완료 토스트 노출
        #"tests/mylist_detail_contact_delete_check.py",
        # 53번 - 확인하고자하는 리스트 항목 선택 후 view contacts 버튼 클릭 시 연락처 확인 Flow 진행
        #"tests/mylist_detail_contact_view_contacts_check.py",
        # 54번 - Upgrade my plan 모달 버튼 클릭 시 flow  정상 작동 확인
        #"tests/mylist_detail_freeplan_upgrade_myplan_modal_upgrade_myplan_click.py",
        # 55번 - 팀관리(Team management)_Free, Pro일때 팀원 초대 불가
        #"tests/team_management_free_invite_member_limit_check.py",
        # 56번 - 팀관리(Enterprise)_Enterprise(4명) 회원 수가 이미 차있을 경우 팀원 초대 불가
        #"tests/team_management_enterprise_seat_full_charge_and_invite_member_limit_check.py",
        # 57번 - 좌석 추가(Add seat) 클릭 시, 요금 안내 및 결제 페이지로 이동
        #"tests/team_management_free_team_owner_addseat_click.py",
        # 58번 - Team(4명) 팀 초대 가능 회원수가 남아 있을 때 팀오너는 팀 초대 가능
        #"tests/team_management_team_owner_invite_member_flow_check.py",
        # 59번 - 유료플랜 사용자가 다른 팀에 초대된 사용자를 팀멤버로 초대 할 경우 Unable to invite 모달 노출
        #"tests/team_management_team_owner_other_team_member_invite_limit_check.py",
        # 60번 - 팀 멤버 삭제 정상 작동 확인
        #"tests/team_management_team_owner_delete_member.py",
        # 61번 - 팀 멤버 팀 초대 메일 수신 및 팀 합류 플로우 작동 확인
        "tests/team_management_team_member_join_the_team_flow_check.py",
        # 62번 - 팀 멤버 Leave the team 클릭 시, 무료 회원 전환 및 5크레딧 부여
        "tests/team_management_team_member_leave_the_team_flow_check.py",
        # 63번 - 회사 정보(company) 탭 최초 클릭시 회사 정보를 입력하지 않은 경우 설정하기(set up) 노출, Company set up_Main 화면 노출
        #"tests/company_setup_and_main_page_check.py",
        # 64번 - 회사 정보 메인 (company_main) 화면에서 회사 검색 후 선택 시, Register modal 노출 및 등록 시, 회사 정보(Company) 탭 클릭 시 해당 회사 노출
        #"tests/company_register_flow_check.py",
        # 65번 - 회사 정보 생성 (Register for a new company page) 새 회사 등록 작동 확인
        "tests/company_register_for_a_new_company_flow_check.py",
        # 67번 - My Profile 모든 항목 정상 기입, 추가, 수정 가능 여부 확인
        #"tests/account_and_settings_my_profile_input_add_edit_flow_check.py",
        # 68번 - 회원 탈퇴 플로우 확인 (단, 탈퇴 전 화면까지만 확인하는 것으로 변경)
        #"tests/account_and_settings_my_profile_membership_withdrawal_flow_check.py",
        # 70번 - 소속된 회사가 있을 때 Leave company 클릭 시 소속 회사 떠나기 모달 노출_팀오너일 경우
        #"tests/account_and_settings_team_owner_my_profile_leave_company_flow_check.py",
        # 71번 - 소속된 회사가 있을 때 Leave company 클릭 시 소속 회사 떠나기 모달 노출_ 팀오너가 아닌경우
        #"tests/account_and_settings_freeplan_my_profile_leave_company_flow_check.py",
        # 72번 - 소속된 회사가 없을 때 설정하기(set up) 버튼 노출, 설정하기(set up) 버튼 클릭 시 회사 정보 페이지(company_set up) 페이지로 이동
        #"tests/account_and_settings_company_info_no_company_affiliation_setup_check.py",
        # 73번 - 무료 회원 : charging credit, payment information 노출 X
        #"tests/account_and_settings_freeplan_payment_and_plan_charging_credit_payment_info_not_display_check.py",
        # 74번 - 유료 회원(팀멤버) : charging credit, payment information 노출 X
        #"tests/account_and_settings_team_member_payment_and_plan_charging_credit_payment_info_not_display_check.py",
        # 75번 - 유료 회원(팀오너) : charging credit, payment information 노출
        #"tests/account_and_settings_team_owner_payment_and_plan_charging_credit_payment_info_display_check.py",
        # 76번 - 팀 요금제에 가입되어 있는 팀 맴버의 경우 Go to team managent로 이동할 수 있는 링크 제공
        #"tests/account_and_settings_team_member_go_to_team_management_link_move.py",
        # 77번 - Payment information에 Register a card 클릭 시, 카드 등록 플로우 진행
        #"tests/account_and_settings_team_owner_payment_info_register_card_flow_check.py",
        # 78번 - Payment information > show detail 클릭 시 Payment information 페이지로 이동
        #"tests/account_and_settings_team_owner_payment_and_plan_payment_info_show_detail_link_move.py"
    ]

    exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml", "--alluredir=allure-results"])
    #exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml"])

    if exit_code == 0:
        print("모든 테스트 성공")
    else:
        print(f"X 테스트 실패: 종료 코드 {exit_code}")

if __name__ == "__main__":
    Chrome_Run_Main()

