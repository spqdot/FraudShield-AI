
from fraudshield.agents.risk_assessment_agent import assess_transaction_risk
from typing import TypedDict, Any
from langgraph.graph import StateGraph, START, END


class FraudState(TypedDict):
    """
    Shared state for the FraudShield investigation workflow.
    """

    transaction: Any
    actual_label: int | None
    fraud_result: dict | None
    risk_result: dict | None
    investigation_status: str
    error: str | None


from fraudshield.agents.fraud_detection_agent import run_fraud_detection


def fraud_detection_node(state: FraudState) -> dict:
    """
    LangGraph node that executes the Fraud Detection Agent.
    """

    try:
        result = run_fraud_detection(
            transaction=state["transaction"],
            model_name="xgboost"
        )

        return {
            "fraud_result": result,
            "investigation_status": "fraud_detection_completed",
            "error": None
        }

    except Exception as e:
        return {
            "fraud_result": None,
            "investigation_status": "failed",
            "error": str(e),
            "risk_result": None
        }


def build_fraud_workflow():
    """
    Build and compile the FraudShield LangGraph workflow.
    """

    workflow = StateGraph(FraudState)

    workflow.add_node("fraud_detection", fraud_detection_node)
    workflow.add_node("risk_assessment", risk_assessment_node)

    workflow.add_edge(START, "fraud_detection")
    workflow.add_edge("fraud_detection", "risk_assessment")
    workflow.add_edge("risk_assessment", END)

    return workflow.compile()






def risk_assessment_node(state: FraudState) -> dict:
    """
    LangGraph node that executes the Risk Assessment Agent.
    """

    try:
        result = assess_transaction_risk(
            transaction=state["transaction"],
            fraud_result=state["fraud_result"]
        )

        return {
            "risk_result": result,
            "investigation_status": "risk_assessment_completed",
            "error": None
        }

    except Exception as e:
        return {
            "investigation_status": "failed",
            "error": str(e)
        }