"""
Models
"""

from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class Employee(BaseModel):
    """
    The model for employees
    """
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0, lt=100)
    company: str = Field(...)
    join_date: datetime = Field(...)
    job_title: str = Field(...)
    gender: str = Field(...)
    salary: int = Field(..., gt=0)

    class Config:
        """
        Configs for Employee class
        """
        schema_extra = {
            'example': {
                "name": "Xanthus Mullen",
                "email": "Duis.dignissim.tempor@nislNullaeu.edu",
                "age": 61,
                "company": "Amazon",
                "join_date": "2009-02-13T01:48:14-08:00",
                "job_title": "janitor",
                "gender": "female",
                "salary": 6227
            }
        }
