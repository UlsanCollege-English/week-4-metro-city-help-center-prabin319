# Weekly Coding #4— Metro City Help Center
## Data Structures, Spring 2026

## Snapshot
- **Topic:** Stacks and queues
- **Standards focus:** S7 primary, plus clear functions/tests from earlier weeks
- **Language:** Python 3.11+
- **Allowed libraries:** Standard library only
- **Submit:** `src/challenges.py` + `tests/test_challenges.py` + `README.md`
- **Also due:** Journal #4

## Story
Metro City Help Center is building a small support system.

Different parts of the system need different data structures:

- recent staff actions should be tracked so they can be undone
- waiting citizens should be served in arrival order
- request notes should be checked for balanced brackets before being saved
- the help center should be able to process its waiting line correctly

Your job is to build the small parts of that system.

## Big idea
This week is about using the right structure for the behavior you need:

- **Stack** -> last in, first out (**LIFO**)
- **Queue** -> first in, first out (**FIFO**)

For this course:
- use a **`list`** for stack behavior
- use a **`deque`** for queue behavior

## Learning goals
By completing this homework, you should be able to:
- implement stack behavior with a `list`
- implement queue behavior with a `deque`
- choose stack vs queue from a short real-world prompt
- handle empty cases safely
- write short `pytest` tests for the core behavior

## Files to submit
```text
src/challenges.py
tests/test_challenges.py
README.md
.github/workflows/tests.yml
```

## Required work

### Part 1 — `ActionStack`
Metro City Help Center wants to track recent staff actions so the most recent action can be undone first.

Create an `ActionStack` class with these methods:

- `push(action: str) -> None`
- `pop() -> str | None`
- `peek() -> str | None`
- `is_empty() -> bool`

#### Rules
- Use a Python `list`
- If the stack is empty, `pop()` should return `None`
- If the stack is empty, `peek()` should return `None`

#### Example
```python
stack = ActionStack()
stack.push("open ticket")
stack.push("assign worker")
stack.pop()   # "assign worker"
```

---

### Part 2 — `RequestQueue`
Citizens arrive at the help center in order. The first person to arrive should be the first person served.

Create a `RequestQueue` class with these methods:

- `enqueue(name: str) -> None`
- `dequeue() -> str | None`
- `peek() -> str | None`
- `is_empty() -> bool`

#### Rules
- Use `deque` from `collections`
- If the queue is empty, `dequeue()` should return `None`
- If the queue is empty, `peek()` should return `None`

#### Example
```python
queue = RequestQueue()
queue.enqueue("Mina")
queue.enqueue("Jay")
queue.dequeue()   # "Mina"
```

---

### Part 3 — `is_note_balanced`
Before saving a help-center note, the system checks whether brackets are balanced correctly.

Write a function:

```python
def is_note_balanced(note: str) -> bool:
```

Return `True` if all brackets are balanced correctly, and `False` otherwise.

Check these bracket types:
- `()`
- `[]`
- `{}`

#### Examples
```python
is_note_balanced("Call back (urgent)")                  # True
is_note_balanced("Repair request [building A]")         # True
is_note_balanced("Issue details: {network}[floor 2]")   # True
is_note_balanced("(]")                                  # False
is_note_balanced("(()")                                 # False
```

#### Rule
- Use **stack behavior**
- A plain `list` is fine here

---

### Part 4 — `process_request_line`
At the end of the hour, the help center processes waiting citizens in arrival order.

Write a function:

```python
def process_request_line(citizens: list[str]) -> list[str]:
```

Return a new list showing the order citizens are served.

#### Example
```python
process_request_line(["Mina", "Jay", "Omar"])
# returns ["Mina", "Jay", "Omar"]
```

#### Rules
- Use **queue behavior**
- Use `deque`
- If the input list is empty, return `[]`

## Stretch challenge (optional, not required)
### `undo_recent_actions`
Write a function:

```python
def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
```

Treat `actions` like a stack of completed help-center actions.
Remove the most recent `undo_count` actions and return the remaining actions.

#### Example
```python
undo_recent_actions(["open ticket", "assign worker", "close ticket"], 2)
# returns ["open ticket"]
```

## README requirements
Your `README.md` must include:

### 1. Summary
1–3 sentences explaining the story and the week’s topic.

### 2. Complexity
Give time complexity for:
- `ActionStack.pop`
- `RequestQueue.dequeue`
- `is_note_balanced`
- `process_request_line`

Add a short reason for each.

### 3. Edge-case checklist
Explain how your code handles:
- empty action stack
- empty request queue
- empty string for `is_note_balanced`
- note with no brackets
- empty citizen list

### 4. Assistance & sources
Include:
- AI used? (Y/N)
- What it helped with
- Any outside sources

## Testing expectations
You must write tests for:
- normal action-stack behavior
- empty action-stack behavior
- normal request-queue behavior
- empty request-queue behavior
- at least 4 `is_note_balanced` cases
- empty and normal `process_request_line`

## Style rules
- stdlib only
- PEP 8
- type hints on public functions
- docstrings on public functions
- small, readable functions

## Advice
Start in this order:
1. `ActionStack`
2. `RequestQueue`
3. `is_note_balanced`
4. `process_request_line`
5. tests
6. README

Do not try to write everything at once.
