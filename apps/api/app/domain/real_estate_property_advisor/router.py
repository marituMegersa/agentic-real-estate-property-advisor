from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.real_estate_property_advisor.schemas import AgenticRealEstatePropertyAdvisorSessionCreate, AgenticRealEstatePropertyAdvisorSessionResponse
from app.domain.real_estate_property_advisor.service import AgenticRealEstatePropertyAdvisorService

router = APIRouter(prefix="/api/v1/real_estate_property_advisor", tags=["Agentic Real Estate Property Advisor Domain"])

@router.post("/sessions", response_model=AgenticRealEstatePropertyAdvisorSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticRealEstatePropertyAdvisorSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Real Estate Property Advisor.
    """
    return AgenticRealEstatePropertyAdvisorService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticRealEstatePropertyAdvisorSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticRealEstatePropertyAdvisorService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
