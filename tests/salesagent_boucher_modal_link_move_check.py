import re
import config
import cv2
import numpy as np
from playwright.sync_api import expect

def test_salesagent_boucher_modal_link_move_check(page):
    print("---- 89번 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 테스트 시작 ----")

    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    page.wait_for_timeout(1000)

    page.get_by_role("link", name="세일즈 에이전트 바우처").click()
    page.wait_for_timeout(1000)

    print("세일즈 에이전트 랜딩 페이지 진입 완료")

    page.get_by_role("button", name="플랜 확인하기").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="바우처 혜택 상세 보기").click()
    page.wait_for_timeout(1000)

    print("정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 출력 완료")

    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="바로가기").first.click()
    page2 = page2_info.value

    #20260312 - 대기시간 3초 -> 4초로 변경
    page2.wait_for_timeout(4000)

    print("산업통상자원부 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER1_URL == page2.url, \
        "산업통상자원부 바로가기 1 -> 수출 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 1"
    assert "수출바우처 사업" == page2.get_by_role("heading", name="수출바우처 사업").inner_text(), \
        "산업통상자원부 바로가기 1 -> 홈페이지 이동 후 수출 바우처 사업 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 2"

    page2.close()
    page.wait_for_timeout(1000)

    #with page.expect_popup() as page2_info:
    #    page.get_by_role("link", name="바로가기").nth(1).click()
    #page2 = page2_info.value

    #assert config.BOUCHER2_URL == page2.url, \
    #    "중소벤처기업부 바로가기 2 -> 수출 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 3"
    #assert "수출바우처 사업" == page2.get_by_role("heading", name="수출바우처 사업").inner_text(), \
    #    "중소벤처기업부 바로가기 2 -> 홈페이지 이동 후 수출 바우처 사업 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 4"

    #page2.close()
    #page.wait_for_timeout(1000)

    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="바로가기").nth(2).click()
    page2 = page2_info.value

    #20260312 - 대기 시간 3초 -> 4초로 변경
    page2.wait_for_timeout(4000)

    #20260312 -과학기술정보통신부 URL 연동 후 특정 앨리먼트 노출되는지 확인하는 코드 추가
    target_text = page2.get_by_text("AI바우처 지원")
    expect(target_text).to_be_visible(timeout=10000)

    print("과학기술정보통신부 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER3_URL == page2.url, \
        "과학기술정보통신부 바로가기 3 -> AI 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 5"
    assert "AI바우처 지원" == page2.get_by_text("AI바우처 지원").inner_text(), \
        "과학기술정보통신부 바로가기 3 -> 홈페이지 이동 후 AI 바우처 사업 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 6"

    page2.close()
    page.wait_for_timeout(1000)

    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="바로가기").nth(3).click()
    page2 = page2_info.value

    # 20260312 - 대기 시간 3초 -> 4초로 변경
    page2.wait_for_timeout(4000)

    print("문화체육관광부 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER4_URL == page2.url, \
        "문화체육관광부 바로가기 4 -> 전통문화 혁신 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 7"
    assert "사업소개" == page2.get_by_role("heading", name="사업소개").locator("span").inner_text(), \
        "문화체육관광부 바로가기 4 -> 홈페이지 이동 후 전통문화포털 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 8"

    page2.close()
    page.wait_for_timeout(1000)

    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="바로가기").nth(4).click()
    page2 = page2_info.value

    # 20260312 - 대기 시간 3초 -> 4초로 변경
    page2.wait_for_timeout(4000)

    print("한국데이터산업진흥원 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER5_URL == page2.url, \
        "한국데이터산업진흥원 바로가기 5 -> 데이터 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 9"
    assert "데이터바우처 소개" == page2.get_by_role("heading", name="데이터바우처 소개").inner_text(), \
        "한국데이터산업진흥원 바보가기 5 -> 홈페이지 이동 후 데이터바우처 소개 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 8"

    page2.close()
    page.wait_for_timeout(1000)

    print("---- 89번 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 테스트 시작 -> 성공 ----")

