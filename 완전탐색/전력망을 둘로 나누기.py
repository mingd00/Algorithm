def solution(n, wires):
    values = []
    for i in range(len(wires)):
        wire = wires[:i] + wires[i+1:]
        wset = set(wire[0])
        previous = set()
        while wset != previous:
            previous = wset.copy()
            for i in range(1, len(wire)):
                # wset에 값이 있을 때
                if set(wire[i]) & wset:
                    wset.update(wire[i])

        values.append(abs(2*len(wset) - n))
                
    return min(values)

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))