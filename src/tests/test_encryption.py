import unittest
from encryption_decryption import encrypt, decrypt


class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        # >1000-bit keys (n, e, d)
        self.large_keys = [(7283304073906391527569238214388719467562205812483952240664102897219768164391168807562534389989482734269774647101729191884216362905323509252484506929528492404665897686966550491103087809726790776279430766858499216326657930073329251940850441783930184092603279037455955216984115249901415485904291938198800582354778228328314979768330889310123619457937356862827317939531575621692292970639076996253747266371674855141611203810468622555843305831447344593502817918290916309527053149438891229275082552738099886547565876212517786675602650010241531232012883697598489659684599977836549028130159420079156307031095112195931383026928949, 65537,
                            967882509203491774287538152778811282525384759332527595892455226171647556124384499401315327769289142063857589533709735941797936411999157315061731418526878289749858391904014981836818400397684553280004156526273468419258519271421377046032801472552816818110458335855520972481482303739931684706531494617664891150436495458451103318238566747666209530931973875326680727328150067822631093694423091060439190266405330618685332757088080777111646624786027191461584306326998788330138691053283915981303578269928804553914115238108001437465997486270322889776164802157970590052561684892921512043074140314748505626721869082747957125697457)]

        self.messages = ["987654321",
                         "This is top secret classified information."]


    def test_encryption_with_large_keys(self):
        (n, e, d) = self.large_keys[0] # add more keys for testing

        for i in range(len(self.messages)):
            message = self.messages[i]
            cipher = encrypt(n, e, message)
            self.assertNotEqual(cipher, message)
            self.assertTrue(isinstance(cipher, int))


    def test_decryption_with_large_keys(self):
        (n, e, d) = self.large_keys[0]

        for i in range(len(self.messages)):
            message = self.messages[i]
            cipher = encrypt(n, e, message)
            decrypted_message = decrypt(n, d, cipher)
            self.assertEqual(message, decrypted_message)


    def test_encryption_returns_none_if_message_too_long(self):
        # ~2048 bit key
        (n, e, d) = self.large_keys[0]

        # ~2200 bit message
        message = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Maecenas diam lorem, semper at tortor sed, tincidunt accumsan nunc.
                    Suspendisse lorem metus, suscipit ut aliquam vehicula, rhoncus rutrum odio.
                    Suspendisse tincidunt tortor eget quam eleifend, sed malesuada est posuere."""
        self.assertIsNone(encrypt(n, e, message))


    def test_encryption_returns_none_if_message_empty(self):
        (n, e, d) = self.large_keys[0]
        self.assertIsNone(encrypt(n, e, ""))


    def test_decryption_returns_none_if_cipher_empty(self):
        (n, e, d) = self.large_keys[0]
        self.assertIsNone(decrypt(n, d, ""))
