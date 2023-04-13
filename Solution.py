
def wordPattern(pattern, s):
    l=s.split()
    map={}
    visited=[]
    if len(pattern)!=len(l):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in map:
            if l[i] not in visited:
                map[pattern[i]]=l[i]
                visited.append(l[i])
            else:
                return False
        elif map[pattern[i]]!=l[i]:
            return False
    return True
pattern="abba"
s="dog cat cat dog"
print(wordPattern(pattern,s))