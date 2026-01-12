import re
import config
import cv2
import numpy as np

def test_MO_salesagent_boucher_modal_link_move_check(mobile_page):
    print("---- 89번 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 테스트 시작 ----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="세일즈 에이전트 바우처").tap()
    mobile_page.wait_for_timeout(1000)

    print("세일즈 에이전트 랜딩 페이지 진입 완료")

    mobile_page.get_by_role("button", name="플랜 확인하기").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="바우처 혜택 상세 보기").tap()
    mobile_page.wait_for_timeout(1000)

    print("정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 출력 완료")

    with mobile_page.expect_popup() as page2_info:
        mobile_page.get_by_role("link", name="바로가기").first.tap( )
    mobile_page2 = page2_info.value

    mobile_page2.wait_for_timeout(3000)

    print("산업통상자원부 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER1_URL == mobile_page2.url, \
        "산업통상자원부 바로가기 1 -> 수출 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 1"
    assert "수출바우처 사업" == mobile_page2.get_by_role("heading", name="수출바우처 사업").inner_text(), \
        "산업통상자원부 바로가기 1 -> 홈페이지 이동 후 수출 바우처 사업 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 2"

    mobile_page2.close()
    mobile_page.wait_for_timeout(1000)

    #with page.expect_popup() as page2_info:
    #    page.get_by_role("link", name="바로가기").nth(1).click()
    #page2 = page2_info.value

    #assert config.BOUCHER2_URL == page2.url, \
    #    "중소벤처기업부 바로가기 2 -> 수출 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 3"
    #assert "수출바우처 사업" == page2.get_by_role("heading", name="수출바우처 사업").inner_text(), \
    #    "중소벤처기업부 바로가기 2 -> 홈페이지 이동 후 수출 바우처 사업 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 4"

    #page2.close()
    #page.wait_for_timeout(1000)

    with mobile_page.expect_popup() as page2_info:
        mobile_page.get_by_role("link", name="바로가기").nth(2).tap()
    mobile_page2 = page2_info.value

    mobile_page2.wait_for_timeout(3000)

    print("과학기술정보통신부 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER3_URL == mobile_page2.url, \
        "과학기술정보통신부 바로가기 3 -> AI 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 5"
    assert "AI바우처 지원" == mobile_page2.get_by_text("AI바우처 지원").inner_text(), \
        "과학기술정보통신부 바로가기 3 -> 홈페이지 이동 후 AI 바우처 사업 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 6"

    mobile_page2.close()
    mobile_page.wait_for_timeout(1000)

    with mobile_page.expect_popup() as page2_info:
        mobile_page.get_by_role("link", name="바로가기").nth(3).tap()
    mobile_page2 = page2_info.value

    mobile_page2.wait_for_timeout(3000)

    print("문화체육관광부 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER4_URL == mobile_page2.url, \
        "문화체육관광부 바로가기 4 -> 전통문화 혁신 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 7"
    assert "사업소개" == mobile_page2.get_by_role("heading", name="사업소개").locator("span").inner_text(), \
        "문화체육관광부 바로가기 4 -> 홈페이지 이동 후 전통문화포털 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 8"

    mobile_page2.close()
    mobile_page.wait_for_timeout(1000)

    with mobile_page.expect_popup() as page2_info:
        mobile_page.get_by_role("link", name="바로가기").nth(4).tap()
    mobile_page2 = page2_info.value

    mobile_page2.wait_for_timeout(3000)
    print("한국데이터산업진흥원 > 바로가기 선택 후 페이지 이동 완료")

    assert config.BOUCHER5_URL == mobile_page2.url, \
        "한국데이터산업진흥원 바로가기 5 -> 데이터 바우처 사업 url 연동 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 9"
    assert "데이터바우처 소개" == mobile_page2.get_by_role("heading", name="데이터바우처 소개").inner_text(), \
        "한국데이터산업진흥원 바보가기 5 -> 홈페이지 이동 후 데이터바우처 소개 문구 확인 실패 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 실패 8"

    mobile_page2.close()
    mobile_page.wait_for_timeout(1000)

    print("---- 89번 - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 각 URL 연동 확인 테스트 시작 -> 성공 ----")

