---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell}
:tags: [remove-cell]
from myst_nb import glue
```

# Example: JP4/RFNA Rocket Motor

<!-- This is based on Problem E11.3 from Sforza, Theory of Aerospace Propulsion -->

A liquid propellant rocket motor using [JP-4](https://en.wikipedia.org/wiki/JP-4)/[Red Fuming Nitric Acid (RFNA)](https://en.wikipedia.org/wiki/Red_fuming_nitric_acid) propellant combination must produce 19.6 kN of thrust at sea level. The characteristics of the combustion products are $T_c$ = 3000 K, $\gamma$ = 1.2 (constant), $W$ = 27 kg/kmol (constant), and $p_c$ = 19.34 atm. Determine:

1. the throat and exit diameters, in cm, for matched nozzle exit flow at sea level assuming a nozzle efficiency of $\eta_n$ = 95%
2. the characteristic velocity, $c^*$, in m/s
3. the propellant mass flow rate, in kg/s
4. the specific impulse of the engine, in s
5. the thrust, in kN, at an altitude of 11.5 km where the pressure is $p_0$ = 0.2 atm
6. the thrust, in kN, and exit diameter, in cm, assuming matched operation at this altitude and the same throat diameter

## Solution

```{code-cell}
from pint import UnitRegistry
import numpy as np

units = UnitRegistry()

F_sl = 19.6 * units.kN
T_c = 3000 * units.K
gamma = 1.2 * units.dimensionless
W = 27 * units.kg / units.kmol
R = units.molar_gas_constant / W
c_p = gamma * R / (gamma - 1)
p_c = 19.34 * units.atmosphere
eta_n = 0.95 * units.dimensionless
p_sl = 1 * units.atmosphere
p_0 = 0.2 * units.atmosphere
```

### Engineering Model

1. The nozzle is not isentropic, but is characterized by the nozzle efficiency
2. The specific heat ratio and molecular weight are constant
3. The discharge coefficient and $\lambda$ are equal to one
4. The flow is adiabatic through the nozzle, even though it is not isentropic

### Procedure

In this problem, we are initially given $p_0$ and told the operation of the nozzle is matched. We are also given $p_c$, so we can use the stagnation-to-static pressure ratio for isentropic flow to determine the ideal exit velocity from Eq. {eq}`ideal-exit-velocity`. Using the nozzle efficiency from Eq. {eq}`nozzle-isentropic-efficiency`, we can correct $V_{e,i}$ to find the actual nozzle exit velocity.

Since we are given the thrust and initially the pressure is matched, we can use the actual nozzle exit velocity to calculate the mass flow rate from Eq. {eq}`rocket-thrust`. We can also use the actual nozzle exit velocity to find the actual exit temperature from the energy equation. This determines the actual exit density via the ideal gas law. We can then find the exit area from the definition of the mass flow rate.

Then, assuming the discharge coefficient is unity, the mass flow rate coefficient, $c_m$, is equal to the inverse of the characteristic velocity $c^*$. The characteristic velocity is given in terms of the combustion chamber speed of sound at the specific heat ratio by Eq. {eq}`nozzle-characteristic-velocity`. The mass flow rate coefficient can be used to find the throat area.

Next, the specific impulse can be determined by dividing the actual exit velocity by the gravitational constant.

At the altitude of 11.5 km, we need to correct the thrust by including the pressure thrust in Eq. {eq}`rocket-thrust`.

Finally, we need to calculate the thrust and exit diameter at the altitude of 11.5 km assuming matched operation. This can be done by the thrust coefficient, $c_F$, assuming that $\lambda = c_d = 1$. Since the throat area and chamber conditions are the same, the mass flow rate is the same. This can be used to find the actual exit velocity. From there, the same process as before is used to find the exit diameter.

### Work

```{code-cell}
pe_pc = (p_sl / p_c).to("dimensionless")
V_ei = np.sqrt(2 * gamma / (gamma - 1) * R * T_c * (1 - pe_pc**((gamma - 1) / gamma))).to("m/s")

Ve_sl = V_ei * np.sqrt(eta_n)
mdot = (F_sl / Ve_sl).to("kg/s")

Te_sl = T_c - Ve_sl**2 / (2 * c_p)
rhoe_sl = (p_sl / (R * Te_sl)).to("kg/m**3")
Ae_sl = (mdot / (rhoe_sl * Ve_sl)).to("cm**2")
de_sl = np.sqrt(4 * Ae_sl / units.pi).to("cm")

Gamma = np.sqrt(gamma) * (2 / (gamma + 1))**((gamma + 1) / (2*(gamma - 1)))
a_c = np.sqrt(gamma * R * T_c)
c_star = (a_c / (Gamma * np.sqrt(gamma))).to("m/s")
c_m = 1 / c_star
A_th = (mdot / (p_c * c_m)).to("cm**2")
d_th = np.sqrt(4 * A_th / units.pi).to("cm")

I_sp = (Ve_sl / units.gravity).to("s")

F = (mdot * Ve_sl + Ae_sl * (p_sl - p_0)).to("kN")

c_V = np.sqrt(eta_n)
c_F = c_V * Gamma * np.sqrt(2 * gamma / (gamma - 1) * (1 - (p_0/p_c)**((gamma - 1) / gamma)))
F_alt = (c_F * ((19.34 * 101325) * units.Pa) * A_th).to("kN")
Ve_alt = (F_alt / mdot).to("m/s")
Te_alt = T_c - Ve_alt**2 / (2 * c_p)
rhoe_alt = (p_0 / (R * Te_alt)).to("kg/m**3")
Ae_alt = (mdot / (rhoe_alt * Ve_alt)).to("cm**2")
de_alt = np.sqrt(4 * Ae_alt / units.pi).to("cm")
```

```{code-cell}
:tags: [remove-cell]
for name in [
    "V_ei", "Ve_sl", "mdot", "Te_sl", "rhoe_sl", "Ae_sl", "de_sl",
    "c_star", "A_th", "d_th", "I_sp", "F", "F_alt",
    "Ve_alt", "Te_alt", "rhoe_alt", "Ae_alt", "de_alt"
    ]:
        glue(name, f"{locals()[name]:.2F~P}", display=False)
```

### Results

| Property  | Value | Property | Value | Property | Value |
|-----------|-------|----------|-------|----------|-------|
| $V_{e,i}$ | {glue:text}`V_ei`   | $d_e$     | {glue:text}`de_sl`    | $F$ at 11.5 km, matched | {glue:text}`F_alt` |
| $V_e$     | {glue:text}`Ve_sl`    | $c^*$     | {glue:text}`c_star` | $V_e$ at 11.5 km, matched | {glue:text}`Ve_alt` |
| $\dot{m}$ | {glue:text}`mdot`   | $A_{\text{th}}$ | {glue:text}`A_th` | $T_e$ at 11.5 km, matched | {glue:text}`Te_alt` |
| $T_e$     | {glue:text}`Te_sl`    | $d_{\text{th}}$ | {glue:text}`d_th` | $\rho_e$ at 11.5 km, matched | {glue:text}`rhoe_alt` |
| $\rho_e$  | {glue:text}`rhoe_sl`  | $I_{\text{sp}}$ | {glue:text}`I_sp` | $A_e$ at 11.5 km, matched | {glue:text}`Ae_alt` |
| $A_e$     | {glue:text}`Ae_sl`    | $F$ at 11.5 km  | {glue:text}`F`    | $d_e$ at 11.5 km, matched | {glue:text}`de_alt` |
