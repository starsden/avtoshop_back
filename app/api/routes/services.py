from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin
from app.core.database import get_db
from app.models import Service
from app.schemas.service import ServiceCreate, ServiceResponse, ServiceUpdate

router = APIRouter(prefix="/services", tags=["services"])


@router.get("", response_model=list[ServiceResponse])
def list_services(db: Session = Depends(get_db)):
    return db.query(Service).order_by(Service.created_at.desc()).all()


@router.post("", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
def create_service(
    payload: ServiceCreate,
    db: Session = Depends(get_db),
    _=Depends(get_current_admin),
):
    service = Service(**payload.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(
    service_id: int,
    payload: ServiceUpdate,
    db: Session = Depends(get_db),
    _=Depends(get_current_admin),
):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "service_not_found", "message": "Service not found"}},
        )

    for key, value in payload.model_dump().items():
        setattr(service, key, value)

    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_service(
    service_id: int,
    db: Session = Depends(get_db),
    _=Depends(get_current_admin),
):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "service_not_found", "message": "Service not found"}},
        )

    db.delete(service)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
