def firstTwoFactorOf(num):
    factors = []
    for i in range(2, num):
        if num%i == 0:
            factors.append(i)
            factors.append(num//i)
            return factors
    return factors

def primeFactorize(num):
    if num == 1 or num == 2 or num == 3:
        return [num]
    compositeNumbers = []
    factors = firstTwoFactorOf(num)
    if len(factors) == 0:
        return factors
    if len(factors) == 1:
        compositeNumbers.extend(factors)
    else:
        firstFactor = factors[0]
        secondFactor = factors[1]

        if len(firstTwoFactorOf(firstFactor)) == 1 or len(firstTwoFactorOf(firstFactor)) == 0:
            compositeNumbers.append(firstFactor)
        else:
            compositeNumbers.extend(primeFactorize(firstFactor))

        if len(firstTwoFactorOf(secondFactor)) == 1 or len(firstTwoFactorOf(secondFactor)) == 0:
            compositeNumbers.append(secondFactor)
        else:
            compositeNumbers.extend(primeFactorize(secondFactor))
    return compositeNumbers

num = 315
print('The prime factors of %d are:' % (num))
print(primeFactorize(num))
