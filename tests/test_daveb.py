def test_hello(client):
    res = client.get("/dave")
    assert res.status_code == 200

def test_dave_model(client):
    res = client.get("/dave_model/submodel_1/10")
    assert res.status_code == 200
    assert res.json['score'] == 10

def test_dave_model_404(client):
    res = client.get("/dave_model/submodel_3/10")
    assert res.status_code == 404
