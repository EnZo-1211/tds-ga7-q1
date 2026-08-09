from fastapi import FastAPI
from q1.main import router as q1_router
# from q2.main import router as q2_router # to be added later

app = FastAPI()

app.include_router(q1_router, prefix="/q1")
# app.include_router(q2_router, prefix="/q2")

@app.get("/")
def read_root():
    return {"status": "ok"}
