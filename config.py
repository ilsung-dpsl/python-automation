import json

# config.py

#인증번호 확인용 > 구글 지메일
GMAIL_EMAIL = "ilsung.baek@deepsales.com"
GMAIL_EMAIL_PW = "1@qordlftjd"

#무료회원 1 - 기본 확인용
FREE_ACCOUNT = "starbictoli@naver.com"
FREE_PW = "!deepsales@36"

#유료회원 - 엔터프라이즈 > 팀오너
ENTERPRISE_ACCOUNT = "deepsalesdemo@gmail.com"
ENTERPRISE_PW = "!deepsales@36"

#유료회원 - 엔터프라이즈 > 팀멤버
ENTERPRISE_TEAM_MEMBER_AC = "ilsung.baek@deepsales.com"
ENTERPRISE_TEAM_MEMBER_PW = "!deepsales@36"

#유료회원 - 엔터프라이즈 > 팀오너
ENTERPRISE_SUB_ACCOUNT = "ilsung.baek+pa16@deepsales.com"
ENTERPRISE_SUB_PW = "!deepsales@36"

#무료회원 2 - 확인용 prd5
FREE_ACCOUNT_CHECK = "ilsung.baek+prd5@deepsales.com"
FREE_ACCOUNT_PW = "!deepsales@36"

#무료회원 3 - 확인용 prd2
FREE_PRD2_ACCOUNT = "ilsung.baek+prd2@deepsales.com"
FREE_PRD2_PW = "!deepsales@36"

#무료회원 4 - 확인용 prd3
FREE_PRD3_ACCOUNT = "ilsung.baek+prd3@deepsales.com"
FREE_PRD3_PW = "!deepsales@36"

#무료회원 5 - 확인용 prd4
FREE_PRD4_ACCOUNT = "ilsung.baek+prd4@deepsales.com"
FREE_PRD4_PW = "!deepsales@36"

#무료회원 6 - 확인용 prd5
FREE_PRD5_ACCOUNT = "ilsung.baek+prd5@deepsales.com"
FREE_PRD5_PW = "!deepsales@36"

#무료회원 6 - 확인용 prd6
FREE_PRD6_ACCOUNT = "ilsung.baek+prd6@deepsales.com"
FREE_PRD6_PW = "!deepsales@36"

FREE_PA8_ACCOUNT = "ilsung.baek+pa8@deepsales.com"
FREE_PA8_PW = "!deepsales@36"

FREE_PA9_ACCOUNT = "ilsung.baek+pa9@deepsales.com"
FREE_PA9_PW = "!deepsales@36"

FREE_PA17_ACCOUNT = "ilsung.baek+pa17@deepsales.com"
FREE_PA17_PW = "!deepsales@36"

FREE_PA19_ACCOUNT = "ilsung.baek+pa19@deepsales.com"
FREE_PA19_PW = "!deepsales@36"

FREE_PA24_ACCOUNT = "ilsung.baek+pa24@deepsales.com"
FREE_PA24_PW = "!deepsales@36"

FREE_PA25_ACCOUNT = "ilsung.baek+pa25@deepsales.com"
FREE_PA25_PW = "!deepsales@36"

TEAM_OWNER_ACCOUNT = "ilsung.baek+pa15@deepsales.com"
TEAM_OWNER_PW = "!deepsales@36"

ENTERPRISE_MEMBER_PA20_ACC = "ilsung.baek+pa20@deepsales.com"
ENTERPRISE_MEMBER_PA20_PW = "!deepsales@36"



#딥세일즈 계정 공용 비밀번호
COMMON_PW = "!deepsales@36"

#링크드인 로그인 정보
LINKEDIN_ACCOUNT = "starbictoli@naver.com"
LINKEDIN_PW = "1@qordlftjd"

# 회원가입 계정 - ilsung.baek+pa1@deepsales.com (생성)
#ilsung.baek+pa2@deepsales.com (생성), ilsung.baek+pa3@deepsales.com (생성), ilsung.baek+pa4@deepsales.com (생성)
#ilsung.baek+pa5@deepsales.com (생성), ilsung.baek+pa6@deepsales.com (생성), ilsung.baek+pa7@deepsales.com (생성)
#ilsung.baek+pa8@deepsales.com (생성), ilsung.baek+pa9@deepsales.com (생성), ilsung.baek+pa10@deepsales.com (생성),
#ilsung.baek+pa11@deepsales.com (생성), ilsung.baek+pa12@deepsales.com (생성), ilsung.baek+pa13@deepsales.com (생성)
#ilsung.baek+pa14@deepsales.com (생성), ilsung.baek+pa17@deepsales.com (생성), ilsung.baek+pa23@deepsales.com (생성)
#ilsung.baek+pa24@deepsales.com (생성)
# 아래의 계정은 Enterprise 멤버 소속임
# ilsung.baek+pa20@deepsales.com (생성), ilsung.baek+pa21@deepsales.com (생성), ilsung.baek+pa22@deepsales.com (생성)


# 회원가입 계정 - 유료 계정 전환 내역
# ilsung.baek+pa15@deepsales.com (생성) - Team 계정
# ilsung.baek+pa16@deepsales.com (생성) - Enterprise 계정

#json 설정 (counter)
def read_counter():
    with open("config.json", "r") as f:
        return json.load(f)["counter"]

def write_counter(new_value):
    with open("config.json", "w") as f:
        json.dump({"counter": new_value}, f)
