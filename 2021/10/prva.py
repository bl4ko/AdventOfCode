def main():
    input = open("input.txt")
    illegal = 0
    for line in input:
        line = line.strip()
        char2val = { ")":3, "]":57, "}": 1197, ">": 25137}
        open2close = { "(": ")", "{": "}", "[": "]", "<": ">"}
        vrsta = list()
        for char in line:
            if char in open2close:
                vrsta.append(char)
            else:
                popped = vrsta.pop()
                if (open2close[popped] != char):
                    illegal += char2val[char]
                    break
    print(illegal)
main()