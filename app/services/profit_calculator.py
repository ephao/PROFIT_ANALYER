class ProfitCalculator:
    def __init__(self, owner_repository):
        self.owner_repository = owner_repository

    def calculate_top_n_profitable_owners(self, n):
        self.owner_repository.load_data()
        return self.owner_repository.get_top_n_profitable_owners(n)