import cantera as ct
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Tuple

HERE = Path(__file__).parent

data_file = str(HERE / "data.yaml")

T_H2 = 20.27  # K
T_O2 = 90.17  # K
p_combustor = 20.0e6  # Pa


g = ct.Solution(data_file)
g.TPX = T_H2, p_combustor, "H2(L):1"
fuel = ct.Quantity(g, mass=1.0)

g.TPX = T_O2, p_combustor, "O2(L):1"
oxidizer = ct.Quantity(g, mass=8.0)

fuel.constant = oxidizer.constant = "HP"


def equilibrate(
    of_ratio: float, fuel: ct.Quantity, oxidizer: ct.Quantity, g: ct.Solution
) -> Tuple[float, float, float, float]:
    oxidizer.mass = of_ratio
    fuel.mass = 1.0
    q3 = fuel + oxidizer

    g.TPY = q3.TPY
    g.equilibrate("HP")
    return of_ratio, g.T, g.mean_molecular_weight, g.cp_mass / g.cv_mass


of_ratio = np.linspace(3, 10, 200)
results = np.array([equilibrate(of, fuel, oxidizer, g) for of in of_ratio])
# plt.plot(results[:, 0], results[:, 1])
# plt.show()

p_e = 101325  # Pa
g_E = 9.807  # m/s**2
gamma = results[:, -1]
R_u = 8314  # J/(kmol K)
T_c = results[:, 1]
W_c = results[:, 2]
I_sp = (
    1
    / g_E
    * np.sqrt(
        2
        * gamma
        / (gamma - 1)
        * R_u
        * T_c
        / W_c
        * (1 - (p_e / p_combustor) ** ((gamma - 1) / gamma))
    )
)
print(I_sp)
# plt.plot(results[:, 0], I_sp)
# plt.show()
