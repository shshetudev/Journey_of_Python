if __name__ == '__main__':
    n = int(input())
    num_list = []
    for _ in range(n):
        string = input().split()
        command = string[0]
        args = string[1:]
        if command != "print":
            command += "(" + ",".join(args) + ")"
            eval("num_list." + command)
        else:
            print(num_list)
