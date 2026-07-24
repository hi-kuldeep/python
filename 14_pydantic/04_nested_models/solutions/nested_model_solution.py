from pydantic import BaseModel 
from typing import List

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

class Lesson(BaseModel):
    lesson_id: int
    topic: str

class Module(BaseModel):
    module_id: int
    title: str
    lessons: List[Lesson]

class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]





# Example Usage:
course_data = {
    "course_id": 101,
    "title": "Introduction to Python",
    "modules": [
        {
            "module_id": 1,
            "title": "Basics",
            "lessons": [
                {
                    "lesson_id": 1,
                    "topic": "Variables"
                },
                {
                    "lesson_id": 2,
                    "topic": "Data Types"
                }
            ]
        },
        {
            "module_id": 2,
            "title": "Functions",
            "lessons": [
                {
                    "lesson_id": 3,
                    "topic": "Defining Functions"
                },
                {
                    "lesson_id": 4,
                    "topic": "Lambda Functions"
                }
            ]
        }
    ]
}

course = Course(**course_data)
print(course.model_dump_json(indent=4))

