#Got help from online to get to this solution and to understand what the divmond function does

class KPartition(object):
    def canPartitionKSubsets(self, nums, k):
        target, remaining = divmod(sum(nums), k)
        if remaining or max(nums) > target: return False

        memory = [None] * (1 << len(nums))
        memory[-1] = True
        
        def search(used, todo):
            if memory[used] is None:
                targ = (todo - 1) % target + 1
                memory[used] = any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memory[used]

        return search(0, target * k)
    