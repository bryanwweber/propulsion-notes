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
:tags: [remove-input]

from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import Category10 as palette
from IPython.display import HTML

import numpy as np
from myst_nb import glue

import itertools

output_notebook(hide_banner=True)
opts = dict(plot_width=500, plot_height=300, min_border=0)
colors = itertools.cycle(palette[10])
```

# Flow Machines with No Heat Addition

Under the idealized assumptions we discussed in {ref}`conservation_equations_review`, we assumed that there would be no stray heat transfer. This typically means that devices whose purpose is not to have a heat transfer do not. In propulsion engines, these devices are typically:

* Propellers
* Fans
* Compressors
* Turbines

Consider a simple propeller. This may be attached to an aircraft to provide thrust, if there is a power source. Or, it may be a wind turbine, and there is a power sink. In either case, the system is shown in {numref}`propeller`.

```{figure} ../images/propeller.svg
:name: propeller

A simplified propeller. Note that station 1 is aligned with the plane of the propller blades.
```

The plane through the propeller blades is perpendicular to the oncoming velocity. As the fluid passes over the propeller blades, which are shaped like wings, it experiences a change of momentum. In the case of a power source, the blades do work on the fluid, and the fluid is accelerated by the blades.

Now we will focus on propulsive applications, such that a power input is required ($P > 0$) and the force on the fluid is positive ($F>0$). 

## Energy Conservation

The energy conservation relationship simplifies to:

```{math}
:label: no-heat-addition-energy

P = \dot{m}\left[\left(h_e - h_0\right) + \frac{1}{2}\left(V_e^2 - V_0^2\right)\right]
```

However, we expect that the static temperature of the air stays nearly constant during this process, since $Q = 0$. Since the static enthalpy is directly proportional to the static temperature, if the static temperature is constant so is the static enthalpy. In an equation:

```{math}
:label: static-enthalpy-temperature

h_e - h_0 = \int_{T_0}^{T_e} c_p dT
```

If temperature is constant, then $dT$ is zero and $h_e - h_0 = 0$. This further simplifies Eq. {eq}`no-heat-addition-energy` to:

```{math}
:label: simplified-no-heat-energy

P = \frac{1}{2}\dot{m}\left(V_e^2 - V_0^2\right) = \frac{1}{2}\dot{m}\left(V_e - V_0\right)\left(V_e + V_0\right)
```

where the last equation on the right hand side is found by factoring the squared velocity terms. Then, noting that $\dot{m}\left(V_e - V_0\right)$ is the change in momentum of the fluid, and $\left(V_e + V_0\right)/2$ is the average velocity, we can write:

```{math}
:label: propeller-power

P = F V_{\text{avg}}
```

## Mass Conservation

We will show later on that the average velocity is equal to the velocity at the plane of rotation of the propeller, such that:

```{math}
:label: no-heat-addition-mass

\dot{m} = \rho_0 A_0 V_0 = \rho_e A_e V_e = \rho_1 A_1 V_{\text{avg}}
```

## Constant Applied Power

If the applied power $P$ is constant, Eq. {eq}`propeller-power` shows that the thrust force drops off as flight speed increases:

```{math}
F = \frac{P}{V_{\text{avg}}} = \frac{2P}{V_e + V_0} = \frac{2P}{V_0\left(1 + V_e/V_0\right)}
```

## Propulsive Efficiency

Under our assumption of steady state, the drag is equal to the thrust, $D = F$. The **required power**, also called the **useful power**, is the power required to overcome the drag, $P_u = D V_0 = FV_0$.

<!-- Then, it is useful to divide the total power provided by the propeller into the useful portion and the portion accounting for losses. This will allow us to define a **propulsive efficiency**.

```{math}
P = P_u + P_l = F V_0 + P_l
```

where $P_l$ is the power loss and $P_u$ is the useful power. Solving for the loss term, and plugging in Eq. {eq}`simplified-no-heat-energy`:

```{math}
:label: propeller-power-loss

P_l = \frac{1}{2}\dot{m}\left(V_e^2 - V_0^2\right) - \dot{m}\left(V_e - V_0\right)V_0 = \frac{1}{2}\dot{m}\left(V_e - V_0\right)^2
``` 
-->

Now we can define the **propulsive efficiency** as the ratio of the useful power, $F V_0$, to the total power supplied to the fluid, $P = F V_{\text{avg}}$:

```{math}
:label: propulsive-efficiency

