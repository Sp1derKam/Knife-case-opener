class CaseOpener:
    def __init__(self):
        pass

    def open_case(self, case):
        """
        Perform a full case opening:
        1. Roll rarity
        2. Select a knife from that rarity pool
        3. Return the knife dict
        """
        rarity = case.roll_rarity()
        knife = case.pull_knife(rarity)

        if knife is None:
            return {
                "name": "ERROR: No knife found for rarity",
                "category": "N/A",
                "rarity": rarity
            }

        return knife

