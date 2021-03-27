"""
Tests for function "find_employees"
"""

import datetime

from db import find_employees


def test_unit_search_with_default_param():
    """
    Test function "find_employees" without any parameters (default parameters).
    :return:
    """

    result = find_employees()
    assert len(result) == 600


def test_unit_search_by_name():
    """
    Test function "find_employees" with "name" parameter.
    :return:
    """
    name = 'Sawyer Robbins'

    result = find_employees(name=name)

    assert len(result) == 1
    assert result[0]['name'] == name


def test_unit_search_by_email():
    """
    Test function "find_employees" with "email" parameter.
    :return:
    """
    email = 'imperdiet.non.vestibulum@pede.ca'
    result = find_employees(email=email)

    assert len(result) == 1
    assert result[0]['email'] == email


def test_unit_search_by_one_age():
    """
    Test function "find_employees" with "age" parameters.
    age_min == age_max
    :return:
    """
    age = 36
    result = find_employees(age_min=age, age_max=age)

    assert len(result) == 10
    for i in result:
        assert i['age'] == age


def test_unit_search_by_diff_age():
    """
    Test function "find_employees" with "age" parameters.
    age_min != age_max
    :return:
    """
    age_min = 36
    age_max = 46
    result = find_employees(age_min=age_min, age_max=age_max)

    assert len(result) == 117
    for i in result:
        assert age_min <= i['age'] <= age_max


def test_unit_search_by_company():
    """
    Test function "find_employees" with "company" parameter.
    :return:
    """
    company = 'Yandex'
    result = find_employees(company=company)

    assert len(result) == 84
    for i in result:
        assert i['company'] == company


def test_unit_search_by_one_join_date():
    """
    Test function "find_employees" with "join_date" parameters.
    join_date_start == join_date_stop
    :return:
    """
    join_date = datetime.datetime.strptime("2012-12-29 03:00:10", '%Y-%m-%d %H:%M:%S')

    result = find_employees(join_date_start=join_date, join_date_stop=join_date)

    assert len(result) == 1
    for i in result:
        assert i['join_date'] == join_date


def test_unit_search_by_diff_join_date():
    """
    Test function "find_employees" with "join_date" parameters.
    join_date_start != join_date_stop
    :return:
    """
    join_date_start = datetime.datetime.strptime("2012-12-29 03:00:10", '%Y-%m-%d %H:%M:%S')
    join_date_stop = datetime.datetime.strptime("2013-12-29 03:00:10", '%Y-%m-%d %H:%M:%S')

    result = find_employees(join_date_start=join_date_start, join_date_stop=join_date_stop)

    assert len(result) == 41
    for i in result:
        assert join_date_start <= i['join_date'] <= join_date_stop


def test_unit_search_by_job_title():
    """
    Test function "find_employees" with "job_title" parameter.
    :return:
    """
    job_title = 'developer'
    result = find_employees(job_title=job_title)

    assert len(result) == 102
    for i in result:
        assert i['job_title'] == job_title


def test_unit_search_by_gender():
    """
    Test function "find_employees" with "gender" parameter.
    :return:
    """
    gender = 'male'
    result = find_employees(gender=gender)

    assert len(result) == 203
    for i in result:
        assert i['gender'] == gender


def test_unit_search_by_one_salary():
    """
    Test function "find_employees" with "salary" parameters.
    salary_min == salary_max
    :return:
    """
    salary = 4944
    result = find_employees(salary_min=salary, salary_max=salary)

    assert len(result) == 1
    for i in result:
        assert i['salary'] == salary


def test_unit_search_by_diff_salary():
    """
    Test function "find_employees" with "salary" parameters.
    salary_min != salary_max
    :return:
    """
    salary_min = 3600
    salary_max = 4600
    result = find_employees(salary_min=salary_min, salary_max=salary_max)

    assert len(result) == 62
    for i in result:
        assert salary_min <= i['salary'] <= salary_max


def test_unit_search_with_multi_parameters():
    """
    Test function "find_employees" with multiples parameters.
    :return:
    """
    company = 'Google'
    age_min = 22
    age_max = 56
    gender = 'female'
    join_date_start = datetime.datetime.strptime("2005-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
    join_date_stop = datetime.datetime.strptime("2005-12-31 23:59:59", '%Y-%m-%d %H:%M:%S')
    job_title = 'driver'
    salary_min = 1600
    salary_max = 6600

    result = find_employees(
        company=company,
        age_min=age_min,
        gender=gender,
        join_date_start=join_date_start,
        join_date_stop=join_date_stop,
        job_title=job_title,
        salary_min=salary_min,
        salary_max=salary_max
    )

    assert len(result) == 2

    for i in result:
        assert age_min <= i['age'] <= age_max
        assert i['company'] == company
        assert join_date_start <= i['join_date'] <= join_date_stop
        assert i['gender'] == gender
        assert i['job_title'] == job_title
        assert salary_min <= i['salary'] <= salary_max
