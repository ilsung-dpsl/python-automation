import config
import re

def test_discover_freeplan_industry_or_keyword_search_limit_check(page):
    print("40번 - 발견하기 > 무료 회원 사용자 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA9_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA9_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    # 20250930 - 탐색하기 ui(LNB 영역) 변경으로 인한 LNB 숨김처리됨 -> LNB 마우스 호버하는 코드 추가 및 수정
    lnb_hover_target = page.get_by_text("대시보드탐색하기발견하기마이 리스트").first
    lnb_hover_target.hover()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 사이드바 메뉴 펼침  버튼 선택 코드 추가
    page.get_by_role("button").first.click()
    page.wait_for_timeout(2000)

    # 20250930 - LNB > 발견하기 메뉴 영역 선택 위치 변경으로 인한 코드 수정
    page.get_by_role("link", name="발견하기").nth(1).click()
    page.wait_for_timeout(3000)

    print("발견하기 페이지 진입")

    page.locator("header").filter(has_text="고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.locator(".cursor-pointer").first.click()
    page.wait_for_timeout(2000)

    print("요금제 제한 안내 모달 노출 전")

    assert "이런! 무료 플랜에서는 키워드 검색 및\n필터 사용이 제한됩니다." == page.locator("header").filter(has_text="이런! 무료 플랜에서는 키워드 검색 및 필터 사용이 제한됩니다").inner_text(), \
        "요금제 제한 안내 모달 > 타이틀 문구 노출 실패 - 발견하기 산업군 탐색 시 요금제 제한 안내 모달 출력 실패 1"
    assert "요금제 업그레이드" == page.get_by_role("button", name="요금제 업그레이드").inner_text(), \
        "요금제 제한 안내 모달 > 요금제 업그레이드 버튼 노출 실패 - 발견하기 산업군 탐색 시 요금제 제한 안내 모달 출력 실패 2"

    print("요금제 제한 안내 모달 노출 확인 완료")

    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()


    # 20251014 - 키워드 검색 시 제한 수정으로 인해 코드 추가
    page.get_by_placeholder("제목으로 찾기").fill("도매")
    page.get_by_placeholder("제목으로 찾기").press("Enter")

    page.wait_for_timeout(1000)

    assert "이런! 무료 플랜에서는 키워드 검색 및\n필터 사용이 제한됩니다." == page.locator("header").filter(
        has_text="이런! 무료 플랜에서는 키워드 검색 및 필터 사용이 제한됩니다").inner_text(), \
        "요금제 제한 안내 모달 > 타이틀 문구 노출 실패 - 발견하기 키워드 탐색 시 요금제 제한 안내 모달 출력 실패 3"
    assert "플랜을 변경하고 더 많은 잠재고객을 만나보세요." in page.get_by_text("플랜을 변경하고 더 많은 잠재고객을 만나보세요. AI").inner_text(), \
        "요금제 제한 안내 모달 > 안내 문구 노출 실패 - 발견하기 키워드 탐색 시 요금제 제한 안내 모달 출력 실패 4"

    page.locator("#modal-root").get_by_role("button").filter(has_text=re.compile(r"^$")).click()

    print("발견하기 > 무료 회원 사용자 키워드/산업군 탐색 시 요금제 업그레이드 모달 노출 확인 테스트 시작 -> 성공 -----")
