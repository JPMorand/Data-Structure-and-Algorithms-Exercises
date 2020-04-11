from itertools import combinations

def ClosestPair(my_list):
    '''
        This function prepares the data for ClosestPairSolver, which finds
        the closest points in a 2D space using a recursive algorithm.
    '''
        Px = sorted(my_list, key = lambda x: x[0])
        Py = sorted(my_list, key = lambda x: x[1])
        return ClosestPairSolver(Px, Py)

def ClosestPairSolver(Px, Py):
    '''
        This function finds the closest pair of points in a 2D dimension
        space in a recursive form, using euclidian distance.
        It takes as input two copies of the same array of points, one sorted
        by axis 0 (Px), the other by axis 1 (Py).
    '''
    if len(Px)<4: #base case (2 or 3 points, brute force)
        return BruteDist(Px)
    
    Qx = Px[:len(Px)//2]#left-half
    Rx = Px[len(Px)//2:]#right-half
    Qy = []
    Ry = []

    print("Qx: ", Qx)
    print("Rx: ", Rx)

    mid = Px[len(Px)//2][0]
    
    for i in Py:
        if i in Qx:
            Qy.append(i)
        else:
            Ry.append(i)
    print("Qy: ", Qy)
    print("Ry: ", Ry)
    
    p1, q1, d1 = ClosestPairSolver(Qx, Qy)
    p2, q2, d2 = ClosestPairSolver(Rx, Ry)

    delta = min(dist(p1, q1), dist(p2, q2))
    
    p3, q3, d3 = ClosestSplitPair(Px, Py, delta)
    dists = [d1, d2, d3]
    print(dists)
    print(min(filter(lambda x: x is not None, dists)))
    minimum_dist =  min(filter(lambda x: x is not None, dists))
    
    if d1 == minimum_dist:
        return p1, q1, d1
    elif d2 == minimum_dist:
        return p2, q2, d2
    else:
        return p3, q3, d3

def BruteDist(Px):
    best_pair = []
    min_dist = None
    for p,q in combinations(Px, 2):
        if min_dist == None or dist(p, q)<min_dist:
            min_dist = dist(p,q)
            best_pair = [p, q]
    return best_pair[0], best_pair[1], min_dist
    
def ClosestSplitPair(Px, Py, delta):
    '''
        This function is auxiliary to ClosestPair and find the closest
        pair of points between adjacent two sorted arrays.
    '''
    x_m = Px[-1][0]
    best = delta
    best_pair = []
    Sy = [x for x in Py if x[0] >= (x_m - delta) and x[0] <= (x_m + delta)]
    len_Sy = len(Sy)
    
    for i in range(len_Sy-1): #compare each one to the next 7
        for j in range(i+1, min(i+7, len_Sy)):
            p, q = Sy[i], Sy[j]
            dst = dist(p,q)
            if dst < best:
                best_pair = [p,q]
                best = dst
    if best < delta:
        return best_pair[0], best_pair[1], best
    else:
        return None, None, None
    
def dist(x1, x2):
    '''
        This function calculates the Euclidian distance between two pairs of points
    '''
    return ((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2)**(1/2)
