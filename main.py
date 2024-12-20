from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, create_engine, select

from src.Model.Muscle import Muscle, MusclePublic, MuscleCreate, MuscleUpdate
from src.Model.MuscleGroup import Muscle_Group, MuscleGroupPublic, MuscleGroupCreate, MuscleGroupUpdate

from src.Database.db import get_db


database_url = get_db()

engine = create_engine(database_url)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
app.title = "Get your training"
app.description = "Get your training program with scientific information about muscle"

# Muscle Request
@app.post("/muscle/", response_model=MusclePublic)
def create_muscle(muscle: MuscleCreate, session: SessionDep):
    db_Muscle = Muscle.model_validate(muscle)
    session.add(db_Muscle)
    session.commit()
    session.refresh(db_Muscle)
    return db_Muscle

@app.get("/muscle/", response_model=list[MusclePublic])
def get_muscle(
    session: SessionDep,
    offset : int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    muscle = session.exec(select(Muscle).offset(offset).limit(limit)).all()
    return muscle


@app.get("/muscle/{muscle_id}", response_model=MusclePublic)
def get_Muscle(muscle_id: int, session: SessionDep) :
    muscle = session.get(Muscle, muscle_id)
    if not Muscle:
        raise HTTPException(status_code=404, detail="Muscle not found")
    return muscle

@app.delete("/muscle/{muscle_id}")
def delete_Muscle(muscle_id: int, session: SessionDep):
    muscle = session.get(Muscle, muscle_id)
    if not Muscle:
        raise HTTPException(status_code=404, detail="Muscle not found")
    session.delete(muscle)
    session.commit()
    return {"ok": True}

@app.patch("/muscle/{muscle_id}", response_model=MusclePublic)
def update_Muscle(muscle_id: int, muscle: MuscleUpdate, session: SessionDep):
    muscle_db = session.get(Muscle, muscle_id)
    if not muscle_db:
        raise HTTPException(status_code=404, detail="Muscle not found")
    muscle_data = muscle.model_dump(exclude_unset=True)
    muscle_db.sqlmodel_update(muscle_data)
    session.add(muscle_db)
    session.commit()
    session.refresh(muscle_db)
    return muscle_db

# Muscle Group requests
@app.post("/muscleGroup/", response_model=MuscleGroupPublic)
def create_muscleGroup(muscleGroup: MuscleGroupCreate, session: SessionDep):
    db_MuscleGroup = Muscle_Group.model_validate(muscleGroup)
    session.add(db_MuscleGroup)
    session.commit()
    session.refresh(db_MuscleGroup)
    return db_MuscleGroup

@app.get("/muscleGroup/", response_model=list[MuscleGroupPublic])
def get_muscleGroup(
    session: SessionDep,
    offset : int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    muscleGroup = session.exec(select(Muscle_Group).offset(offset).limit(limit)).all()
    return muscleGroup



@app.get("/muscleGroup/{muscleGroup_id}", response_model=MuscleGroupPublic)
def get_MuscleGroup(muscleGroup_id: int, session: SessionDep) :
    muscleGroup = session.get(Muscle_Group, muscleGroup_id)
    if not Muscle_Group:
        raise HTTPException(status_code=404, detail="Muscle Group not found")
    return muscleGroup

@app.delete("/muscleGroup/{muscleGroup_id}")
def delete_MuscleGroup(muscleGroup_id: int, session: SessionDep):
    muscleGroup = session.get(Muscle_Group, muscleGroup_id)
    if not Muscle_Group:
        raise HTTPException(status_code=404, detail="Muscle Group not found")
    session.delete(muscleGroup)
    session.commit()
    return {"ok": True}

@app.patch("/muscleGroup/{muscleGroup_id}", response_model=MuscleGroupPublic)
def update_MuscleGroup(muscleGroup_id: int, muscleGroup: MuscleGroupUpdate, session: SessionDep):
    muscleGroup_db = session.get(Muscle_Group, muscleGroup_id)
    if not muscleGroup_db:
        raise HTTPException(status_code=404, detail="Muscle Group not found")
    muscleGroup_data = muscleGroup.model_dump(exclude_unset=True)
    muscleGroup_db.sqlmodel_update(muscleGroup_data)
    session.add(muscleGroup_db)
    session.commit()
    session.refresh(muscleGroup_db)
    return muscleGroup_db



