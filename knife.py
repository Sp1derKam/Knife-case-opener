class Knife:
    def __init__(self, name, category, rarity, image_path=None):
        self.name = name
        self.category = category
        self.rarity = rarity
        self.image_path = image_path

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "rarity": self.rarity,
            "image_path": self.image_path
        }

    def __repr__(self):
        return f"<Knife {self.name} ({self.rarity})>"

