from sqlalchemy import select
from app.db import SessionLocal
from app.models import Employee
EMPLOYEES=[
 {"slug":"killua","display_name":"Killua","role":"Executive Secretary & Chief of Staff","department":"Executive Office"},
 {"slug":"dipa","display_name":"Dipa","role":"Customer Relations","department":"Customer Operations"},
 {"slug":"kyou","display_name":"Kyou","role":"Business Intelligence","department":"Strategy & Analytics"},
 {"slug":"ren","display_name":"Ren","role":"Finance Manager","department":"Finance"}]
def main()->None:
    with SessionLocal() as db:
        for item in EMPLOYEES:
            if db.scalar(select(Employee).where(Employee.slug==item["slug"])) is None:
                db.add(Employee(**item,status="inactive"))
        db.commit()
    print("Employee directory seed completed.")
if __name__=="__main__":
    main()
