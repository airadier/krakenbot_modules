class Greeter:
    def __init__(self, module_info, client, respond, command):
        self.module_info = module_info
        self.client = client
        self.respond = respond
        self.command = command

    def execute(self):
        self.respond("HI @{}!".format(self.command['user_id']))
