import React from 'react';
import '../styles/Footer.css';

const Footer = () => {
  return (
    <footer className="app-footer">
      <div className="footer-container">
        <div className="footer-content">
          <div className="footer-section">
            <h4>About FraudShield AI</h4>
            <p>
              An AI-powered financial fraud detection system using machine learning and multi-agent orchestration.
              Combines fraud detection with risk assessment for comprehensive transaction analysis.
            </p>
          </div>
          <div className="footer-section">
            <h4>Technology</h4>
            <ul>
              <li>Backend: FastAPI, Python</li>
              <li>ML: XGBoost, Scikit-learn</li>
              <li>Agents: LangGraph, LangChain</li>
              <li>Frontend: React, Vite</li>
            </ul>
          </div>
          <div className="footer-section">
            <h4>Documentation</h4>
            <ul>
              <li><a href="https://github.com/spqdot/FraudShield-AI" target="_blank" rel="noopener noreferrer">GitHub Repository</a></li>
              <li><a href="/docs" target="_blank" rel="noopener noreferrer">API Documentation</a></li>
            </ul>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 FraudShield AI. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
