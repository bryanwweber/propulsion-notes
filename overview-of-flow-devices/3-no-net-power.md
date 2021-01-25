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

# Flow Machines with No Net Power Input

From the energy equation, we can also set the net power input to zero. In that case, the energy equation becomes:

```{math}
:label: no-power-energy-equation
\left(h_e - h_0\right) + \frac{1}{2}\left(V_e^2 - V_0^2\right) = Q
```

Relating the kinetic energy term to the thrust via the conservation of momentum equation, we can write:

```{math}
:label: simplify-kinetic-energy
\frac{1}{2}\left(V_e^2 - V_0^2\right) = \frac{1}{2}\left(V_e - V_0\right)\left(V_e + V_0\right) = V_{\text{avg}}\frac{F}{\dot{m}}
```

Plugging Eq. {eq}`simplify-kinetic-energy` into Eq. {eq}`no-power-energy-equation` and solving for the thrust, we find:

```{math}
:label: no-power-thrust
F = \frac{\dot{m}}{V_{\text{avg}}} \left[Q - \left(h_e - h_0\right)\right]
```

For Eq. {eq}`no-power-thrust` to be positive, and therefore to be a thrust rather than a drag, the terms in square brackets must be larger than zero. This means that $Q > 0$ (an input) and $Q > (h_e - h_0)$. The heat transfer input typically comes from the combustion of a fuel with air in a jet engine.

## Engine Designs

The specific choice of fuel and engine components depends on the operating speed range of the flow machine. In all air-breathing engine designs, an inlet, called a **diffuser**, captures air during flight. The air is mixed with fuel and ignited in the **combustor**, providing the input heat transfer. After combustion, the products are exhausted through a **nozzle** to produce thrust.

```{note}
In Section {ref}`conservation_equations_assumptions`, we assumed that the mass flow rate of the added fuel was negligible compared to the other flows in the engine. In principle, neglecting the fuel flow can cause between a 2-5% error in the mass flow rate. However, it happens that some air typically needs to be extracted for functions within the aircraft outside the engine. The mass flow rate of this **bleed air**, taken from the compressor, happens to be approximately equal to the mass flow rate of fuel added in the combustor. This reduces the error even further!
```

### Turbojet

```{margin}
The **Mach number**, named for Ernst Mach, is the ratio of the flight velocity to the local speed of sound. It is a dimensionless number that is critically important in the analysis of flows through propulsion devices. We will work with the Mach number more specifically in an upcoming section. For now, it is sufficient to identify $M_0 > 1$ as supersonic flight and $M_0 < 1$ as subsonic flight.
```

For flight **Mach numbers** in the range of 0 < $M_0$ < 3, the pressure of the air must be increased after it is ingested. This is accomplished by a mechanical **compressor**, typically an axial compressor. To provide shaft power input to the compressor, a **turbine** is installed after the combustor, before the nozzle. The power extracted by the turbine exactly offsets the power input by the compressor, so the entire system has no _net_ power. This engine design is called a **turbojet** engine, and the compressor and turbine are typically called **turbomachinery**.

One limitation of turbojet engines is that the amount of energy that can be added in the combustor is limited by the material properties of the downstream components. This is particularly true for the turbine, whose blades are rotating at extremely high RPM and are under very large stresses as a result. This temperature limit, in turn, limits the exhaust velocity $V_e$, which limits the thrust output of a turbojet.

One way to cool the flow is by directing "cold" air from the compressor around the combustor and injecting it into the flow through cooling holes. Cooling holes are usually installed just downstream of the combustor and within the first few stages of turbine blades.

For steady state flight, we know that the thrust must equal the drag. However, in the transonic regime (0.8 < $M_0$ < 1.2), the drag on the aircraft is significantly increased due to a phenomenon called **drag-divergence**. Drag divergence means that most turbojet powered aircraft cannot generate enough thrust to cruise at transsonic Mach numbers.

However, the engine can be modified to increase the amount of heat transfer input by adding an **afterburner**. This is an additional combustor that is added between the turbine exit and the nozzle. Extra fuel is injected into the flow and ignited. Since there are no turbomachinery components downstream of the afterburner, the temperature can be much higher.

