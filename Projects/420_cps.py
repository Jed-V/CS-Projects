# 420. Strong Password
class Solution:
    def strongPasswordChecker(password):
        errorCount  = 0
        passLenLow = False
        passLenHigh = False
        passUpCase = False
        passlowCase = False
        passDigit = False
        passRepeat = False

        if len(password) >= 6:
            passLenLow = True

        else:
            errorCheck += abs(6-len(password))
            
        if len(password) <= 20:
            passLenHigh = True

        else:
            errorCount += abs(20- len(password))

        for i in password:
            if i.isupper():
                passUpcase = True
        if 
