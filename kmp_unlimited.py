from collections import deque

def classicStrMatching(patternStr:str):
    def equalFunc(inputData):
        return lambda x: x == inputData
    funcDict = {char:equalFunc(char) for char in set(patternStr)}
    return [funcDict[c] for c in patternStr]

class kmp_unlimited:
    # classic KMP matching algorithm applied to a unlimited sequence
    _window: deque  # fixed length queue used as a window, use method: append(), popleft()
    _next: list     # next array
    _needle = None  # pattern array
    _l = 0          # pattern length
    _i = 0          # classic pointer i
    _j = 0          # classic pointer j

    def __init__(self, needle):
        def getNext(needle): # calculate next array
            i, j, l = 2, 0, len(needle)
            next = [0] * l
            while i < l:
                while j > 0 and needle[i-1] != needle[j]:
                    j = next[j]
                if needle[i-1] == needle[j]:
                    j += 1
                next[i] = j
                i += 1
            return next
        self._needle = needle
        self._next = getNext(needle)
        self._l = len(needle)
        self._window = deque(maxlen=self._l)

    def feedData(self, inputData):
        self._window.append(inputData)
        self._i += 1
        if not len(self._window) == self._l:
            return None
        else:
            for i in range(self._j, self._l):
                if not self._needle[i](self._window[i]):
                    for j in range(i - self._next[i]):
                        self._window.popleft() # window move right (pop left)
                    self._j = self._next[i]
                    return None
            self._j = 0 # reset j pointer
            return self._i - self._l, list(self._window)

def standardKmp(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    def getNext(needle):
        i, j, l = 2, 0, len(needle)
        next = [0] * l
        while i < l:
            while j > 0 and needle[i-1] != needle[j]:
                j = next[j]
            if needle[i-1] == needle[j]:
                j += 1
            next[i] = j
            i += 1
        return next
    next = getNext(needle)
    i, n, j, m = 0, len(haystack), 0, len(needle)
    while i < n and j < m:
        while j > 0 and haystack[i] != needle[j]:
            j = next[j]
        if haystack[i] == needle[j]:
            j += 1
        i += 1
        if j == m:
            return i - j
    return -1

strRaw = 'ababaaabaababaaaaaaaaabaabaaa'
strPattern = 'aaaaaa'

print(standardKmp(strRaw, strPattern))
test=kmp_unlimited(classicStrMatching(strPattern))
for c in strRaw:
    result = test.feedData(c)
    if result:
        print(result[0], ''.join(result[1]))
