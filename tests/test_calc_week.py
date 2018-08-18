import datetime
import pytz
from nflgame.live import calc_week

"""
The tests run through a bunch of switches (from one season to
another, one phase to another, one week to another) over a set
of seasons (e.g. the real dates from seasons in the past) to verify 
that the code seems to correspond with the NFL scheduling logic.
"""

def test_season_switches():
    assert calc_week(datetime.datetime(2014, 2, 28, tzinfo=pytz.utc)) == (2013, 'POST', 4)
    assert calc_week(datetime.datetime(2014, 3, 1, tzinfo=pytz.utc)) == (2014, 'PRE', 0)
    assert calc_week(datetime.datetime(2015, 2, 28, tzinfo=pytz.utc)) == (2014, 'POST', 4)
    assert calc_week(datetime.datetime(2015, 3, 1, tzinfo=pytz.utc)) == (2015, 'PRE', 0)
    # 2016 was a leap year
    assert calc_week(datetime.datetime(2016, 2, 29, tzinfo=pytz.utc)) == (2015, 'POST', 4)
    assert calc_week(datetime.datetime(2016, 3, 1, tzinfo=pytz.utc)) == (2016, 'PRE', 0)
    assert calc_week(datetime.datetime(2017, 2, 28, tzinfo=pytz.utc)) == (2016, 'POST', 4)
    assert calc_week(datetime.datetime(2017, 3, 1, tzinfo=pytz.utc)) == (2017, 'PRE', 0)
    assert calc_week(datetime.datetime(2018, 2, 28, tzinfo=pytz.utc)) == (2017, 'POST', 4)
    assert calc_week(datetime.datetime(2018, 3, 1, tzinfo=pytz.utc)) == (2018, 'PRE', 0)

def test_hof_to_pre_switches():
    assert calc_week(datetime.datetime(2014, 8, 5, tzinfo=pytz.utc)) == (2014, 'PRE', 0)
    assert calc_week(datetime.datetime(2014, 8, 6, tzinfo=pytz.utc)) == (2014, 'PRE', 1)
    assert calc_week(datetime.datetime(2015, 8, 11, tzinfo=pytz.utc)) == (2015, 'PRE', 0)
    assert calc_week(datetime.datetime(2015, 8, 12, tzinfo=pytz.utc)) == (2015, 'PRE', 1)
    assert calc_week(datetime.datetime(2016, 8, 9, tzinfo=pytz.utc)) == (2016, 'PRE', 0)
    assert calc_week(datetime.datetime(2016, 8, 10, tzinfo=pytz.utc)) == (2016, 'PRE', 1)
    assert calc_week(datetime.datetime(2017, 8, 8, tzinfo=pytz.utc)) == (2017, 'PRE', 0)
    assert calc_week(datetime.datetime(2017, 8, 9, tzinfo=pytz.utc)) == (2017, 'PRE', 1)
    assert calc_week(datetime.datetime(2018, 8, 7, tzinfo=pytz.utc)) == (2018, 'PRE', 0)
    assert calc_week(datetime.datetime(2018, 8, 8, tzinfo=pytz.utc)) == (2018, 'PRE', 1)

def test_pre_to_reg_switches():
    assert calc_week(datetime.datetime(2014, 9, 2, tzinfo=pytz.utc)) == (2014, 'PRE', 4)
    assert calc_week(datetime.datetime(2014, 9, 3, tzinfo=pytz.utc)) == (2014, 'REG', 1)
    assert calc_week(datetime.datetime(2015, 9, 8, tzinfo=pytz.utc)) == (2015, 'PRE', 4)
    assert calc_week(datetime.datetime(2015, 9, 9, tzinfo=pytz.utc)) == (2015, 'REG', 1)
    assert calc_week(datetime.datetime(2016, 9, 6, tzinfo=pytz.utc)) == (2016, 'PRE', 4)
    assert calc_week(datetime.datetime(2016, 9, 7, tzinfo=pytz.utc)) == (2016, 'REG', 1)
    assert calc_week(datetime.datetime(2017, 9, 5, tzinfo=pytz.utc)) == (2017, 'PRE', 4)
    assert calc_week(datetime.datetime(2017, 9, 6, tzinfo=pytz.utc)) == (2017, 'REG', 1)
    assert calc_week(datetime.datetime(2018, 9, 4, tzinfo=pytz.utc)) == (2018, 'PRE', 4)
    assert calc_week(datetime.datetime(2018, 9, 5, tzinfo=pytz.utc)) == (2018, 'REG', 1)

