from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    students = relationship("Student",back_populates="teachers")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teachers = relationship("Teacher",back_populates="students")