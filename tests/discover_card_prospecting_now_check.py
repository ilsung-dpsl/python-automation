from httplib2 import ProxyInfo

import config

def test_discover_card_prospecting_now_check(page):
    print("----- 발견하기 > 임의 카드 > 지금 탐색하기 선택 시 탐색결과 연동 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.ENTERPRISE_SUB_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.ENTERPRISE_SUB_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="발견하기").click()
    page.wait_for_timeout(1000)

    print("발견하기 페이지 진입 완료")
    page.locator("header").filter(has_text="고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.get_by_role("article").filter(has_text="소매업홍콩 메이크업 마케팅 전문가홍콩 유통사에서 메이크업 제품 출시를 주도하는 마케팅 전문가를 탐색해보세요.Retail +1,").get_by_role("button").click()

    page.wait_for_timeout(5000)

    print("발견하기 연동 후 탐색하기 진입 완료")

    assert "홍콩" == page.get_by_text("홍콩").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 필터 > 위치 키워드 추가 실패 - 탐색하기 연동 실패 1"
    assert "소매업" == page.get_by_text("소매업").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 필터 > 산업군 키워드 추가 실패 - 탐색하기 연동 실패 2"
    assert "Makeup Marketing Professionals in Hong Kong" == page.get_by_text("Makeup Marketing").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 검색결과 문구에 카드 제목 반영 실패 - 탐색하기 연동 실패 3"
    assert "Sunny Cheng" == page.get_by_text("Sunny Cheng").inner_text(), \
        "발견하기 > 카드 > 지금 탐색하기 연동 후 탐색하기 > 리드 성함 확인 실패 - 탐색하기 연동 실패 4"

    print("----- 발견하기 > 임의 카드 > 지금 탐색하기 선택 시 탐색결과 연동 확인 테스트 시작 -> 성공 -----")
