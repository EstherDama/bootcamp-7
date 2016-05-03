from cmd import Cmd

class HelloWorld(Cmd):
    """Simple command processor example."""
    
    def do_greet(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'Stranger'
        else:
            name = args
        print "Hello, %s" % name
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()