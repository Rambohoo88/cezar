import cezar


class TestCezar:
    def testEncryptLetters(self):
        c = cezar.Cezar()
        name = 'Bartek'
        encrypted_text = c.encrypt(name, 3)
        print(f'Encrypted text: {encrypted_text}')
        assert len(encrypted_text) == len(name)
        assert 'Edutwhn'

    def testDecryptLetters(self):
        c = cezar.Cezar()
        assert 'Bartek' == c.decrypt('Eduwhn', 3)