class ArrayRotation:
    def rotate_arr(self, A, D, N):
        D = D%N
        for _ in range(D):
            k = A[0]
            for ind in range(1, len(A)):
                A[ind-1] = A[ind]
            A[N - 1] = k


N = int(input("Enter Size of Array: "))
A = input("Enter Elements seperated by ' ' : ")
D = int(input("Enter the number by which elements should shift: "))
A = A.split()


array_rotation = ArrayRotation()
array_rotation.rotate_arr(A, D, N)
print(A)
