import React, { useState, useEffect } from 'react';
import { checkHealth } from '../services/api';
import '../styles/Header.css';

const Header = () => {
  const [healthStatus, setHealthStatus] = useState('checking');
  const [apiUrl, setApiUrl] = useState('');

  useEffect(() => {
    const checkBackendHealth = async () => {
      try {
        const apiUrl = import.meta.env.VITE_API_BASE_URL;
        setApiUrl(apiUrl);

        const result = await checkHealth();
        setHealthStatus(result.status === 'healthy' ? 'healthy' : 'unhealthy');
      } catch (error) {
        console.error('Health check failed:', error);
        setHealthStatus('error');
      }
    };

    checkBackendHealth();
    const interval = setInterval(checkBackendHealth, 30000);
    return () => clearInterval(interval);
  }, []);

  const getStatusClass = () => {
    switch (healthStatus) {
      case 'healthy':
        return 'status-healthy';
      case 'unhealthy':
        return 'status-unhealthy';
      case 'checking':
        return 'status-checking';
      case 'error':
        return 'status-error';
      default:
        return '';
    }
  };

  const getStatusText = () => {
    switch (healthStatus) {
      case 'healthy':
        return 'Backend Connected';
      case 'unhealthy':
        return 'Backend Unhealthy';
      case 'checking':
        return 'Checking...';
      case 'error':
        return 'Connection Error';
      default:
        return 'Unknown';
    }
  };

  return (
    <header className="app-header">
      <div className="header-container">
        <div className="header-content">
          <div className="branding">
            <h1>FraudShield AI</h1>
            <p>Financial Fraud Detection & Investigation System</p>
          </div>
          <div className={`health-status ${getStatusClass()}`}>
            <div className="status-indicator"></div>
            <span className="status-text">{getStatusText()}</span>
            {apiUrl && <span className="api-url">{apiUrl}</span>}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
