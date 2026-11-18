# FraudShield AI Frontend - Setup & Configuration Guide

## 📋 Frontend Overview

This document provides a complete guide for setting up and running the FraudShield AI React frontend.

### What's Included

- **React 19** with modern hooks and functional components
- **Vite** for ultra-fast development and optimized production builds
- **Responsive CSS** with CSS variables and media queries
- **API Integration Layer** for seamless backend communication
- **Professional UI** with intuitive transaction analysis workflow
- **Health Monitoring** with real-time backend connectivity checks

## 🗂️ Frontend File Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Header.jsx               # Header with health status indicator
│   │   │   - Displays FraudShield AI branding
│   │   │   - Shows backend connection status (healthy/error/checking)
│   │   │   - Displays backend API URL
│   │   │   - Pings backend every 30 seconds
│   │   │
│   │   ├── TransactionForm.jsx      # Main transaction input form
│   │   │   - 30 numeric input fields organized in 5 groups
│   │   │   - Input validation with error feedback
│   │   │   - Load Sample button for testing
│   │   │   - Clear button to reset form
│   │   │   - Disabled state during API request
│   │   │
│   │   ├── ResultsDisplay.jsx       # Results display & visualization
│   │   │   - Shows fraud detection results (probability, threshold, model)
│   │   │   - Shows risk assessment results (score, risk level, amount)
│   │   │   - Displays investigation status
│   │   │   - Loading spinner animation
│   │   │   - Error message display
│   │   │   - Empty state before first analysis
│   │   │   - Animated probability progress bar
│   │   │   - Color-coded risk levels (Red=High, Amber=Medium, Green=Low)
│   │   │
│   │   └── Footer.jsx               # App footer
│   │       - Project description
│   │       - Technology stack
│   │       - Links to GitHub and API docs
│   │
│   ├── services/
│   │   └── api.js                   # API service layer
│   │       - checkHealth()          - GET /health endpoint
│   │       - analyzeTransaction()   - POST /api/v1/analyze endpoint
│   │       - validateTransaction()  - Local validation of 30 fields
│   │
│   ├── styles/
│   │   ├── index.css                # Global CSS variables and base styles
│   │   │   - CSS custom properties for colors, spacing, typography
│   │   │   - Base element styles (typography, links, layout)
│   │   │   - Responsive breakpoints
│   │   │   - Utility classes
│   │   │
│   │   ├── Header.css               # Header component styles
│   │   ├── Footer.css               # Footer component styles
│   │   ├── TransactionForm.css      # Form component styles
│   │   │   - Feature groups layout
│   │   │   - Input field styling
│   │   │   - Button styles (primary, secondary, tertiary)
│   │   │   - Error state styling
│   │   │   - Responsive grid for fields
│   │   │
│   │   └── ResultsDisplay.css       # Results component styles
│   │       - Result sections with colored left borders
│   │       - Badge styling (fraud/legitimate, risk levels)
│   │       - Probability bar with gradient fill
│   │       - Risk score display
│   │       - Loading spinner animation
│   │       - Error alert styling
│   │       - Empty state styling
│   │
│   ├── App.jsx                      # Main app component
│   │   - Manages transaction analysis state
│   │   - Handles form submission
│   │   - Passes results to display component
│   │   - Two-column layout (form | results)
│   │
│   ├── App.css                      # App layout styles
│   │   - Two-column grid layout on desktop
│   │   - Single-column stack on mobile
│   │   - Container constraints
│   │
│   └── main.jsx                     # React entry point
│       - Mounts React app to #root DOM element
│
├── index.html                       # HTML template
│   - Single page app shell
│   - <div id="root"></div> for React mounting
│   - Links to main.jsx
│
├── vite.config.js                   # Vite configuration
│   - React plugin for JSX support
│   - Development and production settings
│
├── package.json                     # Node dependencies and scripts
│   - React 19 and ReactDOM
│   - Vite and plugins
│   - Scripts: dev, build, preview, lint
│
├── .env.example                     # Example environment file
│   - Template showing VITE_API_BASE_URL configuration
│   - Instructions for local vs. production
│
├── .env.local                       # Local environment (DO NOT COMMIT)
│   - Set VITE_API_BASE_URL=http://localhost:8000 for local development
│   - Set VITE_API_BASE_URL=http://13.53.168.74:8000 for AWS backend
│
├── .gitignore                       # Git ignore rules
│   - node_modules/, dist/, build/
│   - .env, .env.local, *.local files
│   - Editor and OS-specific files
│
├── README.md                        # Frontend documentation
│   - Quick start guide
│   - Available npm scripts
│   - Project structure
│   - Configuration instructions
│   - Component descriptions
│   - API integration details
│   - Troubleshooting guide
│   - Deployment instructions
│
└── FRONTEND_SETUP.md               # This file
    - Detailed setup and configuration guide
    - File structure explanation
    - Running the application
    - Building for production
    - Environment configuration
