"""
DB module
"""

from datetime import datetime

import os

from pymongo import MongoClient

m_client = MongoClient("mongodb://root:example@mongo:27017")

if os.getenv('STAGE') == 'prod':
    db_name = 'employees'
else:
    db_name = 'test-employees'

db = m_client[db_name]

collection = db['employees_collection']


def find_employees(name: str = None,
                   email: str = None,
                   age_min: int = 1,
                   age_max: int = 99,
                   company: str = None,
                   join_date_start: datetime = datetime.strptime('1900-01-01', '%Y-%m-%d'),
                   join_date_stop: datetime = datetime.today(),
                   job_title: str = None,
                   gender: str = None,
                   salary_min: int = 0,
                   salary_max: int = 99999999999):
    """
    Function for searching employees in db
    :param name:
    :param email:
    :param age_min:
    :param age_max:
    :param company:
    :param join_date_start:
    :param join_date_stop:
    :param job_title:
    :param gender:
    :param salary_min:
    :param salary_max:
    :return: list of employees
    """

    conditions = {
        'salary': {
            '$gte': salary_min,
            '$lte': salary_max
        },
        'age': {
            '$gte': age_min,
            '$lte': age_max
        },
        'join_date': {
            '$gte': join_date_start,
            '$lte': join_date_stop
        }
    }

    if name:
        conditions['name'] = {'$eq': name}
    if email:
        conditions['email'] = {'$eq': email}
    if company:
        conditions['company'] = {'$eq': company}
    if job_title:
        conditions['job_title'] = {'$eq': job_title}
    if gender:
        conditions['gender'] = {'$eq': gender}

    result = list(collection.find(conditions))

    return result
