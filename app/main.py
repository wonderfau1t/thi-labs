from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def get_health():
    return {"status": "OK"}


def experimental_score(value: int) -> int:
    if value < 0:
        return 0
    result = value * 2
    return result + 1
