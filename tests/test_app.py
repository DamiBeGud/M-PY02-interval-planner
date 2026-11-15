from fastapi.testclient import TestClient
from interval_planner.app import app
client=TestClient(app)
def test_overlap_and_touching():
    assert client.post('/normalize',json={'intervals':[[1,4],[3,6],[8,9]]}).json()=={'intervals':[[1,6],[8,9]],'overlap':True}
    assert client.post('/normalize',json={'intervals':[[1,2],[2,3]]}).json()=={'intervals':[[1,2],[2,3]],'overlap':False}
    assert client.post('/normalize',json={'intervals':[[1,2],[2,3]],'merge_touching':True}).json()=={'intervals':[[1,3]],'overlap':False}
def test_reversed_and_bounds():
    assert client.post('/normalize',json={'intervals':[[4,1]]}).status_code==400
    assert client.post('/normalize',json={'intervals':[[-1,2]]}).status_code==400
