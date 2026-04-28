class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)

        for i in words:
            for j in i:
                count[j] += 1
        
        for j in count:
            if count[j] % len(words):
                return False
        return True
