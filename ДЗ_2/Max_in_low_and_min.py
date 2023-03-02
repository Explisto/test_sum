def funct_max( *args, low=54, hi=96):

    max_element = max(args)

    if (low <= max_element <= hi):
        return max_element

    if (max_element < low):
        return low

    if (max_element > hi):
        return hi

# print(funct_max())