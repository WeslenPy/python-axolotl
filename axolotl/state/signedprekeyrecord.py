# -*- coding; utf-8 -*-
from ..ecc.curve import Curve
from ..ecc.eckeypair import ECKeyPair

class SignedPreKeyRecord:
    def __init__(self, _id=None, timestamp=None, ecKeyPair=None, signature=None):
        self.id = _id
        self.publicKey = ecKeyPair.getPublicKey().serialize()
        self.privateKey = ecKeyPair.getPrivateKey().serialize()
        self.signature = signature
        self.timestamp = timestamp

    def getId(self):
        return self.id

    def getTimestamp(self):
        return self.timestamp

    def getKeyPair(self):
        publicKey = Curve.decodePoint(bytearray(self.publicKey), 0)
        privateKey = Curve.decodePrivatePoint(bytearray(self.privateKey))

        return ECKeyPair(publicKey, privateKey)

    def getSignature(self):
        return self.signature