```

## 🚀 Getting Started

### Step 1: Verify Prerequisites
Ensure you have:
- **Node.js 16+** installed (`node --version`)
- **npm 7+** installed (`npm --version`)
- **Backend** running (at http://localhost:8000 or http://13.53.168.74:8000)

### Step 2: Install Dependencies
```bash
cd frontend
npm install
```

This installs:
- **react** (19.3.1) - React library
- **react-dom** (19.3.1) - React DOM rendering
- **vite** (8.3.6) - Build tool and dev server
- **@vitejs/plugin-react** (6.1.2) - React support for Vite
- **oxlint** (1.90.0) - Code linting tool

### Step 3: Configure Backend URL
```bash
cp .env.example .env.local
```

Edit `.env.local` and set the backend URL:

**For local development (backend on same machine):**
```
VITE_API_BASE_URL=http://localhost:8000
```

**For AWS Fargate backend:**
```
VITE_API_BASE_URL=http://13.53.168.74:8000
```

### Step 4: Start Development Server
```bash
npm run dev
```

Expected output:
```
  VITE v8.3.8  ready in 324 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

### Step 5: Open in Browser
Navigate to `http://localhost:5173/` in your web browser.

## 🎮 Using the Application

### 1. Check Backend Status
- Look at the header's health indicator
- **Green indicator** = Backend is healthy
- **Red indicator** = Connection error
- Indicator checks every 30 seconds

### 2. Enter Transaction Data
- Manually enter all 30 required fields, OR
- Click "Load Sample" to populate a legitimate transaction

### 3. Analyze Transaction
- Click "Analyze Transaction" button
- Watch the loading spinner
- Wait for results to display

### 4. Review Results
- **Fraud Detection Section**:
  - Prediction (Fraud / Legitimate)
  - Fraud Probability (0-100%)
  - Decision Threshold
  - Risk Level (Low / Medium / High)
  - Model Used (xgboost)
  
- **Risk Assessment Section**:
  - Risk Score (0-100)
  - Risk Level (Low / Medium / High)
  - Transaction Amount
  - Fraud Probability
  
- **Investigation Status**: Overall analysis status

## 📦 npm Scripts

### Development
```bash
npm run dev
```
Starts Vite development server with hot reload at `http://localhost:5173`
- Changes to any .jsx or .css file reload instantly
- Error messages appear in browser console and Vite terminal

### Build for Production
```bash
npm run build
```
Creates optimized production build in `dist/` folder
- Minified JavaScript (69.28 kB gzipped)
- Optimized CSS (1.47 kB gzipped)
- Asset optimization
- Build time: ~225 ms

### Preview Production Build
```bash
npm run preview
```
Serves the production build locally at `http://localhost:5173`
- Useful for testing before deployment
- Same as production environment

### Code Linting
```bash
npm run lint
```
Runs oxlint to check code quality
- Detects potential bugs
- Checks code style
- Validates best practices

## 🔧 Configuration

### Environment Variables

The frontend uses Vite's environment variable system. Variables prefixed with `VITE_` are exposed to client code.

**Available Variables:**
- `VITE_API_BASE_URL` - Backend API base URL (required)

**How They're Used:**
```javascript
// In src/services/api.js
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// In src/components/Header.jsx
const apiUrl = import.meta.env.VITE_API_BASE_URL;
```

