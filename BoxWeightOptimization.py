#https://leetcode.com/discuss/interview-question/1085968/Amazon-OA-or-Optimization-Box-Weights/862764

from collections import Counter

def optimizeBoxWeight(arr):
  halfSum=sum(arr)//2
  countDict=Counter(arr)
  sortedCounts=[(n,count) for n,count in countDict.items()]
  sortedCounts.sort(key=lambda x: -x[0])
  output=[]
  outputSum=0
  subset=[]
  for i in range(0, len(sortedCounts)):
    subsetSum=sum(subset)
    if subsetSum>halfSum:
      if not output or len(subset)<len(output):
        output=subset
        outputSum=sum(output)
      if len(subset)==len(output):
        if subsetSum > outputSum:
          output=subset
          outputSum=sum(output)
      break
    n, count=sortedCounts[i][0], sortedCounts[i][1]
    if count>0:
      subset.extend([n]*count)
  output.sort()
  return output
