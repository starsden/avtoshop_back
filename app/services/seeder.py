from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import hash_password
from app.models import AdminUser, Review, Service


def seed_admin(db: Session) -> None:
    existing = db.query(AdminUser).filter(AdminUser.email == settings.seed_admin_email.lower()).first()
    if existing:
        return

    user = AdminUser(
        email=settings.seed_admin_email.lower(),
        password_hash=hash_password(settings.seed_admin_password),
        role="admin",
    )
    db.add(user)
    db.commit()


def seed_sample_data(db: Session) -> None:
    if not settings.seed_sample_data:
        return

    has_services = db.query(Service).first() is not None
    if not has_services:
        db.add_all(
            [
                Service(
                    name="Engine Diagnostics",
                    icon="Wrench",
                    description="Comprehensive diagnostics for modern vehicles.",
                    price="from $50",
                ),
                Service(
                    name="Oil Change",
                    icon="Droplets",
                    description="Fast synthetic or regular oil replacement.",
                    price="from $40",
                ),
            ]
        )

    has_reviews = db.query(Review).first() is not None
    if not has_reviews:
        db.add_all(
            [
                Review(name="Anton", text="Quick and professional service.", rating=5, status="published"),
                Review(name="Mila", text="Transparent pricing and nice staff.", rating=4, status="published"),
            ]
        )

    db.commit()
