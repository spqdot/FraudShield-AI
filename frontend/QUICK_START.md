# FraudShield AI Frontend - Quick Start Guide

## 🚀 Get Started in 2 Minutes

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Run the Application
```bash
npm run dev
```

The application will open at **http://localhost:5174/**

## 📋 What You Need

- Node.js 16+ (download from https://nodejs.org/)
- npm 7+ (comes with Node.js)
- Backend running at http://13.53.168.74:8000

## 🎯 First Test

1. Click **"Load Sample"** button to populate test data
2. Click **"Analyze Transaction"** button
3. View results in the right panel showing:
   - Fraud Probability
   - Prediction (Legitimate/Fraud)
   - Risk Score
   - Risk Level

## 🔧 Configuration

The backend URL is set in `.env.local`:

```env
VITE_API_BASE_URL=http://13.53.168.74:8000
```

For local backend, change to:
```env
VITE_API_BASE_URL=http://localhost:8000
```

## 📦 Available Commands

```bash
npm run dev      # Start development server (default: port 5174)
npm run build    # Create production build (output: dist/)
npm run preview  # Test production build locally
npm run lint     # Run code linter
```

## 🌐 Backend Connection

The dashboard connects to the FastAPI backend via:
- **Health Check**: GET `/health` (every 30 seconds)
- **Analysis**: POST `/api/v1/analyze` (on form submission)

## 📋 Input Fields (30 Total)

**Form Sections**:
- Time (1 field)
- PCA Features V1-V9 (9 fields)
- PCA Features V10-V19 (10 fields)
- PCA Features V20-V28 (9 fields)
- Transaction Amount (1 field)

## 💡 Key Features

✅ Real-time backend health status indicator  
✅ Sample transaction data for quick testing  
✅ Form validation with error messages  
✅ Loading indicators during analysis  
✅ Comprehensive results display  
✅ Responsive design for all devices  

## 🐛 Troubleshooting

**"Cannot connect to backend"**
→ Verify backend is running: `curl http://13.53.168.74:8000/health`

**"Port already in use"**
→ Vite will automatically use port 5175, 5176, etc.

**"Form won't submit"**
→ Check console for validation errors

## 📚 More Information

See [README.md](./README.md) for complete documentation including:
- Detailed setup instructions
- Component descriptions
- Styling and customization
- Deployment options
- API schema reference

## 🔗 Useful Links

- **Frontend**: http://localhost:5174/
- **Backend API Docs**: http://13.53.168.74:8000/docs
- **Backend Health**: http://13.53.168.74:8000/health
- **GitHub**: https://github.com/spqdot/FraudShield-AI

---

Happy fraud detection! 🛡️
