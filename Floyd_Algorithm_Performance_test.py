import timeit
import sys
import itertools

NO_PATH = float('inf')

def floyd_recursive(distance, intermediate, start_node, end_node):
    global MAX_LENGTH
    
    # Base case: if start_node and end_node are the same, distance is zero
    if start_node == end_node:
        distance[start_node][end_node] = 0
        return
    
    # Base case: any value that has sys.maxsize has no path
    if distance[start_node][end_node] == NO_PATH:
        return
    
    # Update the distance using recursion
    distance[start_node][end_node] = min(
        distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )
    
    # Recursive calls for all possible intermediate nodes
    if intermediate < MAX_LENGTH - 1:
        floyd_recursive(distance, intermediate + 1, start_node, end_node)
    elif start_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, start_node + 1, end_node)
    elif end_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, 0, end_node + 1)

def floyd(distance):
    global MAX_LENGTH
    
    for intermediate, start_node, end_node in itertools.product(
            range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)
    ):
        floyd_recursive(distance, intermediate, start_node, end_node)
    
    # Return the resulting distance matrix
    return distance

def generate_large_graph(size):
    """
    Generate a large graph for performance testing
    """
    graph = [[NO_PATH] * size for _ in range(size)]
    for i in range(size):
        graph[i][i] = 0
        for j in range(i + 1, size):
            graph[i][j] = graph[j][i] = i + j  # Some arbitrary values for testing
    return graph

def performance_test():
    setup_code = """
import itertools

NO_PATH = float('inf')

def floyd_recursive(distance, intermediate, start_node, end_node):
    global MAX_LENGTH
    
    if start_node == end_node:
        distance[start_node][end_node] = 0
        return
    
    if distance[start_node][end_node] == NO_PATH:
        return
    
    distance[start_node][end_node] = min(
        distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )
    
    if intermediate < MAX_LENGTH - 1:
        floyd_recursive(distance, intermediate + 1, start_node, end_node)
    elif start_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, start_node + 1, end_node)
    elif end_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, 0, end_node + 1)

def floyd(distance):
    global MAX_LENGTH
    
    for intermediate, start_node, end_node in itertools.product(
            range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)
    ):
        floyd_recursive(distance, intermediate, start_node, end_node)
    
    for row in distance:
        pass

MAX_LENGTH = len(graph[0])
    """

    test_code = """
floyd(graph)
    """

    graph_size = 100  # Adjust the size as needed for your performance test
    graph = generate_large_graph(graph_size)

    time_taken = timeit.timeit(test_code, setup=setup_code, number=1)  # Adjust the number as needed
    print(f"Time taken for 1 execution: {time_taken} seconds")

if __name__ == "__main__":
    performance_test()
