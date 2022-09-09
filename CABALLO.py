list_1 = [6,8]
list_2 = [7,9]
list_3 = [4,8]
list_4 = [3,9,0]
list_6 = [1,7,0]
list_7 = [2,6]
list_8 = [1,3]
list_9 = [2,4]
list_0 = [4,6]
dicc = [list_0, list_1, list_2, list_3, list_4, list_6, list_7, list_8, list_9]
def movimientos(n):
    p = 0
    for i in range(len(dicc)):
        k = i
        if n == 1:
                p = p + len(dicc[i])
        elif n == 2:
            for j in range(len(dicc[i])):
                m = 0
                while m < n-1:
                    if dicc[k][j] == 1:
                        k = 1
                    elif dicc[k][j] == 2:
                        k = 2
                    elif dicc[k][j] == 3:
                        k = 3
                    elif dicc[k][j] == 4:
                        k = 4
                    elif dicc[k][j] == 6:
                        k = 5
                    elif dicc[k][j] == 7:
                        k = 6
                    elif dicc[k][j] == 8:
                        k = 7
                    elif dicc[k][j] == 9:
                        k = 8
                    elif dicc[k][j] == 0:
                        k = 0
                    m = m+1
                if m == n-1:
                    p = p + len(dicc[k])
                    k = i                    
    print(p)
        
movimientos(3)