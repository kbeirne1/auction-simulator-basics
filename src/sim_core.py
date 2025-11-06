import numpy as np

def private_values(n_bidders, n_units, dist="uniform", seed=0):
    """
    Create a matrix of private values for each bidder and unit.
    Highest value first (sorted descending per bidder).
    """
    rng = np.random.default_rng(seed)
    if dist == "uniform":
        vals = rng.uniform(0, 1, size=(n_bidders, n_units))
    else:
        raise ValueError("Only 'uniform' supported in this simple demo.")
    return np.sort(vals, axis=1)[:, ::-1]

def revenue_uniform(clearing_price, quantity):
    """
    Uniform-price auction revenue = clearing price * total units sold.
    """
    return float(clearing_price) * int(quantity)

def revenue_discriminatory(winning_bids):
    """
    Discriminatory auction revenue = sum of winning bids (list/array).
    """
    return float(np.sum(winning_bids))
