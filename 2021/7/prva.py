import statistics

def main():
    input = open("input.txt")
    nums = [int(x) for x in input.readline().strip().split(",")]
    median = int(round(statistics.median(nums)))
    cost = 0
    for num in nums:
        cost += abs(num - median)
    
    print(cost)
main()