Since cooling air is added to the flow to keep the turbine from failing, there is sufficient oxygen in the flow after the turbine to support more combustion. However, the total air-to-fuel ratio, which may be as high as 50 for standard turbojets, is halved to approximately 25 by the use of the afterburner.

### Ramjet and Scramjet

At higher flight Mach numbers, between 3 < $M_0$ < 5, a properly designed inlet can reduce the flow velocity to a subsonic velocity and compress the ingested air to high enough pressures that a compressor is not required. This pressure increase is called the **ram pressure**. Since no turbomachinery components are required, the design of the engine is substantially simplified. This design is called a **ramjet**.

For flight Mach numbers greater than about 5, reducing the inlet flow to subsonic velocities would cause such a large temperature increase that any combustion would not be able to effectively provide heat transfer. Therefore, the inlet must be designed to reduce the flow velocity to a lower, but still supersonic, velocity. The inlet still provides a ram pressure increase, so no turbomachinery is required. This design is called a **scramjet** where the _s_ and _c_ stand for <emph>S</emph>upersonic <emph>C</emph>ombustion ramjet.

```{note}
The biggest challenge with the design of scramjet engines is stabilizing the combustion within the engine. In a turbojet or ramjet engine, the flame is usually stabilized by introducing a **flame holder**, essentially a metal wedge, which causes the flow to recirculate. This mixes hot combustion products with fresh mixture, bringing the fresh mixture up to the ignition temperature. However, designers cannot use flame holders in scramjet engines because they would reduce the flow to subsonic velocity, with the accompaning temperature increase and pressure loss.
```

Eliminating turbomachinery simplifies the design of the ramjet and scramjet, but this comes with a major disadvantage. Ramjets and scramjets do not produce thrust unless they are flying at a high enough velocity to provide enough ram pressure. This means that they cannot accelerate from a standstill to their flight velocity. Instead, they must be started by launching from a high-speed platform, or have an additional on-board engine (for example, a rocket) to propel them to supersonic speeds.

## Efficiency of Jet Engines

We can expand Eq. {eq}`no-power-thrust` with the definition of $\dot{m}$ and $V_{\text{avg}}$ to find:

```{math}
:label: expanded-thrust-no-heat
F = \rho_0 A_0 \frac{V_0}{\left(V_0 + V_e\right)/2} \left[Q - \left(h_e - h_0\right)\right]
```

As flight velocity $V_0$ increases, both the top and bottom of the fraction in the middle of Eq. {eq}`expanded-thrust-no-heat` will increase. This means that the thrust is approximately constant as flight speed changes. This is the primary advantage of jet engines over propellers, because it is not inherently speed-limited.

To define the overall efficiency of the propulsion engine, we can take the ratio of the useful power output to the rate of heat transfer input:

```{math}
:label: overall-efficiency
\eta_o = \frac{F V_0}{\dot{m}Q} = \frac{V_0}{V_{\text{avg}}} \left[1 - \frac{h_e - h_0}{Q}\right]
```

In Eq. {eq}`overall-efficiency`, we identify the ratio $V_0/V_{\text{avg}}$ as the **propulsive efficiency**, $\eta_{\text{p}}$. In addition, we can define the thermal efficiency as:

```{math}
:label: thermal-efficiency
\eta_{\text{th}} = 1 - \frac{h_e - h_0}{Q}
```

This means we can represent the overall thermal efficiency as:

```{math}
\eta_o = \eta_{\text{p}} \eta_{\text{th}}
```

The thermal efficiency captures the imperfect conversion of heat input to usable thermal energy, since some energy is stored in the flow of gases. The propulsive efficiency captures the effect of imperfect conversion of thrust into velocity change.

In a typical jet engine, these two efficiencies move in opposite directions. When the thermal efficiency is high, the exit velocity is high as well. This leads to a lower propulsive efficiency for a given flight speed. Typical jet aircraft will cruise around $V_0/V_e \approx 0.6$, which represents a good balance between the two efficiencies.
