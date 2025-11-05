import re
import config

def test_editorspick_detail_enterpriseplan_all_contact_open_check(page):
    print("---- 83번 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 테스트 시작 ----")

    page.goto("https://deepsales.com/ko/intro")
    page.wait_for_timeout(1000)

    page.get_by_role("banner").get_by_role("link", name="에디터 픽").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("로그인 후 에디터픽 메인 페이지 진입 완료")

    page.get_by_role("img", name="Cosmoprof 바이어 리스트").click()
    page.wait_for_timeout(1000)

    print("에디터픽 상세 페이지 진입 완료")

    assert "Ardit Iljazi" == page.get_by_text("Ardit Iljazi").inner_text(), \
        "에디터픽 상세 > 가장 상단 연락처 이름 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 1"
    assert "arditiljazi@meiyume.com" == page.get_by_text("arditiljazi@meiyume.com").inner_text(), \
        "에디터픽 상세 > 가장 상단 연락처 이메일 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 2"
    assert "Maelle Carriou" == page.get_by_text("Maelle Carriou").inner_text(), \
        "에디터픽 상세 > 가장 하단 연락처 이름 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 3"
    assert "mcarriou@labogilbert.fr" == page.get_by_text("mcarriou@labogilbert.fr").inner_text(), \
        "에디터픽 상세 > 가장 하단 연락처 이메일 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 4"

    print("---- 83번 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 테스트 시작 -> 성공 ----")