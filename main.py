# Name: 류동우
# Date: 2022-04-19

MAX_ERROR = 1e-5
print('Welcome to interactive calculator')

end_of_input = False

while not end_of_input:

    expression = input('Enter mathematical expression : ')

    for char in '() ':
        expression = expression.replace(char, '')  # remove parentheses, spaces

    if expression == 'q':
        end_of_input = True                        # 프로그램 종료
        continue                                   # skip below codes

    elif '+' in expression:
        
        n1, n2 = expression.split('+')
        a = float(n1)
        b = float(n2)
        print(format(a + b, '.3f'))
    
    elif '*' in expression:
        
        n1, n2 = expression.split('*')
        a = float(n1)
        b = float(n2)
        print(format(a*b, '.3f'))
        
    elif '//' in expression:
        
        n1, n2 = expression.split('//')
        a = int(n1)
        b = int(n2)
        if b is 0:
            print("Division by zero error")
            continue
        print(a//b)
        
    elif '/' in expression:
        
        n1, n2 = expression.split('/')
        a = float(n1)
        b = float(n2)
        try:
            print(format(a/b, '.3f'))
        except ZeroDivisionError:
            print("Division by zero error")
            continue
        
    elif '%' in expression:
        
        n1, n2 = expression.split('%')
        a = int(n1)
        b = int(n2)
        if b is 0:
            print("Division by zero error")
            continue
        print(a%b)
        
    elif '^' in expression:
        
        n1, n2 = expression.split('^')
        a = int(n1)
        b = int(n2)
        print(format(a**b, '.3f'))
        
    elif 'P' in expression:
        
        n1, n2 = expression.split('P')
        a = int(n1)
        b = int(n2)
        
        result = 1
        for i in range(a-b+1, a+1):
            result *= i
            
        print(result)
        
    elif 'C' in expression:
        
        n1, n2 = expression.split('C')
        a = int(n1)
        b = int(n2)
        
        result = 1
        for i in range(a-b+1, a+1):                  #aPb를 result에 곱함
            result *= i
        for j in range(1, b+1):                      #result를 b!로 나눔
            result /= j
        result = int(result)                         #나눗셈으로 인해 실수형이 되어버린 result를 정수형으로 변환
        
        print(result)
        
        
    elif 'r' in expression:
        n1 = expression.replace('r', '')
        a = float(n1)
        
        root = a
        
        while abs(root - (a/root + root)/2) > MAX_ERROR:
            root = (a/root + root)/2
        
        print(format(root, '.3f'))


    elif 'g' in expression:
        n1, n2 = expression.replace('g', '').split(',')
        a = int(n1)
        b = int(n2)
        r = a%b
        
        while r is not 0:
            a = b
            b = r
            r = a%b
            
        print(b)
    
    elif 'b' in expression:
        n1 = expression.replace('b', '')
        a = int(n1)
        result = str()
        
        while True:
            result = str(a%2) + result
            a = a//2
            if a is 0:
                break
            
        print(result)
        
    elif 'd' in expression:
        n1 = expression.replace('d', '')
        result = 0
        
        for i in range(len(n1)):
            result += (2**i)*(int(n1[-i-1]))
            
        print(result)
        
    elif 'e' in expression:
        
        
        '''
        a(n) = 1/n!
        s(n) = a(0) + a(1) + ... + a(n-1) + a(n)
        error(n) = s(n+1) - s(n) = a(n+1) = a(n) / (n + 1)
        
        '''
        
        n = 0
        a_n = 1                            # a(0) = 1/0! = 1
        s_n = 1                            # s(0) = a(0) = 1
        error_n = 1                        # error(0) = s(1) - s(0) = 1

        while error_n > MAX_ERROR:
            n += 1
            a_n /= n
            s_n += a_n
            error_n = a_n / (n+1)
            
        print(format(s_n, '.3f'))
        
    elif 'pi' in expression:
        
        
        '''
        a(n) = (-1)^n / (2n + 1)
        s(n) = a(0) + a(1) + ... + a(n-1) + a(n)
        error(n) = | s(n+1) - s(n) | = | a(n+1) | = | (-1)^(n + 1) / (2(n + 1) + 1) | = 1 / (2n + 3)
        
        '''
        
        n = 0
        a_n = 1                            # a(0) = 1
        s_n = 1                            # s(0) = a(0) = 1
        error_n = 1/3                      # error(0) = | s(1) - s(0) | = 1/3
        
        while error_n > MAX_ERROR:
            n += 1
            a_n = (-1)**n / (2*n + 1)
            s_n += a_n
            error_n = 1 / (2*n + 3)
            
        pi = 4 * s_n
            
        print(format(pi, '.3f'))
        
    
    #####################################################
    ################### Do not change ###################
    #####################################################

    elif '-' in expression:
        try:
            if '--' in expression:
                n1, n2 = expression.split('--')
                a = float(n1)
                b = - float(n2)
                
            else:
                if expression[0] != '-':
                    n1, n2 = expression.split('-')
                    a = float(n1)
                    b = float(n2)
            
                else:
                    _, n1, n2 = expression.split('-')
                    a = -float(n1)
                    b = float(n2)
            
            print(format(a - b, '.3f'))

        except:
            print("Unknown expression")

    else:
        print("Unknown expression")

    #####################################################
    ################### Do not change ###################
    #####################################################
        
