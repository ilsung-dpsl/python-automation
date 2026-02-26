import config
import re

def test_MO_company_register_flow_check(mobile_page):
    print("----- 32번 - MO 회사 정보 메인 > 등록하기 -> 회사 등록 후 확인 테스트 시작 -----")

    #20251209 - url 이동 시 로드 타임아웃 50초 코드로 수정
    mobile_page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=50000)
    mobile_page.wait_for_timeout(500)

    mobile_page.get_by_role("banner").get_by_role("img").first.tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_placeholder("이메일").fill(config.FREE_PA24_ACCOUNT)
    mobile_page.get_by_placeholder("비밀번호").fill(config.FREE_PA24_PW)
    mobile_page.get_by_role("button", name="로그인").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="Confirm").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 로그인 후 탐색하기 페이지 진입 완료")

    # 20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    mobile_page.get_by_role("button").nth(2).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_text("회사 정보", exact=True).tap()
    mobile_page.wait_for_timeout(3000)

    print("MO Web - 회사 정보 페이지 진입 완료")

    mobile_page.locator(".text-FG-Primary.css-124rwol").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.locator("#react-select-2-input").fill("deepsales")
    mobile_page.wait_for_timeout(1000)

    #deepsales 옵션 1번쨰 선택 코드로 재변경 - 20250904
    mobile_page.locator("#react-select-2-option-0").get_by_text("DeepSales").tap()
    #page.locator("#react-select-2-option-1").get_by_text("DeepSales").click()
    mobile_page.wait_for_timeout(1000)

    # 20260115 - 코드 수정
    mobile_page.get_by_text("회사 페이지 등록하기").tap(timeout=10000)
    mobile_page.wait_for_timeout(500)
    mobile_page.get_by_role("button", name="확인").tap(timeout=10000)
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 회사 정보 메인 > 회사 정보 등록 완료")

    mobile_page.locator(".text-\\[18px\\]").first.tap()
    mobile_page.wait_for_timeout(1000)

    #20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    mobile_page.get_by_role("button").nth(2).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_text("팀 관리").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 팀관리 페이지 진입 완료")

    #20251001 - 상단 우측 마이페이지 버튼 선택 코드 수정
    mobile_page.get_by_role("button").nth(2).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_text("회사 정보").tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 회사 정보 상세 페이지 진입 완료")

    assert "DeepSales" == mobile_page.locator(".text-\\[18px\\]").first.inner_text(), \
        "MO Web - 회사 정보 상세 페이지 > 회사명 출력 실패 - 회사 정보 등록 실패 1"
    assert "2021" == mobile_page.get_by_text("2021", exact=True).inner_text(), \
        "MO Web - 회사 정보 상세 페이지 > 설립연도 출력 실패 - 회사 정보 등록 실패 2"
    assert "Seed" == mobile_page.get_by_text("Seed").inner_text(), \
        "MO Web - 회사 정보 상세 페이지 > 펀딩 > 투자 단계 출력 실패 - 회사 정보 등록 실패 3"

    print("MO Web - 회사 정보 등록 완료 확인")

    mobile_page.get_by_text("소속된 회사에서 나가기").tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="확인", exact=True).tap()
    mobile_page.wait_for_timeout(1000)

    mobile_page.get_by_role("button", name="확인", exact=True).tap()
    mobile_page.wait_for_timeout(1000)

    print("MO Web - 회사 정보 등록 후 소속된 회사 떠니기 완료")
    print("----- 32번 - MO 회사 정보 메인 > 등록하기 -> 회사 등록 후 확인 테스트 시작 -> 성공 -----")