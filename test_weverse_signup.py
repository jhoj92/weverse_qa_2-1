import os
from dotenv import load_dotenv
from weverse_page import WeverseSignupPage

load_dotenv()

def test_weverse_signup_and_extract_wid(page):
    
    extracted_wid = None
    
    # WID 데이터 확인 함수
    def handle_response(response):
        nonlocal extracted_wid
        if "me?" in response.url:
            try:
                data = response.json()
                if "wid" in data:
                    extracted_wid = data["wid"]
            except:
                pass

    page.on("response", handle_response)

    signup_page = WeverseSignupPage(page)
    print("테스트 시작: Weverse 회원가입 및 WID 데이터 추출")

    # 0. 테스트 데이터 불러오기
    test_id = os.getenv("TEST_ID")
    test_pw = os.getenv("TEST_PW")
    test_nickname = os.getenv("TEST_NICKNAME")

    signup_page.navigate()
    signup_page.go_to_email_signup()
    
    signup_page.submit_email_for_verification(test_id)
    print("\n1. 인증코드 수동 입력 대기 중...")
    signup_page.wait_for_manual_verification()

    signup_page.fill_account_details(test_pw, test_nickname)
    signup_page.complete_signup()
    
    page.wait_for_timeout(3000) # WID 데이터 응답 대기
    print("2. WID 데이터 추출 대기 중...")

    print("\n==============================")
    print("[과제 2-1 테스트 결과]")
    print(f"ID : {test_id}")
    print(f"PW : {test_pw}")
    print(f"WID : {extracted_wid}")
    print("==============================\n")

    assert extracted_wid is not None, "WID 데이터가 추출되지 않았습니다."