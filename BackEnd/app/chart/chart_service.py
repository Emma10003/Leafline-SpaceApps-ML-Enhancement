# app/chart/chart_service.py
from fastapi import HTTPException
from datetime import datetime
from app.chart import chart_database

# ML 예측 함수 import
from app.ml.ml_service import predict_honey

def get_current_year_bloom_data(species: str = "almond", use_ml: bool = False):
    """
    현재 연도 데이터를 가져와 프론트엔드가 예상하는
    {"bloom": {...}, "honey": [...]} 형태로 재구성하여 반환합니다.
    """
    current_year = datetime.now().year
    current_month = datetime.now().month

    if current_year not in chart_database.bloom_data:
        raise HTTPException(status_code=404, detail=f"Chart data for {current_year} not found")

    original_data = chart_database.bloom_data[current_year]

    bloom = {
        "acacia": original_data.get("acacia", []),
        "almond": original_data.get("almond", []),
    }

    honey_original = original_data.get("honey", [])
    honey_map = {}
    for it in honey_original:
        try:
            m = int(it.get("month"))
            a = float(it.get("amount"))
            honey_map[m] = a
        except Exception:
            continue

    honey = []
    for m in range(1, 13):
        if(not use_ml) or (m <= current_month and m in honey_map):
            amount = float(honey_map.get(m, 0.0))
        else:
            amount = float(predict_honey(month=m, species=species))
        
        honey.append({"month": m, "amount": amount})

    formatted_data = {"bloom": bloom, "honey": honey}

    print("✅ Formatted Data:")
    print(formatted_data)

    return formatted_data