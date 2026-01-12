import re
import config

def test_MO_salesagent_ui_check(mobile_page):
    print("---- 66번 - MO 세일즈 에이전트 UI 확인 테스트 시작 ----")

    # 20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="세일즈 에이전트 바우처").tap()
    mobile_page.wait_for_timeout(1000)

    print("세일즈 에이전트 페이지 진입 완료")

    assert "해외 바이어 발굴,\n저희가 대신합니다" == mobile_page.get_by_role("heading", name="해외 바이어 발굴, 저희가 대신합니다").inner_text(), \
        "세일즈 에이전트 UI > 해외 바이어 관련 텍스트 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 1"
    # 20251202 - 세일즈 에이전트 랜딩페이지 > [플랜 확인하기] 버튼으로 변경되어 코드 수정
    assert "플랜 확인하기" == mobile_page.get_by_role("button", name="플랜 확인하기").inner_text(), \
        "세일즈 에이전트 UI > [시작하기] 버튼 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 2"

    # 20251202 - 바우처 및 정부 지원 관련 QA 반영으로 인해, 세일즈 에이전트 랜딩 페이지 > 정부 지원 바우처 > [잠깐!] 배치 노출 확인 코드 추가
    wait_badge = mobile_page.get_by_text("잠깐!")
    assert wait_badge.is_visible(), \
        "세일즈 에이전트 UI > 정부 지원 바우처 혜택 > [잠깐!] 배지 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 3"
    # 20251202 - 세일즈 에이전트 랜딩 페이지 > 정부 지원 바우처 혜택 영역의 타이틀 문구 노출 확인 코드 추가
    assert "정부 지원 바우처 혜택" == mobile_page.get_by_text("정부 지원 바우처 혜택").inner_text(), \
        "세일즈 에이전트 UI > 정부 지원 바우처 혜택 타이틀 문구 노출 확인 실패 - 세일즈 에이전트 UI  확인 실패 4"
    # 20251202 - 세일즈 에이전트 랜딩 페이지 > 정부 지원 바우처 혜택 > 안내 문구 노출 확인 코드 추가
    assert "딥세일즈의 에이전트 서비스는 다양한 정부 부처 및 공공기관이 주관하는 사업과 함께 합니다." == mobile_page.get_by_text("딥세일즈의 에이전트 서비스는 다양한 정부 부처 및 공공기관이 주관하는 사업과 함께 합니다").inner_text(), \
        "세일즈 에이전트 UI > 정부 지원 바우처 혜택 > 안내 문구 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 5"
    assert "플랜, 이렇게 선택하면 됩니다" == mobile_page.get_by_role("heading", name="플랜, 이렇게 선택하면 됩니다").inner_text(), \
        "세일즈 에이전트 UI > 플랜 소개 > 플랜, 이렇게 선택하면 됩니다 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 3"
    # 20251202 - 세일즈 에이전트 ui > Starter > [시작하기] 버튼 노출 및 실제 확인 위치 변경으로 코드로 수정
    assert "시작하기" == mobile_page.get_by_role("button", name="시작하기").first.inner_text(), \
        "세일즈 에이전트 UI > Starter > [시작하기] 버튼 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 4"
    # 20251202 - 세일즈 에이전트 ui > Enterprisze > [시작하기] 버튼 노출 및 실제 확인 위치 변경으로 코드로 수정
    assert "시작하기" == mobile_page.get_by_role("button", name="시작하기").nth(2).inner_text(), \
        "세일즈 에이전트 UI > Enterprise > [시작하기] 버튼 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 5"

    print("---- 66번 - MO 세일즈 에이전트 UI 확인 테스트 시작 -> 성공 ----")