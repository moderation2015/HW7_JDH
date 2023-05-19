import numpy as np

def main():
    arr = np.arange(1,5,1).reshape(2,2)
    eigenvalues, eigenvectors = np.linalg.eig(arr)
    determinant = np.linalg.det(arr)

    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])
    cross_product = np.cross(vec1,vec2)

    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b = np.array([-15,-21,18])
    x = np.linalg.solve(A,b)
    
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:")
    print(eigenvectors)
    print("Determinant:", determinant)
    print("Cross product:", cross_product)
    print("Solution:", x)


if __name__ == '__main__':
    main()
