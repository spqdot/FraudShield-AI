import React from 'react';
import '../styles/ResultsDisplay.css';
import { formatCurrency, formatPercentage, formatDecimal } from '../services/formatters';

const ResultsDisplay = ({ results, loading, error }) => {
  if (loading) {
    return (
      <div className="results-container loading">
        <div className="loader"></div>
        <p className="loading-text">Analyzing transaction...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="results-container error">
        <div className="alert alert-error">
          <h3>Analysis Error</h3>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  if (!results) {
    return (
      <div className="results-container empty">
        <div className="empty-state">
          <svg className="empty-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p>Enter transaction details and click "Analyze Transaction" to get started.</p>
        </div>
      </div>
    );
  }

  const { fraud_detection, risk_assessment, investigation_status } = results;

  const getPredictionBadgeClass = (prediction) => {
    return prediction === 'Fraud' ? 'badge-fraud' : 'badge-legitimate';
  };

  const getRiskLevelBadgeClass = (riskLevel) => {
    if (!riskLevel) return '';
    const level = riskLevel.toLowerCase();
    if (level === 'high') return 'badge-high';
    if (level === 'medium') return 'badge-medium';
    return 'badge-low';
  };

  return (
    <div className="results-container">
      <div className="results-header">
        <div>
          <h2>Analysis Results</h2>
          <p className="results-subtitle">FraudShield AI Fraud Detection & Risk Assessment</p>
        </div>
        <div className="investigation-status">
          <div className="status-label">Investigation Status</div>
          <span className="status-badge">{investigation_status || 'Unknown'}</span>
        </div>
      </div>

      {fraud_detection && (
        <div className="result-section fraud-detection">
          <div className="section-header">
            <h3>Fraud Detection Analysis</h3>
            <span className="section-badge">Fraud Detection Agent</span>
          </div>
          <div className="result-grid">
            <div className="result-item">
              <span className="label">Prediction</span>
              <span className={`value badge ${getPredictionBadgeClass(fraud_detection.prediction)}`}>
                {fraud_detection.prediction || 'N/A'}
              </span>
            </div>

            <div className="result-item">
              <span className="label">Fraud Probability</span>
              <div className="probability-display">
                <div className="probability-value">
                  {formatPercentage(fraud_detection.fraud_probability, true)}
                </div>
                <div className="probability-bar">
                  <div
                    className="probability-fill"
                    style={{
                      width: `${Math.min((fraud_detection.fraud_probability || 0) * 100, 100)}%`,
                    }}
                  ></div>
                </div>
              </div>
            </div>

            <div className="result-item">
              <span className="label">Decision Threshold</span>
              <span className="value">{formatPercentage(fraud_detection.threshold, true)}</span>
            </div>

            <div className="result-item">
              <span className="label">Risk Level</span>
              <span className={`value badge ${getRiskLevelBadgeClass(fraud_detection.risk_level)}`}>
                {fraud_detection.risk_level || 'N/A'}
              </span>
            </div>

            <div className="result-item">
              <span className="label">Model Used</span>
              <span className="value model-info">{fraud_detection.model || 'N/A'}</span>
            </div>

            {fraud_detection.status && (
              <div className="result-item">
                <span className="label">Status</span>
                <span className="value status-info">{fraud_detection.status}</span>
              </div>
            )}
          </div>
        </div>
      )}

      {risk_assessment && (
        <div className="result-section risk-assessment">
          <div className="section-header">
            <h3>Risk Assessment Analysis</h3>
            <span className="section-badge">Risk Assessment Agent</span>
          </div>
          <div className="result-grid">
            <div className="result-item">
              <span className="label">Risk Score</span>
              <div className="risk-score-display">
                <div className="risk-score-value">
                  {formatDecimal(risk_assessment.risk_score, 2)}
                </div>
                <span className="score-scale">/ 100</span>
              </div>
            </div>

            <div className="result-item">
              <span className="label">Risk Level</span>
              <span className={`value badge ${getRiskLevelBadgeClass(risk_assessment.risk_level)}`}>
                {risk_assessment.risk_level || 'N/A'}
              </span>
            </div>

            <div className="result-item">
              <span className="label">Transaction Amount</span>
              <span className="value currency">{formatCurrency(risk_assessment.transaction_amount)}</span>
            </div>

            <div className="result-item">
              <span className="label">Fraud Probability (from Detection)</span>
              <span className="value">
                {formatPercentage(risk_assessment.fraud_probability, true)}
              </span>
            </div>

            {risk_assessment.status && (
              <div className="result-item">
                <span className="label">Status</span>
                <span className="value status-info">{risk_assessment.status}</span>
              </div>
            )}
          </div>
        </div>
      )}

      <div className="result-section investigation-info">
        <h3>System Information</h3>
        <div className="summary-box">
          <p>
            This transaction has been analyzed by the <strong>FraudShield AI</strong> multi-agent system. 
            The fraud detection agent analyzed the transaction features to provide a fraud probability score, 
            and the risk assessment agent evaluated the overall transaction risk based on fraud probability and transaction characteristics.
          </p>
          <div className="color-legend">
            <div className="legend-item">
              <span className="legend-color" style={{ backgroundColor: '#00b366' }}></span>
              <span>Low Risk</span>
            </div>
            <div className="legend-item">
              <span className="legend-color" style={{ backgroundColor: '#ff9900' }}></span>
              <span>Medium Risk</span>
            </div>
            <div className="legend-item">
              <span className="legend-color" style={{ backgroundColor: '#cc0000' }}></span>
              <span>High Risk / Fraud</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultsDisplay;
