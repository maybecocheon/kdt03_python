print("hello, world!")
# 1 2 3 4 5
data = input("입력: ")
print(type(data))  # input 함수는 항상 문자열로 입력 받음

# 입력받은 값 전부 더하려면?
# 1. 공백을 기준으로 분리된 단어들을 리스트로 저장
data = data.split(" ")
print(data)

# 2. 정수로 변환하여 리스트에 저장
data = list(map(int, data))
print(data)

# 3. 정수 합계
print(sum(data))


# 혹은 각 변수를 따로 저장
a, b, c, d, e = map(int, input("입력: ").split(" "))
print(a + b + c + d + e)