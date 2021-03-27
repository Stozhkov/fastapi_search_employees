"""
Tests for API "search_employees"
"""

import datetime
import json

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

expected_result = {
    "name": "Sawyer Robbins",
    "email": "imperdiet.non.vestibulum@pede.ca",
    "age": 37,
    "company": "Yandex",
    "join_date": "2012-12-29T03:00:10",
    "job_title": "developer",
    "gender": "female",
    "salary": 4944
}


def test_api_search_wo_param():
    """
    Test API "search_employees" without any parameters.
    :return:
    """
    response = client.get('/search_employees')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert response.status_code == 200
    assert len(result) == 600


def test_api_search_by_name():
    """
    Test API "search_employees" with "name" parameter.
    :return:
    """
    name = 'Sawyer Robbins'
    response = client.get(f'/search_employees?name={name}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 1
    assert result[0]['name'] == name


def test_api_search_by_email():
    """
    Test API "search_employees" with "email" parameter.
    :return:
    """
    email = 'imperdiet.non.vestibulum@pede.ca'
    response = client.get(f'/search_employees?email={email}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 1
    assert result[0]['email'] == email


def test_api_search_by_one_age():
    """
    Test API "search_employees" with "age" parameters.
    age_min == age_max
    :return:
    """
    age = 36
    response = client.get(f'/search_employees?age_min={age}&age_max={age}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 10
    for i in result:
        assert i['age'] == age


def test_api_search_by_diff_age():
    """
    Test API "search_employees" with "age" parameters.
    age_min != age_max
    :return:
    """
    age_min = 36
    age_max = 46
    response = client.get(f'/search_employees?age_min={age_min}&age_max={age_max}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 117
    for i in result:
        assert age_min <= i['age'] <= age_max


def test_api_search_by_company():
    """
    Test API "search_employees" with "company" parameter.
    :return:
    """
    company = 'Yandex'
    response = client.get(f'/search_employees?company={company}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 84
    for i in result:
        assert i['company'] == company


def test_api_search_by_one_join_date():
    """
    Test API "search_employees" with "join_date" parameters.
    join_date_start == join_date_stop
    :return:
    """
    join_date = "2012-12-29 03:00:10"
    response = client.get(f'/search_employees?join_date_start={join_date}&'
                          f'join_date_stop={join_date}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 1
    for i in result:
        assert datetime.datetime.strptime(i['join_date'], '%Y-%m-%dT%H:%M:%S') == \
               datetime.datetime.strptime(join_date, '%Y-%m-%d %H:%M:%S')


def test_api_search_by_diff_join_date():
    """
    Test API "search_employees" with "join_date" parameters.
    join_date_start != join_date_stop
    :return:
    """
    join_date_start = "2012-12-29 03:00:10"
    join_date_stop = "2013-12-29 03:00:10"
    response = client.get(f'/search_employees?join_date_start={join_date_start}&'
                          f'join_date_stop={join_date_stop}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 41
    for i in result:
        assert datetime.datetime.strptime(join_date_start, '%Y-%m-%d %H:%M:%S') <= \
               datetime.datetime.strptime(i['join_date'], '%Y-%m-%dT%H:%M:%S') <= \
               datetime.datetime.strptime(join_date_stop, '%Y-%m-%d %H:%M:%S')


def test_api_search_by_job_title():
    """
    Test API "search_employees" with "job_title" parameter.
    :return:
    """
    job_title = 'developer'
    response = client.get(f'/search_employees?job_title={job_title}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 102
    for i in result:
        assert i['job_title'] == job_title


def test_api_search_by_gender():
    """
    Test API "search_employees" with "gender" parameter.
    :return:
    """
    gender = 'male'
    response = client.get(f'/search_employees?gender={gender}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 203
    for i in result:
        assert i['gender'] == gender


def test_api_search_by_one_salary():
    """
    Test API "search_employees" with "salary" parameters.
    salary_min == salary_max
    :return:
    """
    salary = 4944
    response = client.get(f'/search_employees?salary_min={salary}&salary_max={salary}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 1
    for i in result:
        assert i['salary'] == salary


def test_api_search_by_diff_salary():
    """
    Test API "search_employees" with "salary" parameters.
    salary_min != salary_max
    :return:
    """
    salary_min = 3600
    salary_max = 4600
    response = client.get(f'/search_employees?salary_min={salary_min}&salary_max={salary_max}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert len(result) == 62
    for i in result:
        assert salary_min <= i['salary'] <= salary_max


def test_api_search_with_multi_parameters():
    """
    Test API "search_employees" with multiples parameters.
    :return:
    """
    company = 'Google'
    age_min = 22
    age_max = 56
    gender = 'female'
    join_date_start = "2005-01-01 00:00:00"
    join_date_stop = "2005-12-31 23:59:59"
    job_title = 'driver'
    salary_min = 1600
    salary_max = 6600

    response = client.get(f'/search_employees?company={company}&'
                          f'age_min={age_min}&'
                          f'age_max={age_max}&'
                          f'gender={gender}&'
                          f'join_date_start={join_date_start}&'
                          f'join_date_stop={join_date_stop}&'
                          f'job_title={job_title}&'
                          f'salary_min={salary_min}&'
                          f'salary_max={salary_max}')
    result = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    for i in result:
        print(i)
        assert age_min <= i['age'] <= age_max
        assert i['company'] == company
        assert datetime.datetime.strptime(join_date_start, '%Y-%m-%d %H:%M:%S') <= \
               datetime.datetime.strptime(i['join_date'], '%Y-%m-%dT%H:%M:%S') <= \
               datetime.datetime.strptime(join_date_stop, '%Y-%m-%d %H:%M:%S')
        assert i['gender'] == gender
        assert i['job_title'] == job_title
        assert salary_min <= i['salary'] <= salary_max
    assert len(result) == 2
