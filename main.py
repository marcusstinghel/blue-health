from fastapi import FastAPI, APIRouter
import middleware

process = APIRouter(prefix="/process", tags=["process"])


@process.post("/purchasing/approval_compliance_to_approval_accountability")
async def approval_compliance_to_approval_accountability(request):
    print(request)
    try:
        middleware.approval_compliance_to_approval_accountability(request=request)
        return {"Success": "True"}
    except Exception as e:
        return {"Error": str(e)}


@process.post("/purchasing/approval_accountability_to_approval_financial")
async def approval_accountability_to_approval_financial(request):
    try:
        middleware.approval_accountability_to_approval_financial(request=request)
        return {"Success": "True"}
    except Exception as e:
        return {"Error": str(e)}


app = FastAPI()
app.include_router(process)
