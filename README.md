# Assignment 6: Medians and Order Statistics & Elementary Data Structures

### Student Name: Shreya Rai

### Course: Algorithms and Data Structures (MSCS-532-B01)

### Instructor: Michael Solomon

---

## **Overview**

This repository contains the implementation and analysis of selection algorithms (Median of Medians and Quickselect) and basic data structures (Stack, Queue, Linked List, Arrays/Matrices). The project demonstrates algorithm design, recursion, and elementary data structures, with empirical evaluation and time complexity analysis.

---

## **Directory Structure**

```
Assignment6/
│
├── part1_selection_algorithms/
│   ├── deterministic_selection.py   # Median of Medians algorithm
│   ├── randomized_selection.py     # Quickselect algorithm
│   ├── empirical_analysis.py       # Script to test and compare algorithms
│   └── requirements.txt            # Required Python packages
│
├── part2_data_structures/
│   ├── stack_queue.py              # Stack and Queue implementations
│   ├── linked_list.py              # Singly Linked List implementation
│   └── arrays_matrices.py          # Arrays and Matrices examples (optional)
│
├── report/
│   └── report.pdf                  # Full assignment report
│
└── README.md
```

---

## **Setup Instructions**

1. **Clone the repository:**

```bash
git clone https://github.com/ShreyaRai20/Assignment-6-Medians-Order-Statistics-Elementary-Data-Structures.git
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. **Install required Python packages:**

```bash
pip install -r part1_selection_algorithms/requirements.txt
```

> **Requirements include:**
>
> ```
> matplotlib
> numpy
> ```

---

## **Part 1: Selection Algorithms**

1. Navigate to the selection algorithms folder:

```bash
cd part1_selection_algorithms
```

2. Run the empirical analysis script to test both algorithms:

```bash
python empirical_analysis.py
```

3. Output will show execution times for deterministic and randomized algorithms for different input sizes.
4. Optional: Modify the script to generate runtime graphs using `matplotlib`.

---

## **Part 2: Elementary Data Structures**

1. Navigate to the data structures folder:

```bash
cd ../part2_data_structures
```

2. Open Python interactive mode to test implementations:

```bash
python
```

3. Import and run the data structures:

```python
from stack_queue import Stack, Queue
from linked_list import LinkedList
from arrays_matrices import Matrix  # Optional demonstration
```

4. Example commands:

```python
# Stack
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # Output: 20

# Queue
q = Queue()
q.enqueue(5)
q.enqueue(10)
print(q.dequeue())  # Output: 5

# Linked List
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
print(ll.traverse())  # Output: [1, 2, 3]
```

---

## **Report**

The full assignment report is available in `report/report.pdf`. It includes explanations, time complexity analysis, screenshots, and graphs.

---

## **Time Complexity**

Refer to the report for detailed tables of time complexities for selection algorithms and data structures.

---

## **Contributing**

This is an academic assignment; contributions are not expected. For learning purposes, feel free to extend the code with additional data structures or selection algorithms.

---

## **License**

This project is created for academic purposes by Shreya Rai and is not intended for commercial use.
