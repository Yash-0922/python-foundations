"""
Topic: Dictionaries & Sets in Python
Covers: creation, CRUD, methods, dict comprehension, set operations
Author: [Your Name]
Date: [Date]

INTERVIEW TIP: Dictionaries in Python 3.7+ maintain INSERTION ORDER.
Sets are UNORDERED and store only UNIQUE values.
Both use hashing internally — O(1) average lookup time.
"""

# ─────────────────────────────────────────────
# 1. Dictionary Basics
# ─────────────────────────────────────────────

print("=" * 50)
print("1. DICTIONARY BASICS")
print("=" * 50)

student: dict = {
    "name":   "Rohan Mehta",
    "age":    22,
    "city":   "Pune",
    "skills": ["Python", "SQL", "Excel"],
    "active": True
}

print(f"student   : {student}")
print(f"name      : {student['name']}")            # direct access
print(f"age       : {student.get('age')}")         # safe access
print(f"missing   : {student.get('gpa', 'N/A')}")  # default if key missing
print(f"keys      : {list(student.keys())}")
print(f"values    : {list(student.values())}")
print(f"items     : {list(student.items())}")       # list of (key, value) tuples


# ─────────────────────────────────────────────
# 2. CRUD Operations on Dictionaries
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("2. CREATE / READ / UPDATE / DELETE")
print("=" * 50)

inventory: dict[str, int] = {"apples": 10, "bananas": 5, "oranges": 8}
print(f"initial   : {inventory}")

# Create / Update
inventory["mangoes"] = 15                      # add new key
inventory["apples"] = 12                       # update existing key
print(f"after add : {inventory}")

# Update multiple at once
inventory.update({"bananas": 20, "grapes": 7})
print(f"update()  : {inventory}")

# Delete
del inventory["oranges"]                       # raises KeyError if missing
removed = inventory.pop("grapes", 0)           # safe remove, returns value
print(f"after del : {inventory}  (removed grapes: {removed})")

# Check key existence
print(f"'mangoes' in inventory : {'mangoes' in inventory}")
print(f"'oranges' in inventory : {'oranges' in inventory}")


# ─────────────────────────────────────────────
# 3. Iterating Over Dictionaries
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("3. ITERATING OVER DICTS")
print("=" * 50)

scores: dict[str, int] = {
    "Ananya": 88,
    "Vikram": 74,
    "Divya":  92,
    "Karan":  65,
}

# Iterate over keys
print("Keys only :")
for name in scores:
    print(f"  {name}")

# Iterate over values
print("Values only :")
for score in scores.values():
    print(f"  {score}")

# Iterate over key-value pairs — most common
print("Key-value pairs :")
for name, score in scores.items():
    grade = "A" if score >= 85 else "B" if score >= 70 else "C"
    print(f"  {name:10} → {score}  ({grade})")


# ─────────────────────────────────────────────
# 4. Dictionary Comprehension
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("4. DICT COMPREHENSION")
print("=" * 50)

# Basic: square each number
squares: dict[int, int] = {n: n**2 for n in range(1, 6)}
print(f"squares          : {squares}")

# Filtered: only passing scores
passing: dict[str, int] = {name: s for name, s in scores.items() if s >= 75}
print(f"passing students : {passing}")

# Transform: convert Celsius to Fahrenheit
temps_c: dict[str, float] = {"Delhi": 38.5, "Mumbai": 32.0, "Shimla": 15.0}
temps_f: dict[str, float] = {city: round(c * 9/5 + 32, 1) for city, c in temps_c.items()}
print(f"celsius          : {temps_c}")
print(f"fahrenheit       : {temps_f}")

# Invert a dictionary (swap keys and values)
original: dict = {"a": 1, "b": 2, "c": 3}
inverted: dict = {v: k for k, v in original.items()}
print(f"inverted dict    : {inverted}")


# ─────────────────────────────────────────────
# 5. Nested Dictionaries
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("5. NESTED DICTIONARIES")
print("=" * 50)

employees: dict = {
    "E001": {"name": "Riya Shah",  "dept": "Analytics", "salary": 55000},
    "E002": {"name": "Amit Joshi", "dept": "ML",         "salary": 72000},
    "E003": {"name": "Neha Patel", "dept": "Analytics",  "salary": 60000},
}

