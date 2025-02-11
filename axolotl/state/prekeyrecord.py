
from ..ecc.curve import Curve
from ..ecc.eckeypair import ECKeyPair


class PreKeyRecord:
    def __init__(self, _id=None, ecKeyPair=None):
        self.id = _id
        self.publicKey = ecKeyPair.getPublicKey().serialize()
        self.privateKey = ecKeyPair.getPrivateKey().serialize()

    def getId(self):
        return self.id

    def getKeyPair(self):
        publicKey = Curve.decodePoint(bytearray(self.publicKey), 0)
        privateKey = Curve.decodePrivatePoint(bytearray(self.privateKey))
        return ECKeyPair(publicKey, privateKey)

