from Utils.Writer import Writer


class LogicAllianceUnitReceivedCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 5

    def encode(self):

        self.writeString("Solar")  # Name

        self.writeInt()  # UnitType