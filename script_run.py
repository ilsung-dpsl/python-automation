import pytest


def script_run():
    test_files = [
        # MO Web 24번 - Contact 리스트 중 담당자 이름 클릭 시 담당자 상세 페이지로 이동
        "tests_mo/MO_prospecting_contacts_name_click_and_contact_detail_check.py",
        # MO Web 31번 - Quick view_company 정상 노출
        "tests_mo/MO_prospecting_quickview_company_check.py",

    ]

    exit_code = pytest.main(
        test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml", "--alluredir=allure-results"])
    #exit_code = pytest.main(test_files + ["-s", "-v", "--disable-warnings", "--junitxml=reports/report.xml"])

    if exit_code == 0:
        print("모든 테스트 성공")
    else:
        print(f"X 테스트 실패: 종료 코드 {exit_code}")


if __name__ == "__main__":
    script_run()
