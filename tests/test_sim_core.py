from src.sim_core import private_values, revenue_uniform, revenue_discriminatory
import numpy as np

def test_private_values_shape():
    v = private_values(5, 3, seed=42)
    assert v.shape == (5, 3)

def test_revenue_uniform():
    assert revenue_uniform(10.0, 4) == 40.0

def test_revenue_discriminatory():
    bids = np.array([5.0, 4.0, 3.0])
    assert revenue_discriminatory(bids) == 12.0
