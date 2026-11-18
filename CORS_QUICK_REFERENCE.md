# CORS Quick Reference - 1-Page Cheat Sheet

## 🎯 What Was Done

**File**: `src/fraudshield/api/main.py`  
**Change**: Added CORS middleware (lines 1-26)  
**Result**: React frontend at `localhost:5173` can now access backend at `localhost:8000`

---

## 💻 The Code

```python
# Line 2: Import
from fastapi.middleware.cors import CORSMiddleware

# Lines 18-26: Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],           # ← Only this frontend origin
    allow_credentials=True,                             # ← Allow cookies/auth
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # ← Explicit methods
    allow_headers=["*"],                                # ← All headers OK
)
```

---

## 🚀 To Run (3 Commands)

### Terminal 1 - Backend
```bash
cd D:\Shrabani.Personal\Self_Project\FraudShield_AI
uvicorn src.fraudshield.api.main:app --reload --host 0.0.0.0 --port 8000
```

### Terminal 2 - Frontend
```bash
cd frontend
npm run dev
```

### Then
- Open http://localhost:5173
- Load sample transaction
- Click "Analyze Transaction"
- ✅ Results should display (no CORS errors)

---

## 🔒 Security Summary

| Aspect | Before | After |
|--------|--------|-------|
| Origins | 4 ports | 1 port ✅ |
| Methods | Wildcard | Explicit ✅ |
| Security | Permissive | Restrictive ✅ |

---

## 🧪 Quick Test

**Browser DevTools (F12) → Network Tab → Click "Analyze"**

Look for POST request to `/api/v1/analyze` with these response headers:
```
✅ Access-Control-Allow-Origin: http://localhost:5173
✅ Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
✅ Status: 200 OK
```

---

## 📋 HTTP Methods Enabled

| Method | Use | Status |
|--------|-----|--------|
| GET | Retrieve data | ✅ |
| POST | Submit data | ✅ |
| PUT | Update data | ✅ |
| DELETE | Delete data | ✅ |
| OPTIONS | Preflight | ✅ |

---

## 🎓 What CORS Does

```
React App (localhost:5173)
        ↓
Browser: "Can I call localhost:8000?"
        ↓
CORS Middleware checks:
- Is origin localhost:5173? ✅ YES
- Is method POST? ✅ YES
        ↓
"Yes, you can call it"
        ↓
Request succeeds → Results display
```

---

## ⚠️ Common Issues & Fixes

### "CORS Error" in Console
❌ **Cause**: Backend not running or wrong port  
✅ **Fix**: Verify backend running on port 8000

### "Cannot GET /"
❌ **Cause**: Frontend not running  
✅ **Fix**: Run `npm run dev` in frontend folder

### Results not displaying
❌ **Cause**: CORS blocked or API error  
✅ **Fix**: Check DevTools → Network tab for errors

### 404 on /api/v1/analyze
❌ **Cause**: Backend version issue  
✅ **Fix**: Verify endpoint exists in `main.py`

---

## 📝 Configuration for Production

Replace this line in `main.py`:
```python
allow_origins=["http://localhost:5173"],
```

With this:
```python
allow_origins=[
    "https://yourdomain.com",
    "https://www.yourdomain.com",
],
```

**Key changes**:
- Use `https://` (not `http://`)
- Use your actual domain
- Include both www and non-www versions

---

## 📂 Files Involved

| File | Role | Status |
|------|------|--------|
| `src/fraudshield/api/main.py` | Backend + CORS | ✅ Updated |
| `frontend/` | React app | ✅ Already working |
| All others | Unchanged | ✅ Preserved |

---

## ✅ Verification Checklist

Before considering complete:

- [ ] Backend starts on port 8000
- [ ] Frontend starts on port 5173
- [ ] No CORS errors in DevTools console
- [ ] "Load Sample" button works
- [ ] "Analyze Transaction" button works
- [ ] Results display correctly
- [ ] Health status shows "Connected ✓"

---

## 🔗 Endpoints Now Accessible

```
✅ GET  http://localhost:8000/
✅ GET  http://localhost:8000/health
✅ POST http://localhost:8000/api/v1/analyze
```

All from: `http://localhost:5173`

---

## 💡 Remember

✅ CORS middleware is **between** app imports and routes  
✅ Only one origin specified: `localhost:5173`  
✅ Methods are explicit (not wildcard "*")  
✅ All headers allowed (fine for development)  
✅ Credentials enabled (ready for auth)  

---

## 🆘 Still Having Issues?

1. **Read** `CORS_CONFIGURATION.md` (detailed explanation)
2. **Compare** `CORS_BEFORE_AND_AFTER.md` (code comparison)
3. **Check** `CORS_UPDATE_SUMMARY.md` (troubleshooting section)
4. **Verify** both services running: 
   - Backend: `curl http://localhost:8000/health`
   - Frontend: Check browser can reach `http://localhost:5173`

---

## 📊 Quick Visual

```
┌─────────────────────────────┐
│   React Frontend            │
│   localhost:5173            │
│  ┌────────────────────────┐ │
│  │ Transaction Form       │ │
│  │ [Load Sample]          │ │
│  │ [Analyze Transaction]  │ │
│  └────────────────────────┘ │
└─────────────────────────────┘
            ↓ (POST)
   ┌────────────────────┐
   │  CORS Middleware   │
   │  Origin OK? ✅     │
   │  Method OK? ✅     │
   └────────────────────┘
            ↓
┌─────────────────────────────┐
│   FastAPI Backend           │
│   localhost:8000            │
│  ┌────────────────────────┐ │
│  │ /api/v1/analyze        │ │
│  │ ├─ Fraud Detection     │ │
│  │ ├─ Risk Assessment     │ │
│  │ └─ Investigation       │ │
│  └────────────────────────┘ │
└─────────────────────────────┘
            ↓ (JSON Response)
   ┌────────────────────┐
   │  CORS Headers      │
   │  Allow: 5173 ✅    │
   └────────────────────┘
            ↓
┌─────────────────────────────┐
│   Browser displays results  │
│   ✅ No CORS errors         │
│   ✅ Fraud probability      │
│   ✅ Risk score             │
│   ✅ Investigation status   │
└─────────────────────────────┘
```

---

## 🎉 You're All Set!

Your FraudShield AI project is configured and ready to go. Start the services and test the integration!

**Status**: ✅ Complete  
**Next Step**: Run the services and test!
