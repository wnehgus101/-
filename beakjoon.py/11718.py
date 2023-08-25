while True:
    try:
        print(input())
    except EOFError:
        break
    
# 문제의 핵심은 입력값이 주어지지 않은 상태애서 문자열을 출력하는 것이다. 따라서 EOF를 떠올렸고 try-except구문이 필요하다고 생각했다.