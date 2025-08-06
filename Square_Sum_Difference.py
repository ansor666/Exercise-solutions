#Here I found the difference between the sum of the squares of the natural numbers and the square of the sum


def diff():
    sum_sq = sum([i**2 for i in range(1,101)])
    sq_sum = sum([i for i in range(1,101)])**2      
    d = sq_sum - sum_sq
    print(d)


#####################################################
if __name__ == "__main__":
    diff()