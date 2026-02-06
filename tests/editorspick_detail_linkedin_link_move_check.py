import re
import config

def test_editorspick_detail_linkedin_link_move_check(page):
    print("---- 86번 - 에디터픽 상세 > 링크드인 연동 확인 테스트 시작 ----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.wait_for_timeout(1000)
    page.get_by_role("banner").get_by_role("link", name="에디터 픽").click()
    page.wait_for_timeout(1000)

    print("에디터픽 메인 페이지 진입 완료")
    page.get_by_role("img", name="글로벌 K-POP 굿즈 바이어 리스트").click()
    page.wait_for_timeout(1000)

    page.locator("div:nth-child(2) > div > .flex > .shrink-0").click()
    page.wait_for_timeout(1000)

    page.locator("#modal-root").get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    print("로그인 페이지 진입 완료")
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    # 20260122 - 타임아웃 대기 방어코드 추가
    with page.expect_popup() as page1_info:
        page.locator("div:nth-child(2) > div > .flex > .shrink-0").click(timeout=10000)
    page1 = page1_info.value

    # 20250122 - 3초 -> 5초 대기 추가
    page1.wait_for_timeout(5000)

    page1.get_by_role("link", name="LinkedIn").click(timeout=10000)
    page1.wait_for_timeout(1000)

    page1.get_by_role("link", name="로그인", exact=True).click()
    page1.wait_for_timeout(1000)

    with page1.expect_popup() as page2_info:
        page1.locator("iframe[title=\"Sign in with Google Button\"]").content_frame.get_by_role("button", name="Continue with Google. Opens").click()
    page2 = page2_info.value

    page2.wait_for_timeout(3000)

    page2.get_by_role("textbox", name="이메일 또는 휴대전화").fill(config.GMAIL_EMAIL)
    page2.get_by_role("button", name="다음").click()

    page2.get_by_role("textbox", name="비밀번호 입력").fill(config.GMAIL_EMAIL_PW)
    page2.get_by_role("button", name="다음").click()
    #page2.close()

    page1.goto("https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin")
    page1.wait_for_timeout(5000)

    page1.close()
    page2.close()

    with page.expect_popup() as page3_info:
        page.locator("div:nth-child(2) > div > .flex > .shrink-0").click()
    page3 = page3_info.value

    page3.wait_for_timeout(5000)

    with page.expect_popup() as page3_info:
        page.locator("div:nth-child(2) > div > .flex > .shrink-0").click()
    page4 = page3_info.value

    page4.wait_for_timeout(5000)


    # 20250206 - 링크드인 페이지 > 성함 / 소속 회사&직함 변경 및 링크드인 경력사항 파싱 막힘으로 인한 체크 제거
    #assert "Wanda Martinez" == page4.locator("div").filter(has_text=re.compile(r"^Wanda Martinez$")).first.inner_text(), \
    #    "링크드인 페이지 > 성함 노출 확인 - 에디터픽 > 링크드인 연동 확인 실패 1"
    assert "Ejecutiva de Ventas en Uno Radio Group" == page4.get_by_test_id("lazy-column").get_by_text("Ejecutiva de Ventas en Uno").inner_text(), \
           "링크드인 페이지 > 소속 회사 / 직함 노출 확인 - 에디터픽 > 링크드인 연동 확인 실패 2"
    #assert "Ejecutiva de Ventas" in page4.gget_by_test_id("lazy-column").get_by_role("button", name="Wanda Martinez", exact=True).inner_text(), \
    #    "링크드인 페이지 > 경력 사항 > 직함 노출 확인 - 에디터픽 > 링크드인 연동 확인 실패 3"
    print("---- 86번 - 에디터픽 상세 > 링크드인 연동 확인 테스트 시작 -> 성공 ----")



