/**
 * Format a number as currency with thousands separators
 * @param {number} value - The numeric value to format
 * @returns {string} Formatted currency string
 */
export function formatCurrency(value) {
  if (value === null || value === undefined || isNaN(value)) {
    return 'N/A';
  }

  const numValue = parseFloat(value);

  // Handle very large numbers to avoid scientific notation
  if (Math.abs(numValue) >= 1e15) {
    return numValue.toLocaleString('en-US', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });
  }

  return numValue.toLocaleString('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
}

/**
 * Format a decimal number with appropriate precision
 * @param {number} value - The numeric value to format
 * @param {number} decimals - Number of decimal places (default: 4)
 * @returns {string} Formatted number string
 */
export function formatDecimal(value, decimals = 4) {
  if (value === null || value === undefined || isNaN(value)) {
    return 'N/A';
  }

  const numValue = parseFloat(value);
  return numValue.toLocaleString('en-US', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

/**
 * Format a percentage value
 * @param {number} value - The numeric value (0-1 or 0-100)
 * @param {boolean} isDecimal - If true, value is 0-1; if false, value is 0-100
 * @returns {string} Formatted percentage string
 */
export function formatPercentage(value, isDecimal = true) {
  if (value === null || value === undefined || isNaN(value)) {
    return 'N/A';
  }

  const numValue = isDecimal ? parseFloat(value) * 100 : parseFloat(value);
  return numValue.toLocaleString('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }) + '%';
}
