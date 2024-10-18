from sqlmodel import Field, SQLModel

class MuscleBase(SQLModel):
    name : str = Field(index=True)
    description : str | None = Field(default=None,index=True)
    muscleGroup_id : int = Field(foreign_key="muscle_group.id",index=True)
    
class Muscle(MuscleBase, table= True):
    id : int = Field(default=None, primary_key=True)

class MusclePublic(MuscleBase):
    id: int

class MuscleCreate(MuscleBase):
    name: str
    description: str | None = None
    muscleGroup_id: int
    
class MuscleUpdate(MuscleBase):
    name: str | None = None
    description: str | None = None
    muscleGroup_id: int | None = None