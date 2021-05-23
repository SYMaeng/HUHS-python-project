def std_weight(height, gender): #키는 m 단위, 성별은 남자 또는 여자
    """ 표준 체중을 구하는 프로그램입니다. """
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21

height = int(input('키를 입력해 주세요. '))
gender = input('남자? 여자? ')
weight = round(std_weight(height/100, gender), 2)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")