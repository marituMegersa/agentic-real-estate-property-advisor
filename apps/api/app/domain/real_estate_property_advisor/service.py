from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.real_estate_property_advisor.models import AgenticRealEstatePropertyAdvisorSession, AgenticRealEstatePropertyAdvisorItem
from app.domain.real_estate_property_advisor.schemas import AgenticRealEstatePropertyAdvisorSessionCreate, AgenticRealEstatePropertyAdvisorItemCreate

class AgenticRealEstatePropertyAdvisorService:
    @staticmethod
    def create_session(db: Session, data: AgenticRealEstatePropertyAdvisorSessionCreate) -> AgenticRealEstatePropertyAdvisorSession:
        db_obj = AgenticRealEstatePropertyAdvisorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticRealEstatePropertyAdvisorSession:
        return db.query(AgenticRealEstatePropertyAdvisorSession).filter(AgenticRealEstatePropertyAdvisorSession.id == session_id).first()
