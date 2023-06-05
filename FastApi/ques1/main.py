from fastapi import FastAPI, Depends, Body, HTTPException
from typing import List
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import schemas


Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
def get_root():
    return {"message":"hello world"}


@app.get("/students")
def get_students(session: Session = Depends(get_session)):
    students = session.query(models.Student).all()
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int, session: Session = Depends(get_session)):
    student = session.query(models.Student).get(student_id)
    if student:
        return {
            "id": student.id,
            "name": student.name,
            "teacher": {
                "id": student.teachers.id,
                "name": student.teachers.name
            }
        }
    else:
        raise HTTPException(status_code=404, detail="Student not found")



@app.post("/students")
def post_students(student: schemas.Student, session: Session = Depends(get_session)):
    student = models.Student(name = student.name)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@app.put("/students/{student_id}")
def update_students(student_id: int, student: schemas.Student,session: Session = Depends(get_session)):
    db_student = session.query(models.Student).get(student_id)
    db_student.name = student.name
    session.commit()
    session.refresh(db_student)
    return db_student

@app.delete("/students/{student_id}")
def delete_students(student_id: int, student: schemas.Student,session: Session = Depends(get_session)):
    db_student = session.query(models.Student).get(student_id)
    session.delete(db_student)
    session.commit()
    # session.refresh(db_student)
    return {"message":"Student deleted"}


@app.get("/teachers")
def get_teachers(session: Session = Depends(get_session)):
    teachers = session.query(models.Teacher).all()
    return teachers

@app.post("/teachers")
def post_teachers(teacher: schemas.Teacher, session: Session = Depends(get_session)):
    teacher = models.Teacher(name = teacher.name)
    session.add(teacher)
    session.commit()
    session.refresh(teacher)
    return teacher

@app.put("/teachers/{teacher_id}")
def update_teachers(teacher_id: int, teacher: schemas.Teacher,session: Session = Depends(get_session)):
    db_teacher = session.query(models.Teacher).get(teacher_id)
    db_teacher.name = teacher.name
    session.commit()
    session.refresh(db_teacher)
    return db_teacher

@app.delete("/teachers/{teacher_id}")
def delete_teachers(teacher_id: int, teacher: schemas.Teacher,session: Session = Depends(get_session)):
    db_teacher = session.query(models.Teacher).get(teacher_id)
    session.delete(db_teacher)
    session.commit()
    return {"message":"Teacher deleted"}



@app.put("/students/{student_id}/assign/{teacher_id}")
def assign_student_to_teacher(student_id : int, teacher_id : int, student: schemas.Student, teacher: schemas.Teacher,session: Session = Depends(get_session)):
    db_student = session.query(models.Student).get(student_id)
    db_student.teacher_id = teacher_id
    session.commit()
    session.refresh(db_student)
    return db_student