\eta_p = \frac{F V_0}{F V_{\text{avg}}} = \frac{V_0}{\left(V_0 + V_e\right)/2} = \frac{2\left(V_0/V_e\right)}{1 + \left(V_0/V_e\right)}
```

The figure below plots $\eta_p$ on the $y$-axis and the ratio $V_0/V_e$ on the $x$-axis. Larger values of the ratio correspond to $V_0$ getting close to $V_e$, and $V_0$ cannot exceed $V_e$ for steady, level flight. We can see that as the flight velocity approaches the exit velocity, the propulsive efficiency goes to 1. This means that all of the power supplied by the propeller is going to overcome the drag.

```{code-cell}
:tags: [remove-input]

p1 = figure(x_axis_label="V₀/Vₑ", y_axis_label="𝜂", title="Propulsive efficiency vs. V₀/Vₑ", **opts)
ratio = np.linspace(0, 1, 250)
eta_p = 2 * ratio / (1 + ratio)
p1.line(ratio, eta_p, line_width=2)
show(p1)
```

However, flying at a certain velocity requires a minimum thrust to balance the drag. For a fixed value of the total power, Eq. {eq}`propeller-power` shows that the thrust drops off as the flight speed increases:

```{math}
:label: thrust-drop-off-propeller

F = \frac{P}{V_{\text{avg}}} = \frac{P}{\left(V_0 + V_e\right)/2} = \frac{2P}{V_0\left(1 + V_e/V_0\right)}
```

The figure below plots the thrust divided by the power on the $y$-axis. For a fixed value of the power, higher values of $F/P$ are better. On the $x$-axis is the $V_0/V_e$ ratio. The different curves on the plot represent different values of the flight speed, $V_0$. At a fixed value of $V_0$, smaller values of $V_0/V_e$ mean a larger value of $V_e$.

```{code-cell}
:tags: [remove-input]

p2 = figure(x_axis_label="V₀/Vₑ", y_axis_label="F/P (N/W)", title="Thrust-to-power ratio", **opts)
ratio = np.linspace(0.01, 1.0, 250)
flight_velocities = np.array((50, 100, 150, 200))
for V_0 in flight_velocities:
    p2.line(ratio, 2 / (V_0 * (1 + 1/ratio)),
            legend_label=f"{V_0} m/s", color=next(colors), line_width=2)

p2.legend.location = "top_left"
p2.legend.title = "V₀"
show(p2)
```

As we can see from the figure, smaller values of $V_0/V_e$ result in lower values of the thrust for a fixed power input. From Eq. {eq}`ideal-conservation-of-momentum`, conservation of momentum, we can see that the thrust force is the product of the mass flow rate and the velocity difference. From the figure above, we get a higher thrust output for a given power when the fluid is accelerated as little as possible. Thus, we want to have a very large mass flow rate to achieve the best propulsive efficiency. Effectively, this means the propeller should have the largest diameter (area) possible, since the density is constant.

Another way to approach this function is to plot the thrust-to-power ratio versus the flight speed, for a given ratio of $V_0/V_e$.

```{code-cell}
:tags: [remove-input]

colors = itertools.cycle(palette[10])
p3 = figure(x_axis_label="V₀", y_axis_label="F/P (N/W)", title="Thrust-to-power ratio", **opts)
flight_velocities = np.linspace(25, 250, 250)
ratios = np.array((0.9, 0.6, 0.3))
for ratio in ratios:
    p3.line(flight_velocities, 2 / (flight_velocities * (1 + 1/ratio)),
            legend_label=f"{ratio}", color=next(colors), line_width=2)

p3.legend.title = "V₀/Vₑ"
show(p3)
```

From this plot, we can see that as the flight velocity increases, the thrust decreases for a fixed power input. For a fixed power input, there is then a maximum speed that the aircraft can fly where it can balance the drag.

## Example

The engine on a propeller-driven aircraft provides $P_s$ = 1000 kW of shaft power to the propeller. Of that, 90% is transferred to the air by the propeller. At high speeds, the drag coefficient of the aircraft is $c_D$ = 0.02. The wing area of the aircraft is $S$ = 21.6 m² and the propeller diameter is 3.4 m. Determine the maximum speed of the aircraft at 6,000 m altitude and the corresponding propulsive efficiency.

The drag on the aircraft, and therefore the thrust, is given by:

```{math}
:label: drag-equation

