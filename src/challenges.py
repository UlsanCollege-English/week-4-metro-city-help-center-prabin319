"""Weekly Coding #3 starter code: Metro City Help Center.

Implement the required classes and functions below.
Use standard library only.
"""

from __future__ import annotations

from collections import deque


class ActionStack:
    """Stack of recent help-center actions using a Python list."""

    def __init__(self) -> None:
        self.items: list[str] = []

    def push(self, action: str) -> None:
        """Add an action to the top of the stack."""
        self.items.append(action)

    def pop(self) -> str | None:
        """Remove and return the top action, or None if empty."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self) -> str | None:
        """Return the top action without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no actions."""
        return len(self.items) == 0


class RequestQueue:
    """Queue of waiting citizens using collections.deque."""

    def __init__(self) -> None:
        self.items: deque[str] = deque()

    def enqueue(self, name: str) -> None:
        """Add a citizen name to the back of the queue."""
        self.items.append(name)

    def dequeue(self) -> str | None:
        """Remove and return the front citizen, or None if empty."""
        if self.is_empty():
            return None
        return self.items.popleft()

    def peek(self) -> str | None:
        """Return the front citizen without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no waiting citizens."""
        return len(self.items) == 0


def is_note_balanced(note: str) -> bool:
    """Return True if (), [], and {} are balanced correctly in a note."""
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for char in note:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    return len(stack) == 0


def process_request_line(citizens: list[str]) -> list[str]:
    """Return citizens in the order they are served."""
    queue = RequestQueue()
    for citizen in citizens:
        queue.enqueue(citizen)
    served = []
    while not queue.is_empty():
        served.append(queue.dequeue())
    return served


def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
    """Optional stretch: remove the most recent undo_count actions."""
    stack = ActionStack()
    for action in actions:
        stack.push(action)
    for _ in range(undo_count):
        if stack.is_empty():
            break
        stack.pop()
    return stack.items.copy()