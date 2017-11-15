from .recognize import recognize
from .speak     import speak

class Switchboard:
    def __init__(self, functionDictionary):
        self.functions = functionDictionary

    def run(self, subcommand, *args):
        print(subcommand, args)
        try:
            self.functions[subcommand](*args)
        except KeyError:
            print('The subcommand {} does not exist'.format(subcommand))

    def loop(self):
        while True:
            # Idealized usage, probably won't work :)
            speech = recognize()
            if speech != '':
                subcommand, *args = speech.lower().split(' ')
                self.run(subcommand, *args)
