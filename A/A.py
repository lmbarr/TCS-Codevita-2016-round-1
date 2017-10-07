N = 20
n = range(sum(range(N+1)))
k = 0
num_serie_actual = 6
import sys
for i in range(1, N+1):
    print (N-1)*' ',
    for j in range(i):
        sys.stdout.write('{:05d}'.format(num_serie_actual)+' ')
        #sys.stdout.flush()
        num_serie_actual = num_serie_actual + 22 + n[k]*16
        k += 1
    N -= 1
    print;
    
