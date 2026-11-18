# FraudShield AI Frontend

A professional React + Vite dashboard for financial fraud detection and investigation using the FraudShield AI backend API.

## Overview

This React frontend provides a user-friendly interface to:
- **Input transaction data** with 30 required numeric fields (Time, V1-V28, Amount)
- **Analyze transactions** for fraud probability and risk assessment
- **Display results** including fraud detection metrics, risk scores, and investigation status
- **Monitor backend connectivity** with real-time health status indicator

## Features

✅ **Professional Dashboard Layout** - Clean, responsive design optimized for financial technology  
✅ **Transaction Input Form** - Organized fields grouped by feature type  
✅ **Sample Data** - Load sample transaction for quick testing  
✅ **Real-time Results** - Displays fraud probability, prediction, risk score, and investigation status  
✅ **Backend Health Monitoring** - Shows connection status to FastAPI backend  
✅ **Error Handling** - User-friendly error messages with detailed logging  
✅ **Responsive Design** - Works on desktop, tablet, and mobile devices  
✅ **Environment Configuration** - API URL configurable via Vite environment variables  

## Technology Stack

- **Framework**: React 18+ with Hooks
- **Build Tool**: Vite 4+
- **Styling**: CSS with CSS custom properties (variables)
- **HTTP Client**: Fetch API
- **Environment**: Vite environment variables (VITE_API_BASE_URL)

## Project Structure

```
frontend/
├── src/
│   ├── components/           # React components
│   │   ├── Header.jsx       # App header with health status
│   │   ├── TransactionForm.jsx  # Form for transaction input
│   │   ├── ResultsDisplay.jsx   # Results display panel
│   │   └── Footer.jsx           # App footer
│   ├── services/            # API layer
│   │   └── api.js          # Backend communication
│   ├── styles/             # Component-specific CSS
│   │   ├── Header.css
│   │   ├── TransactionForm.css
│   │   ├── ResultsDisplay.css
│   │   └── Footer.css
│   ├── App.jsx             # Main application component
│   ├── App.css             # Global app styles
│   ├── index.css           # Global styles and CSS variables
│   └── main.jsx            # React entry point
├── .env.example            # Environment variables template
├── .env.local              # Local environment configuration (not committed)
├── .gitignore              # Git ignore rules
├── package.json            # Dependencies and scripts
├── vite.config.js          # Vite configuration
└── README.md               # This file
```

## Installation

### Prerequisites

- Node.js 16+ (LTS recommended)
- npm 7+ or yarn

### Setup Steps

1. **Install dependencies** (if not already done):
   ```bash
   cd frontend
   npm install
   ```

2. **Configure the backend URL**:
   
   The frontend uses the `VITE_API_BASE_URL` environment variable to connect to the backend.
   
   For local development, edit `.env.local`:
   ```env
   VITE_API_BASE_URL=http://localhost:8000
   ```
   
   For AWS Fargate (production):
   ```env
   VITE_API_BASE_URL=http://13.53.168.74:8000
   ```
   
   > **Note**: `.env.local` is excluded from Git and not committed to the repository.

3. **Verify the `.env.local` file exists**:
   ```bash
   cat .env.local
   ```

## Running the Application

### Development Server

Start the Vite development server with hot module replacement (HMR):

```bash
npm run dev
```

This will start the server on `http://localhost:5173` (or the next available port if 5173 is busy).

Output example:
```
  VITE v8.3.8  ready in 489 ms

  ➜  Local:   http://localhost:5174/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

Open the URL in your browser to access the dashboard.

### Production Build

Create an optimized production build:

```bash
npm run build
```

The build output will be in the `dist/` folder, ready for deployment.

Preview the production build locally:

```bash
npm run preview
```

## API Integration

### Backend Connection

The frontend communicates with the FastAPI backend at the configured `VITE_API_BASE_URL`.

**Health Check Endpoint**:
- `GET /health` - Returns `{"status": "healthy"}`
- Checked automatically on app load and every 30 seconds
- Status indicator in the header shows the connection status

**Fraud Analysis Endpoint**:
- `POST /api/v1/analyze` - Analyzes a transaction for fraud
- Request: `TransactionRequest` with 30 numeric fields
- Response: `{fraud_detection, risk_assessment, investigation_status}`

### Request Schema

The form sends a JSON object with 30 numeric fields:

```json
{
  "Time": 0,
  "V1": -1.3598071,
  "V2": -0.0727464,
  ...
  "V28": -0.0020311,
  "Amount": 149.62
}
```

### Response Schema

The API returns a comprehensive analysis result:

```json
{
  "fraud_detection": {
    "fraud_probability": 0.123,
    "threshold": 0.5,
    "prediction": "Legitimate",
    "risk_level": "Low",
    "model": "xgboost",
    "agent": "fraud_detection_agent",
    "status": "completed"
  },
  "risk_assessment": {
    "risk_score": 25.5,
    "risk_level": "Low",
    "transaction_amount": 149.62,
    "fraud_probability": 0.123,
    "agent": "risk_assessment_agent",
    "status": "completed"
  },
  "investigation_status": "completed"
}
```

## Components

### Header.jsx
- Displays FraudShield AI branding and tagline
- Shows backend connection status (healthy/error/checking)
- Displays the configured API URL
- Performs health checks every 30 seconds

### TransactionForm.jsx
- Input form for all 30 transaction features
- Organized feature groups: Time, V1-V9, V10-V19, V20-V28, Amount
- Load Sample button to populate test data
- Clear button to reset the form
- Validation error messages per field
- Disabled state during analysis

### ResultsDisplay.jsx
- Shows loading spinner during analysis
- Displays error messages if analysis fails
- Shows empty state with instructions when no results
- Fraud Detection section: probability, threshold, prediction, risk level
- Risk Assessment section: risk score, risk level, amount
- Investigation summary
- Responsive grid layout for results

### Footer.jsx
- About FraudShield AI description
- Technology stack information
- Links to GitHub repository and API documentation
- Copyright information

## Styling

### CSS Variables

The application uses CSS custom properties (variables) for consistent theming:

**Colors**:
- `--primary-color: #0066cc` - Main brand color
- `--success-color: #00b366` - Success states
- `--danger-color: #cc0000` - Error/fraud states
- `--warning-color: #ff9900` - Warning states
- `--text-primary: #333333` - Primary text color
- `--bg-secondary: #f9fafb` - Secondary background

