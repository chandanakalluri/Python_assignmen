def can_stack_cubes(n, blocks):
    left = 0  # Index of the leftmost cube
    right = n - 1  # Index of the rightmost cube

    prev_cube = float('inf')  # Initialize previous cube size to infinity

    # Iterate until left pointer crosses or meets right pointer
    while left <= right:
        # Check if the leftmost cube can be stacked
        if blocks[left] <= blocks[right]:
            # Check if the current cube is smaller than the previous cube
            if blocks[right] <= prev_cube:
                prev_cube = blocks[right]  # Update previous cube size
                right -= 1  # Move right pointer to the left
            else:
                return "No"  # Cannot stack the cubes
        else:
            # Check if the current cube is smaller than the previous cube
            if blocks[left] <= prev_cube:
                prev_cube = blocks[left]  # Update previous cube size
                left += 1  # Move left pointer to the right
            else:
                return "No"  # Cannot stack the cubes

    return "Yes"  # All cubes stacked successfully

# Input
T = int(input())
for _ in range(T):
    n = int(input())  # Number of cubes
    blocks = list(map(int, input().split()))  # Side lengths of each cube

    # Output
print(can_stack_cubes(n, blocks))
