import config
import re

def test_discover_freeplan_industry_or_keyword_search_limit_check(page):
    print("발견하기 > 무료 회원 사용자 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA9_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA9_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="발견하기").click()
    page.wait_for_timeout(1000)

    print("발견하기 페이지 진입")

    page.locator("header").filter(has_text="고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.locator(".cursor-pointer").first.click()
    page.wait_for_timeout(2000)

    print("요금제 제한 안내 모달 노출 전")

    assert "이런! 무료 플랜에서는 키워드 검색 및\n필터 사용이 제한됩니다." == page.locator("header").filter(has_text="이런! 무료 플랜에서는 키워드 검색 및 필터 사용이 제한됩니다").inner_text(), \
        "요금제 제한 안내 모달 > 타이틀 문구 노출 실패 - 발견하기 키워드/산업군 탐색 시 요금제 제한 안내 모달 출력 실패 1"
    assert "요금제 업그레이드" == page.get_by_role("button", name="요금제 업그레이드").inner_text()

    print("요금제 제한 안내 모달 노출 확인 완료")

    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    print("발견하기 > 무료 회원 사용자 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출 확인 테스트 시작 -> 성공 -----")
