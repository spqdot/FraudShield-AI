# FraudShield AI Frontend - Quick Reference Guide

## 🚀 Start Here (3 Minutes to Running)

### 1️⃣ Install & Run
```bash
cd frontend
npm install
npm run dev
```

### 2️⃣ Open Browser
Navigate to: **http://localhost:5173**

### 3️⃣ Configure Backend (if needed)
Edit `frontend/.env.local`:
```
VITE_API_BASE_URL=http://localhost:8000
```

Done! You're ready to analyze transactions.

---

## 📂 Project Layout

```
FraudShield_AI/
├── src/                              # Backend Python code
├── models/                           # Trained ML models
├── frontend/                         # React frontend (NEW)
│   ├── src/
│   │   ├── components/               # 4 React components
│   │   ├── services/                 # API layer
│   │   ├── styles/                   # Component CSS
│   │   ├── App.jsx                   # Main component
│   │   └── main.jsx                  # Entry point
│   ├── package.json                  # npm dependencies
│   ├── vite.config.js                # Build config
│   ├── .env.example                  # Env template
│   ├── .env.local                    # Your local config
│   ├── README.md                     # Quick start
│   ├── FRONTEND_SETUP.md             # Detailed guide
│   └── dist/                         # Production build
├── FRONTEND_IMPLEMENTATION_SUMMARY.md # This project summary
├── docker-compose.yml
├── Dockerfile
└── README.md                         # Main project README
```

---

## 🎮 How It Works

### 1. User Enters Transaction
- Fill in all 30 numeric fields OR click "Load Sample"
- Form validates inputs automatically

### 2. User Clicks Analyze
- Sends POST request to `/api/v1/analyze`
- Backend processes with LangGraph workflow
- Shows loading spinner while waiting

### 3. Results Display
- **Fraud Detection**: Probability, threshold, model, risk level
- **Risk Assessment**: Risk score, risk level, amount
- **Status**: Investigation status

---

## 📋 npm Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start dev server (hot reload) |
| `npm run build` | Create production build |
| `npm run preview` | Preview production build |
| `npm run lint` | Check code quality |

---

## 🔧 Configuration

### Environment Variables
Create `frontend/.env.local`:
```
# Local backend
VITE_API_BASE_URL=http://localhost:8000

# AWS backend
# VITE_API_BASE_URL=http://13.53.168.74:8000
```

**Important**: `.env.local` is NOT committed to Git (security best practice)

---

## 📱 Responsive Design

| Screen | Layout |
|--------|--------|
| Desktop (>1200px) | 2 columns (form \| results) |
| Tablet (768-1200px) | 2 columns (responsive) |
| Mobile (<768px) | 1 column (stacked) |

---

## 🔌 API Endpoints Used

### Health Check (Auto, every 30 seconds)
```
GET /health
Response: { "status": "healthy" }
```

### Transaction Analysis
```
POST /api/v1/analyze
Content-Type: application/json

Body: {
  "Time": 0,
  "V1": -1.3598071,
  "V2": -0.0727464,
  ...
  "V28": -0.0020311,
  "Amount": 149.62
}

Response: {
  "fraud_detection": { ... },
  "risk_assessment": { ... },
  "investigation_status": "..."
}
```

---

## 🎨 Component Structure

### Header Component
- Shows FraudShield AI title
- Backend health indicator
- API URL display
- Auto-checks every 30 seconds

### TransactionForm Component
- 30 numeric input fields
- Organized in 5 groups
- Validation feedback
- Load Sample / Clear buttons
- Analyze button

### ResultsDisplay Component
- Fraud Detection results
  - Prediction badge (Fraud/Legitimate)
  - Fraud probability bar
  - Decision threshold
  - Risk level
  - Model used
  
- Risk Assessment results
  - Risk score (0-100)
  - Risk level
  - Transaction amount
  - Fraud probability
  
- Investigation Status
- Error messages & loading states

### Footer Component
- Project description
- Technology stack
- Links to GitHub & API docs

---

## 🔐 Security Notes

✅ Environment variables NOT in Git (.env.local in .gitignore)
✅ No hardcoded API keys or credentials
✅ Input validation before API calls
✅ Error messages don't expose sensitive details
✅ CORS-aware frontend

---

## 🐛 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| "Connection Error" | Check backend is running, verify .env.local URL |
| Form won't submit | Ensure all 30 fields have valid numbers |
| Results not showing | Check backend is running, see browser console for errors |
| "VITE_API_BASE_URL not set" | Create .env.local with VITE_API_BASE_URL value |
| Dev server won't start | Run `npm install` again, check Node.js 16+ |

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Build time | ~225 ms |
| Bundle size | 222 KB (69 KB gzipped) |
| Dev server startup | ~324 ms |
| Load time | <1 second |
| Health checks | Every 30 seconds |

---

## 🎯 Next Steps

### For Local Testing
1. Run `npm run dev`
2. Open http://localhost:5173
3. Click "Load Sample"
4. Click "Analyze Transaction"
5. Review fraud & risk results

### For Production Deployment
1. Run `npm run build` → creates `dist/` folder
2. Upload `dist/` to your web server
3. Set backend URL via `.env.production`
4. Deploy!

### To Modify / Extend
- Edit `.jsx` files in `src/components/`
- Edit `.css` files in `src/styles/`
- Modify API calls in `src/services/api.js`
- Add new components as needed

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Quick start guide |
| `FRONTEND_SETUP.md` | Detailed setup & configuration |
| `FRONTEND_IMPLEMENTATION_SUMMARY.md` | Project summary (this folder) |

---

## 💡 Tips

**Hot Reload**: Changes to .jsx/.css automatically reload in browser
**Load Sample**: Fills form with real transaction data for testing
**Health Indicator**: Green = backend healthy, Red = error
**Console Errors**: Press F12 to see browser console for debug info
**API Response**: Check Network tab in Dev Tools to see API responses

---

## ✅ Verification Checklist

Before deployment:
- [ ] `npm run build` completes successfully
- [ ] `npm run preview` shows working app
- [ ] Backend is accessible from frontend URL
- [ ] Health indicator shows green
- [ ] Sample transaction analyzes successfully
- [ ] All results display correctly
- [ ] Responsive design works on mobile

---

## 🆘 Need Help?

**Common Issues**:
1. **Backend won't connect** → Check URL in .env.local
2. **Form validation errors** → Ensure all fields are numbers
3. **Build fails** → Delete node_modules, run npm install again
4. **Port 5173 in use** → Run `npm run dev -- --port 5174`

**Check These**:
- Backend running: `curl http://localhost:8000/health`
- Node version: `node --version` (needs 16+)
- npm version: `npm --version` (needs 7+)
- .env.local exists: `ls frontend/.env.local`

---

## 🚀 You're Ready!

**Start developing:**
```bash
cd frontend && npm run dev
```

**Deploy to production:**
```bash
npm run build
# Upload dist/ folder to your server
```

Enjoy your professional fraud detection dashboard! 🎉
