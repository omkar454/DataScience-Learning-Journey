
from collections import Counter
import pprint

# --- Synthetic Dataset Generation ---
# Features: Income, Student, Credit_Rating | Target: Buys_Laptop
dataset = [
    ['High', 'No', 'Fair', 'No'],
    ['High', 'No', 'Excellent', 'No'],
    ['High', 'Yes', 'Fair', 'Yes'],
    ['Medium', 'No', 'Fair', 'Yes'],
    ['Low', 'Yes', 'Fair', 'Yes'],
    ['Low', 'Yes', 'Excellent', 'No'],
    ['Medium', 'Yes', 'Excellent', 'Yes'],
    ['High', 'No', 'Fair', 'No'],
    ['Medium', 'Yes', 'Fair', 'Yes'],
    ['Low', 'No', 'Excellent', 'Yes'],
    ['High', 'Yes', 'Excellent', 'Yes'],
    ['Medium', 'No', 'Excellent', 'Yes']
]

attributes = ['Income', 'Student', 'Credit_Rating']

# --- ID3 Algorithm Functions ---
def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    ent = 0
    for c in counts:
        p = counts[c] / total
        ent -= p * math.log2(p)
    return ent

def information_gain(data, index):
    total_entropy = entropy(data)
    total = len(data)
    values = set(row[index] for row in data)
    weighted_entropy = 0
    
    for v in values:
        subset = [row for row in data if row[index] == v]
        weighted_entropy += (len(subset) / total) * entropy(subset)
        
    return total_entropy - weighted_entropy

def id3(data, attrs):
    labels = [row[-1] for row in data]
    
    # Base Case 1: All labels are the same
    if labels.count(labels[0]) == len(labels):
        return labels[0]
        
    # Base Case 2: No more attributes left to split
    if not attrs:
        return Counter(labels).most_common(1)[0][0]

    # Find the best attribute
    gains = [information_gain(data, i) for i in range(len(attrs))]
    best_idx = gains.index(max(gains))
    best_attr = attrs[best_idx]
    
    # Initialize the tree with the best attribute
    tree = {best_attr: {}}
    values = set(row[best_idx] for row in data)
    
    # Build branches recursively
    for v in values:
        subset = [row[:best_idx] + row[best_idx+1:] for row in data if row[best_idx] == v]
        new_attrs = attrs[:best_idx] + attrs[best_idx+1:]
        
        if not subset:
            tree[best_attr][v] = Counter(labels).most_common(1)[0][0]
        else:
            tree[best_attr][v] = id3(subset, new_attrs)

    return tree

# --- Execution ---
if __name__ == "__main__":
    print(f"Synthetic Dataset loaded with {len(dataset)} rows.")
    print("Total Entropy:", round(entropy(dataset), 4))
    
    print("\nInformation Gain Values:")
    for i in range(len(attributes)):
        print(f"{attributes[i]}: {round(information_gain(dataset, i), 4)}")
        
    decision_tree = id3(dataset, attributes)
    
    print("\nFinal Decision Tree:")
    pprint.pprint(decision_tree)
