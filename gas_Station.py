class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        N = len(A)
        for i in range(N):
            out = self.for_start(i,N)
            if out != -1:
                return out
        return -1

    def for_start(self, i,N):
        fuel_reqd = 0
        gas_available = 0
        for j in range(N):
            idx = (i + j) % N
            #print(i,j,idx)
            fuel_reqd += B[idx]
            gas_available += A[idx]
            #print('gas_available, fuel_reqd', gas_available, fuel_reqd)
            if gas_available < fuel_reqd:
                return -1
        return i

sol = Solution()
# A = [1, 2, 3, 4, 5]
# B = [3, 4, 5, 1, 2]
A=[0]
B=[0]
o = sol.canCompleteCircuit(A, B)
print(o)
