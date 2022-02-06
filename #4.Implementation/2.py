"""
문제)
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도
포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
- 00시 00분 03초
- 00시 13분 30초
반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.
- 00시 02분 55초
- 01시 27분 45초

입력 조건)
첫째 줄에 정수 N이 입력된다. (0<=N<=23)

출력 조건)
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
"""

"""
아이디어)
xx시 xx분 xx초를 6자리 문자열로 생각하자.
"""

n = int(input())
ans = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                ans += 1

print(ans)

# 문제 분석
# 완전 탐색(Brute Forcing)문제이다.
#
# 완전 탐색 알고리즘은 가능한 경우의 수를 모두 검사해보는 탐색 방법이다.
# 일반적으로 완전 탐색 알고리즘은 비효율적인 시간 복잡도를 가지고 있으므로 데이터 개수가 큰 경우에 정상적으로 동작하지 않을 수 있다.
# 그래서 일반적으로 알고리즘 문제를 풀 때는 확인(탐색)해야 할 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색을 사용하면 적절하다.
#
# 위 문제의 경우 전체 경우의 수가 24x60x60 = 86,400(가지)로 완전 탐색을 사용하여 문제를 풀어도 된다.
