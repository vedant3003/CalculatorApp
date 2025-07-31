def solve():
    t = int(input())
    for _ in range(t):
        a, b, k = map(int, input().split())
        
        # We need to move from (a,b) to (0,0)
        # This means we need to move 'a' units left and 'b' units down
        
        # The maximum we can move in one operation is (k,k)
        # So we need at least ceil(a/k) operations for x-direction
        # and at least ceil(b/k) operations for y-direction
        
        # Calculate minimum operations needed for each direction
        min_ops_x = (a + k - 1) // k  # This is ceil(a/k)
        min_ops_y = (b + k - 1) // k  # This is ceil(b/k)
        
        # The minimum cost is the maximum of these two values
        # because we can combine movements in both directions
        result = max(min_ops_x, min_ops_y)
        
        print(result)

solve()