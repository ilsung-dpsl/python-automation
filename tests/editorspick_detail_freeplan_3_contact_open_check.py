import re
import config

def test_editorspick_detail_freeplan_3_contact_open_check(page):
    print("---- 81번 - 무료 회원일 경우, 에디터픽 상세 > 연락처 3개 정보 노출 확인 테스트 시작 ----")
    page.goto("https://deepsales.com/ko/intro")
    page.wait_for_timeout(1000)
    page.get_by_role("banner").get_by_role("link", name="에디터 픽").click()
    page.wait_for_timeout(1000)

    print("에디터픽 메인 페이지 진입 완료")
    page.get_by_role("img", name="해외 화장품 수입·도매·소매 유통사 DB").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("로그인 페이지 진입 완료")
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("무료 회원 로그인 후 에디터픽 상세 페이지 진입 완료 ")

    assert "Aneta Kuc" == page.get_by_text("Aneta Kuc").inner_text(), \
        "에디터픽 상세 > 연락처 > 1번 연락처 이름 확인 실패 - 무료회원 일 경우, 에디터픽 상세 > 연락처 오픈 확인 실패 1"
    assert "aneta.kuc@makeup.pl" == page.get_by_text("aneta.kuc@makeup.pl").inner_text(), \
        "에디터픽 상세 > 연락처 > 1번 연락처 이메일 확인 실패 - 무료회원 일 경우, 에디터픽 상세 > 연락처 오픈 확인 실패 2"
    assert "Martin Charon" == page.get_by_text("Martin Charon").inner_text(), \
        "에디터픽 상세 > 연락처 > 2번 연락처 이름 확인 실패 - 무료회원 일 경우, 에디터픽 상세 > 연락처 오픈 확인 실패 3"
    assert "mcharon@sobio.fr" == page.get_by_text("mcharon@sobio.fr").inner_text(), \
        "에디터픽 상세 > 연락처 > 2번 연락처 이메일 확인 실패 - 무료회원 일 경우, 에디터픽 상세 > 연락처 오픈 확인 실패 4"
    assert "Oskar Cielecki" == page.get_by_text("Oskar Cielecki").inner_text(), \
        "에디터픽 상세 > 연락처 > 3번 연락처 이름 확인 실패 - 무료회원 일 경우, 에디터픽 상세 > 연락처 오픈 확인 실패 5"
    assert "oskar@beautyexchanger.pl" == page.get_by_text("oskar@beautyexchanger.pl").inner_text(), \
        "에디터픽 상세 > 연락처 > 3번 연락처 이메일 확인 실패 - 무료회원 일 경우, 에디터픽 상세 > 연락처 오픈 확인 실패 6"
    assert "********@sobio.fr" == page.get_by_text("********@sobio.fr").inner_text(), \
        "에디터픽 상세 > 연락처 > 4번 연락처 이메일 미오픈 확인 실패 - 무료회원 일 경우, 에디터픽 상세 > 연락처 오픈 확인 실패 7"

    print("---- 80번 - 무료 회원일 경우, 에디터픽 상세 > 연락처 3개 정보 노출 확인 테스트 시작 -> 성공 ----")
