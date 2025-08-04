
def calcular_quota(queda, mesos, rate):
    l, r = 0, queda
    its = 30
    for _ in range(its):
        quota = (l + r) / 2
        cq = queda
        for _ in range(mesos):
            cq = (cq - quota)*(1 + rate/12)
            if cq < 0:
                r = quota
        if cq >= 0:
            l = quota
    return l

def calcular_quota2(queda, anys, rate):
    # L'interès s'actualitza cada any, no cada mes
    # L'aproximació és pitjor i s'obté una quota menor
    l, r = 0, queda
    its = 30
    for _ in range(its):
        quota = (l + r) / 2
        cq = queda
        for _ in range(anys):
            cq = (cq - quota)*(1 + rate)
            if cq < 0:
                r = quota
        if cq >= 0:
            l = quota
    return l/12

print(calcular_quota(167000, 12*30-21, 0.0375))
print(calcular_quota(167000, 12*30-21, 0.0145))