import random

class DropTable:
    def __init__(self, rarity_odds):
        """
        rarity_odds: dict like {
            "Standard": 0.70,
            "Refined": 0.20,
            "Elite": 0.08,
            "Masterwork": 0.02,
            "Legendary": 0.005
        }
        """
        self.rarity_odds = rarity_odds

    def roll(self):
        """Return a rarity based on weighted probability."""
        r = random.random()
        cumulative = 0

        for rarity, weight in self.rarity_odds.items():
            cumulative += weight
            if r <= cumulative:
                return rarity

        # Fallback (should never happen if weights sum correctly)
        return list(self.rarity_odds.keys())[0]

