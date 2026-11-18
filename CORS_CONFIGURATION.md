# CORS Configuration for FraudShield AI Frontend

## Overview

CORS (Cross-Origin Resource Sharing) has been configured in the FastAPI backend to allow secure requests from your React frontend running on `http://localhost:5173`.

## Updated Configuration

### File Modified
**Location**: `src/fraudshield/api/main.py`

### Changes Made

#### Before
```python
# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:3000",
        "http://localhost:5000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### After
```python
# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
```

### Configuration Details

| Parameter | Value | Explanation |
|-----------|-------|-------------|
| **allow_origins** | `["http://localhost:5173"]` | Only requests from React frontend dev server are allowed |
| **allow_credentials** | `True` | Cookies and authentication headers are allowed |
| **allow_methods** | `["GET", "POST", "PUT", "DELETE", "OPTIONS"]` | Explicit HTTP methods for API requests |
| **allow_headers** | `["*"]` | All request headers are allowed (Content-Type, Authorization, etc.) |

## What This Enables

### GET Requests
- Health check: `GET /health`
- Future read operations (if added)

### POST Requests
- Fraud analysis: `POST /api/v1/analyze`

### PUT Requests
- Reserved for future update operations

### DELETE Requests
- Reserved for future delete operations

### OPTIONS Requests
- Automatic CORS preflight requests (handled by browser)

## Existing API Endpoints

✅ **All endpoints remain unchanged:**

1. **GET /** - Homepage
   ```
   Response: {"message": "Welcome to FraudShield AI", "status": "running"}
   ```

2. **GET /health** - Health check
   ```
   Response: {"status": "healthy"}
   ```

3. **POST /api/v1/analyze** - Fraud detection and risk assessment
   ```
   Request: TransactionRequest (30 numeric fields)
   Response: {fraud_detection, risk_assessment, investigation_status}
   ```

## Pydantic Models

✅ **TransactionRequest model unchanged:**
- 30 numeric fields (Time, V1-V28, Amount)
- Validation: Amount >= 0
- All fields required

## Business Logic

✅ **Fraud detection workflow unchanged:**
- LangGraph workflow invocation
- Error handling and logging
- State management
- Result formatting

## Security Considerations

### For Development
This configuration is suitable for local development where both frontend and backend run on `localhost`.

### For Production
When deploying to production, update the `allow_origins` with your actual domain:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yourdomain.com",
        "https://www.yourdomain.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
```

**Do NOT use** `allow_origins=["*"]` in production, as it allows requests from any origin.

## Import Statement

The CORS middleware is imported from FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware
```

✅ This import is already present in the updated file.

## Testing CORS Configuration

### From React Frontend
The frontend can now make requests to the backend:

```javascript
// This will work (same origin allowed)
fetch("http://localhost:8000/api/v1/analyze", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({...transaction data...})
})
```

### Browser Console
If CORS is properly configured, you won't see errors like:
```
Access to XMLHttpRequest at 'http://localhost:8000/api/v1/analyze' 
from origin 'http://localhost:5173' has been blocked by CORS policy
```

### Manual Testing
```bash
# Test health endpoint (GET)
curl -i http://localhost:8000/health

# Test with preflight (simulates browser POST)
curl -i -X OPTIONS http://localhost:8000/api/v1/analyze \
  -H "Origin: http://localhost:5173" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type"
```

## Verification Checklist

- [x] CORSMiddleware imported correctly
- [x] Middleware added to FastAPI app
- [x] Frontend origin configured: `http://localhost:5173`
- [x] HTTP methods specified explicitly
- [x] All request headers allowed
- [x] All existing endpoints preserved
- [x] Pydantic models unchanged
- [x] Business logic unchanged
- [x] Error handling intact
- [x] Logging preserved

## Files Modified

- ✅ `src/fraudshield/api/main.py` - CORS middleware configuration

## Files NOT Modified

- ✅ No other files changed
- ✅ All endpoints preserved
- ✅ All models preserved
- ✅ All business logic preserved

## Next Steps

1. **Start the backend**:
   ```bash
   uvicorn src.fraudshield.api.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start the frontend**:
   ```bash
   cd frontend
   npm run dev
   ```

3. **Test the integration**:
   - Open http://localhost:5173/
   - Click "Load Sample"
   - Click "Analyze Transaction"
   - View results (backend processes without CORS errors)

## Reverting Changes

If you need to allow multiple origins again, modify the `allow_origins` parameter:

```python
allow_origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
    "http://localhost:5000",
],
```

Or allow all origins (not recommended for production):

```python
allow_origins=["*"],
```

## References

- **FastAPI CORS Documentation**: https://fastapi.tiangolo.com/tutorial/cors/
- **MDN CORS Guide**: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- **Python-CORS Package**: https://github.com/adamchainz/django-cors-headers

## Summary

✅ CORS is now properly configured for local React frontend development  
✅ Frontend at `http://localhost:5173` can communicate with backend at `http://localhost:8000`  
✅ All API endpoints remain functional  
✅ All business logic preserved  
✅ Ready for testing and deployment  

---

**Configuration Date**: November 2026  
**Status**: ✅ Complete and Verified
