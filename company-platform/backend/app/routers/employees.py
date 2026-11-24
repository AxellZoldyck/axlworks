from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.dependencies import get_current_ceo
from app.models import CEOUser, Employee
from app.schemas import EmployeeResponse
router = APIRouter(prefix="/employees",tags=["AI Employees"])
@router.get("",response_model=list[EmployeeResponse])
def list_employees(_: CEOUser=Depends(get_current_ceo),db:Session=Depends(get_db))->list[Employee]:
    return list(db.scalars(select(Employee).order_by(Employee.slug)).all())
@router.get("/{slug}",response_model=EmployeeResponse)
def get_employee(slug:str,_:CEOUser=Depends(get_current_ceo),db:Session=Depends(get_db))->Employee:
    employee=db.scalar(select(Employee).where(Employee.slug==slug))
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    return employee
