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

# Example: LR91 Rocket Motor

<!-- This is based on Example 2.1 from Ward, Aerospace Propulsion Systems -->

The [LR91 rocket motor](https://en.wikipedia.org/wiki/LR91) uses the liquid bipropellants [nitrogen tetroxide (N2O4)](https://en.wikipedia.org/wiki/Dinitrogen_tetroxide#Use_as_a_rocket_propellant) and [Aerozine 50](https://en.wikipedia.org/wiki/Aerozine_50) (a 50/50 mixture by weight of [hydrazine](https://en.wikipedia.org/wiki/Hydrazine) and [unsymmetrical dimethyl hydrazine](https://en.wikipedia.org/wiki/Unsymmetrical_dimethylhydrazine)). Assume that the LR91 is an ideal rocket motor with nozzle expansion ratio of $\varepsilon$ = 49.2, chamber pressure of $p_c$ = 5.6 MPa, chamber temperature of $T_c$ = 3,400 K. The exhaust gas products of combustion have a ratio of specific heats $\gamma$ = 1.3 and a gas constant of $R$ = 390.4 J/(kg K). The nozzle exit diameter is $d_e$ = 1.6 m. Determine:

a. the altitude at which the nozzle is designed for optimal expansion ($p_e = p_0$), in km and ft
b. the nozzle throat diameter ($d_{\text{th}}$), in cm and in.
c. the mass flow rate ($\dot{m}$), in kg/s and lb/s
d. the ideal thrust at the optimal altitude, in kN and lbf

## Solution

```{code-cell}
from pint import UnitRegistry
import numpy as np
from scipy import optimize
from ambiance import Atmosphere

units = UnitRegistry()

T_c = 3400 * units.K
p_c = 5.6 * units.MPa
d_e = 1.6 * units.m
epsilon = 49.2 * units.dimensionless
gamma = 1.3 * units.dimensionless
W = 21.30 * units.kg / units.kmol
R = units.molar_gas_constant / W
```

### Engineering Model

1. Ideal rocket motor, all processes are isentropic
2. Expansion in the nozzle is optimized, so $p_e = p_0$
3. The specific heat ratio and molecular weight are constant

### Procedure

To determine the altitude, we need to determine the ambient pressure around the rocket motor. With the ambient pressure, we can look up or find the altitude in standard atmospheric tables.

Since we are looking for the optimal expansion, we can find the ambient pressure by finding the exit pressure of the nozzle, since they are equal. The exit pressure of the nozzle is going to be found from the isentropic equations for compressible flow, since we are assuming this is an ideal nozzle.

The isentropic equations for compressible flow require the exit Mach number, which we will find from the expansion ratio. Likewise, the nozzle throat diameter is determined by the expansion ratio and the exit diameter.

Finally, the mass flow rate can be found from the maximum flow rate equations, the exit velocity from the exit Mach number, and the ideal thrust by multiplying these two quantities.

### Work

We have two ways of solving for the exit Mach number from the expansion ratio. One is to use the area-Mach-number relation, Eq. {eq}`area-mach-relation`, which we have seen before. The other is to introduce a quantity called the **_X_-function**, defined as:

```{math}
:label: X-function
X = M \sqrt{\gamma} \left[1 + \frac{\gamma - 1}{2} M^2\right]^{\frac{-\left(\gamma + 1\right)}{2\left(\gamma - 1\right)}}
```

Notice that the $X$-function is equivalent to the $\Gamma$ (Gamma) function we defined in Eq. {eq}`Gamma-function` when $M = 1$. Whether you use the area-Mach-number relation, or the $X$-function, you'll get the same answer for $M$ at the end.

In terms of the $X$-function, the ideal maximum mass flow rate can be written as:

```{math}
\dot{m} = \frac{p_t A X}{\sqrt{R T_t}}
```

Since the mass flow rate in the nozzle must be constant, we can plug in the throat quantities and the exit quantities and equate them. The total pressure and temperature are constant, since the nozzle process is isentropic. In addition, at the throat, the Mach number is one, so $X_{\text{th}} = \Gamma$.

```{math}
\frac{p_{t} A_{\text{th}} \Gamma}{\sqrt{R T_t}} = \frac{p_t A_e X_e}{\sqrt{R T_t}}
```

From this equation, the gas constant, total pressure, and total temperature will cancel, leaving:

```{math}
X_e = \frac{1}{\varepsilon}\Gamma = \frac{1}{\varepsilon}\left[\sqrt{\gamma}\left(\frac{2}{\gamma + 1}\right)^{\frac{\gamma + 1}{2\left(\gamma - 1\right)}}\right]
```

```{code-cell}
X_e = 1 / epsilon * (np.sqrt(gamma) * (2 / (gamma + 1))**((gamma + 1)/(2*(gamma - 1))))
```

```{code-cell}
:tags: [remove-cell]
glue("X_e", f"{X_e:.4F~P}", display=False)
```

This gives $X_e$ = {glue:text}`X_e`. Then, the exit Mach number is found from Eq. {eq}`X-function`. This function is transcendental in $M_e$, so we use the `scipy.optimize.brentq()` root finding method.

```{code-cell}
def X_function(M, X, gamma):
    power = -(gamma + 1) / (2 * (gamma - 1))
    return M * np.sqrt(gamma) * (1 + (gamma - 1) / 2 * M**2)**(power) - X
M_e = optimize.brentq(
    X_function, 
    1.1,
    10.0,
    args=(X_e.magnitude, gamma.magnitude)
) * units.dimensionless
```

```{code-cell}
:tags: [remove-cell]
glue("M_e", f"{M_e:.2F~P}", display=False)
```

This gives an exit Mach number of $M_e$ = {glue:text}`M_e`. Next, we can determine the ratio of the stagnation to the static pressure at the exit from Eq. {eq}`isentropic-pressure-mach`:

```{math}
\frac{p_t}{p_e} = \frac{p_c}{p_0} = \left(1 + \frac{\gamma - 1}{2} M_e^2\right)^{\frac{\gamma}{\gamma - 1}}
```

```{code-cell}
pc_p0 = (1 + (gamma - 1) / 2 * M_e**2)**(gamma / (gamma - 1))
p_0 = (p_c / pc_p0).to("Pa")
```

```{code-cell}
:tags: [remove-cell]
glue("pc_p0", f"{pc_p0:.4F~P}", display=False)
glue("p_0", f"{p_0:.2F~P}", display=False)
```

This gives a pressure ratio of {glue:text}`pc_p0` and an ambient pressure of {glue:text}`p_0`. Then, we can use `ambiance` to determine the altitude:

```{code-cell}
atmos = Atmosphere.from_pressure(p_0.magnitude)
h = atmos.h[0] * units.m
```

```{code-cell}
:tags: [remove-cell]
glue("h_meters", f"{h.to('km'):.2F~P}", display=False)
glue("h_feet", f"{h.to('ft'):.0F~P}", display=False)
```

Finally, the altitude is $h$ = {glue:text}`h_meters` = {glue:text}`h_feet`.

The throat diameter is found from the expansion ratio and the known exit diameter:

```{math}
\frac{A_e}{A_{\text{th}}} = \frac{d_e^2}{d_{\text{th}}^2} \Rightarrow d_{\text{th}} = d_e\sqrt{\frac{1}{\varepsilon}}
```

```{code-cell}
d_th = d_e * np.sqrt(1 / epsilon)
```

```{code-cell}
:tags: [remove-cell]
glue("d_th_cm", f"{d_th.to('cm'):.1F~P}", display=False)
glue("d_th_in", f"{d_th.to('in'):.1F~P}", display=False)
```

The diameter is $d_{\text{th}}$ = {glue:text}`d_th_cm` = {glue:text}`d_th_in`. Then, the mass flow rate can be determined from the exit conditions:

```{code-cell}
A_e = np.pi * d_e**2 / 4
mdot = p_c * A_e * X_e / np.sqrt(R * T_c)
```

```{code-cell}
:tags: [remove-cell]
glue("mdot_kg", f"{mdot.to('kg/s'):.1F~P}", display=False)
glue("mdot_lb", f"{mdot.to('lb/s'):.1F~P}", display=False)
```

The mass flow rate is $\dot{m}$ = {glue:text}`mdot_kg` = {glue:text}`mdot_lb`. Finally, we can find the exit velocity in a few ways. Let's compute the speed of sound from the static temperature at the exit, and then use the Mach number to find the exit velocity.

```{code-cell}
Tt_Te = 1 + (gamma - 1) / 2 * M_e**2
T_e = T_c/Tt_Te
a_e = np.sqrt(gamma * R * T_e)
V_e = M_e * a_e
```

```{code-cell}
:tags: [remove-cell]
glue("T_e", f"{T_e:.1F~P}", display=False)
glue("a_e", f"{a_e.to('m/s'):.2F~P}", display=False)
glue("V_e", f"{V_e.to('m/s'):.2F~P}", display=False)
```

The exit static temperature is $T_e$ = {glue:text}`T_e`, the speed of sound is $a_e$ = {glue:text}`a_e`, and the exit velocity is $V_e$ = {glue:text}`V_e`. Finally, the thrust is computed from Eq. {eq}`rocket-thrust`, using the fact that the exit pressure is matched to the ambient.

```{code-cell}
F = mdot * V_e
```

```{code-cell}
:tags: [remove-cell]
glue("thrust_N", f"{F.to('kN'):.2F~P}", display=False)
glue("thrust_lbf", f"{F.to('pound_force'):.2F~P}", display=False)
```

The thrust is $F$ = {glue:text}`thrust_N` = {glue:text}`thrust_lbf`. Alternately, we can calculate the thrust using the ideal thrust coefficient, given by Eq. {eq}`ideal-nozzle-thrust-coefficient`.

```{code-cell}
Gamma = np.sqrt(gamma) * (2 / (gamma + 1))**((gamma + 1)/(2*(gamma - 1)))
p_e = p_0
pe_pc = (p_e / p_c).to("dimensionless")
c_fi = Gamma * np.sqrt(2 * gamma / (gamma - 1) * (1 - pe_pc**((gamma - 1) / gamma)))
A_th = np.pi * d_th**2 / 4
F_alt = A_th * p_c * c_fi
```

```{code-cell}
:tags: [remove-cell]
glue("F_alt", f"{F_alt.to('kN'):.2F~P}", display=False)
```

With this approach, the thrust is $F$ = {glue:text}`F_alt`, equivalent to the first approach. This provides a good check that our work is correct and consistent.
