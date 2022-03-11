import statistics

def main():
    
    input = open("input.txt")
    nums = [int(x) for x in input.readline().strip().split(",")]
    avg = int(sum(nums) / len(nums))
    cost = 0
    for num in nums:
        razlika = abs(num - avg)
        cost += int((razlika*(razlika+1))/2)
    print(cost)
main()