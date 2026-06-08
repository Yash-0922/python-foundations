"""
Topic: Type Conversion in Python
Covers: implicit vs explicit conversion, common pitfalls, real-world use cases
Author: [Your Name]
Date: [Date]

INTERVIEW TIP: Python uses DUCK TYPING — "if it walks like a duck and quacks
like a duck, it's a duck." Type conversion errors are one of the most common
bugs in real data pipelines.
"""

# ─────────────────────────────────────────────
# 1. Checking Types
# ─────────────────────────────────────────────

print("=" * 50)
print("1. CHECKING TYPES")
print("=" * 50)

values = [42, 3.14, "hello", True, None, [1, 2], {"a": 1}]

for val in values:
    print(f"  {str(val):15} | type: {type(val).__name__:8} | isinstance(int): {isinstance(val, int)}")

# INTERVIEW TIP: isinstance() is preferred over type() for checking types
# because isinstance handles inheritance (bool IS a subclass of int!)
print(f"\ntype(True) == int  : {type(True) == int}")   # False — exact match
print(f"isinstance(True, int): {isinstance(True, int)}")  # True — inheritance


# ─────────────────────────────────────────────
# 2. Explicit Type Conversion (Casting)
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("2. EXPLICIT TYPE CONVERSION")
print("=" * 50)

# int()
print(f"int('42')     : {int('42')}")
print(f"int(3.99)     : {int(3.99)}")    # truncates, does NOT round
print(f"int(True)     : {int(True)}")    # True = 1, False = 0
print(f"int('0b1010') : N/A — use int('0b1010', 2) = {int('0b1010', 2)}")  # binary

# float()
print(f"\nfloat('3.14') : {float('3.14')}")
print(f"float(5)      : {float(5)}")
print(f"float('inf')  : {float('inf')}")   # positive infinity

# str()
print(f"\nstr(42)       : '{str(42)}'")
print(f"str(3.14)     : '{str(3.14)}'")
print(f"str(True)     : '{str(True)}'")
print(f"str([1,2,3])  : '{str([1,2,3])}'")

# bool()
print("\nbool() — what is FALSY in Python:")
falsy_values = [0, 0.0, "", [], {}, set(), None, False]
for val in falsy_values:
    print(f"  bool({str(val):8}) = {bool(val)}")

# list(), tuple(), set()
text: str = "hello"
print(f"\nlist('hello') : {list(text)}")
print(f"tuple([1,2,3]): {tuple([1, 2, 3])}")
print(f"set([1,1,2,3]): {set([1, 1, 2, 3])}")


# ─────────────────────────────────────────────
# 3. Implicit Conversion (Python does automatically)
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("3. IMPLICIT CONVERSION")
print("=" * 50)

result = 5 + 3.0       # int + float → float
print(f"5 + 3.0   = {result} ({type(result).__name__})")

result2 = True + 1     # bool + int → int
print(f"True + 1  = {result2} ({type(result2).__name__})")

result3 = True + True  # bool + bool → int
print(f"True+True = {result3} ({type(result3).__name__})")

# INTERVIEW TIP: Python NEVER implicitly converts str + int (raises TypeError)
# This is a common gotcha when reading CSV data — all columns come as strings!


# ─────────────────────────────────────────────
# 4. Common Pitfalls & Gotchas
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("4. COMMON PITFALLS")
print("=" * 50)

# Pitfall 1: int() truncates, not rounds
print(f"int(9.9)  = {int(9.9)}  ← NOT 10! Use round(9.9) = {round(9.9)}")

# Pitfall 2: float precision
a = 0.1 + 0.2
print(f"0.1 + 0.2 = {a}  ← floating point imprecision!")
print(f"round fix : {round(a, 2)}")

# Pitfall 3: str → int fails for floats
try:
    bad = int("3.14")
except ValueError as e:
    print(f"int('3.14') error : {e}")
    print(f"fix: int(float('3.14')) = {int(float('3.14'))}")

# Pitfall 4: bool can silently act as int in sum
flags = [True, False, True, True, False]
print(f"\nsum of booleans : {sum(flags)}  ← counts True values!")


# ─────────────────────────────────────────────
# 5. Real-world: Clean a raw CSV row
# ─────────────────────────────────────────────

def clean_csv_row(raw_row: dict[str, str]) -> dict:
    """
    Convert a raw CSV row (all strings) into proper Python types.
    This is what Pandas does internally — important to understand.

    Args:
        raw_row: dict with all values as strings (from CSV reader)

    Returns:
        dict with values cast to appropriate types

    Example:
        >>> clean_csv_row({"age": "23", "salary": "45000.5", "active": "True"})
        {'age': 23, 'salary': 45000.5, 'active': True}
    """
    cleaned: dict = {}
    for key, value in raw_row.items():
        value = value.strip()

        # Try integer first
        try:
            cleaned[key] = int(value)
            continue
        except ValueError:
            pass

        # Try float
        try:
            cleaned[key] = float(value)
            continue
        except ValueError:
            pass

        # Try boolean
        if value.lower() in ("true", "yes", "1"):
            cleaned[key] = True
            continue
        if value.lower() in ("false", "no", "0"):
            cleaned[key] = False
            continue

        # Handle None/empty
        if value.lower() in ("null", "none", "na", "n/a", ""):
            cleaned[key] = None
            continue

        # Keep as string
        cleaned[key] = value

    return cleaned


print("\n" + "=" * 50)
print("5. REAL-WORLD: CSV ROW CLEANING")
print("=" * 50)

raw_rows: list[dict[str, str]] = [
    {"name": "Arjun", "age": "24", "salary": "52000.5", "active": "True",  "dept": "Analytics"},
    {"name": "Pooja", "age": "28", "salary": "68000",   "active": "False", "dept": "Data Science"},
    {"name": "Ravi",  "age": "NA", "salary": "null",    "active": "yes",   "dept": "ML"},
]

for raw in raw_rows:
    cleaned = clean_csv_row(raw)
    print(f"\n  raw     : {raw}")
    print(f"  cleaned : {cleaned}")
    print(f"  types   : { {k: type(v).__name__ for k, v in cleaned.items()} }")


# ─────────────────────────────────────────────
# INTERVIEW QUICK REFERENCE
# ─────────────────────────────────────────────
"""
COMMON INTERVIEW QUESTIONS:

Q1: What is the difference between implicit and explicit type conversion?
    → Implicit: Python does it automatically (int + float → float).
      Explicit: You do it manually with int(), str(), float(), etc.

Q2: Why does int(3.99) give 3 and not 4?
    → int() TRUNCATES toward zero, not rounds. Use round() for rounding.

Q3: Is bool a subclass of int in Python?
    → Yes! True == 1 and False == 0. So True + True == 2.

Q4: Why does 0.1 + 0.2 != 0.3 in Python?
    → Floating point representation issue (base-2 math). 
      Fix: use round(), decimal.Decimal, or math.isclose().

Q5: How to safely convert a string that might not be a number?
    → Use try/except ValueError around int() or float().
"""
