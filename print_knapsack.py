def print_knapsack(a,i,d, w):
    if i > 0 or d > 0:
        if a[i][d] == a[i-1][d]:
            print_knapsack(a, i-1, d, w)
        else:
            print_knapsack(a,i-1,d-w[i], w)
            print("i =", i)
            
    


def main():
    array = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,4,4,4,4,4,4,4,4,4],[0,0,4,4,7,7,7,7,7,7,7],[0,0,4,6,7,10,10,13,13,13,13],[0,0,4,6,7,10,10,13,13,15,15],[0,0,4,6,7,10,10,13,13,15,17]]
    w = {1: 2, 2: 2, 3: 3, 4: 4, 5: 5}        
    i = 5
    d = 10
    print_knapsack(array, i, d, w)
    
    


main()