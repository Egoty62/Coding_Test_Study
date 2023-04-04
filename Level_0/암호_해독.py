def solution(cipher, code):
    if len(cipher) % code == 0 :
        return cipher[code-1:-1:code] + cipher[-1]
    else :
        return cipher[code-1:-1:code] 
    
    # return cipher[code-1::code]