D = \frac{1}{2}c_D S \rho V_0^2
```

where $c_D$ is the dimensionless drag coefficient and $S$ is the wing area. This equation is set equal to Eq. {eq}`propeller-power`, and we solve for $V_0$:

```{math}
\begin{aligned}
\frac{P}{V_{\text{avg}}} &= \frac{1}{2}c_D S \rho_0 V_0^2 \\
\frac{4P}{c_D S \rho_0} &= \left(V_0 + V_e\right) V_0^2 \\
\frac{4\left(0.9 P_s\right)}{c_D S \rho_0} &= V_0^3\left(1 + \frac{V_e}{V_0}\right)
\end{aligned}
```

In this equation, the only unknowns are $V_0$ and the ratio $V_e/V_0$. It turns out to be more convenient to work in terms of the ratio rather than explicitly in terms of $V_e$. This is because we can solve the momentum equation, Eq. {eq}`ideal-conservation-of-momentum`, for the ratio as follows. Assuming that the flow is incompressible, such that $\rho_0 = \rho_1$,

```{math}
\begin{aligned}
F &= \dot{m}\left(V_e - V_0\right) \\
\frac{1}{2} \rho_0 c_D S V_0^2 &= \rho_1 A_1 V_{\text{avg}}\left(V_e - V_0\right) \\
\frac{1}{2} c_D S V_0^2 &= \frac{1}{2} A_1 \left(V_0 + V_e\right) \left(V_e - V_0\right) \\
c_D S V_0^2 &= A_1 \left(V_e^2 - V_0^2\right)\\
c_D S &= A_1 \left[\left(\frac{V_e}{V_0}\right)^2 -1\right] \\
\frac{V_e}{V_0} &= \sqrt{\frac{c_D S}{A_1} + 1}
\end{aligned}
```

where $A_1$ is the frontal area of the propeller blades. Now we have two equations and two unknowns to solve for $V_0$.  Finally, we can solve for the propulsive efficiency using Eq. {eq}`propulsive-efficiency`.

The arithmetic is done with Python and the [Pint](https://pint.readthedocs.io) library to keep consistent units. The density of air at 6,000 m is found using the [Ambiance](https://ambiance.readthedocs.io/) package, in Appendix C, or other places online.

```{code-cell}
from pint import UnitRegistry
from ambiance import Atmosphere
import numpy as np

units = UnitRegistry()

P_s = 1000 * units.kW
eta_propeller = 0.9 * units.dimensionless
c_D = 0.02 * units.dimensionless
S = 21.6 * units.m**2
rho_sl = 1.225 * units.kg / units.m**3
sigma = 0.5389 * units.dimensionless
rho = rho_sl * sigma
altitude = 6000 * units.m
propeller_D = 3.4 * units.m
propeller_area = units.pi * propeller_D**2 / 4
atmos = Atmosphere(altitude.to("m").magnitude)
rho_0 = atmos.density * units.kg / units.m**3

# Use NumPy to ensure proper handling of the units
# Can also do **(1/2)
Ve_V0 = np.sqrt(c_D * S / propeller_area + 1)
# Cube root
V_0 = np.cbrt(4 * eta_propeller * P_s / (c_D * rho_0 * S * (1 + Ve_V0))).to("m/s")
print(f"V₀ = {V_0:.2F~P} = {V_0.to('mph'):.2F~P}")

eta_P = 2 / (1 + Ve_V0)
print(f"𝜂 = {eta_P:.4F}")
```

The flight velocity is about 184.1 m/s (412 mph) and the propulsive efficiency is approximately 98.8%.

From this example, we can see that the flight speed is proportional to the cube root of the shaft power, further amplifying the fact that increasing the power input to the propeller provides diminishing returns. Finally, we note that due to the incompressible flow assumption (constant density), the streamtube area in the freestream ahead of the propeller is slightly larger than the propeller area, which is slightly larger than the downstream streamtube area: $A_0 > A_1 > A_e$.
