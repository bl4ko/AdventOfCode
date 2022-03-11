def main():
    input = open("input.txt")
    horizontal = 0
    depth = 0
    aim = 0
    for line in input:
        besede = line.split()
        print(besede)
        if (besede[0] == "forward"):
            horizontal += int(besede[1])
            depth += aim * int(besede[1])
        else:
            if (besede[0] == "down"):
                aim += int(besede[1])
            else:
                aim -= int(besede[1])
    input.close()
    print(horizontal * depth)
main()
# 1813062561