from fastapi import APIRouter, HTTPException
from app.ml.ml_schema import HoneyPredictRequest, HoneyPredictResponse
from app.ml.ml_service import predict_honey

router = APIRouter(prefix="/ml", tags=["ML"])

@router.post("/predict-honey", response_model=HoneyPredictResponse)
def predict_honey_api(req: HoneyPredictRequest):
    try:
        pred = predict_honey(req.month, req.species)
        return HoneyPredictResponse(
            species=req.species,
            month=req.month,
            predicted_honey_amount=pred,
        )
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Model artifact not found. Run training first.")