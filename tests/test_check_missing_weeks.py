import json
import os.path
import copy
from collections import OrderedDict
from nflgame.sched import check_missing_weeks

"""
The test schedule contains a full 2017 and a 2018 schedule up until
REG17. Once read, a copy can be obtained with the 
create_sched_copy()-function. With arguments, this copy can be 
modified (deleting desired records).
"""

test_jsonf = os.path.join(os.path.dirname(__file__), 'test-schedule.json')
test_data = json.loads(open(test_jsonf).read())
test_sched = OrderedDict()
for gsis_id, info in test_data.get('games', []):
    test_sched[gsis_id] = info


def test_full_2018_reg_schedule_on_disk_returns_empty_list_if_during_reg():
    assert check_missing_weeks(create_sched_copy(), 2018, 'REG') == []


def test_full_2018_reg_schedule_on_disk_returns_post_weeks_if_during_post():
    assert check_missing_weeks(create_sched_copy(), 2018, 'POST') == generate_expected(('POST'))


def test_2018_reg_schedule_with_holes_returns_schedule_holes():
    missing_weeks  = [(2018, 'PRE', 3), (2018, 'REG', 2), (2018, 'REG', 10), (2018, 'REG', 12)]
    sched_copy = create_sched_copy(weeks=missing_weeks)
    assert check_missing_weeks(sched_copy, 2018, 'REG') == missing_weeks


def test_empty_2018_schedule_on_disk_returns_all_pre_and_reg_if_reg17():
    assert check_missing_weeks(create_sched_copy(2018), 2018, 'REG') == generate_expected(('PRE', 'REG'))


def test_empty_2018_schedule_on_disk_returns_all_including_post_if_post1():
    assert check_missing_weeks(create_sched_copy(2018), 2018, 'POST') == generate_expected()



"""
Generates  list of tuples where each tuple is an expected week. 
The whole 2018 season including post season will be returned if 
there are no args. If phases are provided, only those phases will
be returned
"""
def generate_expected(phases=('PRE','REG','POST')):
    expected_weeks = []

    if 'PRE' in phases:
        for week in range(5):
            expected_weeks.append(tuple([2018,'PRE',week]))

    if 'REG' in phases:
        for week in range(1,18):
            expected_weeks.append(tuple([2018,'REG',week]))

    if 'POST' in phases:
        for week in range(1,5):
            expected_weeks.append(tuple([2018,'POST',week]))

    return expected_weeks

"""
Copies the schedule. The arguments state seasons, phases and
weeks that are to be REMOVED from the copy. Thus, no arguments
means an unchanged copy.

Logic explanation: 

A Provided season will delete any game played during that
season (not calendar year).

A provided phase (or phases) will only have effect if season is
provided too. If so, the complete phase(s) for that season is/are
removed.

Provided specific week(s) which are tuples containing season,
phase and week, for example [(2018,'REG',5), (2018,'POST',3)] will
remove specifically those weeks. Will not have any effect if season
is provided
"""
def create_sched_copy(season=None, phases=[], weeks=[]):
    sched_copy = copy.deepcopy(test_sched)

    if not season and not weeks:
        return sched_copy

    for gsis_id, info in test_sched.iteritems():
        if season:
            if info['year'] == season:
                if not phases:
                    del sched_copy[gsis_id]
                    continue
                if info['season_type'] in phases:
                    del sched_copy[gsis_id]
            continue

        season_week = (info['year'], info['season_type'], info['week'])
        if season_week in weeks:
            del sched_copy[gsis_id]

    return sched_copy
