"""
Given a string of brackets, return True if they are all correctly opened and closed.
Uses a stack to push opening brackets and pop/check on closing ones.
"""


MATCHING = {')': '(', ']': '[', '}': '{'}


def is_valid(s: str) -> bool:
    """Return True if all brackets in s are correctly matched and closed."""
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != MATCHING[ch]:
                return False
            stack.pop()
    return len(stack) == 0


def main() -> None:
    test_cases = [
        ("()",        True),
        ("()[]{}",    True),
        ("(]",        False),
        ("([)]",      False),
        ("{[]}",      True),
        ("",          True),
        ("[",         False),
        ("(((",        False),
    ]

    print("Valid Parentheses")
    print("=" * 40)
    all_passed = True
    for s, expected in test_cases:
        result = is_valid(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        display = f'"{s}"' if s else '""  (empty)'
        print(f"  {status}  is_valid({display}) = {result}")

    print()
    print("All tests passed." if all_passed else "Some tests failed.")


if __name__ == "__main__":
    main()