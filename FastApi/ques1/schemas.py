from pydantic import BaseModel


class Teacher(BaseModel):
    id : int
    name : str


    class Config:
        orm_mode = True


class Student(BaseModel):
    id : int
    name : str
    teacher_id : int
    teacher : Teacher

    class Config:
        orm_mode = True