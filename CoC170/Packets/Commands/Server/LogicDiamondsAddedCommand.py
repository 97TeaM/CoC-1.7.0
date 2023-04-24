from Utils.Writer import Writer


class LogicDiamondsAddedCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 7

    def encode(self):

        self.writeByte(0)  # FreeDiamonds

        self.writeInt(99)  # Amount

        self.writeString("G:0")  # TransactionId