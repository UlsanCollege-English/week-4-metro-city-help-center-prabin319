[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KuuIFSwK)
# Weekly Coding #3 — Metro City Help Center

## Summary
This homework uses one connected story to practice stack and queue behavior in Python.

Metro City Help Center needs a small support system for recent staff actions, waiting citizens, request-note checks, and service-line processing.

## How to run
```bash
pytest -q
```

## Complexity
### `ActionStack.pop`
- Time: O(1)
- Why: Removing the last element of a Python list is always constant time, no matter how many items are in the stack.

### `RequestQueue.dequeue`
- Time: O(1)
- Why: collections.deque is designed for fast removals from both ends. popleft() removes the front element in constant time.

### `is_note_balanced`
- Time: O(n)
- Why: We loop through every character in the note exactly once. Each character is either pushed or popped from the stack in O(1), so the total is linear.

### `process_request_line`
- Time: O(n)
- Why: We enqueue all n citizens and then dequeue all n citizens. Each enqueue and dequeue is O(1), so the total is O(n).

## Edge-case checklist
- [x] empty action stack — `pop()` and `peek()` return `None`
- [x] empty request queue — `dequeue()` and `peek()` return `None`
- [x] empty string for `is_note_balanced` — returns `True` (nothing to mismatch)
- [x] note with no brackets — returns `True` (non-bracket characters are ignored)
- [x] empty citizen list — `process_request_line` returns an empty list `[]`

## Assistance & sources
- AI used? (Y/N): Y
- What it helped with: Understanding stack and queue behavior, complexity analysis, and edge case identification
- Other sources: Python official docs for collections.deque