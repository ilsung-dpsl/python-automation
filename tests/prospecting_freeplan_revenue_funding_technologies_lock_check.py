from logging import exception

import cv2
import numpy as np

import config


def compare_images(img1_path, img2_path, threshold=0.56):
    print("----- 이미지 비교 체크 함수 시작 -----")
    """
    두 이미지 파일을 비교하여 유사도 반환
    """
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        print("[X] 이미지 파일 로드 실패")
        return False

    # 크기가 다르면 비교 전 resize
    if img1.shape != img2.shape:
        print("[!] 이미지 크기 불일치. img2를 img1 크기로 resize합니다.")
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # 이미지 차이 계산
    diff = cv2.absdiff(img1, img2)
    non_zero = np.count_nonzero(diff)
    total_pixels = diff.size
    similarity = 1 - (non_zero / total_pixels)

    print(f"[돋보기] 이미지 유사도: {similarity * 100:.2f}%")
    return similarity >= threshold


def test_prospecting_freeplan_revenue_funding_technologies_lock_check(page):
    print("----- 18번 - (Free 플랜) 탐색하기 > 필터 > 연간 매출 / 펀딩 / 기술 > 사용불가 이미지 체크 테스트 시작 -----")
    
    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
   # page.get_by_role("button", name="Start Now").click()
   # page.wait_for_timeout(1000)
#   page.locator("div:nth-child(9) > .flex.justify-between > div:nth-child(2) > svg").first.click()
#   page.locator("div:nth-child(21) > .flex.justify-between > div:nth-child(2) > svg").first.click()
#   page.locator("div:nth-child(23) > .flex.justify-between > div:nth-child(2) > svg").first.click()

    #20241015 - 필터 > 연간 매출 > 자물쇠 아이콘 코드 위치 수정
    svg_element = page.query_selector("div:nth-child(9) > div > div:nth-child(2) > svg")
    svg_element_2 = page.query_selector("div:nth-child(21) > div > div:nth-child(2) > svg")
    svg_element_3 = page.query_selector("div:nth-child(23) > div > div:nth-child(2) > svg")

    # 탐색하기 > 필터 > 연간 매출 > LOCK 자물쇠 아이콘 이미지 확인
    if svg_element:
        svg_element.scroll_into_view_if_needed()

        test_capture_path = ".venv/images/svg_prospecitng_revenue_lock1.png"
        svg_element.screenshot(path=test_capture_path)
        print(f"[저장] SVG 캡처 저장: {test_capture_path}")

        # [V] 기준 이미지와 비교
        reference_path = ".venv/images/svg_prospecting_revenue_lock.png"
        is_same = compare_images(test_capture_path, reference_path)

        if is_same:
            print("[V] 탐색하기 > 연간 매출 > LOCK 아이콘 SVG가 기준 이미지와 일치합니다.")
        else:
            print("[X] 탐색하기 > 연간 매출 > LOCK 아이콘 SVG가 기준 이미지와 다릅니다.")
            raise Exception("연간 매출 > LOCK 아이콘 SVG가 기준 이미지와 다름 > 테스트 실패")
    else:
        print("[X] SVG 요소를 찾지 못했습니다.")

    # 탐색하기 > 필터 > 펀딩 > LOCK 자물쇠 아이콘 이미지 확인
    if svg_element_2:
        svg_element_2.scroll_into_view_if_needed()

        test_capture_path = ".venv/images/svg_prospecting_funding_lock1.png"
        svg_element_2.screenshot(path=test_capture_path)
        print(f"[저장] SVG 캡처 저장: {test_capture_path}")

        # [V] 이미지와 비교
        reference_path = ".venv/images/svg_prospecting_funding_lock.png"
        is_same = compare_images(test_capture_path, reference_path)

        if is_same:
            print("[V] 탐색하기 > 펀딩 > LOCK 아이콘 SVG가 기준 이미지와 일치합니다.")
        else:
            print("[X] 탐색하기 > 펀딩 > LOCK 아이콘 SVG가 기준 이미지와 다릅니다.")
            raise Exception("펀딩 > LOCK 아이콘 SVG가 기준 이미지와 다름 > 테스트 실패")
    else:
        print("[X] SVG 요소를 찾지 못했습니다.")

    # 탐색하기 > 필터 > 기술 > LOCK 자물쇠 아이콘 이미지 확인
    if svg_element_3:
        svg_element_3.scroll_into_view_if_needed()

        test_capture_path = ".venv/images/svg_prospecting_technologies_lock1.png"
        svg_element_3.screenshot(path=test_capture_path)
        print(f"[저장] SVG 캡처 저장: {test_capture_path}")

        # [V] 기준 이미지와 비교
        reference_path = ".venv/images/svg_prospecting_technologies_lock.png"
        is_same = compare_images(test_capture_path, reference_path)

        if is_same:
            print("[V] 탐색하기 > 기술 > LOCK 아이콘 SVG가 기준 이미지와 일치합니다.")
        else:
            print("[X] 탐색하기 > 기술 > LOCK 아이콘 SVG가 기준 이미지와 다릅니다.")
            raise Exception("기술 > LOCK 아이콘 SVG가 기준 이미지와 다름 > 테스트 실패")
    else:
        print("[X] SVG 요소를 찾지 못했습니다.")

    print("----- (Free 플랜) 탐색하기 > 필터 > 연간 매출 / 펀딩 / 기술 > 사용불가 이미지 체크 테스트 시작 -> 성공 -----")

"""
    svg_element = page.query_selector("div:nth-child(23) > div > div:nth-child(2) > svg")

    if svg_element:
        # [V] SVG가 보이게 스크롤
        svg_element.scroll_into_view_if_needed()

        # [V] 스크린샷 저장
        svg_element.screenshot(path="svg_prospecting_technologies_lock.png")
        print("[저장] SVG 스크린샷 저장 완료: svg_prospecting_technologies_lock.png")
    else:
         print("[X] SVG 요소를 찾을 수 없습니다.")
"""



