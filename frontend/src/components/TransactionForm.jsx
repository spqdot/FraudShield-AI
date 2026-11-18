
import React, { useState } from 'react';
import '../styles/TransactionForm.css';

const defaultData = {
  Time: 0,
  V1: 0, V2: 0, V3: 0, V4: 0, V5: 0, V6: 0, V7: 0, V8: 0, V9: 0,
  V10: 0, V11: 0, V12: 0, V13: 0, V14: 0, V15: 0, V16: 0, V17: 0, V18: 0, V19: 0,
  V20: 0, V21: 0, V22: 0, V23: 0, V24: 0, V25: 0, V26: 0, V27: 0, V28: 0,
  Amount: 0,
};

// Real examples from data/processed/test.csv
const normalSample = {
  Time: 160760,
  V1: -0.6744660646, V2: 1.4081050197, V3: -1.1106220536, V4: -1.3283657784,
  V5: 1.3889960325, V6: -1.3084390671, V7: 1.8858789027, V8: -0.6142329663,
  V9: 0.3116522125, V10: 0.6507570036, V11: -0.8577846615, V12: -0.2299614458,
  V13: -0.1998170048, V14: 0.2663713263, V15: -0.0465441685, V16: -0.7413980897,
  V17: -0.6056166441, V18: -0.3925681879, V19: -0.162648311, V20: 0.3943218208,
  V21: 0.0800842396, V22: 0.8100335956, V23: -0.2243272304, V24: 0.7078992374,
  V25: -0.1358370227, V26: 0.0451021965, V27: 0.5338372191, V28: 0.2913192526,
  Amount: 23.0,
};

const fraudSample = {
  Time: 57007,
  V1: -1.2712441917, V2: 2.4626752685, V3: -2.8513950033, V4: 2.3244800653,
  V5: -1.3722448898, V6: -0.9481956865, V7: -3.0652343617, V8: 1.1669269479,
  V9: -2.2687705884, V10: -4.8811429269, V11: 2.2551474887, V12: -4.6863868976,
  V13: 0.6523746685, V14: -6.174288348, V15: 0.594379608, V16: -4.8496923871,
  V17: -6.5365207353, V18: -3.1190938816, V19: 1.7154944198, V20: 0.5604780757,
  V21: 0.6529410513, V22: 0.0819309764, V23: -0.2213478312, V24: -0.5235821592,
  V25: 0.2242281619, V26: 0.7563345227, V27: 0.6328004773, V28: 0.2501870928,
  Amount: 0.01,
};

const TransactionForm = ({ onSubmit, isLoading }) => {
  const [formData, setFormData] = useState(defaultData);
  const [errors, setErrors] = useState({});
  const [sampleChoice, setSampleChoice] = useState('');

  const getFieldLabel = (fieldName) => {
    if (fieldName === 'Time') return 'Transaction Time (seconds)';
    if (fieldName === 'Amount') return 'Transaction Amount';
    const num = fieldName.replace('V', '');
    return `PCA Component ${num} (${fieldName})`;
  };

  const featureGroups = [
    { label: 'PCA Features (Components 1-9)', fields: ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9'] },
    { label: 'PCA Features (Components 10-19)', fields: ['V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19'] },
    { label: 'PCA Features (Components 20-28)', fields: ['V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28'] },
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: parseFloat(value) || 0 }));

    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  const validateForm = () => {
    const newErrors = {};

    for (const [key, value] of Object.entries(formData)) {
      if (typeof value !== 'number' || isNaN(value)) {
        newErrors[key] = 'Must be a valid number';
      }
      if (key === 'Amount' && value < 0) {
        newErrors[key] = 'Transaction amount must be non-negative';
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) onSubmit(formData);
  };

  const handleLoadSample = (choice) => {
    if (choice === 'normal') {
      setFormData({ ...normalSample });
    } else if (choice === 'fraud') {
      setFormData({ ...fraudSample });
    } else {
      setFormData({ ...defaultData });
    }

    setSampleChoice(choice);
    setErrors({});
  };

  const handleClear = () => {
    setFormData({ ...defaultData });
    setSampleChoice('');
    setErrors({});
  };

  return (
    <form className="transaction-form" onSubmit={handleSubmit}>
      <h2>Transaction Analysis Form</h2>

      <p className="form-description">
        Choose a sample transaction or enter the transaction details manually.
      </p>

      <div className="feature-group">
        <h3>Quick Demo</h3>

        <div className="field-wrapper">
          <label htmlFor="sampleChoice">Load a Sample Transaction</label>
          <select
            id="sampleChoice"
            value={sampleChoice}
            onChange={(e) => handleLoadSample(e.target.value)}
            disabled={isLoading}
          >
            <option value="">Choose a sample...</option>
            <option value="normal">Normal Transaction (Sample)</option>
            <option value="fraud">Fraudulent Transaction (Sample)</option>
          </select>
        </div>

        <p className="pca-explanation">
          Samples are real transactions from the test dataset. PCA features are
          anonymized mathematical components and cannot be interpreted as ordinary
          transaction details.
        </p>
      </div>

      <div className="feature-group">
        <h3>Transaction Details</h3>

        {['Time', 'Amount'].map(field => (
          <div key={field} className="field-wrapper">
            <label htmlFor={field}>{getFieldLabel(field)}</label>
            <input
              type="number"
              id={field}
              name={field}
              value={formData[field]}
              onChange={handleInputChange}
              disabled={isLoading}
              step="any"
              className={errors[field] ? 'input-error' : ''}
            />
            {errors[field] && <span className="error-text">{errors[field]}</span>}
          </div>
        ))}
      </div>

      <details className="advanced-options">
        <summary>Advanced Options – PCA Components (V1–V28)</summary>

        {featureGroups.map((group, groupIndex) => (
          <div key={groupIndex} className="feature-group">
            <h3>{group.label}</h3>

            <div className="fields-grid">
              {group.fields.map(field => (
                <div key={field} className="field-wrapper">
                  <label htmlFor={field}>{getFieldLabel(field)}</label>
                  <input
                    type="number"
                    id={field}
                    name={field}
                    value={formData[field]}
                    onChange={handleInputChange}
                    disabled={isLoading}
                    step="any"
                    className={errors[field] ? 'input-error' : ''}
                  />
                  {errors[field] && (
                    <span className="error-text">{errors[field]}</span>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </details>

      <div className="form-actions">
        <button
          type="submit"
          className="btn btn-primary"
          disabled={isLoading}
        >
          {isLoading ? 'Analyzing...' : 'Analyze Transaction'}
        </button>

        <button
          type="button"
          className="btn btn-secondary"
          onClick={() => handleLoadSample('normal')}
          disabled={isLoading}
        >
          Load Normal Sample
        </button>

        <button
          type="button"
          className="btn btn-secondary"
          onClick={() => handleLoadSample('fraud')}
          disabled={isLoading}
        >
          Load Fraud Sample
        </button>

        <button
          type="button"
          className="btn btn-tertiary"
          onClick={handleClear}
          disabled={isLoading}
        >
          Clear
        </button>
      </div>
    </form>
  );
};

export default TransactionForm;
