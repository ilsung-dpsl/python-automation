import re
import config

def test_salesagent_ui_check(page):
    print("---- 85번 - 세일즈 에이전트 UI 확인 테스트 시작 ----")

    page.goto("https://deepsales.com/ko/intro")
    page.wait_for_timeout(1000)
    page.get_by_role("banner").get_by_role("link", name="세일즈 에이전트").click()
    page.wait_for_timeout(1000)

    print("세일즈 에이전트 페이지 진입 완료")

    assert "해외 바이어 발굴,\n저희가 대신합니다" == page.get_by_role("heading", name="해외 바이어 발굴, 저희가 대신합니다").inner_text(), \
        "세일즈 에이전트 UI > 해외 바이어 관련 텍스트 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 1"
    # 20251125 - 세일즈 에이전트 ui > 상단 > [시작하기] 버튼 노출 확인 코드로 수정
    assert "시작하기" == page.get_by_role("button", name="시작하기").nth(1).inner_text(), \
        "세일즈 에이전트 UI > [시작하기] 버튼 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 2"
    assert "플랜, 이렇게 선택하면 됩니다" == page.get_by_role("heading", name="플랜, 이렇게 선택하면 됩니다").inner_text(), \
        "세일즈 에이전트 UI > 플랜 소개 > 플랜, 이렇게 선택하면 됩니다 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 3"
    # 20251125 - 세일즈 에이전트 ui > Starter > [시작하기] 버튼 노출 확인 코드로 수정
    assert "시작하기" == page.get_by_role("button", name="시작하기").nth(2).inner_text(), \
        "세일즈 에이전트 UI > Starter > [시작하기] 버튼 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 4"
    # 20251125 - 세일즈 에이전트 ui > Enterprise > [시작하기] 버튼 노출 확인 코드로 수정
    assert "시작하기" == page.get_by_role("button", name="시작하기").nth(4).inner_text(), \
        "세일즈 에이전트 UI > Enterprise > [시작하기] 버튼 노출 확인 실패 - 세일즈 에이전트 UI 확인 실패 5"

    print("---- 85번 - 세일즈 에이전트 UI 확인 테스트 시작 -> 성공 ----")