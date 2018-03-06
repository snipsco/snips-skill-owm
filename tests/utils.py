DUMMY_API_KEY = "dummykey"
DUMMY_LOCATION = "DUMMY LOCATION"


class MockSnips(object):
    class MockDialogue(object):
        def __init__(self):
            self._called = False
            self._speak_called = False

        def speak(self, sentence, session_id):
            self._speak_called = True

    class MockTypes(object):
        def __init__(self):
            pass

    def __init__(self):
        self._called = False
        self.dialogue = MockSnips.MockDialogue()
        self.session_id = "DummySessionId"
        self.types = MockSnips.MockTypes()
