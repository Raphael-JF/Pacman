import math,heapq,assets
from classes.blocks import *

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
    
    def __init__(self,game_map):
        self.nodes = {}
        self.game_map = game_map


    def add_node(self, node:Node):
        self.nodes[tuple(node.pos)] = node


    def insert(self,pos) -> Node:

        try:
            self.nodes[tuple(pos)]
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
            self.nodes[tuple(pos)]
        except:
            return
        next_top = self.nearest_node(pos,"top")
        next_bottom = self.nearest_node(pos,"bottom")
        next_left = self.nearest_node(pos,"left")
        next_right = self.nearest_node(pos,"right")
        if next_top:
            if next_bottom:
                self.add_edge(next_top,next_bottom)
            else:
                next_top.next["bottom"] = [None,None]
        if next_bottom:
            if next_top:
                self.add_edge(next_bottom,next_top)
            else:
                next_bottom.next["top"] = [None,None]
        if next_left:
            if next_right:
                self.add_edge(next_left,next_right)
            else:
                next_left.next["right"] = [None,None]
        if next_right:
            if next_left:
                self.add_edge(next_right,next_left)
            else:
                next_right.next["left"] = [None,None]
        del self.nodes[tuple(pos)]


    def nearest_node(self,pos,side):

        temp_pos = list(pos)

        if side == "top":
            while temp_pos[1] >= 0:
                if type((self.game_map.cells[temp_pos[1]][temp_pos[0]])) is Wall:
                    return
                temp_pos[1] -= 1
                try:
                    return self.nodes[tuple(temp_pos)]
                except:
                    pass
        elif side == "bottom":
            while temp_pos[1] < self.game_map.y_cells:
                if type((self.game_map.cells[temp_pos[1]][temp_pos[0]])) is Wall:
                    return
                temp_pos[1] += 1
                try:
                    return self.nodes[tuple(temp_pos)]
                except:
                    pass
        elif side == "left":
            while temp_pos[0] >= 0:
                if type((self.game_map.cells[temp_pos[1]][temp_pos[0]])) is Wall:
                    return
                temp_pos[0] -= 1
                try:
                    return self.nodes[tuple(temp_pos)]
                except:
                    pass
        elif side == "right":
            while temp_pos[0] < self.game_map.x_cells:
                if type((self.game_map.cells[temp_pos[1]][temp_pos[0]])) is Wall:
                    return
                temp_pos[0] += 1
                try:
                    return self.nodes[tuple(temp_pos)]
                except:
                    pass


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
        
        created_start = False
        try:
            start_node = self.nodes[tuple(start_pos)]
        except:
            created_start = True
            start_node = self.insert(start_pos)

        created_target = False
        try:
            target_node = self.nodes[tuple(target_pos)]
        except:
            created_target = True
            target_node = self.insert(target_pos)

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
        
        if created_start:
            self.delete(start_pos)
        if created_target:
            self.delete(target_pos)

        # if len(path) == 1:
        #     return []
        path.reverse()
        return path