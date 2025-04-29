import pytest
from dbsrv import DBService
from dbsrv import save_users


@pytest.fixture
def crdb():
    # Craete a DBService 
    dbselector = DBService()
    yield dbselector
    dbselector.dbdata.clear()

def test_add_user(crdb):
    crdb.add_user(1, "Adrey")
    assert crdb.get_user(1) == "Adrey"

def test_add_duplicate_user(crdb):
    crdb.add_user(1, "Adrey")
    with pytest.raises(ValueError, match="This user already exist in a DB"):
        crdb.add_user(1, "Vladimir")

def test_delete_user(crdb):
    crdb.add_user(2, "Vladimir")
    crdb.delete_user(2)
    assert crdb.get_user(2) is None
