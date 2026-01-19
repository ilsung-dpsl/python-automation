import config
import re

def test_MO_prospecting_contacts_name_click_and_contact_detail_check(mobile_page):
    print("----- 24번 - MO 탐색하기 > 성함 선택 후 담당자 상세 화면 이동 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 페이지 진입 완료")

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    #20260119 - 1초 -> 2초로 대시 시간 변경
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 탐색하기 진입 완료")

    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").tap(timeout=10000)
    mobile_page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("한국 화장품 유통 회사 중 직급이 매니저인 Danny Jung을 찾아줘")
    mobile_page.wait_for_timeout(500)

    # 20250930 - 탐색하기 UI 변경으로 프롬프트 창 > 검색 버튼 코드 수정
    mobile_page.locator("label").get_by_role("img").nth(1).tap(timeout=10000)
    # 20260116 - 5초 -> 7초 대기로 변경
    mobile_page.wait_for_timeout(7000)

    print("MO Web - 탐색하기 검색 완료 후")

    mobile_page.get_by_text("Danny Jung", exact=True).tap(timeout=10000)
    mobile_page.wait_for_timeout(5000)

    print("MO Web - 연락처 상세 페이지 진입 완료")

    # 연락처 상세 UI 변경 QA 항목 배포로 인한 연락처 상세 페이지 확인 코드 수정 - 20250911
    assert "탐색하기" == mobile_page.get_by_label("Breadcrumb").get_by_role("link",
                                                                 name="탐색하기").inner_text(), \
        "MO Web - 연락처 상세 페이지 > 타이틀 문구 '탐색하기' 확인 실패 - 연락처 상세 페이지 이동 실패 1"
    assert "Danny Jung" == mobile_page.locator("span").filter(
        has_text="Danny Jung").inner_text(), \
        "MO Web - 연락처 상세 페이지 > 타이틀 문구 '/ Danny Jung' 확인 실패 - 연락처 상세 페이지 이동 실패 2"
    assert "Manager" == mobile_page.get_by_text("Manager",
                                         exact=True).inner_text(), \
        "MO Web - 연락처 상세 페이지 > 직급 - Manager 확인 실패 - 연락처 상세 페이지 이동 실패 3"
    assert "skin79 Co., Ltd." in mobile_page.locator("div").filter(has_text=re.compile(
        r"^skin79 Co\., Ltd\.$")).inner_text(), \
        "MO Web - 연락 상세 페이지 > 회사 영역 > 소속 회사 문구 확인 실패 - 연락처 상세 페이지 이동 실패 4"
    assert "****@skin79.com" in mobile_page.locator("[id=\"__next\"]").get_by_text(
        "****@skin79.com").inner_text(), \
        "MO Web - 연락 상세 페이지 > 연락처 상세 영역 > 미확인된 이메일 확인 실패 - 연락처 상세 페이지 이동 실패 5"

    print("----- 24번 - MO 탐색하기 > 성함 선택 후 담당자 상세 화면 이동 확인 테스트 시작 -> 성공 -----")