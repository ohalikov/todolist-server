from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import user, auth, todo

app = FastAPI(debug=True)

#       [
#         {
#           "id": 0,
#           "text": 'Learn the basics of Vue',
#           "completed": True,
#         },
#         {
#           "id": 1,
#           "text": 'Learn the basics of Typescript',
#           "completed": False,
#         },
#         {
#           "id": 2,
#           "text": 'Subscribe to the channel',
#           "completed": False,
#         },
#         {
#           "id": 3,
#           "text": 'Learn the basics of JS',
#           "completed": True,
#         },
#       ]

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(todo.router, tags=['Todos'], prefix='/api/todos')


@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}

# if __name__ == "__main__": 
#     config = uvicorn.Config("main:app", port=5000, log_level="debug", reload=True)
#     server = uvicorn.Server(config)
#     server.run()
