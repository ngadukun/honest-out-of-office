"""The Painfully Honest Out-of-Office.

A single out-of-office email auto-reply, painfully honest about the
sender's absence, inbox and enthusiasm, yet still polite enough that
a manager would let it stand. Running this module prints the entry.
"""

ENTRY = (
    "I'm out of the office until Monday, ignoring email with great "
    "enthusiasm and limited guilt. For anything urgent, please ask "
    "someone who is actually here."
)


def main():
    print(ENTRY)


if __name__ == "__main__":
    main()
