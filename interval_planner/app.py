from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict, StrictInt

from .domain import normalize
class Intervals(BaseModel):
    intervals:list[tuple[StrictInt,StrictInt]]=Field(max_length=100)
    merge_touching:bool=False
def create_app():
    app=FastAPI(title='Interval planner')
    @app.get('/health/live')
    def live():return {'status':'ok'}
    @app.post('/normalize')
    def run(p:Intervals):
        try:return normalize(p.intervals,p.merge_touching)
        except ValueError as exc:raise HTTPException(400,str(exc)) from None
    return app
app=create_app()
