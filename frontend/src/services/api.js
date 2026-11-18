/**
 * API Service - Handles all backend communication
 * Uses the VITE_API_BASE_URL environment variable for the backend URL
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

if (!API_BASE_URL) {
  console.warn('Warning: VITE_API_BASE_URL environment variable is not set');
}

/**
 * Check the health status of the backend
 */
export async function checkHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`Health check failed: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Health check error:', error);
    throw error;
  }
}

/**
 * Analyze a transaction for fraud
 * @param {Object} transaction - Transaction data with 30 numeric fields
 * @returns {Object} - Fraud detection and risk assessment results
 */
export async function analyzeTransaction(transaction) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/v1/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(transaction),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({
        detail: response.statusText,
      }));
      throw new Error(errorData.detail || `HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Transaction analysis error:', error);
    throw error;
  }
}

/**
 * Validate transaction data
 * Ensures all 30 required fields are present and are numbers
 */
export function validateTransaction(transaction) {
  const requiredFields = [
    'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
    'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
    'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
  ];

  const errors = [];

  for (const field of requiredFields) {
    if (!(field in transaction)) {
      errors.push(`Missing field: ${field}`);
    } else if (typeof transaction[field] !== 'number') {
      errors.push(`Field ${field} must be a number`);
    }
  }

  return {
    isValid: errors.length === 0,
    errors,
  };
}
