def solution(bridge_length, weight, truck_weights):
    time = 0
    first = sum(truck_weights)
    in_bridge= [0] * bridge_length
    while truck_weights:
        print('in_bridge :', in_bridge, 'time :', time)
        print('truck_weights :', truck_weights)
        print()
        if sum(in_bridge):
            for truck in in_bridge:
                if truck != 0:
                    time += 1
                    if in_bridge.index(truck) == 0:
                        in_bridge.remove(truck)
                        in_bridge.append(0)
                        break
                    else:
                        front = in_bridge.index(truck) - 1
                        del in_bridge[front]
                        in_bridge.append(0)
                        break
        print('in_bridge :', in_bridge, 'time :', time)
        print('truck_weights :', truck_weights)
        print()

        if sum(in_bridge) == 0 and sum(truck_weights) != first:
            time -= 1
        elif sum(in_bridge) != 0 and sum(in_bridge) + truck_weights[0] <= weight:
            time -= 1
        if (truck_weights[0] + sum(in_bridge)) <= weight:
            in_bridge[-1] = truck_weights[0]
            time += 1
            del truck_weights[0]
        print('in_bridge :', in_bridge, 'time :', time)
        print('truck_weights :', truck_weights)
        print()
        print()
        print('truck_weights')
        print()
        print()

    while in_bridge:
        if sum(in_bridge) == 0:
            break
        else:
            for truck in in_bridge:
                if truck != 0:
                    time += 1
                    if in_bridge.index(truck) == 0:
                        in_bridge.remove(truck)
                        in_bridge.append(0)
                        break
                    else:
                        front = in_bridge.index(truck) - 1
                        del in_bridge[front]
                        in_bridge.append(0)
                        break
        print('in_bridge :', in_bridge, 'time :', time)
        print('truck_weights :', truck_weights)
        print()
    return time

list1 = [7,4,5,6]
list2 = [10]
list3 = [10,10,10,10,10,10,10,10,10,10]
# print('final time is',solution(2, 10, list1))
# print('final time is',solution(100, 100, list2))
print('final time is',solution(100, 100, list3))