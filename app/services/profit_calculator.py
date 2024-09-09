from app.repositories.owner_repository import OwnerRepository

class ProfitCalculator:
    """
    Service for calculating profits and retrieving top profitable owners.
    """

    def __init__(self, owner_repository: OwnerRepository):
        """
        Initializes the ProfitCalculator with an OwnerRepository.
        Args:
            owner_repository (OwnerRepository): Repository for owner data.
        """
        self.owner_repository = owner_repository

    def calculate_top_n_profitable_owners(self, n: int):
        """
        Calculates and retrieves the top N profitable owners.
        Args:
            n (int): Number of top owners to retrieve.
        Returns:
            list[Owner]: List of top N profitable Owner objects.
        """
        return self.owner_repository.get_top_n_profitable_owners(n)

    def calculate_total_profit(self):
        """
        Calculates the total profit across all owners.
        Returns:
            float: Total profit sum.
        """
        owners = self.owner_repository.get_all_owners()
        return sum(owner.total_profit for owner in owners)

    def calculate_average_profit(self):
        """
        Calculates the average profit across all owners.
        Returns:
            float: Average profit.
        """
        owners = self.owner_repository.get_all_owners()
        if not owners:
            return 0
        total_profit = sum(owner.total_profit for owner in owners)
        return total_profit / len(owners)