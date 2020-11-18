import json

from filelock import FileLock
import pytest

from weixin.api.wework import Wework


# @pytest.fixture(scope="session")
# def token():
#     yield Wework().get_token()

@pytest.fixture(scope="session")
def token(tmp_path_factory, worker_id):
    if worker_id == "master":
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return Wework().get_token()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent
    # C:\Users\Ling\AppData\Local\Temp\pytest - of - Ling\pytest - current
    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = Wework().get_token()
            fn.write_text(json.dumps(data))
    return data