import re
import config

def test_salesagent_start_counseling_register_check(page):
    print("---- 84번 - 세일즈 에이전트 > Starter > 상담하기 등록 확인 ----")

    page.goto("https://deepsales.com/ko/intro")
    page.get_by_role("banner").get_by_role("link", name="세일즈 에이전트").click()
    page.wait_for_timeout(1000)

    print("세일즈 에이전트 페이지 진입 완료 ")

    page.get_by_role("button", name="상담하기").first.click()
    page.wait_for_timeout(1000)

    print("영업팀에 연락하기 모달 노출 완료")

    page.get_by_placeholder("이름 입력", exact=True).fill("일성")
    page.get_by_placeholder("성 입력").fill("백")
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 이름 / 성 입력 완료")

    page.get_by_placeholder("회사 이름 입력").fill("딥세일즈")
    page.get_by_placeholder("직함 입력").fill("Sales Agent Test")
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 회사 / 직함 입력 완료")

    page.locator("#react-select-2-input").fill("대한민국")
    page.wait_for_timeout(500)
    page.get_by_text("대한민국", exact=True).click()
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 회사 위치 입력 완료")

    page.get_by_placeholder("회사 이메일 입력").fill(config.GMAIL_EMAIL)
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 회사 이메일 입력 완료")

    page.locator("#react-select-3-input").fill("82")
    page.wait_for_timeout(500)
    page.get_by_text("+82").click()
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 나라 번호 입력 완료")

    page.get_by_placeholder("- 없이 전화번호 입력").fill("01041342385")
    page.wait_for_timeout(500)

    print("영업팀에 연락하기 모달 > 전화번호 입력 완료")

    page.get_by_role("textbox", name="귀하의 사업과 문의사항을 알려주세요").fill("QA 테스트 입니다. \nQA 운영 테스트 입니다. \nStarter > 상담하기 등록하기 완료 케이스 확인")
    page.wait_for_timeout(1000)

    print("영업팀에 연락하기 모달 > 문의사항 내용 입력 완료")

    page.get_by_role("button", name="제출하기").click()
    page.wait_for_timeout(1000)

    print("영업팀에 연락하기 모달 > 문의사항 등록 완료")

    assert "문의 전송" == page.get_by_text("문의 전송").inner_text(), \
        "문의 전송 완료 모달 > 문의 전송 타이틀 문구 노출 확인 - 세일즈 에이전트 > Starter > 상담하기 등록 확인 실패 1"
    assert ("문의하신 내용은 발송되었습니다. 저희 영업팀에서 문의하신 내용을 확인하고 다시 연락드리겠습니다."
            == page.get_by_text("문의하신 내용은 발송되었습니다. 저희 영업팀에서 문의하신 내용을 확인하고 다시 연락드리겠습니다").inner_text()), \
        "문의 전송 완료 모달 > 문의 전송 가이드 문구 노출 확인 - 세일즈 에이전트 > Starter > 상담하기 등록 확인 실패 2"
    assert "확인" == page.get_by_role("button", name="확인").inner_text(), \
        "문의 전송 완료 모달 > [확인] - 세일즈 에이전트 > Starter > 삼당하기 등록 확인 실패 3"

    page.get_by_role("button", name="확인").click()

    print("---- 84번 - 세일즈 에이전트 > Starter > 상담하기 등록 확인 -> 성공 ----")
