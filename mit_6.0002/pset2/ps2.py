# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
#           Nodes represent the buildings on the campus.
#           Edges represent the connections between buildings. And edges are directed, indicating one-way 
#                       connections from one building(Node) to another(Node). 
#           Distances are represented by weights on the edges. Two types of distances are considered: total 
#                       distance (overall distance between buildings) and outdoor distance (distance spent 
#                       outdoors when traveling between buildings).


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    with open(map_filename) as file:
        mit_graph = Digraph()
        for line in file.readlines():
            src, dest, total_dist, outdoor_dist = line.split(" ")
            src_node = Node(src)
            dest_node = Node(dest)
            weighted_edge = WeightedEdge(src_node, dest_node, int(total_dist), int(outdoor_dist))
            if not mit_graph.has_node(src_node):
                mit_graph.add_node(src_node)
            if not mit_graph.has_node(dest_node):
                mit_graph.add_node(dest_node)
            mit_graph.add_edge(weighted_edge)
    return mit_graph

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:
#           Objective function is to find the shortest path between two buildings on the map.
#                       Path's lenght is determined by the total distance walked.
#           Constraints are the maximum values of total distance and outdoor distance. The total
#                       distance traveled on the path must not exceed these specified maximums.

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    
    path[0] = path[0] + [start]                     # updating list of nodes in the path.
    if path[2] > max_dist_outdoors:                 # checking if max_dist_outdoors was exceeded. No point going deeper if so.
        return None
    temp_start, temp_end = Node(start), Node(end)   # Digraph has_node method accepts only Node object
    if digraph.has_node(temp_start) is False or digraph.has_node(temp_end) is False:
        raise KeyError
    elif start == end:
        return path
    for edge in digraph.edges[temp_start]:
        node = edge.get_destination().get_name()                # destination node as a string
        if node not in path[0]:                                 # checking in order to avoid infinite loops.
            distance = edge.get_total_distance() + path[1]      # updating total distance.
            outdoors = edge.get_outdoor_distance() + path[2]    # updating outdoor distance.
            updated_path = [path[0], distance, outdoors]
            new_path = get_best_path(digraph, node, end, updated_path, max_dist_outdoors, best_dist, best_path)
            if new_path:
                if not best_dist or new_path[1] < best_dist:            # if distance on current path shorter than best one,
                    best_path, best_dist = new_path[0], new_path[1]     # update and sign new best distance and path.
        else:
            print(f'{node} node is already in your path!')
    return best_path, best_dist



# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    
    path = [[], 0, 0]   # initial empty path.
    result = get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist=None, best_path=None)
    if result[1] is None:
        print('There is no result that meets constraints!')
        raise ValueError
    else:
        if result[1] > max_total_dist:
            print('Result exceeded max_total_dist')
            raise ValueError
        else:
            return result[0]


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
