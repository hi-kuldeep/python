from unicodedata import name
from pydantic import BaseModel, Field 
from typing import Optional

# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)


class Employee(BaseModel):
    id : int
    name : str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name must be between 3 to 50 characters long",
        example = "Kuldeep"
    )
    department : Optional[str] = 'General'
    salary : float = Field(
        ...,
        gt=10000
    )