class Solution(object):
    
    def splitLoopedString(self, strs):
        # Preprocess: make each string the lexicographically larger of itself or its reverse
        strs = [max(s, s[::-1]) for s in strs]
        res = ""

        for i, base in enumerate(strs):
            other = strs[i+1:] + strs[:i]  # everything except the i-th, in rotated order

            for version in [base, base[::-1]]:  # try both normal and reversed
                for k in range(len(version)):
                    # make candidate using split at position k
                    candidate = version[k:] + ''.join(other) + version[:k]
                    if candidate > res:
                        res = candidate

        return res
