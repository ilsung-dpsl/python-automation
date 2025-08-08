import cv2
import numpy as np

import config

def compare_images(img1_path, img2_path, threshold=0.60):
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



def test_prospecting_quickview_company_check(page):
    print("----- 퀵뷰(회사) 정보 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PRD6_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PRD6_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("멕시코 위주의 여행 상품을 파는 업체를 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    print("탐색하기 > 검색 완료")

    page.get_by_role("tab", name="회사(96)").click()
    page.wait_for_timeout(1000)
    page.locator(".truncate > .flex-1").first.click()
    page.wait_for_timeout(3000)
#    with page.expect_popup() as page1_info:
#        page.get_by_role("article").get_by_text("Corporate Travel Services").click()
#    page1 = page1_info.value

    assert "Corporate Travel Services" == page.get_by_role("article").get_by_text(
        "Corporate Travel Services").inner_text(), \
        "퀵뷰 (회사) > 회사 명칭 확인 실패 - 퀵뷰 노출 확인 실패 1"
    assert "1996" == page.get_by_text("1996").inner_text(), \
        "퀵뷰 (회사) > 설립 연도 확인 실패 - 퀵뷰 노출 확인 실패 2"
    # assert "Administrative and Support Services" == page.get_by_role("article").get_by_text("Administrative and Support").inner_text(), \
    #    "퀵뷰 (회사) > 산업군 확인 실패 - 퀵뷰 노출 확인 실패 2"
    assert "직원 정보 확인" == page.get_by_role("article").get_by_role("button", name="직원 정보 확인").inner_text(), \
        "퀵뷰 (회사) > [직원정보확인] 버튼 출력 실패 - 퀵뷰 노출 확인 실패 3"

    print("----- 퀵뷰(회사) 정보 노출 확인 테스트 시작 -> 성공 -----")

"""
   svg_element = page.get_by_role("article").locator("img")
   
    # 탐색하기 > 필터 > 연간 매출 > LOCK 자물쇠 아이콘 이미지 확인
    if svg_element:
        svg_element.scroll_into_view_if_needed()

        test_capture_path = ".venv/images/svg_quickview_company_logo1.png"
        svg_element.screenshot(path=test_capture_path)
        print(f"📸 SVG 캡처 저장: {test_capture_path}")

        # ✅ 기준 이미지와 비교
        reference_path = ".venv/images/svg_quickview_company_logo.png"
        is_same = compare_images(test_capture_path, reference_path)

        if is_same:
            print("✅ 탐색하기 > 퀵뷰(회사) > 회사 로고 SVG가 기준 이미지와 일치합니다.")
        else:
            print("❌ 탐색하기 > 퀵뷰(회사) > 회사 로고 SVG가 기준 이미지와 다릅니다.")
            raise Exception("탐색하기 > 퀵뷰(회사) > 회사 로고 SVG가 기준 이미지와 다름 > 테스트 실패")
    else:
        print("❌ SVG 요소를 찾지 못했습니다.")
"""

