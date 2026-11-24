import sys
from sqlalchemy import select
from app.core.config import settings
from app.db import SessionLocal
from app.models import CEOUser
from app.security import hash_password

def main() -> None:
    email = settings.ceo_bootstrap_email.strip().lower()
    password = settings.ceo_bootstrap_password
    if (
        not email
        or email.endswith(".example")
        or not password
        or password.startswith("replace_")
        or len(password) < 12
    ):
        print("CEO bootstrap blocked: set a real CEO email and a unique password (12+ characters) in company-platform/.env.")
        sys.exit(1)
    with SessionLocal() as db:
        existing = db.scalar(select(CEOUser).where(CEOUser.email == email))
        if existing:
            print("CEO account already exists; bootstrap will not overwrite its password.")
            return
        db.add(CEOUser(email=email, password_hash=hash_password(password), is_active=True))
        db.commit()
        print(f"CEO account created for {email}.")

if __name__ == "__main__":
    main()
