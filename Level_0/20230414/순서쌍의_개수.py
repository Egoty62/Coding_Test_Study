# 순서쌍 : 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍
# 1, n을 포함한 n의 약수의 개수를 구하면 됨

def solution(n):
    return len([i for i in range(1, n + 1) if n % i == 0])