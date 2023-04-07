# 첫 chicken의 수에 맞춰 coupon 증가
    # coupon 10장 당 result +1, 나머지 coupon은 추가 coupon에 +
        # coupon으로 증가한 result 만큼 추가 coupon +
            # 추가 coupon 10장 당 result +1, 나머지 coupon은 추가 coupon에 +
                # 추가 coupon으로 증가한 result 만큼 추가 coupon +
                    # 추가 coupon의 값이 10 미만으로 떨어질 때 까지 반복

def solution(chicken):
    result = 0
    coupon = chicken
    result += coupon // 10
    additional_coupon = result + coupon % 10 
    while additional_coupon >= 10 :
        result += additional_coupon // 10
        additional_coupon = additional_coupon // 10 + additional_coupon % 10
    return result