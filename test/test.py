from unittest import TestCase, main

from pymceliece import (
    mceliece348864,
    mceliece348864f,
    mceliece460896,
    mceliece460896f,
    mceliece6688128,
    mceliece6688128f,
    mceliece6960119,
    mceliece6960119f,
    mceliece8192128,
    mceliece8192128f,
)


class TestMcEliece(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_all(self) -> None:
        kems = [
            mceliece348864,
            mceliece348864f,
            mceliece460896,
            mceliece460896f,
            mceliece6688128,
            mceliece6688128f,
            mceliece6960119,
            mceliece6960119f,
            mceliece8192128,
            mceliece8192128f,
        ]

        for kem in kems:
            print(f"mceliece{kem._params}...", end="")
            pk, sk = kem.keypair()
            c, k = kem.enc(pk)
            self.assertEqual(kem.dec(c, sk), k)
            print("Good")


if __name__ == "__main__":
    main()