def test_reg_to_post_switches():
    assert calc_week(datetime.datetime(2014, 12, 30, tzinfo=pytz.utc)) == (2014, 'REG', 17)
    assert calc_week(datetime.datetime(2014, 12, 31, tzinfo=pytz.utc)) == (2014, 'POST', 1)
    assert calc_week(datetime.datetime(2016, 1, 5, tzinfo=pytz.utc)) == (2015, 'REG', 17)
    assert calc_week(datetime.datetime(2016, 1, 6, tzinfo=pytz.utc)) == (2015, 'POST', 1)
    assert calc_week(datetime.datetime(2017, 1, 3, tzinfo=pytz.utc)) == (2016, 'REG', 17)
    assert calc_week(datetime.datetime(2017, 1, 4, tzinfo=pytz.utc)) == (2016, 'POST', 1)
    assert calc_week(datetime.datetime(2018, 1, 2, tzinfo=pytz.utc)) == (2017, 'REG', 17)
    assert calc_week(datetime.datetime(2018, 1, 3, tzinfo=pytz.utc)) == (2017, 'POST', 1)
    assert calc_week(datetime.datetime(2019, 1, 1, tzinfo=pytz.utc)) == (2018, 'REG', 17)
    assert calc_week(datetime.datetime(2019, 1, 2, tzinfo=pytz.utc)) == (2018, 'POST', 1)

