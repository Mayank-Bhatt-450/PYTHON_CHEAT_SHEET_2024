Here's a cheat sheet for **FastAPI**, covering the essentials to get you started with building APIs in Python:

---

### **Python FastAPI Cheat Sheet**

#### **Installation**

```bash
pip install fastapi
pip install uvicorn
```

#### **Basic Application Setup**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

- **Run with Uvicorn**:
  ```bash
  uvicorn main:app --reload
  ```

  - `main`: Python file name
  - `app`: FastAPI instance
  - `--reload`: Auto-reloads on code changes (useful for development)

---

### **Path Parameters**

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

- **Path Parameters** are dynamic parts of the URL, accessible in the function.

#### **Query Parameters**

```python
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

- **Query Parameters** are optional parameters in the URL after `?`.

---

### **Request Body with Pydantic**

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item
```

- Use **Pydantic Models** for data validation and serialization.

---

### **Form Data**

```python
from fastapi import Form

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
```

- Use **Form** for form data in POST requests.

---

### **File Uploads**

```python
from fastapi import File, UploadFile

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

- Use **File** and **UploadFile** for handling file uploads.

---

### **Response Models**

```python
from typing import List

@app.get("/items/", response_model=List[Item])
async def get_items():
    return [{"name": "Item1", "description": "An item", "price": 10}]
```

- **response_model** ensures the response matches the specified model type.

---

### **Status Codes**

```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item
```

- Use predefined **status codes** from `fastapi.status`.

---

### **Handling Errors**

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id > 10:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

- **HTTPException** to return custom error responses.

---

### **Dependencies**

```python
from fastapi import Depends

def verify_token(token: str):
    return token == "secure_token"

@app.get("/secure-data/")
async def secure_data(token: str = Depends(verify_token)):
    return {"data": "Secure Data"}
```

- **Dependencies** allow shared logic, like authentication or authorization.

---

### **Background Tasks**

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send-notification/")
async def send_notification(background_tasks: BackgroundTasks, message: str):
    background_tasks.add_task(write_log, message)
    return {"message": "Notification sent"}
```

- **BackgroundTasks** allows tasks to run after a response is sent.

---

### **Middleware**

```python
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "My custom header"
    return response
```

- **Middleware** can add logic that runs for every request, such as CORS.

---

### **Security**

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/secure-endpoint/")
async def secure_endpoint(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

- **OAuth2PasswordBearer** sets up token-based authentication.

---

### **OpenAPI & Documentation**

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- You can add custom metadata:

  ```python
  app = FastAPI(
      title="My API",
      description="API for my app",
      version="1.0.0",
  )
  ```

---

### **Testing with FastAPI**

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

---

This covers the main concepts and functions you'll use in FastAPI! You can always expand further by exploring specific advanced topics like **WebSockets**, **GraphQL**, or more intricate **dependency injection**.
