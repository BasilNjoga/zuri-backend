from fastapi import FastAPI


app = FastAPI()

# app.middleware('HTTPs')

@app.get("/")
async def root():
    return {"slack_name":  "Basil Njoga",
            "current_day": "day",
            "utc_time": "time",
            "track": "backend",
            "github_file_url": "lkd;fja",
            "github_repo_url": 200}

@app.get("/tracks")
async def root():
    return {"slack_name":  "Basil Njoga",
            "current_day": "day",
            "utc_time": "time",
            "track": "backend",
            "github_file_url": "lkd;fja",
            "github_repo_url": 200}


