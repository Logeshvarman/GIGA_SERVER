from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob"]}


@app.get("/products")
def get_products():
    return {"products": ["Laptop", "Phone"]}


@app.get("/health")
def health():
    return {"status": "ok"}
