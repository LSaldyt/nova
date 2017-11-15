from .recognize import recognize

class Switchboard:
    def __init__(self, functionDictionary):
        self.functions = functionDictionary

    def run(self, subcommand, *args):
        print(subcommand, args)
        self.functions[subcommand](*args)

    def loop(self):
        while True:
            # Idealized usage, probably won't work :)
            speech = recognize()
            if speech != '':
                subcommand, *args = speech.split(' ')
                self.run(subcommand, *args)