### Environment Files
- `.env` - Local env (not tracked by git)
- `.env.local` - Local overrides (not tracked)
- `.env.example` - Template showing required variables
- `.env.production` - Production-specific variables (optional)

**Important**: Never commit `.env` or `.env.local` files. They're in `.gitignore` for security.

## 🎨 Styling System

### CSS Architecture
- **Global Variables**: Defined in `src/styles/index.css` via `:root {}`
- **Component Styles**: Modular CSS files for each component
- **Responsive Design**: Mobile-first approach with breakpoints at 768px and 1200px

### CSS Variables Reference

**Colors:**
```css
--primary-color: #2563eb         /* Main brand blue */
--primary-dark: #1e40af          /* Darker blue for hover */
--success-color: #10b981         /* Legitimate transactions */
--danger-color: #ef4444          /* Fraud/error red */
--warning-color: #f59e0b         /* Medium risk amber */
--info-color: #06b6d4            /* Information cyan */
```

**Spacing Scale:**
```css
--spacing-xs: 0.25rem   /* 4px */
--spacing-sm: 0.5rem    /* 8px */
--spacing-md: 1rem      /* 16px */
--spacing-lg: 1.5rem    /* 24px */
--spacing-xl: 2rem      /* 32px */
--spacing-2xl: 3rem     /* 48px */
```

**Typography:**
```css
--font-size-xs: 0.75rem      /* 12px */
--font-size-sm: 0.875rem     /* 14px */
--font-size-base: 1rem       /* 16px */
--font-size-lg: 1.125rem     /* 18px */
--font-size-xl: 1.25rem      /* 20px */
--font-size-2xl: 1.5rem      /* 24px */
--font-size-3xl: 1.875rem    /* 30px */
```

**Other:**
```css
--border-color: #e2e8f0
--shadow: 0 1px 3px rgba(0, 0, 0, 0.1)
--shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.1)
--radius-md: 0.375rem
--radius-lg: 0.5rem
```

## 🔌 API Integration

### Request/Response Flow

1. **User fills form** → `TransactionForm.jsx` state
2. **User clicks Analyze** → `App.jsx` calls `analyzeTransaction()`
3. **API Layer** → `api.js` formats and sends POST to backend
4. **Backend processes** → LangGraph workflow analyzes transaction
5. **Response received** → Results stored in `App.jsx` state
6. **Display updates** → `ResultsDisplay.jsx` renders results

### Error Handling

**Network Errors:**
- Caught in `analyzeTransaction()` with try-catch
- Displayed in `ResultsDisplay` with error alert
- User can try again after fixing backend

**Validation Errors:**
- Form validates all 30 fields before submission
- Error messages shown per field
- Cannot submit until all fields are valid

**Backend Errors:**
- HTTP errors (4xx, 5xx) caught and displayed
- Backend error messages shown to user
- Specific error details logged to console

## 📱 Responsive Design

### Breakpoints

**Desktop (> 1200px):**
- Two-column layout (form on left, results on right)
- Full-width controls

**Tablet (768px - 1200px):**
- Two-column layout maintained but narrower
- Smaller spacing and fonts

**Mobile (< 768px):**
- Single-column stacked layout
- Form above results
- Full-width buttons
- Smaller feature group grid (1 column)
- Smaller fonts and spacing

## 🚀 Building for Production

### Pre-Deployment Checklist
1. ✅ Backend is deployed and accessible
2. ✅ `.env.production` is configured with correct backend URL
3. ✅ Run `npm run build` successfully
4. ✅ Test with `npm run preview`
5. ✅ No console errors or warnings

### Build Output
```
frontend/dist/
├── index.html              # Main HTML file
├── assets/
│   ├── index-DykytF2W.css  # Minified styles
│   ├── index-DSXtc1GT.js   # Minified React app
│   ├── react-CHdo91hT.svg  # React logo
│   ├── vite-BF8QNONU.svg   # Vite logo
│   └── hero-CLDdwZDr.png   # Hero image
```

### Deployment Options

