import config
import re

def test_mylist_detail_enterpriseplan_exporttocsv_check(page):
    print("----- 49번 - 마이리스트 상세 > 유료회원 > csv 내보내기 시 미확인 연락처 포함 모달 및 크레딧 사용 메시지 출력 테스트 시작 -----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(2000)

    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 마이 리스트 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="마이 리스트").nth(1).click()
    page.wait_for_timeout(1000)

    print("마이리스트 페이지 진입 완료")

    # 20250930 - 마이리스트 > test 1 (일반 폴더) 선택 코드 수정
    page.get_by_text("test 1").click(timeout=10000)
    page.wait_for_timeout(1000)
    print("마이리스트 상세 페이지 (일반 폴더) 진입 완료")

    page.locator("div").filter(has_text=re.compile(r"^이름 / 직함연락처회사담당자 위치산업군추가일자$")).get_by_role("checkbox").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="내보내기").click()
    page.wait_for_timeout(500)
    page.get_by_role("menuitem", name="CSV 내보내기").click()
    page.wait_for_timeout(2000)

    assert "미확인 연락처는 내보낼 수 없습니다." == page.get_by_text("미확인 연락처는 내보낼 수 없습니다").inner_text(), \
        "미확인 연락처 포함 모달 > 타이틀 문구 확인 실패 - 미확인 연락처 모달 노출 실패 1"
    assert "확인" == page.get_by_role("button", name="확인", exact=True).inner_text(), \
        "미확인 연락처 포함 모달 > 확인 버튼 출력 실패 - 미확인 #연락처 모달 노출 실패 2"

    print("마이리스트 상세 페이지 (일반 폴더) > 미확인 연락처 포함 모달 출력 확인 완료")

    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(1000)

    assert "3 크레딧이 사용되었습니다." ==  page.locator("div").filter(has_text=re.compile(r"^3 크레딧이 사용되었습니다\.$")).nth(1).inner_text(), \
        "CSV 내보내기 완료 후 크레딧 사용 토스트 메시지 출력 실패 - CSV 내보내기 실패 3"

    print("마이리스트 상세 페이지 (일반 폴더) > CSV 내보내기 완료 후 크레딧 사용 메시지 출력 확인")
    print("----- 마이리스트 상세 > 유료회원 > csv 내보내기 시 미확인 연락처 포함 모달 및 크레딧 사용 메시지 출력 테스트 시작 -> 성공 -----")

