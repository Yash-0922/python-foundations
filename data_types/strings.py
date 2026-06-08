"""
Topic: String Data Type in Python
Covers: creation, indexing, slicing, methods, formatting, f-strings
Author: [Your Name]
Date: [Date]

INTERVIEW TIP: Strings in Python are IMMUTABLE — you can never change a
string in place. Every method returns a NEW string.
"""

# ─────────────────────────────────────────────
# 1. String Creation & Basics
# ─────────────────────────────────────────────

name: str = "Arjun Sharma"
city: str = 'Mumbai'
multiline: str = """This is a
multiline string used for
long text or docstrings."""

print("=" * 50)
print("1. STRING BASICS")
print("=" * 50)
print(f"name      : {name}")
print(f"type      : {type(name)}")
print(f"length    : {len(name)}")
print(f"uppercase : {name.upper()}")
print(f"lowercase : {name.lower()}")


# ─────────────────────────────────────────────
# 2. Indexing & Slicing
# ─────────────────────────────────────────────

word: str = "PYTHON"

print("\n" + "=" * 50)
print("2. INDEXING & SLICING")
print("=" * 50)
print(f"word           : {word}")
print(f"first char     : {word[0]}")       # P
print(f"last char      : {word[-1]}")      # N
print(f"slice [0:3]    : {word[0:3]}")     # PYT
print(f"every 2nd char : {word[::2]}")     # PTO
print(f"reversed       : {word[::-1]}")    # NOHTYP

# INTERVIEW TIP: word[start:stop:step] — stop is EXCLUSIVE


# ─────────────────────────────────────────────
# 3. Common String Methods
# ─────────────────────────────────────────────

sentence: str = "  hello, world! welcome to python.  "

print("\n" + "=" * 50)
print("3. STRING METHODS")
print("=" * 50)
print(f"original  : '{sentence}'")
print(f"strip()   : '{sentence.strip()}'")
print(f"title()   : '{sentence.strip().title()}'")
print(f"replace() : '{sentence.strip().replace('python', 'DATA SCIENCE')}'")
print(f"split()   : {sentence.strip().split(', ')}")
print(f"startswith: {sentence.strip().startswith('hello')}")
print(f"endswith  : {sentence.strip().endswith('.')}")
print(f"count('o'): {sentence.count('o')}")
print(f"find('wor'): {sentence.find('world')}")   # returns index or -1


# ─────────────────────────────────────────────
# 4. String Formatting (3 ways — know all 3)
# ─────────────────────────────────────────────

person: str = "Priya"
score: float = 92.5
rank: int = 3

print("\n" + "=" * 50)
print("4. STRING FORMATTING")
print("=" * 50)

# Old style (% formatting) — you may see this in legacy code
print("Old style  : %s scored %.1f and ranked %d" % (person, score, rank))

# .format() — Python 2/3 compatible
print(".format()  : {} scored {:.1f} and ranked {}".format(person, score, rank))

# f-strings — PREFERRED (Python 3.6+)
print(f"f-string   : {person} scored {score:.1f} and ranked {rank}")
print(f"expression : {person.upper()} has {'Pass' if score >= 40 else 'Fail'}")

# INTERVIEW TIP: f-strings support expressions inside {}
# {score:.2f} = 2 decimal places, {num:,} = thousand separator


# ─────────────────────────────────────────────
# 5. String Joining & Splitting
# ─────────────────────────────────────────────

skills: list = ["Python", "Pandas", "SQL", "Power BI"]

print("\n" + "=" * 50)
print("5. JOIN & SPLIT")
print("=" * 50)

joined: str = ", ".join(skills)
print(f"join()  : {joined}")

csv_line: str = "Delhi,Mumbai,Bangalore,Chennai"
cities: list = csv_line.split(",")
print(f"split() : {cities}")

# Joining back
print(f"rejoin  : {' | '.join(cities)}")


# ─────────────────────────────────────────────
# 6. String Checking Methods
# ─────────────────────────────────────────────

samples: list[str] = ["Hello123", "12345", "hello", "HELLO", "   "]

print("\n" + "=" * 50)
print("6. STRING CHECKING METHODS")
print("=" * 50)
for s in samples:
    print(
        f"'{s}' → isalpha={s.isalpha()}, "
        f"isdigit={s.isdigit()}, "
        f"isupper={s.isupper()}, "
        f"isspace={s.isspace()}"
    )


# ─────────────────────────────────────────────
# 7. Real-world: Clean messy user input
# ─────────────────────────────────────────────

def clean_name(raw_input: str) -> str:
    """
    Clean and normalize a user-entered name.

    Args:
        raw_input: raw string from user input (may have spaces, wrong case)

    Returns:
        Cleaned, title-cased name

    Example:
        >>> clean_name("  rAHUL verMa  ")
        'Rahul Verma'
    """
    return raw_input.strip().title()


def is_valid_email(email: str) -> bool:
    """
    Basic email validation using string methods (no regex).

    Args:
        email: email address to validate

    Returns:
        True if email has '@' and a '.' after '@', else False
    """
    if "@" not in email:
        return False
    local, domain = email.split("@", 1)
    return len(local) > 0 and "." in domain


print("\n" + "=" * 50)
print("7. REAL-WORLD: INPUT CLEANING")
print("=" * 50)

raw_names: list[str] = ["  rAHUL verMa  ", "PRIYA SINGH", "ankit"]
for raw in raw_names:
    print(f"'{raw}' → '{clean_name(raw)}'")

print()
emails: list[str] = ["user@example.com", "bademail.com", "@nodomain", "ok@site.co.in"]
for email in emails:
    status = "✓ valid" if is_valid_email(email) else "✗ invalid"
    print(f"{email:25} → {status}")


# ─────────────────────────────────────────────
# INTERVIEW QUICK REFERENCE
# ─────────────────────────────────────────────
"""
COMMON INTERVIEW QUESTIONS ON STRINGS:
Q1: Are strings mutable in Python?
    → No. s[0] = 'X' raises TypeError. Use list(s) to mutate, then join.

Q2: How do you reverse a string?
    → s[::-1]  ← most Pythonic way

Q3: How to check if a string is a palindrome?
    → s == s[::-1]

Q4: Difference between find() and index()?
    → find() returns -1 if not found; index() raises ValueError.

Q5: How to count occurrences of a substring?
    → s.count('sub') — overlapping counted separately with manual loop.
"""
