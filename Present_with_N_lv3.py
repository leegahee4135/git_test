def solution(N,number):

    # 기저 상태 만들기
    # S[i] 는 N을 i+1번 써서 만들 수 있는 숫자들의 집합임
    S = [ set() for i in range(8)]
    for i in range(8):
        S[i].add(int(str(N)*(i+1)))

    if N == number:
        return 1

    for i in range(8):
        for j in range(i):
            for k in S[j]:
                for l in S[i-j-1]:
                    S[i].add(k+l)
                    S[i].add(k-l)
                    S[i].add(k*l)
                    if l != 0:
                        S[i].add(k/l)
        if number in S[i]:
            return i+1
    return -1

N = 2
number = 11

answer = solution(N, number)
print(answer)