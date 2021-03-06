"""
문제) 왕실의 나이트
행복 왕국의 왕실 정원은 체스판과 같은 8x8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
이처럼 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
이때 왕실의 정원에서 행 위치를 표한할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.

입력 조건)
첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
입력 문자는 a1처럼 열과 행으로 이뤄진다.

출력 조건)
첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""

"""
아이디어)
상하좌우 문제의 응용,,,
가로축 x, 세로축 y
갈 수 있는 경로 최대 8가지
   (x ,  y)
LU (-2, -1)
LD (-2, +1)
UL (-1, -2)
UR (+1, -2)
RU (+2, -1)
RD (+2, +1)
DL (-1, +2)
DR (+1, +2)
"""

# x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# y = [1, 2, 3, 4, 5, 6, 7, 8]
dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, -2, -2, -1, 1, 2, 2]

location = list(input())
currentX = location[0]
currentY = location[1]
ans = 0

for i in range(len(dx)):
    x = (ord(currentX) - 96) + dx[i]  # 아스키코드 변환
    y = int(currentY) + dy[i]
    print(x, y)

    if x > 8 or x < 1 or y > 8 or y < 1:
        continue

    ans += 1
