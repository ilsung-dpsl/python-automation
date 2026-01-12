import config
import re

def test_MO_discover_card_prospecting_now_check(mobile_page):
    print("----- 38번 - MO 발견하기 > 임의 카드 > 지금 탐색하기 선택 시 탐색결과 연동 확인 테스트 시작 -----")

    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").click()
    mobile_page.wait_for_timeout(1000)
    mobile_page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    mobile_page.get_by_role("button", name="로그인").click()
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    # 20250930 - LNB > 발견하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    mobile_page.get_by_role("link").filter(has_text="발견하기").tap()
    mobile_page.wait_for_timeout(3000)

    print("발견하기 페이지 진입 완료")

    mobile_page.get_by_text("고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").tap()
    mobile_page.wait_for_timeout(1000)

    # 페르소나 설정 안내 모달 > 나중에 하기 버튼 선택으로 모달을 닫는다.
    mobile_page.get_by_role("button", name="나중에 하기").tap()
    mobile_page.wait_for_timeout(2000)

    mobile_page.get_by_role("article").filter(
        has_text="소매업홍콩 메이크업 마케팅 전문가홍콩 유통사에서 메이크업 제품 출시를 주도하는 마케팅 전문가를 탐색해보세요.Retail +1,").get_by_role("button").click()

    mobile_page.wait_for_timeout(5000)

    print("발견하기 연동 후 탐색하기 진입 완료")

    assert "홍콩" == mobile_page.get_by_text("홍콩").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 필터 > 위치 키워드 추가 실패 - 탐색하기 연동 실패 1"
    assert "소매업" == mobile_page.get_by_text("소매업").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 필터 > 산업군 키워드 추가 실패 - 탐색하기 연동 실패 2"
    assert "Makeup Marketing Professionals in Hong Kong" == mobile_page.get_by_text("Makeup Marketing").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 검색결과 문구에 카드 제목 반영 실패 - 탐색하기 연동 실패 3"
    assert "Sunny Cheng" == mobile_page.get_by_text("Sunny Cheng").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 리드 성함 확인 실패 - 탐색하기 연동 실패 4"

    print("----- 38번 - MO 발견하기 > 임의 카드 > 지금 탐색하기 선택 시 탐색결과 연동 확인 테스트 시작 -> 성공 -----")