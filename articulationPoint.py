def findArticulationPoints(numNodes, numEdges, edges):
	def dfs(id, node, parent):
		visited.append(node)
		parents[node] = parent
		numEdges=0
		low[node]=id

		for n in graph[node]:
			if n == parent:
				continue
			if n not in visited:
				parents[n] = node
				numEdges +=1
				dfs(id+1, n, node)

			low[node] = min(low[node], low[n]) # whether neighbor node has been seen before or not

		if id <= low[n]: #cut-vertex due to bridge and cut-vertex due to cycle
			if parents[node] != -1:
				artPoints.append(node)

		if (parents[node] == -1 and numEdges>=2): #cut vertex due to root
			artPoints.append(node)

	graph = [[] for i in range(numNodes)]
	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])
	visited = []
	artPoints = []
	parents = {}
	low = {}

	dfs(0,0,-1)
	return artPoints


numNodes = 7 
numEdges = 7 
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
print(findArticulationPoints(numNodes,numEdges,edges))
