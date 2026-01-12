import re
import config

def test_MO_editorspick_detail_enterpriseplan_all_contact_open_check(mobile_page):
    print("---- 83번 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 테스트 시작 ----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="에디터 픽").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("로그인 후 에디터픽 메인 페이지 진입 완료")

    mobile_page.get_by_role("img", name="Cosmoprof 바이어 리스트").tap()
    mobile_page.wait_for_timeout(1000)

    print("에디터픽 상세 페이지 진입 완료")

    assert "Ardit Iljazi" == mobile_page.get_by_text("Ardit Iljazi").inner_text(), \
        "에디터픽 상세 > 가장 상단 연락처 이름 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 1"
    assert "arditiljazi@meiyume.com" == mobile_page.get_by_text("arditiljazi@meiyume.com").inner_text(), \
        "에디터픽 상세 > 가장 상단 연락처 이메일 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 2"
    assert "Maelle Carriou" == mobile_page.get_by_text("Maelle Carriou").inner_text(), \
        "에디터픽 상세 > 가장 하단 연락처 이름 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 3"
    assert "mcarriou@labogilbert.fr" == mobile_page.get_by_text("mcarriou@labogilbert.fr").inner_text(), \
        "에디터픽 상세 > 가장 하단 연락처 이메일 확인 실패 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 실패 4"

    print("---- 83번 - 유료 회원일 경우, 에디터픽 상세 > 모든 연락처 정보 노출 확인 테스트 시작 -> 성공 ----")