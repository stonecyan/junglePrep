#https://leetcode.com/problems/maximum-units-on-a-truck/
#boxTypes: List[List[int]], truckSize: int
def maximumUnits(boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        units=0
        for b in boxTypes:
            if truckSize-b[0]>=0:
                truckSize-=b[0]
                units+=b[0]*b[1] 
            else:
                units+=truckSize*b[1]
                return units
        return units

#can also you heap/priority queue and popoff largest
