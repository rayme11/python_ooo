# import package
from dataclasses import dataclass


# make a dataclass with decorator
@dataclass
class DataClassGFG:
    Job: str
    Salary: float


@dataclass
class SubDataClassGFG(DataClassGFG):
    Standard: str = "Top"
    Salary: float = 100000.00


# make objects with values required by dataclass
DataClassObject1 = DataClassGFG("Author", 100000.00)
DataClassObject2 = DataClassGFG("Author", 50000.00)

# view dataclass objects
print(DataClassObject1)
print(DataClassObject2)

# make object with values required by sub-dataclass
SubDataClassObject = SubDataClassGFG("Author")

# view sub-dataclass object
print(SubDataClassObject)
