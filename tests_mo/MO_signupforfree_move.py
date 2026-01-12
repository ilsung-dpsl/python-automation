import config
import re

def test_MO_signupforfree_move(mobile_page):
    print("--- 1번 - MO 회원가입 페이지 이동 테스트 시작 ---")

    mobile_page.goto("https://deepsales.com/ko/login?page=signup", wait_until="load", timeout=60000)
    mobile_page.wait_for_timeout(3000)

    mobile_page.wait_for_selector("text=DeepSales에 오신 것을 환영합니다!", timeout=3000)

    assert "딥세일즈 | 가입하기" in mobile_page.title(), "회원가입 페이지 타이틀 확인 실패 - 회원가입 페이지 이동 실패 1"
    print("--- 1번 - MO 회원가입 페이징 이동 완료 -> 성공")