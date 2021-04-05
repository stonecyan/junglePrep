#https://leetcode.com/discuss/interview-question/1115038/Amazon-Hackerrank-OA-2021
def binarySearch(arr, flask):
    n=len(arr)
    if flask>arr[-1]:
        return -1
    start=0
    end=n-1
    while start<=end:
        midpoint=start+(end-start)//2
        if flask<arr[midpoint]:
            end=midpoint-1
        elif flask>arr[midpoint]:
            start=midpoint+1
        else:
            return midpoint
    return start
 
def flaskWaste(numOrders, requirements, flaskTypes, totalMarks, markings):
  flaskDict={}
  for marking in markings:
      markingIndex=marking[0]
      markingFlask=marking[1]
      if markingIndex not in flaskDict:
        flaskDict[markingIndex]=[]
      flaskDict[markingIndex].append(markingFlask)
  print(flaskDict)
  wasteList=[]
  for i in range(0,flaskTypes):
      waste=0
      markingsList=flaskDict[i]
      print(markingsList)
      for j in range(0, numOrders):
          marking=binarySearch(markingsList, requirements[j])
          if marking==-1:
              print('break')
              waste=-1
              break
          else:
              waste+=(markingsList[marking]-requirements[j])
      wasteList.append(waste)
      print(wasteList)
  index=-1
  minWaste=float('inf')
  for i in range(0,len(wasteList)):
      if wasteList[i]!=-1 and minWaste>wasteList[i]:
          index=i
          minWaste=wasteList[i]
  return index
  