**Spacing**:
- `--spacing-sm: 8px`
- `--spacing-md: 16px`
- `--spacing-lg: 24px`
- `--spacing-xl: 32px`

**Responsive Breakpoints**:
- Desktop: 1024px and up
- Tablet: 768px - 1023px
- Mobile: Below 768px

### Theme Files

- `index.css` - Global styles and CSS variables
- `App.css` - Main layout styles
- `styles/Header.css` - Header component styles
- `styles/TransactionForm.css` - Form component styles
- `styles/ResultsDisplay.css` - Results component styles
- `styles/Footer.css` - Footer component styles

## Configuration

### Environment Variables

Create a `.env.local` file in the frontend directory:

```env
# Backend API base URL
VITE_API_BASE_URL=http://13.53.168.74:8000
```

**Available Ports** (from the backend perspective):
- Local development: `http://localhost:8000`
- AWS Fargate: `http://13.53.168.74:8000`

### Vite Configuration

The `vite.config.js` file configures:
- React plugin for JSX support
- Port 5173 as default (falls back to next available port)
- HMR for hot module replacement

## CORS Configuration

The backend FastAPI application includes CORS middleware to allow requests from:
- `http://localhost:5173`
- `http://localhost:5174`
- `http://localhost:3000`
- `http://localhost:5000`

If running the frontend on a different host/port, ensure the backend's CORS configuration includes that origin.

## Development Workflow

### 1. Start Development Server
```bash
npm run dev
```

### 2. Make Changes
- Edit React components in `src/`
- Modify styles in `src/styles/`
- Update the API service in `src/services/api.js`

### 3. Hot Module Replacement
Changes are automatically reflected in the browser without full page reload.

### 4. Browser DevTools
- React Developer Tools browser extension recommended
- Use browser console for debugging
- Network tab shows API requests and responses

## Troubleshooting

### "Cannot connect to backend"
1. Verify the backend is running: `curl http://13.53.168.74:8000/health`
2. Check the VITE_API_BASE_URL in `.env.local` matches the backend URL
3. Verify CORS is enabled on the backend
4. Check browser console for CORS errors

### Form validation errors
- Ensure all 30 fields are filled with numeric values
- Decimal values are accepted (e.g., -1.3598071)
- Amount field must be non-negative

### "Analyzing..." spinner doesn't stop
- Check browser console for API errors
- Verify backend is responding
- Check network tab in DevTools for failed requests

### Port already in use
- Vite automatically uses the next available port (5174, 5175, etc.)
- Or specify a different port: `npm run dev -- --port 3000`

## Deployment

### Build for Production
```bash
npm run build
```

### Environment Configuration for Deployment

Update `.env.local` or set environment variables in your deployment platform:

```env
VITE_API_BASE_URL=https://your-production-backend-url:8000
```

### Deployment Platforms

**Docker**:
```dockerfile
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
RUN npm install -g serve
COPY --from=build /app/dist ./dist
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
```

**AWS S3 + CloudFront**:
```bash
# Build
npm run build

# Upload dist/ to S3
aws s3 sync dist/ s3://your-bucket-name/

# Invalidate CloudFront cache
aws cloudfront create-invalidation --distribution-id YOUR_DIST_ID --paths "/*"
```

## Git Workflow

The `.gitignore` file excludes:
- `node_modules/` - Installed dependencies
- `.env.local` - Local environment configuration (sensitive)
- `dist/` - Build output
- `.oxlintrc.json.bak` - Linter backups
- Other temporary files

Committed files:
- `.env.example` - Template for environment variables
- Source code in `src/`
- Configuration files

## Available Scripts

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter (Oxlint)
npm run lint

# Run linter with fix
npm run lint -- --fix
```

## Support and Documentation

- **API Documentation**: http://13.53.168.74:8000/docs (Swagger UI)
- **GitHub Repository**: https://github.com/spqdot/FraudShield-AI
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **React Docs**: https://react.dev/
- **Vite Docs**: https://vitejs.dev/

## License

Part of the FraudShield AI project. See main repository for licensing details.
