from Utils.Writer import Writer


class LogicDonateAllianceUnitCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 4

    def encode(self):

        self.writeInt(0)

        self.writeInt()  # UnitType