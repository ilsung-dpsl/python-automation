import pytest

def Chrome_Run_Main():
    test_files = [
    #       "tests/signupforfree_move.py",
    #       "tests/login.py",
    #       "tests/b_type_randing_prompt_print.py",
    #       "tests/b_type_randing_bottom_recommendation_keyword_check.py",
    #       "tests/gotoproduct_click_after_prospecting_page_move.py",
    #       "tests/price_click_after_price_page_move.py",
    #       "tests/unabletochangetheplan_modal_check.py"
    #       "tests/dashboard_usage_activity_period_selector_and_plan_credit_check.py",
    #       "tests/usageanalysis_section_check.py",
    #       "tests/dashboard_discover_link_move.py",
    #       "tests/dashboard_mylist_contacts_count_check.py",
    #       "tests/dashboard_gotomyaccount_move.py",
    #       "tests/prospecting_setup_your_account_move.py",
           "tests/prospecting_search_and_tag_data_print_check.py",
           "tests/prospecting_freeplan_revenue_funding_technologies_lock_check.py",
         "tests/prospecting_freeplan_revenue_funding_technologies_disable_check.py",
          "tests/prospecting_freeplan_lead_open_limit100_check.py",
     #      "tests/prospecting_enterpriseplan_lead_open_limit5000_check.py",
           "tests/prospecting_insufficient_credit_modal_upgrade_my_plan_click.py",
    #       "tests/dev_prospecting_insufficient_credit_modal_charge_credit_click.py",
    #       "tests/dev_charge_credit_complete.py",
            "tests/prospecting_addtolist_flow_check.py",
            "tests/prospecting_company_view_employees_check.py",
            "tests/prospecting_contacts_name_click_and_contact_detail_check.py",
            "tests/prospecting_quickview_contact_check.py"

     #   "tests/b_type_randing_recommand_keyword_search_integration.py"
         #   "tests/signupforfree_complete.py"
         #  "tests/prospecting_single_contact_view_contacts_check.py"

    ]

    exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings"])

    if exit_code == 0:
        print("모든 테스트 성공")
    else:
        print(f"X 테스트 실패: 종료 코드 {exit_code}")

if __name__ == "__main__":
    Chrome_Run_Main()

