import numpy as np

import numpy as np


def solution(m, n, puddles):
    # DP 테이블 초기화
    S = np.zeros((n + 1, m + 1), dtype=int)

    # 시작점 설정
    S[1][1] = 1

    # 물웅덩이 처리
    for puddle in puddles:
        x, y = puddle
        S[y][x] = -1  # 물웅덩이 위치에 -1 설정

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i][j] == -1:  # 물웅덩이는 건너뛰기
                continue

            # 위쪽에서 오는 경우
            if i > 1 and S[i - 1][j] != -1:
                S[i][j] += S[i - 1][j]

            # 왼쪽에서 오는 경우
            if j > 1 and S[i][j - 1] != -1:
                S[i][j] += S[i][j - 1]

            S[i][j] %= 1_000_000_007

    # 결과는 학교 위치의 경로 수
    return int(S[n][m])  # m x n의 마지막 지점 반환


m = 4
n = 3
puddles = [[2, 2]]

answer = solution(m, n, puddles)

print(answer)