def findMedianSortedArrays(nums1, nums2):
    # 确保 nums1 是较短的数组，以降低时间复杂度
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    total_half = (m + n + 1) // 2  # 总左半部分的长度

    while left <= right:
        # 二分确定 nums1 的分割点 i
        i = (left + right) // 2
        j = total_half - i

        # 处理边界情况
        # 如果nums1 的分割点 i 为 0 或 nums2 的分割点 j 为 0，则取对应的最小值,此时nums1或2左边没有元素,反之为对应值
        # 如果nums2 的分割点 j 为 n 或 nums1 的分割点 i 为 m，则取对应的最大值,此时nums1或2右边没有元素,
        nums1_left_max = -float('inf') if i == 0 else nums1[i - 1]
        nums2_left_max = -float('inf') if j == 0 else nums2[j - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]
        nums2_right_min = float('inf') if j == n else nums2[j]
        # 如果分割线左边的都小于右边的，则满足分割条件
        # 检查分割条件
        if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
            # 计算中位数
            # 判断奇数还是偶数
            if (m + n) % 2 == 1:
                return max(nums1_left_max, nums2_left_max)
            else:
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
        # 如果nums1的最大值大于nums2的最小值，则nums1的右边边界需要向左移动，反之nums2的左边界需要向右移动
        elif nums1_left_max > nums2_right_min:
            # 分割点 i 需要左移
            right = i - 1
        else:
            # 分割点 i 需要右移
            left = i + 1
    return 0.0  # 逻辑上不会执行到这里
print(findMedianSortedArrays([],[1,2,4]))