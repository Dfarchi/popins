
def isWinner(p1, p2):
    pv1 = 0
    pv2 = 0
    for t, (p1_v, p2_v) in enumerate(zip(p1, p2)):
        if p1[t - 1] == 10:
            pv1 += p1_v * 2
        elif p1[t - 1] != 10:
            pv1 += p1_v
        elif p2[t - 1] == 10:
            pv2 += p2_v * 2
        elif p2[t - 1] != 10:
            pv2 += p2_v
    if pv1 > pv2:
        return 1
    elif pv1 < pv2:
        return 2
    else:
        return 0



isWinner([3,5,7,6],[8,10,10,2])