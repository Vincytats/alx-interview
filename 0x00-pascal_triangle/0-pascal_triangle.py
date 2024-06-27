#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
    
    return triangle

if __name__ == "__main__":
    pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
