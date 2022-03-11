def main():
    input = open("input2.txt")
    horizontal = 0
    depth = 0
    for line in input:
        beseda = line.split()
        if (beseda[0] == "forward"):
            horizontal += int(beseda[1])
        else:
            if (beseda[0] == "down"):
                aim += int(beseda[1])
            else:
                aim -= int(beseda[1])
    input.close()
    print(horizontal * depth)
main()