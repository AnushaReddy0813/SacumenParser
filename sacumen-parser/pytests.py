import sacumenparser


def test_yaml():
    ts = sacumenparser.parse("example.yaml", "")
    assert ts['doe'] == 'a deer, a female deer'


def test_cfg():
    ts = sacumenparser.parse("example.cfg", "")
    assert ts['installation.library'] == '/usr/local/lib'
