class ArrayRotation:
    def rotate_arr(self, A, D, N):
        D= D%N
        if D==0:
            return
        start = 0
        end = N-1
        mid = D-1
        while True:
            left = mid - start + 1
            right = end - mid
            if left == right:
                for i in range(left):
                    temp = A[i + start]
                    A[i + start] = A[mid + 1 + i]
                    A[mid + 1 + i] = temp
                break
            elif left < right:
                for i in range(left):
                    temp = A[i + start]
                    A[i + start] = A[end - D + 1 + i]
                    A[end - D + 1 + i] = temp
                end = end-left
            else:
                for i in range(right):
                    temp = A[i + start]
                    A[i + start] = A[mid + 1 + i]
                    A[mid + 1 + i] = temp
                start= start + right 


N = int(input("Enter Size of Array: "))
A = input("Enter Elements seperated by ' ' : ")
D = int(input("Enter the number by which elements should shift: "))
A = A.split()


array_rotation = ArrayRotation()
array_rotation.rotate_arr(A, D, N)
print(A)
