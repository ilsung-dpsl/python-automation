import pytest

def Chrome_Run_Main():
    test_files = [
        # 1번 - 무료로 시작하기 -> 회원가입
        "tests/signupforfree_move.py",
        # 2번 - 회원가입 완료
        "tests/signupforfree_complete.py",
        # 3번 - 로그인 완료
        "tests/login.py",
        # 4번 - B안 랜딩 페이지 > 프롬프트 영역 확인
        "tests/b_type_randing_prompt_print.py",
        # 5번 - B안 랜딩 > 추천검색어 3 입력 확인
        "tests/b_type_randing_bottom_recommendation_keyword_check.py",
        # 6번 - B안 래딩 > 추천검색어 1번 -> 탐색하기 연동 확인
        "tests/b_type_randing_recommand_keyword_search_integration.py",
        # 7번 - 제품 이용하기 연동 확인
        "tests/gotoproduct_click_after_prospecting_page_move.py",
        # 8번 - "가격" 선택 시, 결제 페이지로 이동
        "tests/price_click_after_price_page_move.py",
        # 9번 - 요금제 결제 정상 진행 및 영수증 노출 확인 (결제 전까지로 수정 필요 / 보류)

        # 10번 - "플랜 변경" 선택 시, 팀오너 권한 확인
        "tests/unabletochangetheplan_modal_check.py",
        # 11번 - 사용 내역에 기간별 평균 크레딧 사용 활동 노출,. 현재 사용중인 요금제, 크레딧 정상 노출 확인
        "tests/dashboard_usage_activity_period_selector_and_plan_credit_check.py",
        # 12번 - 사용 현황 분석에 기간별 산업, 부서, 직위 평균 정보 상위 8개 노출 확인
        "tests/usageanalysis_section_check.py",
        # 13번 - 발행일 기준 최신 상위 6개 Discover 노출, 클릭 시 Discover 항목 선택 결과로 연결 확인
        "tests/dashboard_discover_link_move.py",
        # 14번 - My lists 영역에 저장한 연락처, 미확인 연락처, 팀 공유 연락처 개수 확인
        "tests/dashboard_mylist_contacts_count_check.py",
        # 15번 - 내 계정으로 이동하기 버튼 선택 시, 계정 및 설정 > 내 프로필로 이동
        "tests/dashboard_gotomyaccount_move.py",
        # 16번 -
        "tests/prospecting_setup_your_account_move.py",
        "tests/prospecting_search_and_tag_data_print_check.py",
        "tests/prospecting_freeplan_revenue_funding_technologies_lock_check.py",
        "tests/prospecting_freeplan_revenue_funding_technologies_disable_check.py",
        "tests/prospecting_freeplan_lead_open_limit100_check.py",
        "tests/prospecting_enterpriseplan_lead_open_limit5000_check.py",
        "tests/prospecting_insufficient_credit_modal_upgrade_my_plan_click.py",
        "tests/prospecting_addtolist_flow_check.py",
   #     "tests/dev_prospecting_insufficient_credit_modal_charge_credit_click.py",
   #     "tests/dev_charge_credit_complete.py",
        "tests/prospecting_contacts_name_click_and_contact_detail_check.py",
        "tests/prospecting_quickview_contact_check.py",
        "tests/prospecting_quickview_contact_view_contacts_check.py",
       "tests/prospecting_quickview_addtolist_flow.py",
        "tests/prospecting_quickview_companyname_link_move.py",
        "tests/prospecting_company_companyname_click_and_company_info_move.py",
        "tests/prospecting_quickview_contact_linkedin_move.py",
        "tests/prospecting_quickview_company_view_employees_check.py",
        "tests/prospecting_quickview_company_check.py",
        "tests/prospecting_single_contact_view_contacts_check.py",
        "tests/discover_persona_setup_check.py",
        "tests/discover_freeplan_industry_or_keyword_search_limit_check.py",
        "tests/discover_freeplan_viewmore_click.py",
       "tests/discover_industry_and_title_search.py",
       "tests/discover_card_prospecting_now_check.py",
        "tests/mylist_freeplan_exporttocsv_limit_check.py",
        "tests/mylist_edittitle_change_check.py",
        "tests/mylist_delete_list_check.py",
      "tests/mylist_create_list_check.py",
        "tests/mylist_detail_freeplan_exporttocsv_limit_check.py",
        "tests/mylist_detail_enterpriseplan_exporttocsv_check.py",
       "tests/mylist_team_share_detail_move_to_list_not_displayed_check.py",
        "tests/mylist_team_share_detail_delete_not_displayed_check.py",
       "tests/mylist_detail_contact_delete_check.py",
        "tests/mylist_detail_contact_view_contacts_check.py",
        "tests/mylist_detail_freeplan_upgrade_myplan_modal_upgrade_myplan_click.py",
        "tests/team_management_free_invite_member_limit_check.py",
        "tests/team_management_enterprise_seat_full_charge_and_invite_member_limit_check.py",
        "tests/team_management_free_team_owner_addseat_click.py",
        "tests/team_management_team_owner_invite_member_flow_check.py",
        "tests/team_management_team_owner_other_team_member_invite_limit_check.py",
        "tests/team_management_team_owner_delete_member.py",
        "tests/team_management_team_member_join_the_team_flow_check.py",
        "tests/team_management_team_member_leave_the_team_flow_check.py",
        "tests/company_setup_and_main_page_check.py",
        "tests/company_register_flow_check.py",
        "tests/company_register_for_a_new_company_flow_check.py",
        "tests/account_and_settings_my_profile_input_add_edit_flow_check.py",
        "tests/account_and_settings_my_profile_membership_withdrawal_flow_check.py",
        "tests/account_and_settings_team_owner_my_profile_leave_company_flow_check.py",
        "tests/account_and_settings_freeplan_my_profile_leave_company_flow_check.py",
        "tests/account_and_settings_company_info_no_company_affiliation_setup_check.py",
        "tests/account_and_settings_freeplan_payment_and_plan_charging_credit_payment_info_not_display_check.py",
        "tests/account_and_settings_team_member_payment_and_plan_charging_credit_payment_info_not_display_check.py",
        "tests/account_and_settings_team_owner_payment_and_plan_charging_credit_payment_info_display_check.py",
        "tests/account_and_settings_team_member_go_to_team_management_link_move.py",
        "tests/account_and_settings_team_owner_payment_info_register_card_flow_check.py",
        "tests/account_and_settings_team_owner_payment_and_plan_payment_info_show_detail_link_move.py"
    ]


    exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml", "--alluredir=allure-results"])
    #exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml"])

    if exit_code == 0:
        print("모든 테스트 성공")
    else:
        print(f"X 테스트 실패: 종료 코드 {exit_code}")

if __name__ == "__main__":
    Chrome_Run_Main()

