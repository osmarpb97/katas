def tickets(people):
    caja = {
        25: 0,
        50: 0,
        100: 0
    }
    cambio = []
    for element in people:
        caja[element] += 1          
        if element == 50:
            caja[25] -= 1
        if element == 100:
            if caja[50]:
                caja[50] -= 1
            else:
                caja[25] -= 2
            caja[25] -= 1
        cambio.append(caja[25]>=0)
    return "YES" if all(cambio) else "NO"     

