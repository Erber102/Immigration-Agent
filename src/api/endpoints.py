from __future__ import annotations
from fastapi import APIRouter
from pydantic import BaseModel
import uuid

from ..core.plan_matcher import match_plans
from ..agent.qna_agent import QnAAgent

router = APIRouter(prefix="/api/v1")

qna = QnAAgent()


class MatchRequest(BaseModel):
    profile: dict


class MatchResponse(BaseModel):
    session_id: str
    matches: list


@router.post("/plans/match", response_model=MatchResponse)
def plans_match(req: MatchRequest):
    session_id = str(uuid.uuid4())
    qna.register_session(session_id, req.profile)
    matches = match_plans(req.profile)
    return MatchResponse(session_id=session_id, matches=matches)


class QnARequest(BaseModel):
    session_id: str
    question: str


class QnAResponse(BaseModel):
    answer: str


@router.post("/qna", response_model=QnAResponse)
def qna_endpoint(req: QnARequest):
    answer = qna.ask(req.session_id, req.question)
    return QnAResponse(answer=answer)
