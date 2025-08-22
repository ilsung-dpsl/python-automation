import config
import re

def test_discover_persona_setup_check(page):
    print("----- 발견하기 최초 진입 시 퍼소나 설정 안내 모달 표시 및 퍼소나 설정 추가 확인 테스트 시작 -----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("이메일").fill(config.FREE_PA9_ACCOUNT)
    page.get_by_placeholder("비밀번호").fill(config.FREE_PA9_PW)
    page.get_by_role("button", name="로그인").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="발견하기").click()
    page.wait_for_timeout(2000)

    print("발견하기 페이지 진입 완료")

    assert "고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오." == page.get_by_text("고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").inner_text(), \
        "퍼소나 설정 안내 모달 노출 실패 - 퍼소나 설정 안내 모달 및 퍼소나 설정 추가 실패 1"
    assert "페르소나 설정" == page.locator("#modal-root").get_by_role("button", name="페르소나 설정").inner_text(), \
        "퍼소나 설정 안내 모달 > 페르소나 설정 버튼 노출 실패 - 퍼소나 설정 안내 모달 및 퍼소나 설정 추가 실패 2"

    print("발견하기 페이지 진입 후 퍼솬 설정 안내 모달 노출 확인 완료")
    page.locator("header").filter(has_text="고객 페르소나를 통해 고객에게 다가가기 시작할 준비를 하십시오").get_by_role("button").click()
    page.wait_for_timeout(1000)

    page.get_by_role("button", name="페르소나 설정").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="새 페르소나 만들기").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("예: 북미 화장품 회사 슈퍼바이저").click()
    page.get_by_placeholder("예: 북미 화장품 회사 슈퍼바이저").fill("새 페르소나를 만들어 볼까요?")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="산업").click()
    page.wait_for_timeout(1000)
    page.locator("div").filter(has_text=re.compile(r"^가정 건강관리 서비스$")).click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="키워드").click()
    page.get_by_role("textbox", name="키워드").fill("건강")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="위치").click()
    page.wait_for_timeout(1000)
    page.get_by_placeholder("위치 선택").click()
    page.get_by_placeholder("위치 선택").fill("대한민국")
    page.wait_for_timeout(1000)
    page.locator("div").filter(has_text=re.compile(r"^대한민국$")).nth(3).click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="직원 수").click()
    page.wait_for_timeout(1000)
    page.locator("div").filter(has_text=re.compile(r"^1 - 10$")).click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="새 페르소나 만들기").click()
    page.wait_for_timeout(2000)

    assert "새로운 페르소나가 생성되었습니다." == page.get_by_text("새로운 페르소나가 생성되었습니다.").inner_text(), \
        "새로운 페르소나 생성 후 토스트 메시지 출력 실패 - - 퍼소나 설정 안내 모달 및 퍼소나 설정 추가 실패 3"

    print("새 페르소나 생성 후 페르소나 관리 모달 > 생성한 페르소나 목록 확인 전")

    page.wait_for_timeout(2000)

    assert "새 페르소나를 만들어 볼까요?" == page.get_by_text("새 페르소나를 만들어 볼까요?").inner_text(), \
        "새 페르소나 생성한 제목 노출 실패 - 퍼소나 설정 안내 모달 및 퍼소나 설정 추가 실패 4"
    assert "Home Health Care Services" == page.get_by_text("Home Health Care Services").inner_text(), \
        "새 페르소나 생성한 페르소나의 산업군 태그 노출 실패 - 퍼소나 설정 안내 모달 및 퍼소나 설정 추가 실패 5"

    page.get_by_role("article").filter(has_text="새 페르소나를 만들어 볼까요?Home Health").get_by_role("button").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="삭제").click()
    page.wait_for_timeout(500)
    page.locator("header").filter(has_text="페르소나 관리").get_by_role("button").click()
    page.wait_for_timeout(500)

    print("새 페르소나 생성 후 페르소나 관리 모달 > 생성한 페르소나 목록 정상 추가 확인 완료")

    print("----- 발견하기 최초 진입 시 퍼소나 설정 안내 모달 표시 및 퍼소나 설정 추가 확인 테스트 시작 -> 성공 -----")
