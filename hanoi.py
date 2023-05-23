import time

start_time1 = time.time() # 시작시간 체크
def hano(n, n1, n2, n3): # n : 입력 / n1: 출발기둥 / n2 : 도착기둥 / n3 : 보조기둥
    if n == 1: # 만약 n이 1일경우
        print(f"{n1}번 원반 옮기기: 기둥 {n1} -> 기둥 {n2}") # 출발기둥 -> 도착기둥 출력
    else: # 그게아니라면
        hano(n - 1, n1, n3, n2) # 출발 기둥에서 보조기둥으로 n-1개 원반을 옮김 -> 재귀호출을 통해 처리

        print(f"{n}번째 행동 - {n}번 원반 옮기기: 기둥 {n1} -> 기둥 {n2}") # 남은 1개의 원반을 출발 기둥에서 도착기둥으로 옮김

        hano(n - 1, n3, n2, n1) # 보조기둥에 옮겨둔 n-1개의 원반을 도착기둥으로 최종적으로 옮김

n = int(input("원반의 개수(n)는? : "))
print() # 출력

hano(n, 1, 3, 2) # 하노이 함수 호출 -> 출발을 1, 도착을 3, 보조를 2번으로 지정
end_time1 = time.time()
time1 = end_time1 - start_time1 #종료시간 - 시작시간 = 걸린시간
print("재귀함수 성공") # 끝
print(f"소요 시간: {time1}초")  # 소요시간출력

#======================================================
start_time2 = time.time() # 시작시간체크
def hanoi(n): 
    moves = []  # 값을 저장할 리스트

    def move(q1, q2, q3, n): # q1 : 시작기둥 / q2 : 종료기둥 / q3 : 보조기둥
        if n == 1: # 만약 n이 1일경우
            moves.append((q1, q2))  # 원반을 q1에서 q2로 옮기는 행동값을 저장
        else:
            move(q1, q3, q2, n-1)  # n-1개의 원반을 q1에서 q3로 옮김
            moves.append((q1, q2))  # 남은 1개의 원반을 q1에서 q2로 옮기는 행동값 저장
            move(q3, q2, q1, n-1)  # q3에 있는 원반을 q2로 옮김

    move(1, 3, 2, n)  # 하노이탑 움직임 계산

    return moves 
print() # 프린트

moves = hanoi(n)  # hanoi(n) 반환값 저장

end_time2 = time.time() #종료시간
time2 = end_time2 - start_time2 # 종료시간 - 시작시간 = 소요시간

print("행동 :") #출력
for i, move in enumerate(moves): # 이것도출력
    print(f"{i+1}번째 행동 - {move[0]}번 원반 옮기기: 기둥 {move[0]} -> 기둥 {move[1]}") # 

print("비재귀 성공") # 끝
print(f"소요 시간: {time2}초") # 소요시간
