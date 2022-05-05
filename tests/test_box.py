from emsg import box
from emsg.box import full_box
from emsg.box import emsg_box


def test_box():
    atom = box.Builder("test").set_user_data(bytes([0x00, 0x00, 0x00, 0x00])).build()
    assert (
        atom == b"\x00\x00\x00\x0ctest\x00\x00\x00\x00"
    ), "A box failed to be generated"


def test_full_box():
    atom = (
        full_box.Builder("test", 1)
        .set_user_data(bytes([0x00, 0x00, 0x01, 0x00]))
        .build()
    )
    assert (
        atom == b"\x00\x00\x00\x10test\x01\x00\x00\x01\x00\x00\x01\x00"
    ), "A full box failed to be generated"


def test_emsg_box():
    atom = emsg_box.Builder("value", 10, "message data", 0).set_timescale(18000).build()
    assert (
        atom
        == b"\x00\x00\x00Kemsg\x00\x00\x00\x00https://aomedia.org/emsg/ID3\x00value\x00\x00\x00FP\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\nmessage data"
    ), "A emsg box failed to be generated"
