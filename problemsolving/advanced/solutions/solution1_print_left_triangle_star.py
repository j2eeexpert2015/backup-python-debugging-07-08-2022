def print_left_triangle_star_pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print("\r")


n = 5
print_left_triangle_star_pattern(n)
