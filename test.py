# 구구단 2단을 출력하는 함수 만들기
def gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

# 2단 출력
gugudan(2)