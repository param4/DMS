class ArrayRotation:
    def rotate_arr(self, A, D, N):
        D = D%N
        temp_arr = A[:D]
        for ind in range(D,N):
            A[ind-D] = A[ind]
        
        for ind in range(len(temp_arr)):
            A[N - D + ind] = temp_arr[ind]


N = int(input("Enter Size of Array: "))
A = input("Enter Elements seperated by ' ' : ")
D = int(input("Enter the number by which elements should shift: "))
A = A.split()


array_rotation = ArrayRotation()
array_rotation.rotate_arr(A, D, N)
print(A)
