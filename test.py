import math,heapq

class Node:

    def __init__(self, pos):
        self.pos = tuple(pos)
        self.distance = math.inf
        self.visited = False
        self.previous = None
        self.next = {
            "top" : [None]*2,
            "bottom" : [None]*2,
            "left" : [None]*2,
            "right" : [None]*2
        }

    def set_distance(self, distance):
        self.distance = distance

    def set_visited(self,state):
        self.visited = state

    def set_previous(self, previous):
        self.previous = previous

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __eq__(self, other):
        return self.distance == other.distance


class Graph:
    
    def __init__(self):
        self.nodes = {}


    def add_node(self, node:Node):
        self.nodes[node.pos] = node


    def insert(self,pos) -> Node:

        try:
            self.nodes[pos]
            return
        except:
            pass
        new_node = Node(pos)
        self.add_node(new_node)
        next_top = self.nearest_node(pos,"top")
        if next_top is not None:
            self.add_edge(new_node,next_top)
            self.add_edge(next_top,new_node)
        next_bottom = self.nearest_node(pos,"bottom")
        if next_bottom is not None:
            self.add_edge(new_node,next_bottom)
            self.add_edge(next_bottom,new_node)
        next_left = self.nearest_node(pos,"left")
        if next_left is not None:
            self.add_edge(new_node,next_left)
            self.add_edge(next_left,new_node)
        next_right = self.nearest_node(pos,"right")
        if next_right is not None:
            self.add_edge(new_node,next_right)
            self.add_edge(next_right,new_node)
        return new_node
    

    def delete(self,pos):
        try:
            self.nodes[pos]
        except:
            return
        next_top = self.nearest_node(pos,"top")
        next_bottom = self.nearest_node(pos,"bottom")
        next_left = self.nearest_node(pos,"left")
        next_right = self.nearest_node(pos,"right")
        if next_top is not None:
            self.add_edge(next_top,next_bottom)
        if next_bottom is not None:
            self.add_edge(next_bottom,next_top)
        if next_left is not None:
            self.add_edge(next_left,next_right)
        if next_right is not None:
            self.add_edge(next_right,next_left)
        del self.nodes[pos]


    def nearest_node(self,pos,side):

        if side == "top":
            while pos[1] >= 0:
                try:
                    return self.nodes[tuple(pos)]
                except:
                    pos[1] -= 1
        elif side == "bottom":
            while pos[1] < 5:
                try:
                    return self.nodes[tuple(pos)]
                except:
                    pos[1] += 1
        elif side == "left":
            while pos[0] >= 0:
                try:
                    return self.nodes[tuple(pos)]
                except:
                    pos[0] -= 1
        elif side == "right":
            while pos[0] < 5:
                try:
                    return self.nodes[tuple(pos)]
                except:
                    pos[0] += 1


    def add_edge(self, node1:Node, node2:Node):
            
            if node1.pos == node2.pos:
                return
            
            if node1.pos[0] == node2.pos[0]:
                weight = abs(node1.pos[1] - node2.pos[1])
                if node1.pos[1] < node2.pos[1]:
                    dir = "bottom"
                else:
                    dir = "top"
            elif node1.pos[1] == node2.pos[1]:
                weight = abs(node1.pos[0] - node2.pos[0])
                if node1.pos[0] < node2.pos[0]:
                    dir = "right"
                else:
                    dir = "left"
            node1.next[dir] = [node2,weight]

    def dijkstra(self, start_pos, target_pos):
        
        # created_start = False
        # try:
        #     start_node = self.nodes[tuple(start_pos)]
        # except:
        #     created_start = True
        #     start_node = self.insert(start_pos)

        # created_target = False
        # try:
        #     target_node = self.nodes[tuple(target_pos)]
        # except:
        #     created_target = True
        #     target_node = self.insert(target_pos)
        start_node = self.nodes[tuple(start_pos)]
        target_node = self.nodes[tuple(target_pos)]


        for node in self.nodes.values():
            node.set_distance(math.inf)
            node.set_visited(False)

        # File de priorité pour stocker les nœuds à visiter
        queue = [(0, start_node)]
        start_node.set_distance(0)

        while queue:
            current_distance, current_node = heapq.heappop(queue)
            current_node.set_visited(True)

            # Si le nœud actuel est le nœud cible, on a trouvé le chemin le plus court
            if current_node == target_node:
                break

            for neighbor, weight in [[i,j] for i,j in current_node.next.values() if i and j]:
                if not neighbor.visited:
                    new_distance = current_distance + weight
                    if new_distance < neighbor.distance:
                        neighbor.set_distance(new_distance)
                        neighbor.set_previous(current_node)
                        heapq.heappush(queue, (new_distance, neighbor))

        # Construction du chemin le plus court
        path = []
        current_node = target_node

        while current_node:
            path.append(current_node.pos)
            temp_current_node = current_node.previous
            current_node.set_previous(None)
            current_node = temp_current_node
        
        # if created_start:
        #     self.delete(start_pos)
        # if created_target:
        #     self.delete(target_pos)

        # if len(path) == 1:
        #     return []
        path.reverse()
        return path
    
# Création du graphe
graph = Graph()

# Création des nœuds
A = Node([0,0])
B = Node([3,0])
C = Node([3,3])
D = Node([0,3])
E = Node([2,1])
F = Node([3,1])
G = Node([2,2])
H = Node([1,2])
I = Node([1,0])
# Ajout des nœuds au graphe
graph.add_node(A)
graph.add_node(B)
graph.add_node(C)
graph.add_node(D)
graph.add_node(E)
graph.add_node(F)
graph.add_node(G)
graph.add_node(H)
graph.add_node(I)

# Ajout des arêtes
graph.add_edge(A, D)
graph.add_edge(A, I)
graph.add_edge(B, F)
graph.add_edge(B, I)
graph.add_edge(C, D)
graph.add_edge(C, F)
graph.add_edge(E, G)
graph.add_edge(E, F)
graph.add_edge(F, B)
graph.add_edge(G, H)
graph.add_edge(H, I)

# Exécution de l'algorithme de Dijkstra
print(graph.dijkstra([0,0], [1,2]))
print(graph.dijkstra([0,0], [3,3]))