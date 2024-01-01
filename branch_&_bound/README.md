1. **Item Definition:**
   - `Item` is a namedtuple representing items with three attributes: index, value, and weight.

2. **Node Class:**
   - `Node` represents a node in the search tree. It contains information about the current level, value, weight, and the list of items taken.

3. **Upper Bound Function:**
   - `upper_bound` calculates the upper bound of a node based on its current value, weight, and the remaining items in the list.

4. **Branch and Bound Function:**
   - `branch_and_bound` is the main function implementing the branch and bound algorithm.
   - It sorts the items in descending order of value-to-weight ratio.
   - It initializes a priority queue (`q`) with the root node and its upper bound.
   - It iteratively explores nodes in the priority queue until it is empty.
   - For each node, it calculates the upper bound and explores the child nodes (including and excluding the next item) if the upper bound is promising.
   - It updates the best-known solution whenever a better solution is found.

5. **Solve Function:**
   - `solve_it` parses the input, runs the branch and bound algorithm, and formats the output.

6. **Main Section:**
   - The main section reads the input file, calls the `solve_it` function, and prints the result.

The use of the `PriorityQueue` with the `-` sign is to simulate a max heap, where items with higher priorities (larger values) are retrieved first from the queue. This is a common idiom in Python when using a priority queue to represent a max heap.