# Access nested value
print(f"E002 name   : {employees['E002']['name']}")
print(f"E002 salary : ₹{employees['E002']['salary']:,}")

# Iterate nested dict
print("\nAll employees:")
for emp_id, details in employees.items():
    print(f"  {emp_id} | {details['name']:12} | {details['dept']:10} | ₹{details['salary']:,}")

# Find highest salary
top_earner_id: str = max(employees, key=lambda eid: employees[eid]["salary"])
print(f"\nTop earner : {employees[top_earner_id]['name']} (₹{employees[top_earner_id]['salary']:,})")


# ─────────────────────────────────────────────
# 6. Sets — Unique Unordered Collections
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("6. SETS")
print("=" * 50)

# Creating sets
skills_a: set = {"Python", "SQL", "Excel", "Tableau"}
skills_b: set = {"Python", "R", "SQL", "Power BI"}

print(f"skills_a : {skills_a}")
print(f"skills_b : {skills_b}")

# Set operations — very useful in data work
print(f"\nunion (all skills)        : {skills_a | skills_b}")
print(f"intersection (common)     : {skills_a & skills_b}")
print(f"difference (a not in b)   : {skills_a - skills_b}")
print(f"symmetric diff (unique ea): {skills_a ^ skills_b}")

# Membership test — O(1) vs O(n) for list
large_set: set = set(range(1_000_000))
print(f"\n999999 in large_set : {999999 in large_set}")   # instant

# Remove duplicates from a list using set
raw: list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique: list = list(set(raw))
print(f"\nremove duplicates : {raw} → {sorted(unique)}")


# ─────────────────────────────────────────────
# 7. Real-world: Word frequency counter
# ─────────────────────────────────────────────

def word_frequency(text: str) -> dict[str, int]:
    """
    Count the frequency of each word in a text string.

    Args:
        text: input string to analyze

    Returns:
        dict mapping word → count, sorted by frequency (descending)

    Example:
        >>> word_frequency("python is great and python is easy")
        {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'easy': 1}
    """
    words: list[str] = text.lower().split()
    freq: dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Sort by frequency descending
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def find_common_skills(candidates: list[list[str]]) -> set[str]:
    """
    Find skills common to ALL candidates using set intersection.

    Args:
        candidates: list of skill lists (one list per candidate)

    Returns:
        set of skills that ALL candidates possess
    """
    if not candidates:
        return set()
    skill_sets: list[set] = [set(skills) for skills in candidates]
    return skill_sets[0].intersection(*skill_sets[1:])


print("\n" + "=" * 50)
print("7. REAL-WORLD EXAMPLES")
print("=" * 50)

# Word frequency
review: str = "the data science course is great the content is clear and great"
freq_result: dict = word_frequency(review)
print("Word frequency (top 5):")
for word, count in list(freq_result.items())[:5]:
    print(f"  '{word}' : {count}")

# Common skills
all_candidates: list[list[str]] = [
    ["Python", "SQL", "Excel", "Tableau"],
    ["Python", "SQL", "R", "Power BI"],
    ["Python", "SQL", "Excel", "Spark"],
]
common: set = find_common_skills(all_candidates)
print(f"\nSkills all 3 candidates share : {common}")


# ─────────────────────────────────────────────
# INTERVIEW QUICK REFERENCE
# ─────────────────────────────────────────────
"""
COMMON INTERVIEW QUESTIONS:

Q1: What is the time complexity of dict lookup?
    → O(1) average case due to hashing. O(n) worst case (hash collisions).

Q2: How are dict and set implemented internally?
    → Both use hash tables. Sets = dicts with only keys, no values.

Q3: Can you use a list as a dictionary key?
    → No. Keys must be hashable (immutable). Use tuple instead.

Q4: How to merge two dicts in Python 3.9+?
    → merged = dict1 | dict2  (pipe operator)
      Or: merged = {**dict1, **dict2}  (older way, still common)

Q5: What is defaultdict and when do you use it?
    → from collections import defaultdict
      d = defaultdict(int)  — auto-initializes missing keys to 0
      Used to avoid KeyError when counting frequencies.

Q6: Difference between set and frozenset?
    → set is mutable; frozenset is immutable and hashable (can be dict key).
"""
