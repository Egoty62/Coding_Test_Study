# numbers 안에 있는 원소들 중 두 개를 골라서 곱한 값을 리스트로 만들고, max() 사용

def solution(numbers):
    answer = 0 - abs(sorted(numbers)[-1] * sorted(numbers)[-2])
    for i in range(0, len(numbers) - 1) :
        for j in range(i + 1, len(numbers)) :
            a = numbers[i] * numbers[j]
            if answer < a :
                answer = a
    return answer

def solution2(numbers):
    return max([numbers[i] * numbers[j] for i in range(0, len(numbers) -1) for j in range(i + 1, len(numbers))])