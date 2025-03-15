from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo, Field
from typing import Annotated
from enum import Enum

class Standard(Enum):
    primary = 1
    secondary = 2
    matric = 3

class Student(BaseModel):
    id: int
    name: Annotated[str, Field(max_length = 20)]
    age: Annotated[int, Field(ge=1, le=30)]
    email: EmailStr
    standard: Standard
    # Validation
    # @field_validator("age")
    # @classmethod
    # def validate_age(cls, std_age):
    #     if std_age > 30:
    #         raise ValueError("Invalid age")
    #     return std_age
    
    @field_validator("standard")
    @classmethod
    def validate_standard(cls, std_standard, info: ValidationInfo):
        if std_standard is Standard.primary and info.data["age"] > 30:
            raise ValueError("Invalid age")
        # print("standard:",std_standard, "Age:",info.data["age"])
        return std_standard

std1 = Student(
    id = 1,
    name = "Affan",
    age = 18,
    email = "affan@gmail.com",
    standard = Standard.primary
)

print(std1)