def test__2018_schedule():
    """
    Just an extra set of tests to see that the coming season, as of this
    writing, will work.
    """
    # POST4 to PRE0/HOF already tested

    # PRE0/HOF to PRE1 already tested

    assert calc_week(datetime.datetime(2018, 8, 14, tzinfo=pytz.utc)) == (2018, 'PRE', 1)
    assert calc_week(datetime.datetime(2018, 8, 15, tzinfo=pytz.utc)) == (2018, 'PRE', 2)

    assert calc_week(datetime.datetime(2018, 8, 21, tzinfo=pytz.utc)) == (2018, 'PRE', 2)
    assert calc_week(datetime.datetime(2018, 8, 22, tzinfo=pytz.utc)) == (2018, 'PRE', 3)

    assert calc_week(datetime.datetime(2018, 8, 28, tzinfo=pytz.utc)) == (2018, 'PRE', 3)
    assert calc_week(datetime.datetime(2018, 8, 29, tzinfo=pytz.utc)) == (2018, 'PRE', 4)

    # PRE4 to REG1 already tested

    assert calc_week(datetime.datetime(2018, 9, 11, tzinfo=pytz.utc)) == (2018, 'REG', 1)
    assert calc_week(datetime.datetime(2018, 9, 12, tzinfo=pytz.utc)) == (2018, 'REG', 2)

    assert calc_week(datetime.datetime(2018, 9, 18, tzinfo=pytz.utc)) == (2018, 'REG', 2)
    assert calc_week(datetime.datetime(2018, 9, 19, tzinfo=pytz.utc)) == (2018, 'REG', 3)

    assert calc_week(datetime.datetime(2018, 9, 25, tzinfo=pytz.utc)) == (2018, 'REG', 3)
    assert calc_week(datetime.datetime(2018, 9, 26, tzinfo=pytz.utc)) == (2018, 'REG', 4)

    assert calc_week(datetime.datetime(2018, 10, 2, tzinfo=pytz.utc)) == (2018, 'REG', 4)
    assert calc_week(datetime.datetime(2018, 10, 3, tzinfo=pytz.utc)) == (2018, 'REG', 5)

    assert calc_week(datetime.datetime(2018, 10, 9, tzinfo=pytz.utc)) == (2018, 'REG', 5)
    assert calc_week(datetime.datetime(2018, 10, 10, tzinfo=pytz.utc)) == (2018, 'REG', 6)

    assert calc_week(datetime.datetime(2018, 10, 16, tzinfo=pytz.utc)) == (2018, 'REG', 6)
    assert calc_week(datetime.datetime(2018, 10, 17, tzinfo=pytz.utc)) == (2018, 'REG', 7)

    assert calc_week(datetime.datetime(2018, 10, 23, tzinfo=pytz.utc)) == (2018, 'REG', 7)
    assert calc_week(datetime.datetime(2018, 10, 24, tzinfo=pytz.utc)) == (2018, 'REG', 8)

    assert calc_week(datetime.datetime(2018, 10, 30, tzinfo=pytz.utc)) == (2018, 'REG', 8)
    assert calc_week(datetime.datetime(2018, 10, 31, tzinfo=pytz.utc)) == (2018, 'REG', 9)

    assert calc_week(datetime.datetime(2018, 11, 6, tzinfo=pytz.utc)) == (2018, 'REG', 9)
    assert calc_week(datetime.datetime(2018, 11, 7, tzinfo=pytz.utc)) == (2018, 'REG', 10)

    assert calc_week(datetime.datetime(2018, 11, 13, tzinfo=pytz.utc)) == (2018, 'REG', 10)
    assert calc_week(datetime.datetime(2018, 11, 14, tzinfo=pytz.utc)) == (2018, 'REG', 11)

    assert calc_week(datetime.datetime(2018, 11, 20, tzinfo=pytz.utc)) == (2018, 'REG', 11)
    assert calc_week(datetime.datetime(2018, 11, 21, tzinfo=pytz.utc)) == (2018, 'REG', 12)

    assert calc_week(datetime.datetime(2018, 11, 27, tzinfo=pytz.utc)) == (2018, 'REG', 12)
    assert calc_week(datetime.datetime(2018, 11, 28, tzinfo=pytz.utc)) == (2018, 'REG', 13)

    assert calc_week(datetime.datetime(2018, 12, 4, tzinfo=pytz.utc)) == (2018, 'REG', 13)
    assert calc_week(datetime.datetime(2018, 12, 5, tzinfo=pytz.utc)) == (2018, 'REG', 14)

    assert calc_week(datetime.datetime(2018, 12, 11, tzinfo=pytz.utc)) == (2018, 'REG', 14)
    assert calc_week(datetime.datetime(2018, 12, 12, tzinfo=pytz.utc)) == (2018, 'REG', 15)

    assert calc_week(datetime.datetime(2018, 12, 18, tzinfo=pytz.utc)) == (2018, 'REG', 15)
    assert calc_week(datetime.datetime(2018, 12, 19, tzinfo=pytz.utc)) == (2018, 'REG', 16)

    assert calc_week(datetime.datetime(2018, 12, 25, tzinfo=pytz.utc)) == (2018, 'REG', 16)
    assert calc_week(datetime.datetime(2018, 12, 26, tzinfo=pytz.utc)) == (2018, 'REG', 17)

    # REG17 to POST1 already tested

    assert calc_week(datetime.datetime(2019, 1, 8, tzinfo=pytz.utc)) == (2018, 'POST', 1)
    assert calc_week(datetime.datetime(2019, 1, 9, tzinfo=pytz.utc)) == (2018, 'POST', 2)

    assert calc_week(datetime.datetime(2019, 1, 15, tzinfo=pytz.utc)) == (2018, 'POST', 2)
    assert calc_week(datetime.datetime(2019, 1, 16, tzinfo=pytz.utc)) == (2018, 'POST', 3)

    assert calc_week(datetime.datetime(2019, 1, 22, tzinfo=pytz.utc)) == (2018, 'POST', 3)
    assert calc_week(datetime.datetime(2019, 1, 23, tzinfo=pytz.utc)) == (2018, 'POST', 4)
