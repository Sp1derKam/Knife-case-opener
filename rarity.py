class Rarity:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight      # Drop chance weight
        self.color = color        # UI color (hex or name)

    def to_dict(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "color": self.color
        }


# Five rarity tiers for the knife case opener
RARITIES = {
    "Standard": Rarity("Standard", 0.70, "#C0C0C0"),      # Silver/Grey
    "Refined": Rarity("Refined", 0.20, "#4AA3DF"),        # Blue
    "Elite": Rarity("Elite", 0.08, "#9B59B6"),            # Purple
    "Masterwork": Rarity("Masterwork", 0.02, "#E67E22"),  # Orange
    "Legendary": Rarity("Legendary", 0.005, "#FFD700")    # Gold
}


def get_rarity(name):
    return RARITIES.get(name)

