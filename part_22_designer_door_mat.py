def design_door(N,M):
    sign = '.|.'
    n = int((N-1)/2)
    m = int((M-3)/2)

    
    for i in range(1,n+1):
       print(((sign*(i-1)).rjust(m,'-'))+sign+((sign*(i-1)).ljust(m,'-')))

    for i in range(1):
        print('WELCOME'.center(M,'-'))
    
    for i in reversed(range(1,n+1)):
       print(((sign*(i-1)).rjust(m,'-'))+sign+((sign*(i-1)).ljust(m,'-')))
    

N, M = map(int, input().split())
design_door(N,M)
