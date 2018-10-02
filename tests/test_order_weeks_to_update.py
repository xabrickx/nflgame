from nflgame.sched import order_weeks_to_update

"""
The desired functionality of order_weeks_to_update is to put
the current week (2nd arg) in the front of the list with weeks
(1st arg). The list with weeks may be empty, and it may or may not
contain the current week to begin with. The current week must not
be added to the front of the list while still remaining later in the list
(no duplicates)

"""


def test_current_week_is_moved_to_first_place():
    missing_weeks = [(2018, 'PRE', 0), (2018, 'PRE', 1), (2018, 'PRE', 2)]
    ordered_weeks = [(2018, 'PRE', 2), (2018, 'PRE', 0), (2018, 'PRE', 1)]

    assert order_weeks_to_update(missing_weeks, (2018, 'PRE', 2)) == ordered_weeks


def test_current_week_aldready_first_returns_unchanged_list():
    missing_weeks = [(2018, 'PRE', 0), (2018, 'PRE', 1), (2018, 'PRE', 2)]
    assert order_weeks_to_update(missing_weeks, (2018, 'PRE', 0)) == missing_weeks


def test_only_current_week_is_returned_if_empty_list():
    assert order_weeks_to_update([], (2018, 'PRE', 0)) == [(2018, 'PRE', 0)]


def test_operation_does_not_leave_current_week_duplicated():
    missing_weeks = [(2018, 'PRE', 0), (2018, 'PRE', 1), (2018, 'PRE', 2)]
    ordered_weeks = order_weeks_to_update(missing_weeks, (2018, 'PRE', 2))

    assert ordered_weeks.count((2018, 'PRE', 2)) == 1
