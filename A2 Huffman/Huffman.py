import heapq
from collections import defaultdict

# Step 1: Create a class for the nodes of the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char        # Character
        self.freq = freq        # Frequency of the character
        self.left = None        # Left child (for '0')
        self.right = None       # Right child (for '1')
        
    # Define comparison operators for the priority queue (heap)
    def __lt__(self, other):
        return self.freq < other.freq

# Step 2: Build the Huffman Tree using a greedy strategy
def build_huffman_tree(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)  # Min-Heap based on frequency
    
    while len(heap) > 1:
        # Greedily take the two nodes with the smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new internal node with frequency equal to the sum of the two
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]  # Return the root node of the Huffman Tree

# Step 3: Traverse the Huffman tree and generate codes
def generate_huffman_codes(root):
    codes = {}
    
    def assign_codes(node, code):
        if node:
            # If it's a leaf node, assign the code
            if node.char is not None:
                codes[node.char] = code
            assign_codes(node.left, code + '0')
            assign_codes(node.right, code + '1')
    
    assign_codes(root, "")
    return codes

# Step 4: Main function to encode text using Huffman Encoding
def huffman_encoding(char_freq):
    root = build_huffman_tree(char_freq)
    huffman_codes = generate_huffman_codes(root)
    
    return huffman_codes

# Example Usage
if __name__ == "__main__":
    # Character frequencies (example input)
    char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    
    # Get the Huffman codes
    huffman_codes = huffman_encoding(char_freq)
    
    # Display the Huffman codes for each character
    print("Character : Huffman Code")
    for char, code in huffman_codes.items():
        print(f"{char} : {code}")

