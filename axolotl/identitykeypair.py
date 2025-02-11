# -*- coding: utf-8 -*-
from .ecc.djbec import DjbECPrivateKey, DjbECPublicKey
from .identitykey import IdentityKey


class IdentityKeyPair:
    def __init__(self, identityKeyPublicKey=None, ecPrivateKey=None):
        self.publicKey = identityKeyPublicKey
        self.privateKey = ecPrivateKey

    def getPublicKey(self):
        return self.publicKey

    def getPrivateKey(self):
        return self.privateKey

    @staticmethod
    def of(publicKey: bytes, privateKey: bytes):
        return IdentityKeyPair(IdentityKey(DjbECPublicKey(publicKey[1:])), DjbECPrivateKey(privateKey))
