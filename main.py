"""
Main file in project
"""

from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, Query
from fastapi.exceptions import HTTPException

from pydantic import EmailStr

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from db import find_employees
from models import Employee

app = FastAPI()


@app.get('/search_employees/', response_model=List[Employee])
def search_employees(
        name: Optional[str] = Query(None, max_length=100),
        email: Optional[EmailStr] = Query(None),
        age_min: Optional[int] = Query(1, ge=1, le=100),
        age_max: Optional[int] = Query(99, ge=0, le=100),
        company: Optional[str] = Query(None, max_length=100),
        join_date_start: Optional[datetime] = Query(datetime.strptime('1900-01-01', '%Y-%m-%d')),
        join_date_stop: Optional[datetime] = Query(datetime.today()),
        job_title: Optional[str] = Query(None, max_length=100),
        gender: Optional[str] = Query(None, max_length=100),
        salary_min: Optional[int] = Query(0, ge=0, le=99999999999),
        salary_max: Optional[int] = Query(99999999999, ge=0, le=99999999999),
):
    """
    Searching employees by parameters.
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
    :return:
    """
    if age_min > age_max:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail='age_min can not more than age_max'
        )

    if salary_min > salary_max:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail='salary_min can not more than salary_max'
        )

    if join_date_start > join_date_stop:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail='join_date_start can not later than join_date_stop'
        )

    return find_employees(
        name=name,
        email=email,
        age_min=age_min,
        age_max=age_max,
        company=company,
        join_date_start=join_date_start,
        join_date_stop=join_date_stop,
        job_title=job_title,
        gender=gender,
        salary_min=salary_min,
        salary_max=salary_max
    )
