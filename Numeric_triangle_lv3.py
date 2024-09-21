def solution(triangle):
    answer = 0

    H = len(triangle)
    num = len(triangle[H-1])

    S = [[] for i in range(H)]
    for i in range(H):
        for j in range(i+1):
            S[i].append(set())

    for i in range(num):
        S[H-1][i].add(0)

    for i in range(H-1, 0, -1):
        num = len(triangle[i])
        for j in range(num):

            # 아래 부분을 추가하지 않아서 시간초과 & 효율성빵점 결과 나옴
            # 삼각형에서의 현재 위치에서 가능한 합들을 모두 남기지 않고 최대값만 남겨야 계산 경우의 수가 줄어서 테스트 통과 가능함
            max_val = max(S[i][j])
            S[i][j].clear()
            S[i][j].add(max_val)

            for k in S[i][j]:
                if j == 0:
                    S[i-1][0].add(k + triangle[i][j])
                elif j == num - 1:
                    S[i-1][j-1].add(k + triangle[i][j])
                else:
                    S[i-1][j].add(k + triangle[i][j])
                    S[i-1][j-1].add(k + triangle[i][j])

    answer = max(S[0][0]) + triangle[0][0]

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
result = solution(triangle)

print(result)


#------------------ chat GPT 의 해설 -------------------#
# 나처럼 집합을 써서 메모리를 잡아먹지 않고 그냥 triangle의 값을 최대값으로 갱신시키는 방법을 적용함
def solution_chatGPT(triangle):
    # 삼각형의 크기
    n = len(triangle)

    # 아래쪽에서부터 위로 올라가면서 DP 계산
    for i in range(n - 2, -1, -1):  # 밑에서 두 번째 줄부터 위로 이동
        for j in range(i + 1):  # 현재 줄의 각 요소에 대해
            # 아래 행의 두 값 중 큰 값을 선택하여 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # 최종적으로 꼭대기(0, 0)에 최대 경로 합이 저장됨
    return triangle[0][0]