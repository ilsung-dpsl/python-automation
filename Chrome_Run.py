import pytest

def Chrome_Run_Main():
    # 딥세일즈 자동화 스크립트 메인 실행 코드
    test_files = [
        #        "tests/signupforfree_move.py",
        #        "tests/login.py",
        #        "tests/b_type_randing_prompt_print.py",
        #        "tests/b_type_randing_bottom_recommendation_keyword_check.py",
        #        "tests/gotoproduct_click_after_prospecting_page_move.py",
        #        "tests/price_click_after_price_page_move.py",
        #        "tests/unabletochangetheplan_modal_check.py",
        #        "tests/dashboard_usage_activity_period_selector_and_plan_credit_check.py",
        #        "tests/usageanalysis_section_check.py",
        #        "tests/dashboard_discover_link_move.py",
        #        "tests/dashboard_mylist_contacts_count_check.py",
        #       "tests/dashboard_gotomyaccount_move.py",
        #        "tests/prospecting_setup_your_account_move.py",
        #        "tests/prospecting_search_and_tag_data_print_check.py",
        #        "tests/prospecting_freeplan_revenue_funding_technologies_lock_check.py",
        #        "tests/prospecting_freeplan_revenue_funding_technologies_disable_check.py",
        #       "tests/prospecting_freeplan_lead_open_limit100_check.py",
        #        "tests/prospecting_enterpriseplan_lead_open_limit5000_check.py",
        #        "tests/prospecting_insufficient_credit_modal_upgrade_my_plan_click.py",
        #        "tests/prospecting_addtolist_flow_check.py",
        #    "tests/dev_prospecting_insufficient_credit_modal_charge_credit_click.py",
        #    "tests/dev_charge_credit_complete.py",
        #        "tests/prospecting_contacts_name_click_and_contact_detail_check.py",
        #        "tests/prospecting_quickview_contact_check.py",
        #        "tests/prospecting_quickview_contact_view_contacts_check.py",
        #        "tests/prospecting_quickview_addtolist_flow.py",
        #        "tests/prospecting_quickview_companyname_link_move.py",
        #        "tests/prospecting_company_companyname_click_and_company_info_move.py",
        #        "tests/prospecting_quickview_contact_linkedin_move.py",
        #        "tests/b_type_randing_recommand_keyword_search_integration.py",
        #        "tests/prospecting_quickview_company_view_employees_check.py",
        #        "tests/prospecting_quickview_company_check.py",
        #        "tests/signupforfree_complete.py",
        #        "tests/prospecting_single_contact_view_contacts_check.py",
        #        "tests/discover_persona_setup_check.py",

        #
        #        "tests/discover_freeplan_industry_or_keyword_search_limit_check.py",
        #        "tests/discover_freeplan_viewmore_click.py",
        #        "tests/discover_industry_and_title_search.py",
        #        "tests/discover_card_prospecting_now_check.py",
        #        "tests/mylist_freeplan_exporttocsv_limit_check.py",
        #        "tests/mylist_edittitle_change_check.py",
        #        "tests/mylist_delete_list_check.py",
        #       "tests/mylist_create_list_check.py",
        #        "tests/mylist_detail_freeplan_exporttocsv_limit_check.py",
        #        "tests/mylist_detail_enterpriseplan_exporttocsv_check.py",
        #        "tests/mylist_team_share_detail_move_to_list_not_displayed_check.py",
        #        "tests/mylist_team_share_detail_delete_not_displayed_check.py",
        #        "tests/mylist_detail_contact_delete_check.py",
        #        "tests/mylist_detail_contact_view_contacts_check.py",
        #        "tests/mylist_detail_freeplan_upgrade_myplan_modal_upgrade_myplan_click.py",
        #        "tests/team_management_free_invite_member_limit_check.py",
        #       "tests/team_management_enterprise_seat_full_charge_and_invite_member_limit_check.py",
        #        "tests/team_management_free_team_owner_addseat_click.py",
        #        "tests/team_management_team_owner_invite_member_flow_check.py",
        #        "tests/team_management_team_owner_other_team_member_invite_limit_check.py",
        #        "tests/team_management_team_owner_delete_member.py",
        #"tests/team_management_team_member_join_the_team_flow_check.py",
        #"tests/team_management_team_member_leave_the_team_flow_check.py",
        #"tests/company_setup_and_main_page_check.py",
#        "tests/company_register_flow_check.py",
#        "tests/company_register_for_a_new_company_flow_check.py",
#        "tests/account_and_settings_my_profile_input_add_edit_flow_check.py",
#        "tests/account_and_settings_my_profile_membership_withdrawal_flow_check.py",
#        "tests/account_and_settings_team_owner_my_profile_leave_company_flow_check.py",
#        "tests/account_and_settings_freeplan_my_profile_leave_company_flow_check.py",
#        "tests/account_and_settings_company_info_no_company_affiliation_setup_check.py",
        "tests/account_and_settings_freeplan_payment_and_plan_charging_credit_payment_info_not_display_check.py"
    ]

    exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings"])

    if exit_code == 0:
        print("모든 테스트 성공")
    else:
        print(f"X 테스트 실패: 종료 코드 {exit_code}")

if __name__ == "__main__":
    Chrome_Run_Main()

