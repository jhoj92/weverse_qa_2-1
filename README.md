# 위버스 회원가입 및 WID 추출 자동화 과제

## 1. 실행 방법
1. 필수 라이브러리 설치: `pip install pytest pytest-playwright python-dotenv`
2. 루트 경로에 `.env` 파일 생성 후 데이터 입력 (TEST_ID, TEST_PW, TEST_NICKNAME)
3. 실행 명령어: `pytest test_weverse_signup.py --headed -s`

코드를 성공적으로 실행하면 터미널에 아래와 같이 데이터가 정상 출력됩니다.

[과제 2-1 테스트 결과]
- ID  : 이메일
- PW  : 비밀번호
- WID : WID 값
