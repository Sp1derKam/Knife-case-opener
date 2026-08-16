from knife import Knife

class Case:
    def __init__(self, name, drop_table, knife_pool):
        self.name = name
        self.drop_table = drop_table      # DropTable object
        self.knife_pool = knife_pool      # List of knife dicts from JSON

    def roll_rarity(self):
        """Use the drop table to roll a rarity tier."""
        return self.drop_table.roll()

    def get_knives_by_rarity(self, rarity):
        """Return all knives in this case matching the rolled rarity."""
        return [k for k in self.knife_pool if k["rarity"] == rarity]

    def pull_knife(self, rarity):
        """Pick a random knife from the correct rarity pool."""
        pool = self.get_knives_by_rarity(rarity)
        if not pool:
            return None
        import random
        return random.choice(pool)

    def __repr__(self):
        return f"<Case {self.name}>"

