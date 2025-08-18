words = [str(x) for x in input().lower().split()]
words2 =[str(x) for x in input().lower().split()]

set1 = set(words)
set2 = set(words2)
hop = set1 | set2
hop = sorted(hop)
giao =set1 & set2
giao = sorted(giao)
print(' '.join(hop))
print(' '.join(giao))
