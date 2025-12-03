import config
import re

def test_salesagent_plan_benefits_request_a_consultation_register(page):
    print("---- 90번 - 세일즈 에이전트 > 플랜 혜택 보기 > 상담 요청하기 문의사항 등록 테스트 시작 ----")

    page.goto("https://deepsales.com/ko/intro", wait_until="load", timeout=30000)
    page.wait_for_timeout(1000)

    page.get_by_role("link", name="세일즈 에이전트 바우처").click()
    page.wait_for_timeout(1000)

    print("세일즈 에이전트 랜딩페이지 진입 완료")

    page.get_by_role("button", name="플랜 확인하기").click()
    page.wait_for_timeout(500)

    page.locator("#plan").get_by_role("button", name="상담 요청하기").click()
    page.wait_for_timeout(1000)

    print("영엉팀에 연락하기 모달 출력 완료")

    page.get_by_placeholder("이름 입력", exact=True).fill("ILSUNG")
    page.get_by_placeholder("성 입력").fill("BAEK")
    page.get_by_placeholder("성 입력").press("Tab")
    page.wait_for_timeout(500)

    page.get_by_placeholder("회사 이름 입력").fill("DeepSales Test")
    page.get_by_placeholder("회사 이름 입력").press("Tab")
    page.wait_for_timeout(500)

    page.get_by_placeholder("직함 입력").fill("QA Manager and Sales Agent")
    page.get_by_placeholder("직함 입력").press("Tab")
    page.wait_for_timeout(500)

    print("영엉팀에 연락하기 모달 > 이름 / 성 / 회사 이름 / 직함 입력 완료")

    page.locator("#react-select-2-input").fill("대한민국")
    page.locator("#react-select-2-input").press("Enter")
    page.locator("#react-select-2-input").press("Tab")
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 회사 위치 설정 완료")

    page.get_by_placeholder("회사 이메일 입력").fill(config.GMAIL_EMAIL)
    page.get_by_placeholder("회사 이메일 입력").press("Tab")
    page.locator("#react-select-3-input").fill("82")
    page.wait_for_timeout(1000)
    page.get_by_text("+82").click()
    page.wait_for_timeout(1000)

    print("영업팀에 연락하기 모달 > 전화 > 나라 번호 설정 완료")

    page.get_by_placeholder("- 없이 전화번호 입력").fill(config.CARD1_AUTH_PHONE)
    page.get_by_placeholder("- 없이 전화번호 입력").press("Tab")
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 전화번호 입력 완료")

    page.get_by_role("textbox", name="귀하의 사업과 문의사항을 알려주세요").fill("QA 운영 자동화 테스트 입니다. \n세일즈 에이전트 > 플랜 헤택 소개 > 상담 요청하기 > \n문의사항 등록 (크롬)")
    page.wait_for_timeout(1000)

    print("영업팀에 연락하기 모달 > 문의사항 내용 입력 완료")

    page.get_by_role("button", name="제출하기").click()
    page.wait_for_timeout(1000)

    print("영업팀에 연락하기 모달 > 모든 필수 정보 입력 > 문의사항 제출 완료")

    assert "문의 전송" == page.get_by_text("문의 전송").inner_text(), \
        "문의 전송 모달 > 타이틀 문구 확인 실패 - 세일즈 에이전트 > 플랜 혜택 소개 > 상담 요청하기 문의 사항 등록 실패 1"
    assert ("문의하신 내용은 발송되었습니다. 저희 영업팀에서 문의하신 내용을 확인하고 다시 연락드리겠습니다." ==
            page.get_by_text("문의하신 내용은 발송되었습니다. 저희 영업팀에서 문의하신 내용을 확인하고 다시 연락드리겠습니다").inner_text()), \
        "문의 전송 모달 > 안내 문구 확인 실패 - 세일즈 에이전트 > 플랜 혜택 소개 > 상담 요청하기 문의 사항 등록 실패 2"
    assert "확인" == page.get_by_role("button", name="확인", exact=True).inner_text(), \
        "문의 전송 모달 > [확인] 버튼 확인 실패 - 세일즈 에이전트 > 플랜 혜택 소개 > 상담 요청하기 문의 사항 등록 실패 3"

    page.get_by_role("button", name="확인", exact=True).click()
    page.wait_for_timeout(1000)

    print("---- 90번 - 세일즈 에이전트 > 플랜 혜택 보기 > 상담 요청하기 문의사항 등록 테스트 시작 -> 성공 ----")


