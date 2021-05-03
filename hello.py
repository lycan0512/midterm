승리 = {
    '가위': '보',
    '바위': '가위',
    '보': '바위'
}
def start(mine, yours):
    result ='0'
    if mine == yours:
        result = '무승부'
        return result
    elif 승리[mine] == yours:
        result = '승리'
        return result
    else:
        result = '패배'
        return result


while 1:
    me = input('가위, 바위, 보 중 선택 종료는 "종료"를 입력하세요   ')
    if me == '종료':
        break
    elif (me != '가위') and (me != '바위') and (me !='보'):
        print('가위 바위 보를 다시 입력 해주세요')
        continue
    else:
        import random
        list = ['가위', '바위', '보']
        you = random.choice(list)
        print('{} 나:{} 컴퓨터:{}'.format(start(me, you), me, you))
print('프로그램 종료')
