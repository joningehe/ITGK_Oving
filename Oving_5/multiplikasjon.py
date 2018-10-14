
tol_grense = float(input(''))
def tol():
    count = 2
    prev_prod = 0
    prod = 2

    while (prod - prev_prod) > tol_grense:
        prev_prod = prod
        prod *= (1+(1/(count ** 2)))
        count += 1

    return prod, count - 1

print(tol())
