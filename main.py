import numpy as np

def main():
    print("Here is a simple NumPy example:")
    
    # Create a 1D array
    arr = np.array([1, 2, 3, 4, 5])
    print(f"\n1D Array: {arr}")
    print(f"Shape: {arr.shape}")
    
    
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n2D Array:\n{arr2d}")
    print(f"Shape: {arr2d.shape}")
    
    print(f"\nMultiplying the 1D array by 2: {arr * 2}")

if __name__ == "__main__":
    main()
