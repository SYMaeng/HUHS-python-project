#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
site = "http://naver.com"
site1 = site[7:] #규칙1
site2 = site1[:5] #규칙2
password = site2[:3]+str(len(site2))+str(site2.count("e"))+"!"
print(f"생성된 {site2}의 비밀번호 : {password}")