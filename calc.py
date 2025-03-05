import numpy as np

def get_matrix(rows, cols, name="Matrix"):
    print(f"Enter the elements of {name} ({rows}x{cols}):")
    return np.array([[float(input(f"Element ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)])

def main():
    while True:
        print("\nMatrix Calculator - Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Inverse")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice in ['1', '2', '3']:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            A = get_matrix(rows, cols, "Matrix A")
            B = get_matrix(rows, cols, "Matrix B")
            
            if choice == '1':
                result = A + B
                print("Result of Addition:\n", result)
            elif choice == '2':
                result = A - B
                print("Result of Subtraction:\n", result)
            elif choice == '3':
                if A.shape[1] != B.shape[0]:
                    print("Matrix multiplication not possible due to shape mismatch!")
                    continue
                result = np.dot(A, B)
                print("Result of Multiplication:\n", result)
        
        elif choice == '4':
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            A = get_matrix(rows, cols, "Matrix")
            print("Transpose of Matrix:\n", A.T)
            
        elif choice == '5':
            rows = int(input("Enter size of square matrix (NxN): "))
            A = get_matrix(rows, rows, "Square Matrix")
            if np.linalg.det(A) == 0:
                print("Matrix is singular and cannot be inverted!")
            else:
                print("Inverse of Matrix:\n", np.linalg.inv(A))
        
        elif choice == '6':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")
        
if __name__ == "__main__":
    main()
