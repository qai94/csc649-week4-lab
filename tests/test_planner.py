from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 4


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
# TODO 1: days_left is negative when the task is overdue.
def test_days_left_is_negative_when_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == -2

# TODO 2: is_urgent is True when the task is due tomorrow.
def test_is_urgent_when_due_tomorrow():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)
    # Act
    result = is_urgent(due, today)
    # Assert
    assert result is True


# TODO 3: is_urgent is True when the task is due in exactly 2 days (the limit).
def test_is_urgent_when_due_on_limit():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)
    # Act
    result = is_urgent(due, today)
    # Assert
    assert result is True

# TODO 4: is_urgent is False when the task is overdue.
def test_is_urgent_is_false_when_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)
    # Act
    result = is_urgent(due, today)
    # Assert
    assert result is False

# TODO 5: sort_by_due puts the soonest task first.
def test_sort_by_due_puts_soonest_first():
    # Arrange
    tasks = [
        {"title": "Submit report", "due": date(2026, 10, 25)},
        {"title": "Write tests", "due": date(2026, 10, 20)},
    ]
    # Act
    result = sort_by_due(tasks)
    # Assert
    assert result[0]["title"] == "Write tests"

# TODO 6: completion_rate returns 0.0 when there are no tasks.
def test_completion_rate_zero_when_no_tasks():
    # Arrange
    done = 0
    total = 0
    # Act
    result = completion_rate(done, total)
    # Assert
    assert result == 0.0

# TODO 7: completion_rate(1, 3) returns 33.3.
def test_completion_rate_rounds_to_one_decimal():
    # Arrange
    done = 1
    total = 3
    # Act
    result = completion_rate(done, total)
    # Assert
    assert result == 33.3
