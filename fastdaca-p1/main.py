from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"HELLO": "WORLD"}


@app.get("/routes/{route_id}")
def read_item(route_id: int,  q: str | None = None):
    return {"route_id": route_id, "q": q}