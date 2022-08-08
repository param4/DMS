from cgitb import small


class ArrayRotation:
    def rotate_arr(self, A, D, N):
        gcd = self.gcd(D, N)
        for i in range(gcd):
            temp = A[i]
            j = i
            while True:
                k = (j + D) % N
                if k==i:
                    break
                A[j] = A[k]
                j = k
            A[j] = temp


    def gcd(self, a, b):
        if a>b:
            larger = a
            smaller = b
        else: 
            larger = b
            smaller = a
        if smaller == 0:
            return larger
        return self.gcd(smaller, larger % smaller)


N = int(input("Enter Size of Array: "))
A = input("Enter Elements seperated by ' ' : ")
D = int(input("Enter the number by which elements should shift: "))
A = A.split()


array_rotation = ArrayRotation()
array_rotation.rotate_arr(A, D, N)
x = array_rotation.gcd(D, N)
print(A)
