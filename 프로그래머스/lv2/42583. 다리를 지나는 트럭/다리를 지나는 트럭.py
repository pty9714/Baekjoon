from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    bridge = deque(bridge)
    l = len(truck_weights)
    truck = deque(truck_weights)
    arrive_t = 0
    cnt = 0
    bridge_weight = 0
    while True:
        a = bridge.popleft()
        t = truck.popleft()
        bridge_weight += t - a
        if bridge_weight <= weight:
            bridge.append(t)
            truck.append(0)
            cnt +=1
        else:
            truck.appendleft(t)
            bridge.append(0)
            bridge_weight -= t
            cnt+=1
        if a != 0:
            arrive_t +=1
            if arrive_t == l:
                return cnt