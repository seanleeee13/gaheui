import sys

def run(code):
    code = list(map(list, code.split("\n")))
    cursor = [0, 0]
    direction = [1, 0]
    a = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", 
        "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    b = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", 
        "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
    c = [" ", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", 
        "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    cnum = {" ": 0, "ㄱ": 2, "ㄴ": 2, "ㅅ": 2, "ㄷ": 3, "ㅈ": 3, "ㅋ": 3, "ㅁ": 4, "ㅂ": 4, "ㅊ": 4, \
        "ㅌ": 4, "ㅍ": 4, "ㄲ": 4, "ㄳ": 4, "ㅆ": 4, "ㄹ": 5, "ㄵ": 5, "ㄶ": 5, "ㅄ": 6, "ㄺ": 7, \
        "ㄽ": 7, "ㅀ": 8, "ㄻ": 9, "ㄼ": 9, "ㄾ": 9, "ㄿ": 9}
    arr = {i: [] for i in c}
    sel = " "
    while True:
        try:
            t = ord(code[cursor[0]][cursor[1]]) - 44032
        except:
            pass
        else:
            if ord('가') <= ord(code[cursor[0]][cursor[1]]) <= ord('힣'):
                p = a[t // 21 // 28]
                q = b[t % 588 // 28]
                r = c[t % 28]
                rev = False
                if p == "ㅎ":
                    if len(arr[sel]) < 2:
                        return 0
                    else:
                        return arr[sel][0 if sel in "ㅇㅎ" else -1]
                elif p == "ㄷ":
                    if len(arr[sel]) < 2:
                        rev = True
                    else:
                        a1 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        a2 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        arr[sel].append(a2 + a1)
                elif p == "ㅌ":
                    if len(arr[sel]) < 2:
                        rev = True
                    else:
                        a1 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        a2 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        arr[sel].append(a2 - a1)
                elif p == "ㄸ":
                    if len(arr[sel]) < 2:
                        rev = True
                    else:
                        a1 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        a2 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        arr[sel].append(a2 * a1)
                elif p == "ㄴ":
                    if len(arr[sel]) < 2:
                        rev = True
                    else:
                        a1 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        a2 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        arr[sel].append(a2 // a1)
                elif p == "ㄹ":
                    if len(arr[sel]) < 2:
                        rev = True
                    else:
                        a1 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        a2 = arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                        arr[sel].append(a2 % a1)
                elif p == "ㅁ":
                    if len(arr[sel]) < 1:
                        rev = True
                    else:
                        if r == "ㅇ":
                            print(arr[sel].pop(0 if sel in "ㅇㅎ" else -1), end="")
                        elif r == "ㅎ":
                            print(chr(arr[sel].pop(0 if sel in "ㅇㅎ" else -1)), end="")
                        else:
                            arr[sel].pop(0 if sel in "ㅇㅎ" else -1)
                elif p == "ㅂ":
                    if r == "ㅇ":
                        n = ""
                        while True:
                            ch = sys.stdin.read(1)
                            if not ch:
                                break
                            if ch in "-0123456789":
                                n += ch
                            else:
                                break
                        n = int(n)
                        arr[sel].append(n)
                    elif r == "ㅎ":
                        ch = sys.stdin.read(1)
                        arr[sel].append(ord(ch))
                    else:
                        arr[sel].append(cnum[r])
                elif p == "ㅃ":
                    if len(arr[sel]) < 1:
                        rev = True
                    else:
                        if sel in "ㅇㅎ":
                            arr[sel].insert(0, arr[sel][0])
                        else:
                            arr[sel].append(arr[sel][-1])
                elif p == "ㅍ":
                    if len(arr[sel]) < 2:
                        rev = True
                    else:
                        if sel in "ㅇㅎ":
                            temp = arr[sel][0]
                            arr[sel][0] = arr[sel][1]
                            arr[sel][1] = temp
                        else:
                            temp = arr[sel][-1]
                            arr[sel][-1] = arr[sel][-2]
                            arr[sel][-2] = temp
                elif p == "ㅅ":
                    sel = r
                elif p == "ㅆ":
                    if len(arr[sel]) < 1:
                        rev = True
                    else:
                        arr[r].append(arr[sel].pop(0 if sel in "ㅇㅎ" else -1))
                elif p == "ㅈ":
                    if len(arr[sel]) < 2:
                        rev = True
                    else:
                        if arr[sel].pop(0 if sel in "ㅇㅎ" else -1) <= arr[sel].pop(0 if sel in "ㅇㅎ" else -1):
                            arr[sel].append(1)
                        else:
                            arr[sel].append(0)
                elif p == "ㅊ":
                    if len(arr[sel]) < 1:
                        rev = True
                    else:
                        if arr[sel].pop(0 if sel in "ㅇㅎ" else -1) == 0:
                            rev = True
                if q == "ㅏ":
                    direction = [0, 1]
                elif q == "ㅑ":
                    direction = [0, 2]
                elif q == "ㅓ":
                    direction = [0, -1]
                elif q == "ㅕ":
                    direction = [0, -2]
                elif q == "ㅗ":
                    direction = [-1, 0]
                elif q == "ㅛ":
                    direction = [-2, 0]
                elif q == "ㅜ":
                    direction = [1, 0]
                elif q == "ㅠ":
                    direction = [2, 0]
                elif q == "ㅡ":
                    direction = [-direction[0], direction[1]]
                elif q == "ㅣ":
                    direction = [direction[0], -direction[1]]
                elif q == "ㅢ":
                    direction = [-direction[0], -direction[1]]
                if rev:
                    direction = [-direction[0], -direction[1]]
        cursor[0] += direction[0]
        cursor[1] += direction[1]
        if cursor[0] < 0 and direction[0] < 0:
            cursor[0] = len(code) - 1
        if cursor[1] < 0 and direction[1] < 0:
            cursor[1] = len(code[cursor[0]]) - 1
        if cursor[0] >= len(code) and direction[0] > 0:
            cursor[0] = 0
        if cursor[1] >= len(code[cursor[0]]) and direction[1] > 0:
            cursor[1] = 0

run("""
숛숛멍빠빠싼싼산뱐뺘뉴뭏
벊뿌따또볔번벐석떠쇇볏
숟멓묳쑤써순떠뿌처모두샊
빠뿌몽쉐쎼뿌솨쀄토더북무
쑦써뫃멍솎써쏘썪밣봇투무
삭빠쒺섈뷐벳타대뽀숟슏셜
무차쇡뼤썎살밪박토받반투
희토되벅뱷쐬쏶뺴뺴뻐번뎌
    """)