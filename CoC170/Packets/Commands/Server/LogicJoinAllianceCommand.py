import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class LogicJoinAllanceCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 1

    def encode(self):

        self.writeInt(config['AllianceHighID'])
        self.writeInt(config['AllianceLowID'])

        self.writeString(config['AllianceName'])

        self.writeInt(config['AllianceBadge'])

        self.writeByte(config['AllianceRole'])