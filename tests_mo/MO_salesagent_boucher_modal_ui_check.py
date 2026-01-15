import re
import config
import cv2
import numpy as np

def test_MO_salesagent_boucher_modal_ui_check(mobile_page):
    print("---- 69번 - MO 세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 테스트 시작 ----")

    mobile_page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="세일즈 에이전트 바우처").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 세일즈 에이전트 랜딩 페이지 진입 완료")

    mobile_page.get_by_role("button", name="플랜 확인하기").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="바우처 혜택 상세 보기").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 출력")

    assert "정부가 인증한 AI 기반 해외 영업 지원 서비스" == mobile_page.get_by_text("정부가 인증한 AI 기반 해외 영업 지원 서비스").inner_text(), \
        ("MO Web - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 타이틀 문구 확인 실패 - "
         "세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 실패 1")
    assert "수출 바우처 사업" == mobile_page.get_by_text("수출 바우처 사업").first.inner_text(), \
        ("MO Web - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 수출 바우처 사업 1 확인 실패 - "
         "세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 실패 2")
    assert "AI 바우처 사업" == mobile_page.get_by_text("AI 바우처 사업").inner_text(), \
        ("MO Web - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > AI 바우처 사업 3 확인 실패 - "
         "세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 실패 3")
    assert "전통문화 혁신 바우처 사업" == mobile_page.get_by_text("전통문화 혁신 바우처 사업").inner_text(), \
        ("MO Web - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 전통문화 혁신 바우처 사업 4 확인 실패 - "
         "세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 실패 4")
    assert "바로가기" == mobile_page.get_by_role("link", name="바로가기").first.inner_text(), \
        ("MO Web - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > 바로가기 링크 연동 노출 확인 실패 - "
         "세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 실패 5")
    assert "확인" == mobile_page.get_by_role("button", name="확인", exact=True).inner_text(), \
        ("MO Web - 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 > [확인] 노출 확인 실패 - "
         "세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 실패 6")

    mobile_page.wait_for_timeout(1000)
    print("MO Web - 세일즈 에이전트 > 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 UI 체크 확인 완료")

    print("---- 69번 - MO 세일즈 에이전트 > 플랜 혜택 보기의 바우처 혜택 상세 보기 선택 시 정부가 인증한 AI 기반 해외 영업 지원 서비스 모달 노출 확인 테스트 시작 -> 성공 ----")