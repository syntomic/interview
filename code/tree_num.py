'''test_num = int(input())
ans = []

for i in range(test_num):
    train_days = int(input())
    turnover = list(map(int, input().split()))
    
    max_ = 0
    final = 0
    for i in range(1,train_days):
        for j in range(i):
            if turnover[j] < turnover[i]:
                final += 1
            elif turnover[j] > turnover[i]:
                final -= 1
        max_ = max(final, max_)
        
    ans.append([max_, final])
    
for i in ans:
    print(i[0], i[1])
'''
class Solution1(object):
    def countSmaller(self, a: list) -> list:
        """利用语言特性"""

        from bisect import bisect_left
        ans = []
        b = []
        for i in range(len(a) - 1, -1, -1):
            index = bisect_left(b, a[i])
            b.insert(index, a[i])
            ans.append(index)

        return ans[::-1]

class Solution2(object):
    def countSmaller(self, nums):
        """利用归并思想"""

        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        temp = [None for _ in range(size)]
        indexes = [i for i in range(size)]
        res = [0 for _ in range(size)]

        self.__helper(nums, 0, size - 1, temp, indexes, res)

        return res

    def __helper(self, nums, left, right, temp, indexes, res):
        if left == right:
            return

        mid = left + (right - left) // 2
        self.__helper(nums, left, mid, temp, indexes, res)
        self.__helper(nums, mid+1, right, temp, indexes, res)

        if nums[indexes[mid]] <= nums[indexes[mid+1]]:
            return

        self.__sort_and_count_smaller(nums, left, mid, right, temp, indexes, res)

    def __sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
        """
        [left, mid] 前有序数组
        [mid+1, right] 后有序数组

        先拷贝, 再合并
        """
        temp[left: right+1] = indexes[left:right+1]  ## 全局使用一个临时存储数组，而不必每一个归并都新建临时的存储空间

        l = left
        r = mid + 1

        ## 前有序数组出列时, 计算逆序数
        for i in range(left, right + 1):
            if l > mid:
                indexes[i] = temp[r]
                r += 1
            elif r > right:
                indexes[i] = temp[l]
                l += 1
                res[indexes[i]] += (right - mid)
            elif nums[temp[l]] <= nums[temp[r]]:
                indexes[i] = temp[l]
                l += 1
                res[indexes[i]] += (r - mid - 1)
            else:
                assert nums[temp[l]] > nums[temp[r]]
                indexes[i] = temp[r]
                r += 1

class Solution3(object):
    def countSmaller(self, nums: list) -> list:
        """利用树状数组"""
        class FenwickTree(object):
            def __init__(self, n):
                self.size = n
                self.tree = [0 for _ in range(n + 1)]

            def __lowbit(self, index):
                return index & (-index)

            # 单点更新：将 index 这个位置 + 1
            def update(self, index, delta):
                # 从下到上，最多到 size，可以等于 size
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # 区间查询：查询小于等于 index 的元素个数
            # 查询的语义是"前缀和"
            def query(self, index):
                res = 0
                # 从上到下，最少到 1，可以等于 1
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res

        # 特判
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        # 去重，方便离散化
        s = list(set(nums))

        s_len = len(s)

        # 离散化，借助堆
        import heapq
        heapq.heapify(s)

        rank_map = dict()
        rank = 1

        for _ in range(s_len):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1

        fenwick_tree = FenwickTree(s_len)

        # 从后向前填表
        res = [None for _ in range(size)]
        # 从后向前填表
        for index in range(size - 1, -1, -1):
            # 1、查询排名
            rank = rank_map[nums[index]]
            # 2、在树状数组排名的那个位置 + 1
            fenwick_tree.update(rank, 1)
            # 3、查询一下小于等于“当前排名 - 1”的元素有多少
            res[index] = fenwick_tree.query(rank - 1)
        return res

if __name__ == "__main__":
    nums = [5, 2, 6, 1]
    sol1 = Solution1()
    sol2 = Solution2()
    print(sol1.countSmaller(nums))
    print(sol2.countSmaller(nums))