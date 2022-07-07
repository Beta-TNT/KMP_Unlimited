from collections import deque

def classicStrMatching(patternStr:str):
    def equalFunc(inputData):
        return lambda x: x == inputData
    funcDict = {char:equalFunc(char) for char in set(patternStr)}
    return [funcDict[c] for c in patternStr]

class kmp_unlimited:
    # classic KMP matching algorithm applied to an unlimited sequence
    _window: deque  # a queue with maxlen equals to the length of pattern, used as a window, the way I use it: append() / popleft()
    _next: list     # NEXT array
    _pattern = None # pattern array
    _overlap = True # overlap mode
    _l = 0          # pattern length
    _i = 0          # classic pointer i
    _j = 0          # classic pointer j

    def __init__(self, pattern, overlap=True):
        def getNext(pattern): # classic NEXT array calculating function.
            i, j, l = 2, 0, len(pattern)
            next = [0] * l
            while i < l:
                while j > 0 and pattern[i-1] != pattern[j]:
                    j = next[j]
                if pattern[i-1] == pattern[j]:
                    j += 1
                next[i] = j
                i += 1
            return next
        self._pattern = pattern
        self._overlap = overlap
        self._next = getNext(pattern)
        self._l = len(pattern)
        self._window = deque(maxlen=self._l)

    def feedData(self, inputData):
        self._window.append(inputData)
        self._i += 1
        if not len(self._window) == self._l:
            # will not start matching until the window is filled
            return None
        else:
            for i in range(self._j, self._l):
                if not self._pattern[i](self._window[i]):
                    for j in range(i - self._next[i]):
                        self._window.popleft() # window slides right (pops left)
                    self._j = self._next[i]
                    return None
            self._j = 0 # reset j pointer
            rtnContent = list(self._window)
            if not self._overlap: # overlap or not
                self._window.clear()
            return self._i - self._l, rtnContent

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

strRaw = 'ababaaabaabababaaaaaaaabaabaaa'
strPattern = 'abababa'

print(standardKmp(strRaw, strPattern))
test=kmp_unlimited(classicStrMatching(strPattern))
for c in strRaw:
    result = test.feedData(c)
    if result:
        print(result[0], ''.join(result[1]))
