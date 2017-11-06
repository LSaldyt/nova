
class Switchboard:
    def __init__(self, functionDictionary):
        self.functions = functionDictionary

    def run(self, subcommand, *args):
        self.functions[subcommand](*args)
