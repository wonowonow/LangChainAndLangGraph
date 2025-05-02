from pydantic import BaseModel
from typing import List

class Project(BaseModel):
    title: str
    description: str
    tasks: List[str]


class CareerItem(BaseModel):
    company: str
    duration: str
    role: str
    projects: List[Project]


class Experience(BaseModel):
    type: str
    description: str


class Education(BaseModel):
    institution: str
    program: str
    duration: str
    status: str


class Certification(BaseModel):
    name: str
    date: str


class Data(BaseModel):
    email: str
    github: str
    name: str
    position: str
    blog: str
    skills: List[str]
    summary: str
    career: List[CareerItem]
    experience: List[Experience]
    education: List[Education]
    certifications: List[Certification]