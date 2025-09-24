import os, pandas as pd
from datetime import datetime
def log_alert(message: str, severity: str, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    row = pd.DataFrame([{"timestamp":ts,"severity":severity,"message":message}])
    if os.path.exists(path): old=pd.read_csv(path); pd.concat([old,row]).to_csv(path,index=False)
    else: row.to_csv(path,index=False)
    return path
