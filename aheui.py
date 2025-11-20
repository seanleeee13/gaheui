"""
=== 문법 ===
 * 초성
  * ㄱ 묶음
   * ㅇ, ㄱ, ㅋ: 아무 일도 하지 않는다.[* ㅇ은 [[Null]]로 정의되어 있지만 ㄱ과 ㅋ은 아예 정의 자체가 없다.]
   * ㅎ: 프로그램을 종료한다. 종료 시 선택된 저장 공간에 값이 하나 이상 남아 있다면 하나만 뽑아내 운영체제에 반환하고 비어있다면 0을 반환한다.
  * ㄷ 묶음 - 연산
   * ㄷ: 덧셈
   * ㅌ: 뺄셈
   * ㄸ: 곱셈
   * ㄴ: 나눗셈
   * ㄹ: [[나머지#s-2.3|나머지 연산]] (modulo)
   * 모두 공통적으로 저장공간에서 두 값을 뽑아낸 다음 둘을 연산한 값을 저장공간에 저장한다. 순서가 있는 연산자(ㅌ, ㄴ, ㄹ)의 경우 나중에 꺼낸 값이 연산자의 왼쪽, 먼저 꺼낸 값이 오른쪽에 온다. 만약 저장공간에 남은 값이 한 개 이하라면 진행방향을 바꾼다. 자세한 동작은 후술.
  * ㅁ 묶음 - 저장공간
   * ㅁ: 뽑기. 현재 선택된 저장공간에서 자료 구조의 형태에 맞게 하나 꺼내온다.
    * 종성으로 ㅇ이 오는 경우: 값을 숫자 형식으로 출력한다.
    * 종성으로 ㅎ이 오는 경우: 해당하는 유니코드의 문자를 출력한다.
    * 나머지 종성이면 뽑아내서 그냥 버린다.
   * ㅂ: 넣기. 현재 선택된 저장공간에 값을 하나 넣는다.
    * 종성으로 ㅇ이 오는 경우: 값을 숫자 형식으로 입력받는다. 즉 '8'은 8로 저장된다. 공백이나 개행이 나올 때까지 숫자를 읽어들이며, 앞에 -가 존재하는 경우 음수로 취급한다.
    * 종성으로 ㅎ이 오는 경우: 값을 문자 형식으로 입력받는다. 즉 '8'은 56([[아스키 코드]] 기준)으로 저장된다.
    * 나머지의 경우, 종성의 획 수가 집어넣을 값(리터럴)이 된다. 즉 받침 'ㅅ'는 2로, 받침 'ㄹ'는 5가 된다. 이때 1을 곧바로 넣을 수가 없는데, 3 - 2(받반타, 밬밧타 등)를 하면 된다. 종성이 없으면(바, 보 등) 0으로 평가한다. 전체 목록은 [[#s-2.2.1|참고 사항]] 문단의 '종성별 선의 수' 참고.
   * ㅃ: 중복. 현재 선택된 저장공간의 종류에 따라 동작이 달라진다.
    * 스택이라면 맨 위의 값을 그 값 위에 하나 더 집어넣는다.
    * 큐라면 맨 앞의 값을 앞에 하나 더 덧붙인다. 뒤의 값이 아님에 주의하자.
    * 통로라면 가장 마지막으로 보낸 값을 한 번 더 보낸다.
   * ㅍ: 바꿔치기. 
    * 스택이라면 맨 위 값과 그 바로 아래 값의 위치를 서로 바꾼다.
    * 큐라면 맨 앞의 값과 그 바로 뒤 값을 바꾼다.
    * 통로일 때의 동작은 미정.
    * 만약 저장공간에 남은 값이 한 개 이하라면 진행방향을 바꾼다.
  * ㅅ 묶음 - 제어
   * ㅅ: 선택. 종성을 통해 상술한 자료구조에서 선택할 수 있다.
    * 종성이 없다면(사 등) 기본으로 선택되는 스택으로 되돌아온다.
   * ㅆ: 이동. 지금 저장공간에서 값 하나를 뽑아내서 받침이 나타내는 저장공간에 그 값을 집어넣는다.
    * 만약 현재 선택된 저장공간에 값이 하나도 없다면 진행방향을 바꾼다.
   * ㅈ: 비교. 저장공간에서 값 두 개를 뽑아 내서 비교한다. 나중에 뽑아낸 값이 먼저 뽑아낸 값보다 더 크거나 같으면 1을, 아니면 0을 지금 저장공간에 집어넣는다.
   * ㅊ: 조건. 저장공간에서 값 하나를 뽑아내서 그 값이 0이 아니면 진행해야 할 방향대로, 0이면 그 반대 방향대로 간다.
 * 중성
  * ㅏ,ㅓ,ㅗ,ㅜ: 중성의 방향이 커서의 방향이다.
  * ㅑ,ㅕ,ㅛ,ㅠ: 위와 같으나 2칸 옮긴다.
   * 만약 끝에 다다르면 반대쪽으로 이동하되, 1칸으로 취급한다. 즉
    || 악 || 안 || 야 ||
    의 경우 '야' 에서 끝에 다다르면 첫 열로 되돌아가지만, '안'이 아닌 '악'을 실행시킨다. 따라서 '야'를 '아'로 바꿔도 결과는 같다.
  * ㅣ,ㅡ,ㅢ: ㅣ는 커서가 세로 방향으로 들어오면 그대로, 가로로 돌아오면 방향을 뒤집는다. ㅡ는 그 반대다. ㅢ는 어느 방향이든 방향을 뒤집는다.
  * 나머지 중성(ㅘㅚㅐㅙㅝㅟㅔㅞ)은 정의되지 않았다.
 * 이외의 종성은 기능 없음.
 * 한글이 아닌 모든 글자는 빈칸으로 처리된다. 즉 무시된다.
  * '한글'을 가(U+AC00) 이상 힣(U+D7A3) 이하로만 정의하는 구현체도 있고, ㄱ~ㅎ, ㅏ~ㅣ(U+3131 ~ U+3163)등 한글 낱자도 포함하는 구현체도 존재한다. 아희 명세에 따르면 공식적으로는 U+AC00~U+D7A3 사이의 문자만 한글로 취급한다. [[https://aheui.readthedocs.io/ko/latest/specs.en.html|참고]]
"""

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
        k = False
        if cursor[0] < 0:
            cursor[0] = len(code) - 1
            k = True
        if cursor[1] < 0:
            cursor[1] = len(code[cursor[0]]) - 1
            k = True
        if cursor[0] >= len(code):
            cursor[0] = 0
            k = True
        if cursor[1] >= len(code[cursor[0]]):
            cursor[1] = 0
            k = True
        if not k:
            try:
                code[cursor[0]][cursor[1]]
            except:
                if direction[0]:
                    cursor[0] = 0
                else:
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