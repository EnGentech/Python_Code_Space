def pascal_triangle(n):
    tempList = [1, 1]
    pascal = [[1]]
    if n == 1:
        return pascal
    elif n == 2:
        pascal.append(tempList)
        return pascal
    elif n > 2:
        pascal.append(tempList)
        for x in range(2, n):
            new_list = [1]
            for tlist in range(len(tempList)):
                if tlist != len(tempList) - 1:
                    sum = tempList[tlist] + tempList[tlist + 1]
                    new_list.append(sum)
                elif tlist == len(tempList) - 1:
                    new_list.append(1)
                    pascal.append(new_list)
                    tempList = new_list
    return pascal


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

