from fastapi import FastAPI, APIRouter
import middleware

from wepipe_python_sdk import Card

process = APIRouter(prefix="/process", tags=["process"])


@process.post("/purchasing/approval_compliance_to_approval_accountability")
async def approval_compliance_to_approval_accountability(card: Card):
    print(card)
    try:
        middleware.approval_compliance_to_approval_accountability(card=card)
        return {"Success": "True"}
    except Exception as e:
        return {"Error": str(e)}


@process.post("/purchasing/approval_accountability_to_approval_financial")
async def approval_accountability_to_approval_financial(card: Card):
    try:
        middleware.approval_accountability_to_approval_financial(card=card)
        return {"Success": "True"}
    except Exception as e:
        return {"Error": str(e)}


app = FastAPI()
app.include_router(process)
