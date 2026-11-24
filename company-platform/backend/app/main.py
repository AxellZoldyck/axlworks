from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import settings
from app.db import check_database_connection
from app.routers import auth, employees
app=FastAPI(title=settings.app_name,version="0.2.0",description="AXLWORKS autonomous company platform API")
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_origin_list,allow_credentials=True,allow_methods=["GET","POST","PATCH","DELETE"],allow_headers=["Authorization","Content-Type","X-Request-ID"])
app.include_router(auth.router)
app.include_router(employees.router)
@app.get("/health",tags=["Operations"])
def health()->dict[str,str]:
    return {"status":"ok","service":"axlworks-company-api"}
@app.get("/ready",tags=["Operations"])
def readiness()->dict[str,str]:
    try:
        check_database_connection()
    except SQLAlchemyError as exc:
        raise HTTPException(status_code=503,detail="Database unavailable") from exc
    return {"status":"ready","database":"connected"}
