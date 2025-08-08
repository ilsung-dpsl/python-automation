import cv2
import numpy as np

import config

def compare_images(img1_path, img2_path, threshold=0.67):
    print("----- 이미지 비교 체크 함수 시작 -----")
    """
    두 이미지 파일을 비교하여 유사도 반환
    """
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        print("❌ 이미지 파일 로드 실패")
        return False

    # 크기가 다르면 비교 전 resize
    if img1.shape != img2.shape:
        print("⚠ 이미지 크기 불일치. img2를 img1 크기로 resize합니다.")
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # 이미지 차이 계산
    diff = cv2.absdiff(img1, img2)
    non_zero = np.count_nonzero(diff)
    total_pixels = diff.size
    similarity = 1 - (non_zero / total_pixels)

    print(f"🔍 이미지 유사도: {similarity * 100:.2f}%")
    return similarity >= threshold

def test_prospecting_quickview_companyname_link_move(page):
    print("------ 탐색하기 > 퀵뷰 > 회사정보 > 회사명칭 선택 후 해당 회사페이지 이동 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("일본 화장품 제조사 세일즈 매니저")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    print("탐색하기 > 검색 완료")

    page.locator("[id=\"__next\"]").get_by_text("Japan, Okayama").click()

    with page.expect_popup() as page1_info:
        page.get_by_role("article").get_by_text("Hayashibara", exact=True).click()
    page1 = page1_info.value

    page1.wait_for_timeout(3000)

    svg_element = page1.locator("img").nth(1)

    # 탐색하기 > 필터 > 연간 매출 > LOCK 자물쇠 아이콘 이미지 확인
    if svg_element:
        svg_element.scroll_into_view_if_needed()

        test_capture_path = ".venv/images/svg_company_info_logo1.png"
        svg_element.screenshot(path=test_capture_path)
        print(f"📸 SVG 캡처 저장: {test_capture_path}")

        # ✅ 기준 이미지와 비교
        reference_path = ".venv/images/svg_company_info_logo.png"
        is_same = compare_images(test_capture_path, reference_path)

        if is_same:
            print("✅ 회사정보 페이지 > 회사 로고 SVG가 기준 이미지와 일치합니다. > ")
        else:
            print("❌ 회사정보 페이지 > 회사 로고 SVG가 기준 이미지와 다릅니다.")
            raise Exception("회사정보 페이지 > 회사 로고 SVG SVG가 기준 이미지와 다름 - 해당 회사정보 페이지 이동 실패 1")
    else:
        print("❌ SVG 요소를 찾지 못했습니다.")

    assert "Hayashibara" == page1.get_by_text("Hayashibara").nth(1).inner_text(), \
        "회사정보 페이지 > 회사명칭 확인 실패 - 해당 회사정보 페이지 이동 실패 2"
    assert "Wholesale, Wholesale Cosmetics" == page1.get_by_text("Wholesale, Wholesale Cosmetics").inner_text(), \
        "회사정보 페이지 > 산업군 정보 확인 실패 - 해당 회사정보 페이지 이동 실패 3"
    assert "Masahiro Jimba" == page1.get_by_text("Masahiro Jimba").inner_text(), \
        "회사정보 페이지 > 잠재 고객 목록 > 직원 정보 1 > 성함 확인 실패 - 해당 회사정보 페이지 이동 실패 4"

    print("------ 탐색하기 > 퀵뷰 > 회사정보 > 회사명칭 선택 후 해당 회사페이지 이동 테스트 시작 -----")