**Option 1: AWS S3 + CloudFront**
1. Build: `npm run build`
2. Upload `dist/` to S3
3. Set CloudFront to serve from S3

**Option 2: AWS Amplify**
1. Connect GitHub repo
2. Build command: `npm run build`
3. Build output directory: `dist`
4. Auto-deploys on push

**Option 3: Traditional Web Server**
1. Build: `npm run build`
2. Copy `dist/` to server `/var/www/html/`
3. Configure nginx/Apache to serve `index.html` for all routes

**Option 4: Docker Container**
```dockerfile
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## 🧪 Testing Guide

### Manual Testing Checklist

**Initial Load:**
- [ ] Page loads at http://localhost:5173
- [ ] Header displays with FraudShield AI title
- [ ] Health indicator shows in header
- [ ] Form loads with empty fields
- [ ] Results section shows "Enter transaction details..."

**Health Status:**
- [ ] Green indicator = backend healthy
- [ ] Red indicator = backend error
- [ ] API URL displays in header

**Form Testing:**
- [ ] Can type numbers in all 30 fields
- [ ] "Load Sample" fills form with test data
- [ ] "Clear" empties all fields
- [ ] Form validates: can't submit with invalid numbers
- [ ] "Analyze" button disables while processing

**Transaction Analysis:**
- [ ] Submitting form sends request to backend
- [ ] Loading spinner appears during request
- [ ] Results display after response
- [ ] Fraud detection section shows with probability bar
- [ ] Risk assessment section shows with risk score
- [ ] Investigation status displays

**Error Handling:**
- [ ] Disconnect backend, see "Connection Error" in header
- [ ] Submit form with backend down, see error message
- [ ] Reconnect backend, health indicator turns green

**Responsive Testing:**
- [ ] Desktop (1920px): two-column layout
- [ ] Tablet (768px): responsive shrinking
- [ ] Mobile (375px): single-column stack

## 🐛 Troubleshooting

### "VITE_API_BASE_URL is not set"
**Problem:** Warning appears in browser console
**Solution:** Create `.env.local` with:
```
VITE_API_BASE_URL=http://localhost:8000
```
Restart dev server: `npm run dev`

### "Connection Error" in Header
**Problem:** Backend health check fails
**Solutions:**
1. Verify backend is running: `curl http://localhost:8000/health`
2. Check `.env.local` has correct URL
3. Check if URL matches backend location (localhost vs AWS)
4. Check CORS headers on backend

### Form Not Submitting
**Problem:** Analyze button unresponsive
**Solutions:**
1. Check all 30 fields have numbers
2. Look for red error messages under fields
3. Check browser console for errors
4. Verify backend is accessible

### Results Not Displaying
**Problem:** Results section stays empty
**Solutions:**
1. Check loading spinner completes
2. Look for error message
3. Check browser Network tab for HTTP status
4. Check backend logs for processing errors

### Build Fails
**Problem:** `npm run build` shows errors
**Solutions:**
1. Run `npm install` again
2. Delete `node_modules` and `dist`, reinstall
3. Update Node.js to 18+
4. Check for syntax errors in .jsx files

## 📚 Additional Resources

- [Vite Docs](https://vitejs.dev/guide/)
- [React Docs](https://react.dev/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [FraudShield AI Backend](https://github.com/spqdot/FraudShield-AI)

## ✅ What's Working

- ✅ React app creates and builds successfully
- ✅ Vite dev server runs with hot reload
- ✅ All 5 components built and functional
- ✅ API service layer ready for backend integration
- ✅ Comprehensive styling with CSS variables
- ✅ Responsive design for all device sizes
- ✅ Error handling and validation
- ✅ Environment configuration system
- ✅ Production build optimizes to ~70KB gzipped

## 🎯 Next Steps

1. **Local Testing**: Run `npm run dev` and test with local backend
2. **Backend Verification**: Ensure backend is running and accessible
3. **Sample Analysis**: Click "Load Sample" then "Analyze" to test flow
4. **Custom Data**: Enter your own transaction data for analysis
5. **Production Deploy**: When ready, follow deployment options above
