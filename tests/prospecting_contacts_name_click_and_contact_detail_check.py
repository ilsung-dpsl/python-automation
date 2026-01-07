import re
import config

def test_prospecting_contacts_name_click_and_contact_detail_check(page):
    print("----- 29번 - 탐색하기 > 성함 선택 후 담당자 상세 화면 이동 확인 테스트 시작 -----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    #20260108 - 검색어를 변경 (danny jung이 나올 수 있도록 검색어 조정)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("한국 화장품 유통 회사 중 직급이 매니저인 Danny Jung을 찾아줘")

    #20250930 - 탐색하기 UI 변경으로 프롬프트 창 > 검색 버튼 코드 수정
    page.locator("label").get_by_role("img").nth(1).click()
    page.wait_for_timeout(5000)

    #20260108 - danny jung 성함 선택 시에 앨리먼트 요소가 변경되어 코드 수정 및 타임아웃 10초 추가
    page.get_by_text("Danny Jung", exact=True).click(timeout=10000)
    page.wait_for_timeout(5000)

    #연락처 상세 UI 변경 QA 항목 배포로 인한 연락처 상세 페이지 확인 코드 수정 - 20250911
    assert "탐색하기" == page.get_by_label("Breadcrumb").get_by_role("link", name="탐색하기").inner_text(), "연락처 상세 페이지 > 타이틀 문구 '탐색하기' 확인 실패 - 연락처 상세 페이지 이동 실패 1"
    assert "Danny Jung" == page.locator("span").filter(has_text="Danny Jung").inner_text(), "연락처 상세 페이지 > 타이틀 문구 '/ Danny Jung' 확인 실패 - 연락처 상세 페이지 이동 실패 2"
    assert "Manager" == page.get_by_text("Manager", exact=True).inner_text(), "연락처 상세 페이지 > 직급 - Manager 확인 실패 - 연락처 상세 페이지 이동 실패 3"
    assert "skin79 Co., Ltd." in page.locator("div").filter(has_text=re.compile(r"^skin79 Co\., Ltd\.$")).inner_text(), "연락 상세 페이지 > 회사 영역 > 소속 회사 문구 확인 실패 - 연락처 상세 페이지 이동 실패 4"
    assert "****@skin79.com" in     page.locator("[id=\"__next\"]").get_by_text("****@skin79.com").inner_text(), "연락 상세 페이지 > 연락처 상세 영역 > 미확인된 이메일 확인 실패 - 연락처 상세 페이지 이동 실패 5"

    print("----- 29번 - 탐색하기 > 성함 선택 후 담당자 상세 화면 이동 확인 테스트 시작 -> 성공 -----")
