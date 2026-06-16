class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        n = len(nums)

        # Initial closest sum
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Perfect match
                if current_sum == target:
                    return current_sum

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest
