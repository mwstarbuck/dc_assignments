nums = [1, 2, 3, 4, 5]

# itereates through list and appends each iteme to same list


def duplicator(nums):
    for num in range(len(nums)):
        nums.append(nums[num])
    print(nums)


duplicator(nums)

# or shown to me by Bach C. Way easier!!

#nums2 = [1, 2, 3, 4, 5]


# def dupicator2(nums):
#    nums += nums
#    return nums


#new_nums = dupicator2(nums2)
# print(new_nums)
