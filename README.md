# FraudShield AI
### Multi-Agent Financial Fraud Detection and Investigation System

FraudShield AI is an AI-powered financial fraud detection system that combines machine learning and multi-agent orchestration to identify potentially fraudulent transactions and assess transaction risk.

The project uses XGBoost for fraud prediction and LangGraph to coordinate specialized agents. A FastAPI backend exposes the system through REST API endpoints.

## Project Objectives

- Detect potentially fraudulent financial transactions.
- Estimate fraud probability using machine learning.
- Assess transaction risk using additional business rules.
- Coordinate multiple specialized agents using LangGraph.
- Provide an API for transaction analysis.
- Build a foundation for explainable AI-based fraud investigation.

## Architecture

The current implementation contains two agents coordinated through a LangGraph workflow.

**1. Fraud Detection Agent**
- Uses a trained machine learning model.
- Currently uses XGBoost as the default model.
- Calculates fraud probability.
- Compares the probability against a decision threshold.
- Returns a fraud prediction and risk classification.

**2. Risk Assessment Agent**
- Receives the fraud detection result.
- Considers the transaction amount.
- Calculates an illustrative risk score.
- Assigns a Low, Medium, or High risk level.

**LangGraph Workflow**

Transaction Input → Fraud Detection Agent → Risk Assessment Agent → Investigation Result

## Technology Stack

| Category |
