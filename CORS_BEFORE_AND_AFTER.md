# CORS Configuration - Before & After Comparison

## Side-by-Side Code Comparison

### BEFORE ❌ (Permissive)
```python
# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",    # ← Vite default port
        "http://localhost:5174",    # ← Vite fallback port
        "http://localhost:3000",    # ← Alternative port
        "http://localhost:5000",    # ← Alternative port
    ],
    allow_credentials=True,
    allow_methods=["*"],            # ← All methods (too broad)
    allow_headers=["*"],
)
```

**Characteristics**:
- Multiple ports allowed
- All HTTP methods allowed (GET, POST, PUT, DELETE, PATCH, etc.)
- Overly permissive for local development

---

### AFTER ✅ (Specific & Secure)
```python
# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ← Only React dev server
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # ← Explicit methods
    allow_headers=["*"],
)
```

**Characteristics**:
- Single, specific origin (localhost:5173)
- Explicit HTTP methods listed
- More secure and maintainable
- Better follows principle of least privilege

---

## Configuration Parameter Explanation

### `allow_origins`

| Setting | Purpose | Security |
|---------|---------|----------|
| `["http://localhost:5173"]` | Only allow requests from React dev server | ✅ Restrictive |
| `["*"]` | Allow requests from any origin | ❌ Security Risk |
| `["http://localhost:5173", "http://localhost:5174"]` | Multiple origins | ⚠️ Moderate |

**Current**: `["http://localhost:5173"]` ✅

---

### `allow_methods`

| Setting | Methods Allowed | Use Case |
|---------|-----------------|----------|
| `["*"]` | All methods (GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS) | Too permissive |
| `["GET", "POST"]` | Only read and analyze | Minimal |
| `["GET", "POST", "PUT", "DELETE", "OPTIONS"]` | Full CRUD + preflight | **Current (Recommended)** ✅ |

**Current**: `["GET", "POST", "PUT", "DELETE", "OPTIONS"]` ✅

**Breakdown**:
- **GET** - Retrieve data (health check)
- **POST** - Submit data (fraud analysis)
- **PUT** - Update data (future use)
- **DELETE** - Remove data (future use)
- **OPTIONS** - Preflight requests (automatic)

---

### `allow_headers`

| Setting | Headers Allowed | Note |
|---------|-----------------|------|
| `["*"]` | All headers (Content-Type, Authorization, etc.) | Current ✅ |
| `["Content-Type", "Authorization"]` | Only specific headers | Restrictive |

**Current**: `["*"]` - Allows all headers needed by frontend

---

### `allow_credentials`

| Setting | Cookies | Auth Headers | Note |
|---------|---------|--------------|------|
| `True` | ✅ Allowed | ✅ Allowed | Current ✅ |
| `False` | ❌ Blocked | ❌ Blocked | Not recommended |

**Current**: `True` - Allows cookies and authentication

---

## Import Requirements

```python
from fastapi.middleware.cors import CORSMiddleware
```

**Status**: ✅ Already imported in updated file

---

## API Endpoints - Unchanged

### 1. Homepage
```
GET /
Response: {"message": "Welcome to FraudShield AI", "status": "running"}
CORS: ✅ Allowed (GET method)
```

### 2. Health Check
```
GET /health
Response: {"status": "healthy"}
CORS: ✅ Allowed (GET method)
```

### 3. Fraud Analysis
```
POST /api/v1/analyze
Request: TransactionRequest (30 numeric fields)
Response: {fraud_detection, risk_assessment, investigation_status}
CORS: ✅ Allowed (POST method)
```

---

## Pydantic Models - Unchanged

### TransactionRequest
```python
class TransactionRequest(BaseModel):
    Time: float
    V1: float
    V2: float
    # ... (V3 through V28)
    V28: float
    Amount: float = Field(ge=0)
```

**Fields**: 30 total  
**Validation**: Amount must be >= 0  
**Status**: ✅ Unchanged

---

