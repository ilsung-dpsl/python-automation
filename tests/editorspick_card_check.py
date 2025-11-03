import config
import re

def test_editorspick_card_check(page):
    print("---- 79번 - 에디터픽 카드 노출 확인 테스트 시작 ----")
    page.goto("https://deepsales.com/ko/intro")
    page.wait_for_timeout(1000)
    page.get_by_role("banner").get_by_role("link", name="에디터 픽").click()
    page.wait_for_timeout(1000)

    print("에디터픽 메인 페이지 진입 완료")

    assert "Entertainment Providers" in page.get_by_role("article").filter(has_text="Entertainment Providers글로벌 K-").locator("span").inner_text(), \
        "에디터픽 메인 > 글로벌 K-POP 굿즈 바이어 리스트 > 산업군 태그 노출 확인 실패 - 에디터픽 카드 노출 확인 실패 1"
    assert "글로벌 K-POP 굿즈 바이어 리스트" == page.get_by_role("heading", name="글로벌 K-POP 굿즈 바이어 리스트").inner_text(), \
        "에디터픽 메인 > 글로벌 K-POP 굿즈 바이어 리스트 카드 제목 노출 확인 실패 - 에디터픽 카드 노출 확인 실패 2"
    assert "+ 22개 기업" == page.get_by_text("+ 22개 기업").first.inner_text(), \
        "에디터픽 메인 > 글로벌 K-POP 굿즈 바이어 리스트 카드 > + 기업 개수 노출 확인 실패 - 에디터픽 카드 노출 확인 실패 3"
    assert "Professional Services" == page.get_by_role("article").filter(has_text="Professional Services일본 화장품 E").locator("span").inner_text(), \
        "에디터픽 메인 > 일본 화장품 E-커머스 및 마케팅 업체 리스트 카드 > 산업군 노출 확인 실패 - 에디터픽 카드 노출 확인 실패 4"
    assert "일본 화장품 E-커머스 및 마케팅 업체 리스트" == page.get_by_role("heading", name="일본 화장품 E-커머스 및 마케팅 업체 리스트").inner_text(), \
        "에디터픽 메인 > 일본 화장품 E-커머스 및 마케팅 업체 리스트 카드 제목 노출 확인 실패 - 에디터픽 카드 노출 확인 실패 5"
    assert "+ 17개 기업" == page.get_by_text("+ 17개 기업").nth(4).inner_text(), \
        "에디터픽 메인 > 일본 화장품 E-커머스 및 마케팅 업체 리스트 카드 > + 기업 개수 노출 확인 실패 = 에디터픽 카드 노출 확인 실패 6"

    print("---- 79번 - 에디터픽 카드 노출 확인 테스트 시작 -> 성공 ----")
