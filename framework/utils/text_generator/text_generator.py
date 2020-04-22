import random
import string


class TextGenerator:

    @staticmethod
    def generate(size=random.randrange(0, 20),
                 chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
