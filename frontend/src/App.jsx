import React, { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import TransactionForm from './components/TransactionForm';
import ResultsDisplay from './components/ResultsDisplay';
import { analyzeTransaction } from './services/api';
import './App.css';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyzeTransaction = async (formData) => {
    setLoading(true);
    setError(null);
    setResults(null);

    try {
      const response = await analyzeTransaction(formData);
      setResults(response);
    } catch (err) {
      setError(err.message || 'An error occurred while analyzing the transaction');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div id="app">
      <Header />
      <main className="app-main">
        <div className="container">
          <div className="app-layout">
            <section className="form-section">
              <TransactionForm onSubmit={handleAnalyzeTransaction} isLoading={loading} />
            </section>
            <section className="results-section">
              <ResultsDisplay results={results} loading={loading} error={error} />
            </section>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default App;
