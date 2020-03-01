import copy

def checkConnections(tempGraph, n):
	notVisited = [*range(1,n)]
	toVisit = tempGraph[0]
	for node in toVisit:
		notVisited.remove(node)
	while len(toVisit)>0:
		currentNode = toVisit.pop()
		currentNodeList = tempGraph[currentNode]
		for newNode in currentNodeList:
			if newNode in notVisited:
				notVisited.remove(newNode)
				toVisit.append(newNode)
	if len(notVisited)==0:
		return True
	return False

def criticalConnections(n, connections):	
	graph = [ [] for i in range(n)]
	for connect in connections:
		graph[connect[0]].append(connect[1])
		graph[connect[1]].append(connect[0])
	print(graph)

	critConnect = []
	for connect in connections:
		tempGraph = copy.deepcopy(graph)
		tempGraph[connect[0]].remove(connect[1])
		tempGraph[connect[1]].remove(connect[0])
		if not checkConnections(tempGraph, n):
			critConnect.append(connect)
	return critConnect


n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(criticalConnections(n,connections))
