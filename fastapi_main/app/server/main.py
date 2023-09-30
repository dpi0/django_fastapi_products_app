from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from .routers import product_router

from .routers import product_router

app = FastAPI()

# NOTE: this for CORS, used for when a diff lang frontend is used
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NOTE: these connect the main.py to the routers for posts, users and authentication
# app.include_router(product_router.router, tags=["Posts"], prefix="/post")


@app.get("/")
async def root():
    return {"message": "Home Page"}
