import re
import config

def test_salesagent_request_a_consultation_register(page):
    print("---- 87번 - 세일즈 에이전트 > 상단 > 상담요청하기 등록 확인 테스트 시작 ----")

    page.goto("https://deepsales.com/ko/intro",wait_until="load", timeout=30000)
    page.wait_for_timeout(2000)

    page.get_by_role("banner").get_by_role("link", name="세일즈 에이전트").click()
    page.wait_for_timeout(1000)

    print("세일즈 에이전트 랜딩페이지 진입 완료")

    # 20251202 - 세일즈 에이전트 페이지 > 상담 요청하기 앨리먼트 코드 변경으로 코드 수정
    page.get_by_role("button", name="상담 요청하기").first.click()
    page.wait_for_timeout(1000)

    print("영업팀에 연락하기 모달 출력 상태 완료")

    page.get_by_placeholder("이름 입력", exact=True).fill("일성")
    page.get_by_placeholder("성 입력").fill("백")
    page.wait_for_timeout(1000)

    page.get_by_placeholder("회사 이름 입력").fill("딥세일즈 자동화 코퍼레이션")
    page.get_by_placeholder("직함 입력").fill("QA Manager")
    page.wait_for_timeout(1000)

    page.locator("#react-select-2-input").fill("대한민국")
    page.wait_for_timeout(500)
    page.get_by_text("대한민국", exact=True).click()
    page.wait_for_timeout(1000)

    page.get_by_placeholder("회사 이메일 입력").fill(config.ENTERPRISE_TEAM_MEMBER_AC)
    page.wait_for_timeout(500)

    page.locator("#react-select-3-input").fill("82")
    page.wait_for_timeout(500)

    page.get_by_text("+82").click()
    page.wait_for_timeout(500)

    page.get_by_placeholder("- 없이 전화번호 입력").fill("01041342385")
    page.wait_for_timeout(1000)

    page.get_by_role("textbox", name="귀하의 사업과 문의사항을 알려주세요").fill("QA 자동화 운영 테스트 (크롬) \n\n세일즈 에이전트 > 상담 요청하기 > 문의 사항 등록")
    page.wait_for_timeout(500)

    print("영업팀에 문의하기 모달 > 모든 필수 입력 입력 완료")

    page.get_by_role("button", name="제출하기").click()
    page.wait_for_timeout(1000)

    print("영업팀에 문의하기 모달 > 모든 필수 입력 완료 후 제출하기 완료")

    assert "문의 전송" == page.get_by_text("문의 전송").inner_text(), \
        "영업팀에 문의하기 등록 후 문의 전송 모달 > 타이틀 문구 확인 실패 - 세일즈 에이전트 > 상단 > 상담요청하기 등록 확인 실패 1"
    assert ("문의하신 내용은 발송되었습니다. 저희 영업팀에서 문의하신 내용을 확인하고 다시 연락드리겠습니다." in
            page.locator("div").filter(has_text="문의 전송문의하신 내용은 발송되었습니다. 저희 영업팀에서 문의하신 내용을 확인하고 다시 연락드리겠습니다.확인").nth(2).inner_text()), \
        "영업팀에 문의하기 등록 후 문의 전송 모달 > 가이드 문구 확인 실패 - 세일즈 에이전트 > 상단 > 상담요청하기 등록 확인 실패 2"
    # 20251202 - 문의 전송 모달 > 확인 버튼의 앨리먼트 요소가 변경되어 테스트 스크립트 수정함
    assert "확인" == page.get_by_role("button", name="확인", exact=True).inner_text(), \
        "영업팀에 문의하기 등록 후 문의 전송 모달 > [확인] 버튼 확인 실패 - 세일즈 에이전트 > 상단 > 상담요청하기 등록 확인 실패 3"

    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(1000)

    print("---- 세일즈 에이전트 > 상단 > 상담요청하기 등록 확인 테스트 시작 -> 성공 ----")
