'''Koko eating bananas. The slowest she can eat is 1/hour, the fastest that would be beneficial is max(piles)/hour. Binary search for numbers [1, max(piles)]
to find minimum speed that would allow her to eat all bananas in h hours. Time complexity O(nlogn) where n is the number of piles. Space complexity O(1)'''

def minEatingSpeed(self, piles: List[int], h: int) -> int:
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
