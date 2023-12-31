from fastapi import FastAPI
from datetime import datetime, timezone
 


app = FastAPI()






#api methods
@app.get("/api")
async def root(slack_name: str, track: str):
    utcTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    currentDateTime = datetime.now(timezone.utc)
    return {"slack_name":  slack_name,
            "current_day": currentDateTime.strftime('%A'),
            "utc_time": utcTime,
            "track": track,
            "github_file_url": "https://github.com/BasilNjoga/zuri-backend/blob/main/create-and-host-endpoint/main.py",
            "github_repo_url": "https://github.com/BasilNjoga/zuri-backend/tree/main/create-and-host-endpoint",
            "status_code": 200,}


