# 정렬된 리스트 하나 만들고 index(), 리스트 컴프리헨션 사용하면 쉽게 풀릴 것 같았지만...
# 리스트 컴프리헨션 한 줄로 표현해보고 싶었습니다...

# score에 있는 리스트의 원소를 더한 값이 원소가 되는 리스트 a를 생성
    # a를 sorted(reverse = True)하고, enumerate를 하여 등수를 구별한 새로운 이차원 리스트를 만듦
        # 이차원 리스트를 sorted(key = lambda x : (x[1], x[0]), reverse = True)로 다시 정렬
            # 그 후 딕셔너리를 만들고, keys, values를 서로 바꿈 (동점 고려)
                # 이 딕셔너리에 키의 값을 이용해서 등수를 호출 (호출된 값에 +1 해줘야 함)

def solution(score):
    return [{v : k for k, v in dict(sorted(enumerate(sorted([i + j for i, j in score], reverse = True)), key = lambda x : (x[1], x[0]), reverse = True)).items()}[i] + 1 for i in ([j + k for j, k in score])]