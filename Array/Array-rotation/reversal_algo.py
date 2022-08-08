from cgitb import small


class ArrayRotation:
    def rotate_arr(self, A, D, N):
        self.reverse(A, 0 , N-1)
        self.reverse(A, 0 , N-D-1)
        self.reverse(A, N-D , N-1)



    def reverse(self, A, left, right):
        if right <= left:
            return A
        temp = A[left]
        A[left] = A[right]
        A[right] = temp
        return self.reverse(A, left + 1, right -1)



N = int(input("Enter Size of Array: "))
A = input("Enter Elements seperated by ' ' : ")
D = int(input("Enter the number by which elements should shift: "))
A = A.split()


array_rotation = ArrayRotation()
array_rotation.rotate_arr(A, D, N)
x = array_rotation.gcd(D, N)
print(A)
