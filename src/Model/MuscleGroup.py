from sqlmodel import Field, SQLModel


class MuscleGroupBase(SQLModel):
    name : str = Field(index=True)
    description : str | None = Field(default=None,index=True)

class Muscle_Group(MuscleGroupBase, table=True):
    id : int | None  = Field(default=None, primary_key=True)

class MuscleGroupPublic(MuscleGroupBase):
    id: int

class MuscleGroupCreate(MuscleGroupBase):
    name: str
    description: str | None = None

class MuscleGroupUpdate(MuscleGroupBase):
    name : str | None = None
    description : str | None = None