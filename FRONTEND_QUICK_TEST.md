# FraudShield AI Frontend - Quick Test Guide

## Running the Frontend Locally

### Prerequisites
- Node.js 18+ installed
- npm or yarn
- Backend running (or test URL configured)

### Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies (first time only):**
   ```bash
   npm install
   ```

3. **Configure backend URL (optional):**
   
   Create or edit `frontend/.env.local`:
   ```
   VITE_API_BASE_URL=http://13.53.168.74:8000
   ```
   
   Or use localhost for local testing:
   ```
   VITE_API_BASE_URL=http://localhost:8000
   ```

4. **Start development server:**
   ```bash
   npm run dev
   ```
   
   The frontend will start at: **http://localhost:5173** (or next available port)

---

## Testing the Three Improvements

### 1. Sticky Header Overlap Fix ✅

**What to test:**
1. Load http://localhost:5173
2. Scroll down in the form
3. Verify the blue header stays at top but doesn't hide content

**Expected behavior:**
- Header remains fixed and visible
- Form content is never hidden behind the header
- Content has proper spacing below the header

---

### 2. Number Formatting ✅

**What to test:**
1. Click "Load Sample" to auto-fill a sample transaction
2. Click "Analyze Transaction"
3. Check the Results panel (right side) for proper formatting

**Expected formatted values:**
- **Fraud Probability:** Shows as percentage (e.g., "85.42%")
- **Decision Threshold:** Shows as percentage (e.g., "50.00%")
- **Risk Score:** Shows with 2 decimal places (e.g., "75.33 / 100")
- **Transaction Amount:** Shows with thousands separators (e.g., "$149.62")

**Example values:**
- Amount 1234.56 → Displays as "$1,234.56"
- Amount 999999.99 → Displays as "$999,999.99"
- Probability 0.8542 → Displays as "85.42%"
- Risk score 75.33 → Displays as "75.33 / 100"

---

### 3. Amount Validation ✅

**What to test:**
1. Scroll to the "Amount Details" section (bottom of form)
2. Enter a negative number (e.g., "-100")
3. Click "Analyze Transaction"

**Expected behavior:**
- Red error message appears below Amount field
- Message reads: "Transaction amount must be non-negative"
- Form does not submit

**Test cases:**
- Negative amount (-100): Should show validation error ❌
- Zero amount (0): Should be allowed ✅
- Positive amount (149.62): Should be allowed ✅

---

## Form Fields Explanation

The form has 30 required fields:

1. **Time:** Transaction time in seconds
2. **V1–V28:** Principal Component Analysis (PCA) components (anonymized features)
3. **Amount:** Transaction amount in currency

### Sample Transaction (Pre-filled by "Load Sample" button)
```
Time: 0
V1-V28: Various decimal values
Amount: 149.62
```

---

## Results Display

After analyzing, you'll see:

### Fraud Detection Results
- **Prediction:** Fraud or Legitimate (shown in colored badge)
- **Fraud Probability:** Percentage (e.g., 85.42%)
- **Decision Threshold:** Threshold percentage (e.g., 50.00%)
- **Risk Level:** High, Medium, or Low
- **Model Used:** XGBoost, RandomForest, or LogisticRegression
- **Status:** Success or error message

### Risk Assessment Results
- **Risk Score:** Numerical score 0-100
- **Risk Level:** High, Medium, or Low
- **Transaction Amount:** Formatted with currency
- **Fraud Probability:** From detection module

### Investigation Status
- Status of the investigation (Completed, Pending, etc.)

---

## Troubleshooting

### "Port 5173 is in use"
The dev server will automatically use the next available port (5174, 5175, etc.).
Check the console output for the correct URL.

### "Cannot reach backend"
If the backend URL is incorrect or unreachable, the frontend will show:
- "Connection Error" in the header status
- Clear error message in the results panel

### Input fields not visible
- Check that your monitor is set to light theme
- Verify CSS has loaded (check DevTools > Styles)
- Ensure input background is white and text is dark

### "Transaction amount must be non-negative" won't go away
This is expected behavior - the validation clears when you change the Amount value to a valid (non-negative) number.

---

## Production Build

To create an optimized production build:

```bash
npm run build
```

Output will be in `frontend/dist/` - ready to deploy to a web server.

---

## Performance Tips

- Clear browser cache if styles seem outdated: `Ctrl+Shift+Delete`
- Check browser console (F12) for JavaScript errors
- Use the Network tab to verify API calls are being made
- Check the Response tab to see what the backend is returning

---

## Support

For issues with:
- **Frontend:** Check browser console (F12) for JavaScript errors
- **Backend:** Verify the CORS configuration and API URL
- **Formatting:** All numbers use `services/formatters.js` utility functions
- **Validation:** Check `components/TransactionForm.jsx` for validation logic