## Business Logic - Unchanged

```python
@app.post("/api/v1/analyze")
def analyze_transaction(request: TransactionRequest):
    """
    1. Convert request to DataFrame
    2. Build initial workflow state
    3. Invoke LangGraph fraud workflow
    4. Check for errors
    5. Return results or error
    6. Log all activity
    """
    # All logic preserved ✅
```

**Features Preserved**:
- ✅ DataFrame creation
- ✅ State initialization
- ✅ Workflow invocation
- ✅ Error handling
- ✅ Result formatting
- ✅ Logging

---

## Diagram: Request Flow with CORS

```
React Frontend (http://localhost:5173)
        │
        │ 1. Browser sends preflight request (OPTIONS)
        │ Origin: http://localhost:5173
        ↓
FastAPI Backend (http://localhost:8000)
        │
        │ 2. CORS Middleware checks:
        │    - allow_origins: http://localhost:5173 ✅ MATCH
        │    - allow_methods: OPTIONS ✅ MATCH
        │
        │ 3. Send preflight response with CORS headers
        ↓
React Frontend
        │
        │ 4. Browser sends actual request (POST)
        │ Origin: http://localhost:5173
        │ Body: Transaction data
        ↓
FastAPI Backend
        │
        │ 5. CORS Middleware checks:
        │    - allow_origins: http://localhost:5173 ✅ MATCH
        │    - allow_methods: POST ✅ MATCH
        │
        │ 6. Process request → Fraud Analysis
        │
        │ 7. Send response with CORS headers
        ↓
React Frontend
        │
        │ 8. Display results ✅
        │
```

---

## Testing the Configuration

### Browser Console - Successful Request
```
POST http://localhost:8000/api/v1/analyze
Status: 200 OK
Access-Control-Allow-Origin: http://localhost:5173 ✅
```

### Browser Console - CORS Error (Would happen if origin not allowed)
```
Access to XMLHttpRequest at 'http://localhost:8000/api/v1/analyze' 
from origin 'http://localhost:9999' 
has been blocked by CORS policy ❌
```

---

## Production Configuration

### For Production Deployment

**Scenario**: Deploy to domain `fraudshield.example.com`

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fraudshield.example.com",
        "https://www.fraudshield.example.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
```

**Changes**:
- Replace `localhost:5173` with your domain
- Use `https://` instead of `http://`
- Include both `www` and non-`www` versions if needed

---

## Security Best Practices Applied

✅ **Specific Origin**: Only allow trusted frontend URL  
✅ **Explicit Methods**: List only needed HTTP methods  
✅ **No Wildcard Origins**: Never use `allow_origins=["*"]`  
✅ **Credentials Allowed**: For authentication if needed  
✅ **Future-Proof**: PUT/DELETE reserved for scalability  

---

## Summary Table

| Aspect | Before | After | Status |
|--------|--------|-------|--------|
| Origins | 4 ports | 1 port (5173) | ✅ More specific |
| Methods | Wildcard "*" | Explicit list | ✅ More secure |
| Headers | Wildcard "*" | Wildcard "*" | ✅ Appropriate |
| Credentials | Allowed | Allowed | ✅ Unchanged |
| Security | Permissive | Restrictive | ✅ Improved |
| API Endpoints | Preserved | Preserved | ✅ Unchanged |
| Business Logic | Preserved | Preserved | ✅ Unchanged |

---

## Files Summary

| File | Change | Status |
|------|--------|--------|
| `src/fraudshield/api/main.py` | CORS configuration updated | ✅ Modified |
| All other files | No changes | ✅ Preserved |

---

## Related Documentation

- **Main Guide**: See `CORS_CONFIGURATION.md` for detailed setup
- **Testing**: See `frontend/README.md` for integration testing
- **API Docs**: Available at `http://localhost:8000/docs` (Swagger UI)

---

**Update Date**: November 2026  
**Version**: 1.0.0  
**Status**: ✅ Complete and Verified
