

def test_prospecting_insufficient_credit_modal_charge_credit_click(page):
    print("----- 연락처 확인 시 크레딧이 부족할 경우 모달 노출 시 Charge credit 클릭 시 크레딧 충전 모달 노출 확인 테스트 시작 (DEV 기준으로 작성) -----")
    page.goto("https://dev.deepsales.io/ko/intro", wait_until="load", timeout=30000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill("ilsung.baek+devtest66@deepsales.com")
    page.get_by_placeholder("비밀번호").fill("!deepsales@36")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").click()
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").fill("소프트웨어 업체를 찾아줘")
    page.get_by_placeholder("예: 일본 화장품 제조사 세일즈 매니저").press("Enter")

    page.wait_for_timeout(5000)

    page.locator(".flex.justify-center.items-center.relative.hover.overflow-hidden.transition-colors.duration-200.whitespace-nowrap.bg-\\[var\\(--color-BG-Filled-Default\\)\\]").first.click()
    page.get_by_role("button", name="크레딧 충전").click()

    page.wait_for_timeout(1000)

    assert "크레딧 충전하기" in page.content(), "크레딧 충전하기 모달 > 타이틀 문구 출력 실패 - 크레딧 충전 모달 표시 실패 1"
    assert "카드 번호" in page.content(), "크레딧 충전하기 모달 > 카드번호 영역 문구 출력 실패 > 크레딧 충전 모달 표시 실패 2"
    assert "결제를 진행하는 모든 조건들에 동의합니다" in page.content(), "크레딧 충전하기 모달 > 약관 동의 문구 출력 실패 - 크레딧 충전 모달 표시 실패 3"

    page.get_by_role("button", name="취소").click()
