from fastapi import APIRouter
import json

router = APIRouter(prefix="/api")

with open(
    "app/mock_data/board_data.json",
    "r"
) as f:
    data = json.load(f)

@router.get("/companies")
def get_companies():
    return data

@router.get("/metrics")
def get_metrics():
    return {
        "companies": len(data),
        "founder_controlled": 1,
        "investor_controlled": 1
    }

@router.get("/rights")
def get_rights():
    return [
        "budget_approval",
        "new_financing",
        "board_approval",
        "acquisition_approval"
    ]