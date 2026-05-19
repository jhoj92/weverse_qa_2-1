class WeverseSignupPage:
    def __init__(self, page):
        self.page = page
        
        self.login_btn = page.get_by_role("button", name="로그인")
        self.signup_btn = page.get_by_role("button", name="회원가입")
        self.email_signup_btn = page.get_by_role("button", name="이메일로 가입하기")
        
        self.email_input = page.get_by_role("textbox", name="이메일 required")
        self.get_code_btn = page.get_by_role("button", name="인증코드 받기")
        self.validity_check = page.locator("span[class*='text-field_validity']").nth(1)
        self.verify_code_btn = page.get_by_role("button", name="인증코드 확인")
        
        self.password_input = page.get_by_role("textbox", name="비밀번호 required")
        self.password_confirm_input = page.get_by_role("textbox", name="비밀번호 확인 required")
        self.nickname_input = page.get_by_role("textbox", name="닉네임 required")
        
        self.next_btn = page.get_by_role("button", name="다음")
        self.agree_all_chk = page.get_by_role("checkbox", name="모두 동의")
        self.submit_btn = page.get_by_role("button", name="가입하기")
        self.confirm_btn = page.get_by_role("button", name="확인", exact=True)
        self.start_btn = page.get_by_role("button", name="시작하기")

    # ==================================================
    # [회원가입 로직 메서드]
    # ==================================================
    def navigate(self):
        self.page.goto("https://weverse.io/")

    def go_to_email_signup(self):
        self.login_btn.click()
        self.signup_btn.click()
        self.email_signup_btn.click()

    def submit_email_for_verification(self, email):
        self.email_input.click()
        self.email_input.fill(email)
        self.get_code_btn.click()

    def wait_for_manual_verification(self):
        self.validity_check.wait_for(state="visible", timeout=0)
        self.verify_code_btn.click()

    def fill_account_details(self, password, nickname):
        self.password_input.click()
        self.password_input.fill(password)
        self.password_confirm_input.click()
        self.password_confirm_input.fill(password)
        self.nickname_input.click()
        self.nickname_input.fill(nickname)
        self.next_btn.click()

    def complete_signup(self):
        self.agree_all_chk.click()
        self.submit_btn.click()
        self.confirm_btn.click()
        self.start_btn.click()