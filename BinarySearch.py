'''875. Koko eating bananas. The slowest she can eat is 1/hour, the fastest that would be beneficial is max(piles)/hour. Binary search for numbers [1, max(piles)]
to find minimum speed that would allow her to eat all bananas in h hours. Time complexity O(nlogn) where n is the number of piles. Space complexity O(1)'''

def minEatingSpeed(piles: list[int], h: int) -> int:
        s, f = 1, max(piles)
        m = (f + s) // 2
        while s < f:
            time = 0
            for pile in piles:
                time += math.ceil(pile/m)
            if time > h:
                s = m + 1
            elif time <= h:
                f = m
            m = (f + s) // 2
        
        return m

'''153. Minimum of rotated sorted array. If left is bigger than right, than binary search the right half, else binary search the left half. 
When left is less than righ  Time complexity O(logn), space complexity O(1)'''
def findMin(nums: list[int]) -> int:     
    l,r = 0, len(nums)-1
    m = (l + r) // 2
    while l <= r:
        if nums[l] <= nums[r]:
            return nums[l]
        elif nums[m] >= nums[l]:
            l = m + 1
            m = (l + r) // 2
        elif nums[m] < nums[l]:
            r = m
            m = (l + r) // 2


'''33. binary Search in rotated sorted array. In each loop, check if middle is in left half (or if array is not rotated) or right half, and check accordingly'''
def search(nums: list[int], target: int) -> int:
    l,r = 0, len(nums)-1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m
        if nums[m] >= nums[l]:
            if nums[m] < target or nums[l] > target:
                l = m + 1
            else: 
                r = m - 1
        else:
            if nums[m] > target or nums[r] < target:
                r = m - 1
            else:
                l = m + 1


    return -1

'''981. Time based key-value store. Dictionary of with values as keys and list of tuples (timestamp, value) as values.'''
class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key)
        if not values:
            return res
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] == timestamp:
                res = values[m][1]
                break
            elif values[m][0] > timestamp:
                r = m - 1
            else:
                res = values[m][1]
                l = m + 1
        return res


values = TimeMap()

values.set("foo", "bar", 1)
print(values.get("foo", 1))
print(values.get("foo", 3))
values.set("foo", "bar2", 4)
print(values.get("foo", 4))
    
