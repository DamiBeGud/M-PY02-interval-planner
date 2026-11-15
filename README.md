# interval-planner

Native Python3.11–3.13 application; intended acceptance runtime3.12.
Install `python -m pip install -r requirements.txt` in an isolated environment.
Run `python -m pytest`. Start `uvicorn interval_planner.app:app --host 0.0.0.0 --port 8202`.



POST /normalize {intervals:[[start,end]],merge_touching:false}; half-open intervals, touching stays separate by default.
Tests are source-native development checks. Tests exercise actual in-process FastAPI routing and domain rules.
AI-assisted researcher-created source; no deployment files or runtime credentials.
