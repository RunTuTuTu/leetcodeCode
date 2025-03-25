#4. 寻找两个正序数组的中位数
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 总数
        total = len(nums1)+len(nums2)
        #中间序号+1 则是为了循环方便
        #例如 [1,2,3,4] 此时minNum为 3 循环位置为 [1,2,3] 此时a=2 b=3
        #例如 [1,2,3] 此时minNum为 2 循环位置为 [1,2,3] 此时a=3
        minNum = total // 2 + 1
        # 首先判断这两个是否有一个为空
        if nums1 == [] or nums2 == []:
            if len(nums1) + len(nums2) == 1:
                return nums1[0] if len(nums1) == 1 else nums2[0]
            else:
                # 其中有一个为空,需要判断是哪一个
                if len(nums1) == 0:
                    # nums1为空
                    return nums2[len(nums2) // 2] if total % 2 != 0 else (nums2[len(nums2) // 2 - 1] + nums2[
                        len(nums2) // 2]) / 2
                else:
                    return nums1[len(nums1) // 2] if total % 2 != 0 else (nums1[len(nums1) // 2 - 1] + nums1[
                        len(nums1) // 2]) / 2
        # 这是中位数两位，假设为奇则只有a
        a = 0
        b =0 if total % 2 == 0 else False
        #  初始化双方指针
        nums1Point = 0
        nums2Point = 0
        # 为最后一个值打标签
        big=None
        #开始循环到最后一个
        for i in range(0, minNum):
            #进行判断条件为: 先判断nums2指针是否超出nums2长度，超出则已经遍历完nums2，后面不进行判断直接开始nums1遍历
            #如果nums2指针没超过长度，则判断nums1指针是否超出nums1长度，超出则已经遍历完nums1，后面不进行判断直接开始nums2遍历
            #如果都没超出长度，则判断nums1的值是否小于nums2的值，小于等于则nums1指针加一
            if  nums2Point > len(nums2)-1 or (nums1Point < len(nums1) and nums1[nums1Point]<=nums2[nums2Point])  :
                nums1Point += 1
                big =1
            else :
                nums2Point += 1
                big=2
            # 此时就已经跑完了到达中位数的地方
            # minNum-1 获取最后一个值，如果是奇数则为a
            if i == minNum-1:
                if big == 1:
                    a = nums1[nums1Point-1]
                else:
                    a = nums2[nums2Point-1]
            # minNum-2 获取倒数第二个值，如果是偶数为0反正不获取
            if i == minNum -2:
                if type(b) == int:
                    if big == 1:
                        b = nums1[nums1Point - 1]
                    else:
                        b = nums2[nums2Point - 1]
            # 判断是否有b
        if b:
            return (a+b)/2
        else:
            return a
print(Solution().findMedianSortedArrays([1,3],[2]))
