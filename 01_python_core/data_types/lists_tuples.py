"""
Topic: Lists & Tuples in Python
Covers: creation, indexing, slicing, methods, list vs tuple, when to use each
Author: [Your Name]
Date: [Date]

INTERVIEW TIP: List = mutable (changeable), Tuple = immutable (fixed).
Use tuples for data that should NOT change (coordinates, DB records, RGB values).
"""

# ─────────────────────────────────────────────
# 1. List Basics
# ─────────────────────────────────────────────

print("=" * 50)
print("1. LIST BASICS")
print("=" * 50)

marks: list[int] = [85, 92, 78, 95, 88]
names: list[str] = ["Amit", "Sneha", "Raj", "Priya"]
mixed: list = [1, "hello", 3.14, True, None]     # lists allow mixed types

print(f"marks    : {marks}")
print(f"names    : {names}")
print(f"mixed    : {mixed}")
print(f"length   : {len(marks)}")
print(f"max mark : {max(marks)}")
print(f"min mark : {min(marks)}")
print(f"sum      : {sum(marks)}")
print(f"avg      : {sum(marks)/len(marks):.2f}")


# ─────────────────────────────────────────────
# 2. List Methods (must-know for interviews)
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("2. LIST METHODS")
print("=" * 50)

fruits: list[str] = ["mango", "banana", "apple"]
print(f"original : {fruits}")

fruits.append("grape")               # add to end
print(f"append() : {fruits}")

fruits.insert(1, "orange")           # insert at index
print(f"insert() : {fruits}")

fruits.remove("banana")              # remove by value (first occurrence)
print(f"remove() : {fruits}")

popped: str = fruits.pop()           # remove and return last element
print(f"pop()    : removed '{popped}', list = {fruits}")

popped_idx: str = fruits.pop(0)      # pop by index
print(f"pop(0)   : removed '{popped_idx}', list = {fruits}")

fruits.sort()                        # sort in-place (modifies original)
print(f"sort()   : {fruits}")

fruits.sort(reverse=True)
print(f"sort(rev): {fruits}")

fruits_copy: list = fruits.copy()    # shallow copy — important!
print(f"copy()   : {fruits_copy}")

print(f"index()  : 'apple' is at index {fruits.index('apple')}")
print(f"count()  : 'mango' appears {fruits.count('mango')} time(s)")

# INTERVIEW TIP: sort() modifies in-place, sorted() returns new list


# ─────────────────────────────────────────────
# 3. List Slicing
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("3. LIST SLICING")
print("=" * 50)

numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"numbers        : {numbers}")
print(f"first 3        : {numbers[:3]}")
print(f"last 3         : {numbers[-3:]}")
print(f"middle         : {numbers[3:7]}")
print(f"every 2nd      : {numbers[::2]}")
print(f"reversed       : {numbers[::-1]}")
print(f"copy via slice : {numbers[:]}  (same as .copy())")


# ─────────────────────────────────────────────
# 4. Nested Lists (2D — used in data/matrices)
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("4. NESTED LISTS (2D MATRIX)")
print("=" * 50)

matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(" ", row)

print(f"element [1][2] : {matrix[1][2]}")   # row 1, col 2 → 6

# Flatten a 2D list
flat: list[int] = [val for row in matrix for val in row]
print(f"flattened      : {flat}")


# ─────────────────────────────────────────────
# 5. Tuples — Immutable Sequences
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("5. TUPLES")
print("=" * 50)

coordinates: tuple[float, float] = (28.6139, 77.2090)   # Delhi lat/lon
rgb_red: tuple[int, int, int] = (255, 0, 0)
single: tuple = (42,)            # single-element tuple needs trailing comma!

print(f"coordinates : {coordinates}")
print(f"rgb_red     : {rgb_red}")
print(f"single      : {single}  ← note the comma")
print(f"type check  : {type(single)}")

# Tuple unpacking — very Pythonic
lat, lon = coordinates
print(f"unpacked    : lat={lat}, lon={lon}")

# Swap two variables (Python magic using tuples)
a, b = 10, 20
a, b = b, a
print(f"after swap  : a={a}, b={b}")

# Tuple methods — only 2 (count, index)
scores: tuple[int, ...] = (85, 92, 85, 78, 92, 85)
print(f"count(85)   : {scores.count(85)}")
print(f"index(92)   : {scores.index(92)}")


# ─────────────────────────────────────────────
# 6. List vs Tuple — When to use which
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("6. LIST vs TUPLE COMPARISON")
print("=" * 50)

comparison: dict = {
    "Feature":     ["Mutable",  "Syntax",    "Speed",    "Use case"],
    "List  [ ]":   ["Yes",      "[1,2,3]",   "Slower",   "Dynamic data, add/remove"],
    "Tuple ( )":   ["No",       "(1,2,3)",   "Faster",   "Fixed data, dict keys, unpack"],
}

for feature, lst, tpl in zip(
    comparison["Feature"],
    comparison["List  [ ]"],
    comparison["Tuple ( )"]
):
    print(f"  {feature:12} | List: {lst:25} | Tuple: {tpl}")


# ─────────────────────────────────────────────
# 7. Real-world: Student grade analysis
# ─────────────────────────────────────────────

def analyze_grades(student_marks: list[int]) -> dict:
    """
    Analyze a list of student marks and return summary statistics.

    Args:
        student_marks: list of integer marks (0–100)

    Returns:
        dict with average, highest, lowest, pass_count, fail_count

    Example:
        >>> analyze_grades([85, 92, 34, 78, 45, 90])
        {'average': 70.67, 'highest': 92, 'lowest': 34, 'pass_count': 4, 'fail_count': 2}
    """
    if not student_marks:
        return {}

    sorted_marks: list[int] = sorted(student_marks)
    pass_marks: list[int] = [m for m in student_marks if m >= 40]
    fail_marks: list[int] = [m for m in student_marks if m < 40]

    return {
        "average":    round(sum(student_marks) / len(student_marks), 2),
        "highest":    sorted_marks[-1],
        "lowest":     sorted_marks[0],
        "median":     sorted_marks[len(sorted_marks) // 2],
        "pass_count": len(pass_marks),
        "fail_count": len(fail_marks),
        "top_3":      sorted_marks[-3:][::-1],
    }


print("\n" + "=" * 50)
print("7. REAL-WORLD: GRADE ANALYSIS")
print("=" * 50)

class_marks: list[int] = [85, 92, 34, 78, 45, 90, 38, 72, 55, 88]
result: dict = analyze_grades(class_marks)

print(f"Marks    : {class_marks}")
for key, value in result.items():
    print(f"  {key:12}: {value}")


# ─────────────────────────────────────────────
# INTERVIEW QUICK REFERENCE
# ─────────────────────────────────────────────
"""
COMMON INTERVIEW QUESTIONS:

Q1: What is the difference between list and tuple?
    → List: mutable, slower, uses more memory.
      Tuple: immutable, faster, can be used as dict key.

Q2: How to remove duplicates from a list?
    → list(set(my_list)) — but loses order.
      Use dict.fromkeys(my_list) to preserve order.

Q3: What is a shallow vs deep copy?
    → .copy() = shallow (nested objects still shared).
      import copy; copy.deepcopy() = true independent copy.

Q4: How do you sort a list of tuples by the second element?
    → sorted(list_of_tuples, key=lambda x: x[1])

Q5: Can a tuple be used as a dictionary key?
    → Yes, because it's immutable and hashable. Lists cannot.
"""
