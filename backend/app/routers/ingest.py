from fastapi import APIRouter, UploadFile
import pandas as pd
from ..services.schema_matcher import infer_columns, best_map_to_canonical
from ..services.normalizer import normalize

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/")
async def ingest_file(file: UploadFile):
    # Read uploaded file
    df = pd.read_csv(file.file) if file.filename.endswith(".csv") else pd.read_json(file.file)

    # Infer schema and normalize
    cols = infer_columns(df)
    cmap = best_map_to_canonical(cols)
    normalized = normalize(df.rename(columns=dict(zip(df.columns, cols))), cmap)

    return {
        "rows": len(df),
        "normalized_cols": list(normalized.columns),
        "preview": normalized.head(5).to_dict(orient="records")
    }
