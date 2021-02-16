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

import itertools

from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.palettes import Category10 as palette
from bokeh.models import Span, PrintfTickFormatter
from bokeh.layouts import column

import numpy as np
from scipy import optimize

output_notebook(hide_banner=True)
opts = dict(plot_width=500, plot_height=400, min_border=0)
colors = itertools.cycle(palette[10])
```

# Rocket Nozzles

The nozzle is the most important component of the rocket engine. The nozzle converts high pressure, and ideally high temperature, gases into low pressure gases with much higher velocity by changing the cross-sectional area of the flow. This momentum transfer then provides the thrust force on the spacecraft.

In principle, nozzles can function with any source of high pressure fluid upstream. As we'll see, the higher the upstream pressure and temperature, the higher the performance of the nozzle. However, this ability to be very flexible and still provide thrust is why nozzles are the most important component.

For most purposes, we will assume the upstream flow is at **nearly zero velocity**. This means that the upstream temperature and pressure are at the **stagnation** conditions, which is a very important state for the analysis of nozzles.

## Stagnation State

For flowing fluids, we define two conditions at which we can evaluate properties:

1. **Static**: What you would measure if you moved along with the flow
2. **Stagnation**: What you would measure if you slowed the fluid to a stop in an adiabatic and reversible (isentropic) process. Also known as the **total** state, with the subscript $t$.

When the fluid is stationary, the static and stagnation properties are equal, by definition. The objective of the nozzle is to produce high velocity flow at the exit using the high stagnation pressure and temperature upstream of the nozzle.

```{attention}
The word _total_ in _total pressure_ or _total temperature_ has nothing to do with a sum over several states or locations. It is a _total_ in the sense that it accounts for the sum of the **static property** and the portion of that property due to the **velocity of the flow**.

For instance, consider a flow with static temperature $T$ and velocity $V$. The specific kinetic energy (kinetic energy per unit mass) is then $V^2/2$. If we isentropically slow the fluid to a stop, the kinetic energy will be converted internal energy of the fluid. This is because the process is isentropic, so no energy is lost by heat transfer and no potential to do work is lost by irreversibilities.

The temperature is directly proportional to the internal energy of an ideal gas, so increasing the internal energy also increases the temperature. This is the definition of the total temperature. It is measuring the contribution from the static temperature which was in the fluid to begin with, and the result of converting the kinetic energy of the fluid to internal energy. Similar things happen for the pressure, density, and enthalpy.

So we can define _both_ the static properties (no subscript) and the total properties ($t$ subscript) at _every_ axial location in the flow. In general, both static and total properties will change as a function of axial location in the flow. For the special case of _isentropic_ flow, the total properties will be constant throughout the flow domain, even though the static properties may change (quite significantly in some cases).

Finally, the static and total properties will in general be different from each other at every axial location in the flow. However, for the special case of very low velocity ($V\approx 0$), the specific kinetic energy is also very low, so we assume the static and total properties are equal.
```

As implied by the definition of the stagnation state, isentropic processes will be very important for our analysis. The isentropic process usually functions as an ideal _best case_ scenario for the analysis.

## Equation of State

Before continuing to discuss isentropic processes, we must discuss how to evaluate flow properties. We will assume that all of our flows are **ideal** gases, that follow the ideal gas law:

```{math}
:label: ideal-gas-law
p = \frac{\rho R_u T}{W}
```

where $p$, $\rho$, and $T$ are the static pressure, density, and temperature, $R_u$ is the [universal gas constant](https://en.wikipedia.org/wiki/Gas_constant), and $W$ is the molecular weight. We will represent most equations in the log-differential form, as:

```{math}
:label: ideal-gas-differential
\frac{dp}{p} = \frac{d\rho}{\rho} + \frac{dT}{T} - \frac{dW}{W}
```

Note that the for flows undergoing chemical reaction, the change in molecular weight may be significant. We will ignore this effect in the beginning of our analysis, but return to relax that assumption later.

## Speed of Sound

The speed of sound is the speed at which an infinitesimal pressure disturbance propagates through a fluid. The disturbance is of such a small magnitude that the process that the gas goes through is reversible, and the process is adiabatic. Therefore, sound waves are isentropic processes.

The speed of sound is defined by the differential:

```{math}
:label: speed-of-sound-definition
a^2 = \left(\frac{\partial p}{\partial \rho}\right)_{s}
```

where $a$ is the speed of sound and the subscript $s$ indicates the partial derivative is to be taken for a constant entropy process.

The entropy of the ideal gas can be determined from the second Gibbs relation:

```{math}
:label: second-gibbs
ds = c_p \frac{dT}{T} - \frac{dp}{\rho T}
```

where $s$ is the entropy and $c_p$ is the specific heat at constant pressure. Introducing Eq. {eq}`ideal-gas-differential`, we find:

```{math}
:label: entropy-differential
\frac{ds}{c_v} = \frac{dp}{p} - \gamma \frac{d\rho}{\rho} + \gamma \frac{dW}{W}
```

where $c_v$ is the specific heat at constant pressure and $\gamma$ is the ratio of specific heats:

```{math}
:label: ratio-of-specific-heats
\gamma = \frac{c_p}{c_v}
```

Note that $\gamma$, $c_p$, and $c_v$ are functions of the temperature and composition in general. The specific heats are related to each other by the gas constant as well:

```{math}
:label: specific-heat-relationship
c_p - c_v = \frac{R_u}{W}
```

Using Eqs. {eq}`ratio-of-specific-heats` and {eq}`specific-heat-relationship`, we can find $c_p$, $c_v$, or $\gamma$ given any two of them.

If we assume the change in molecular weight is zero, and the process is isentropic, then we can relate the pressure to the density as follows:

```{math}
\frac{dp}{p} = \gamma \frac{d\rho}{\rho}
```

or

```{math}
\frac{dp}{d\rho} = \frac{\gamma p}{\rho}
```

Note that this differential is specifically and only for an isentropic process of an ideal gas, but it meets the definition of the speed of sound earlier. Plugging in Eq. {eq}`ideal-gas-law`, we find:

```{math}
:label: speed-of-sound
a = \sqrt{\gamma \frac{R_u}{W} T}
```

In differential form, this is:

```{math}
:label: speed-of-sound-differential
\frac{da}{a} = \frac{1}{2}\left(\frac{d\gamma}{\gamma} + \frac{dT}{T} - \frac{dW}{W}\right)
```

## Mach Number

The Mach number is defined as the ratio of the current speed to the speed of sound:

```{math}
:label: mach-number
M = \frac{V}{a}
```

In differential form, it is more convenient to work with the square of the Mach number, to cancel some of the fractions from the speed of sound:

```{math}
:label: mach-number-differential
\frac{dM^2}{M^2} = \frac{dV^2}{V^2} + \frac{dW}{W} - \frac{d\gamma}{\gamma} - \frac{dT}{T}
```

By definition, flows with Mach number $M < 1$ are called **subsonic**, flows with $M > 1$ are called **supersonic**, and flows with $M = 1$ are called **sonic**. In addition, the range $0.8 < M < 1.2$ is usually called **transonic** and $M > 5$ is usually called **hypersonic**.

(relations-for-compressible-flow)=
## Relations for Compressible Flow

The flow through rocket nozzles is compressible in general. It will be convenient to relate the static and stagnation properties to each other and to the Mach number. In addition, we will define a set of properties when the Mach number $M = 1$, called the characteristic properties. In all of the following equations, we will assume that the process is isentropic and that the ratio of specific heats $\gamma$ is constant.

### Static and Stagnation Property Ratios

First, we imagine a process which isentropically slows the flow from the current velocity, where the static pressure is $p$, to a stop, where the static pressure is equal to the total pressure, $p_t$. Likewise, the temperature changes from the static temperature $T$ to the total temperature $T_t$ as a result of this process and the density changes from the static density $\rho$ to the total density $\rho_t$.

For any isentropic process of an ideal gas, we can show that the pressure and density have the following relationship {cite}`Hall2018`:

```{math}
:label: p-rho-isentropic
\frac{p_t}{p} = \left(\frac{\rho_t}{\rho}\right)^{\gamma}
```

Plugging in Eq. {eq}`ideal-gas-law` on the right side of Eq. {eq}`p-rho-isentropic` gives:

```{math}
:label: p-T-isentropic
\frac{T_t}{T} = \left(\frac{p_t}{p}\right)^{(\gamma - 1)/\gamma}
```

and plugging it in on the left side of Eq. {eq}`p-rho-isentropic` gives:

```{math}
:label: T-rho-isentropic
\frac{T_t}{T} = \left(\frac{\rho_t}{\rho}\right)^{\gamma - 1}
```

### Relationships to the Mach Number

Next, we would like a way to relate the property ratios to the Mach number. The reason we want this is because we can determine the Mach number at any axial location in the flow. Thus, if we have a relationship between the static properties, total properties, and Mach number, we can find any property at any axial location.

We start from the definition of the enthalpy:

```{math}
:label: enthalpy
h = c_p T
```

where $h$ is the enthalpy. Then, the conservation of energy for this flow is given by:

```{math}
h_t + V_{t}^2/2 = h + V^2/2
```

where $V_{t}$ is zero by definition. Plugging in Eqs. {eq}`speed-of-sound`, {eq}`mach-number`, and {eq}`enthalpy`, we find:

```{math}
:label: isentropic-temperature-mach
\frac{T_t}{T} = 1 + \frac{\gamma - 1}{2}M^2
```

Using Eqs. {eq}`p-T-isentropic` and {eq}`T-rho-isentropic`, we can also find:

```{math}
:label: isentropic-pressure-mach
\frac{p_t}{p} = \left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{\gamma}{\gamma - 1}}
```

and

```{math}
:label: isentropic-density-mach
\frac{\rho_t}{\rho} = \left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{1}{\gamma - 1}}
```

We can also define the stagnation speed of sound, based on the stagnation temperature:

```{math}
:label: a-t-definition
a_t = \sqrt{\gamma R T_t}
```

or we can relate this to the local flow conditions by using the energy equation {cite}`Anderson2003` (Ch. 3.5):

```{math}
:label: stagnation-speed-of-sound
\frac{a_t^2}{\gamma - 1} = \frac{a^2}{\gamma - 1} + \frac{V^2}{2}
```

where $a$, $\gamma$, and $V$ are found at the local axial location.

### Characteristic Properties

Another important set of reference properties are called the **characteristic properties**, related to the sonic condition rather than the stagnation condition. The characteristic properties are defined by another imaginary isentropic process that takes the flow from its current velocity to a Mach number $M = 1$. If the flow is supersonic, this will means slowing it down; if it is subsonic, it will be accelerated.

Since this process is adiabatic, we can imagine that this process will change the static temperature. The static temperature reached when $M = 1$ is defined as the **characteristic temperature**, $T^*$. Then, the **characteristic speed of sound** is:

```{math}
:label: a-star-definition
a^* = \sqrt{\gamma R T^*}
```

and the **characteristic Mach number**:

```{math}
:label: characteristic-mach-number
M^* = \frac{V}{a^*}
```

In general, $M^*\neq M$, where $M$ is the actual Mach number at a given axial location in the flow. For the special case when $M^* = 1$, then $M = 1$ as well.

Like the stagnation properties, the characteristic properties are defined for every point in the flow, given the Mach number and static temperature. If the flow is isentropic throughout, then the values for $T^*$ and $a^*$ will be constant throughout the flow.

We can show {cite}`Anderson2003` (Ch. 3.5) that the characteristic speed of sound is given by:

```{math}
:label: characteristic-speed-of-sound
\left(a^*\right)^2 \frac{\gamma + 1}{2\left(\gamma - 1\right)} = \frac{a^2}{\gamma - 1} + \frac{V^2}{2}
```

where $a$, $V$, and $\gamma$ are calculated at the local flow conditions. From this, we can also determine the characteristic Mach number and temperature. Eq. {eq}`characteristic-speed-of-sound` can also be divided by $V^2$ to give a relationship between $M$ and $M^*$:

```{math}
:label: mach-to-m-star
M^2 = \frac{2}{\left[\left(\gamma + 1\right)/\left(M^*\right)^2\right] - \left(\gamma - 1\right)}
```

From this equation, we can see the following relationships:

* $M^* = 1$ if $M = 1$
* $M^* < 1$ if $M < 1$
* $M^* > 1$ if $M > 1$
* $M^*\rightarrow \sqrt{\left(\gamma + 1\right)/\left(\gamma - 1\right)}$ if $M\rightarrow\infty$

### Ratios of Characteristic Properties

Similar to the ratios of total and static properties, we will find it useful to have ratios related to the characteristic properties. Starting from the characteristic speed of sound, Eq. {eq}`characteristic-speed-of-sound`, and dividing by the stagnation speed of sound, Eq. {eq}`stagnation-speed-of-sound`, we find:

```{math}
:label: a-star-over-a-t
\frac{a^*}{a_t} = \sqrt{\frac{2}{\gamma + 1}}
```

From the definition of the speed of sound, we can also write:

```{math}
:label: T-star-over-T-t
\frac{T^*}{T_t} = \frac{2}{\gamma + 1}
```

Finally, we can use the relationships of stagnation pressure and density with the Mach number, Eqs. {eq}`isentropic-pressure-mach` and {eq}`isentropic-density-mach`, noting that for the characteristic conditions $M = 1$, to write:

```{math}
:label: p-star-over-p-t
\frac{p^*}{p_t} = \left(\frac{2}{\gamma + 1}\right)^{\frac{\gamma}{\gamma - 1}}
```

and

```{math}
:label: rho-star-over-rho-t
\frac{\rho^*}{\rho_t} = \left(\frac{2}{\gamma + 1}\right)^{\frac{1}{\gamma - 1}}
```

## Quasi-One-Dimensional Nozzle Flow

Let's now consider a simple nozzle with varying cross-sectional area. We will neglect the influence of skin friction and heat transfer at the nozzle wall, so that the only way that the flow may change is due to the area change. In this nozzle, the flow is adiabatic and reversible, so the entropy is constant.

### Mass Conservation

In steady flow, the mass flow rate is given by the integral relationship:

```{math}
\int \rho \left(\vec{V}\cdot\hat{n}\right) dA = 0
```

If we further simplify to quasi-one-dimensional flow, and define the $z$ axis as the flow direction, then the mass flow rate is:

```{math}
:label: one-d-mass-flow-rate
\dot{m}(z) = \rho(z) A(z) V(z) = \text{const}
```

where $\dot{m}(z)$ is a constant, and the density, area, or velocity may change as a function of axial location. In differential form, this becomes:

```{math}
:label: mass-flow-rate-differential
\frac{d\dot{m}}{\dot{m}} = 0 =\frac{d\rho}{\rho} + \frac{dV}{V} + \frac{dA}{A}
```

At a given station, or axial ($z$) location, the mass flow rate can be related to the local flow conditions by using Eqs. {eq}`ideal-gas-law` and {eq}`speed-of-sound`:

```{math}
\dot{m} = p A M\sqrt{\frac{\gamma}{R T}}
```

where $R = R_u / W$. Using the results from {ref}`relations-for-compressible-flow`, we can write the mass flow rate as:

```{math}
:label: mass-flow-rate-mach-number
\dot{m} = \frac{p_t A}{\sqrt{T_t}}\sqrt{\frac{\gamma}{R}}M\left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{-\left(\gamma + 1\right)}{2\left(\gamma - 1\right)}}
```

### Momentum Equation

The integral form of the momentum equation for a control volume around the nozzle is:

```{math}
\int_{A} \left(\rho \vec{V}\cdot\hat{n}\right)\vec{V} dA = 0
```

because we are neglecting friction and drag. In the log differential form, this becomes:

```{math}
\frac{dp}{p} + \frac{1}{2}\frac{\rho}{p}\frac{dV^2}{V^2} = 0
```

Replacing $\rho/p$ from the ideal gas law, Eq. {eq}`ideal-gas-law` and multiplying and dividing the second term by $a^2$, we can write:

```{math}
:label: momentum-differential
\frac{dp}{p} + \frac{1}{2}\gamma M^2 \frac{dV^2}{V^2} = 0
```

### Area-Velocity Relation

Using Eq. {eq}`mass-flow-rate-differential` to eliminate the $dp/p$ term from Eq. {eq}`momentum-differential`, we find the **area-velocity relation**:

```{math}
:label: area-velocity-relation
\frac{dA}{A} = \left(M^2 - 1\right) \frac{dV}{V}
```

This important equation gives us the relationship between Mach number, area change, and velocity change. We make a number of observations from this equation:

1. If $M\rightarrow 0$, this tells us that the product of the area and velocity is a constant, which is the continuity equation for incompressible flow.
2. If $M < 1$, the first time on the right-hand side of Eq. {eq}`area-velocity-relation` is negative. This means that if we want the velocity to increase ($dV > 0$), then $dA$ must be negative and the area must decrease. The opposite is also true; if we want velocity to decrease, the area must increase.
3. On the other hand, if $M > 1$, the first time on the right-hand side of Eq. {eq}`area-velocity-relation` is positive. This means that if we want the velocity to increase ($dV > 0$), then $dA$ must be positive and the area must increase. The opposite is also true; if we want velocity to decrease, the area must decrease.
4. If $M = 1$, the area must be constant ($dA = 0$). We can prove that for flow to accelerate from subsonic to supersonic, or to decelerate flow from supersonic to subsonic, this area must be a **minimum**.

### Area-Mach Number Relation

Now let's return to the nozzle. We will consider a **converging-diverging** nozzle, since we know that we want to accelerate the flow from subsonic in the combustion chamber to supersonic exit velocity. From the thrust equation, Eq. {eq}`rocket-momentum`, we know that the thrust is proportional to the nozzle exit velocity, so higher exit velocities will provide more thrust.

The location of the smallest area in the nozzle is called the **throat**. Since the area is at a minimum at this location, the slope must be zero, $dA = 0$. Therefore, the Mach number $M = 1$, and this defines the **characteristic area**, $A^*$.

Let's apply the conservation equations from a point upstream of the throat to the throat. Then:

```{math}
\rho V A = \rho^* V^* A^* \Rightarrow \frac{A}{A^*} = \frac{\rho^*}{\rho} \frac{a^*}{V}
```

Next, multiply and divide the right side by $\rho_t$. This gives us the relationship of $\rho_t/\rho$ and $\rho^*/\rho_t$, which we have developed previously. Finally, using Eq. {eq}`mach-to-m-star`, we find:

```{math}
:label: area-mach-relation
\left(\frac{A}{A^*}\right)^2 = \frac{1}{M^2}\left[\frac{2}{\gamma + 1}\left(1 + \frac{\gamma - 1}{2}M^2\right)\right]^{\frac{\gamma + 1}{\gamma - 1}}
```

This is the **area-Mach number relation** and it is a critically important equation to understand nozzle flows. To help understand why, we will inspect the figure below.

```{code-cell}
:tags: [remove-input]

p1 = figure(
    x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    title="Area-Mach Number Relation",
    y_axis_type="log",
    x_range=(0, 10), y_range=(0.05, 4.25),
    **opts
)
mach_number = np.hstack((np.logspace(-2, 0), np.linspace(1, 5)))
gamma = 1.4
first_term = 2 / (gamma + 1)
second_term = 1 + (gamma - 1)/2 * mach_number**2
power = (gamma + 1) / (gamma - 1)
area_ratio = np.sqrt(1/mach_number**2 * (first_term * second_term)**(power))
p1.line(area_ratio, mach_number, line_width=2)
p1.add_layout(Span(location=1.0, dimension="width"))
p1.add_layout(Span(location=1.0, dimension="height"))
p1.yaxis[0].formatter = PrintfTickFormatter(format="%2f")
show(p1)
```

From the graph, we can see two things immediately:

1. There are no solutions for $A/A^*$ less than 1.0. In other words, for isentropic flow, the area at any cross section must be greater than or equal to the characteristic area.
2. There are two values of $M$ that correspond to a given $A/A^*$ value, a subsonic and a supersonic solution. The only exception is at the point (1.0, 1.0), where the area is minimum and the flow is exactly sonic.

Assume that a convergent-divergent nozzle looks like the figure below. At the inlet, the area ratio goes to infinity, such that the Mach number goes to zero and the conditions are stagnated. The Mach number cannot be identically zero, because then there'd be no flow. In the case of isentropic flow through the nozzle, the flow will be accelerated through the subsonic Mach numbers, to the sonic condition at the throat, and then continue accelerating to supersonic Mach numbers.

The static pressure and temperature will also experience continuous decreases over the nozzle. At the inlet, the ratio of the static property to the stagnation property is one. At the throat, the ratios take on the values of the static property over the characteristic property.

```{code-cell}
:tags: [remove-input]
gamma = 1.4
opts["plot_height"] = 300
p2 = figure(
    title=f"Convergent-Divergent Nozzle, Isentropic Acceleration, 𝛾={gamma}",
    y_range=(-4.1, 4.1),
    **opts
)
p2.outline_line_width = 0
p2.axis.visible = False
p2.xaxis.major_tick_line_color = None
p2.xaxis.minor_tick_line_color = None
p2.xaxis.ticker = [0.0]
p2.ygrid.grid_line_color = None
p2.xaxis.major_label_overrides = {0: "Throat"}

r_t = 1
epsilon = 9
r_e = r_t * np.sqrt(epsilon)
theta_n = np.radians(35)
theta_e = np.radians(0.0)

r_upstream = 1.5 * r_t
upstream_center = r_t + r_upstream
x_upstream = np.linspace(-r_upstream + 0.01, 0, 200)
y_upstream = -np.sqrt(r_upstream**2 - x_upstream**2) + upstream_center

r_downstream = 0.382 * r_t
downstream_center = r_t + r_downstream
downstream_stop = r_downstream*np.cos(np.radians(270) + theta_n)
x_downstream = np.linspace(0, downstream_stop, 200)
y_downstream = -np.sqrt(r_downstream**2 - x_downstream**2) + downstream_center

x_n, y_n = x_downstream[-1], y_downstream[-1]
L = r_e / np.tan(np.radians(15))
l = r_t / np.tan(np.radians(15))
L_n = L - l
x_e, y_e = x_n + L_n, r_e

A = np.array([[x_n**2, x_n, 1.0], [x_e**2, x_e, 1.0], [2 * x_e, 1.0, 0.0]])
b = np.array([y_n, y_e, np.tan(theta_e)])
a, b, c = np.linalg.solve(A, b)

x_bell = np.linspace(x_n, x_e, 200)
y_bell = a * x_bell**2 + b * x_bell + c

x = np.hstack((x_upstream, x_downstream, x_bell))
y = np.hstack((y_upstream, y_downstream, y_bell))
p2.line(x, y)
p2.line(x, -y)

A_t = np.pi * r_t**2

A_ratio = np.pi * y**2 / A_t

def area_ratio(M, A_ratio):
    first_term = 2 / (gamma + 1)
    power = (gamma + 1) / (gamma - 1)
    second_term = 1 + (gamma - 1) / 2 * M**2
    return 1 / M**2 * (first_term * second_term)**(power) - A_ratio**2

M_upstream = optimize.root(
    area_ratio,
    x0=np.linspace(0.15, 1.0, x_upstream.shape[0]),
    args=(A_ratio[:x_upstream.shape[0]],)
)
M_downstream_sup = optimize.root(
    area_ratio,
    x0=np.linspace(1.0, 5.0, x_downstream.shape[0] + x_bell.shape[0]),
    args=(A_ratio[x_upstream.shape[0]:])
)

M_sup= np.hstack((M_upstream.x, M_downstream_sup.x))

p3 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0, 4.1),
    x_range=p2.x_range,
    **opts
)
p3.outline_line_width = 0
p3.xaxis.major_tick_line_color = None
p3.xaxis.minor_tick_line_color = None
p3.xaxis.major_label_text_color = None
p3.xaxis.ticker = [0.0]
p3.yaxis.ticker = [1.0]
p3.line(x, M_sup)

p_ratio_sup = (1 + (gamma - 1)/2 * M_sup**2)**(-gamma/(gamma - 1))
p4 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="p/p_t",
    # title="Area-Mach Number Relation",
    y_axis_type="log",
    y_range=(0.008, 1.1),
    x_range=p2.x_range,
    **opts
)
p4.outline_line_width = 0
p4.xaxis.major_tick_line_color = None
p4.xaxis.minor_tick_line_color = None
p4.xaxis.major_label_text_color = None
p4.xaxis.ticker = [0.0]
p4.yaxis.ticker = [1.0, (2 / (gamma + 1))**(gamma / (gamma - 1))]
p4.line(x, p_ratio_sup)

T_ratio_sup = (1 + (gamma - 1)/2 * M_sup**2)**(-1)
p5 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="T/T_t",
    # title="Area-Mach Number Relation",
    y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0.2, 1.1),
    x_range=p2.x_range,
    **opts
)
p5.outline_line_width = 0
p5.xaxis.major_tick_line_color = None
p5.xaxis.minor_tick_line_color = None
p5.xaxis.major_label_text_color = None
p5.xaxis.ticker = [0.0]
p5.yaxis.ticker = [1.0, (2 / (gamma + 1))]
p5.line(x, T_ratio_sup)

show(column(p2, p3, p4, p5))
```

```{note}
There is exactly one value of the pressure ratio $p_e/p_t$ that gives an isentropic acceleration from subsonic to supersonic flow. Under these conditions, the static pressure outside the nozzle must be equal to the static pressure of the flow at the exit plane.

The particular value of $p_e/p_t$ that gives isentropic acceleration depends on the expansion ratio of the nozzle, $A_e/A^*$.
```

### Effect of Pressure Ratio

So, what happens when the pressure ratio over the nozzle is not equal to the value that gives isentropic acceleration? There are a few different cases. The trivial case is that the outlet pressure is equal to the inlet pressure and there is no flow. Not super useful.

Now, imagine reducing the pressure ratio slightly, say to 0.9999. The flow accelerates in the converging section, but for this nozzle it _does not reach $M=1$ at the throat_. If the flow does not reach sonic velocity at the throat, the diverging section acts as a diffuser according to Eq. {eq}`area-velocity-relation`, and the flow is subsonic throughout.

Next, imagine that we continue to reduce the pressure ratio. Eventually, the pressure ratio will be at some value such that the sonic velocity is reached in the throat. However, the static pressure at the throat, given by Eq. {eq}`p-star-over-p-t`, is lower than the static pressure at the exit. Therefore, the diverging section must act as a diffuser and increase the pressure until the outlet.

This second case is shown in the figure below.

```{code-cell}
:tags: [remove-input]
gamma = 1.4
opts["plot_height"] = 300
p6 = figure(
    title=f"Convergent-Divergent Nozzle, Isentropic Subsonic Flow, 𝛾={gamma}",
    y_range=(-4.1, 4.1),
    **opts
)
p6.outline_line_width = 0
p6.axis.visible = False
p6.xaxis.major_tick_line_color = None
p6.xaxis.minor_tick_line_color = None
p6.xaxis.ticker = [0.0]
p6.ygrid.grid_line_color = None
p6.xaxis.major_label_overrides = {0: "Throat"}

p6.line(x, y)
p6.line(x, -y)

M_downstream_sub = optimize.root(
    area_ratio,
    x0=np.linspace(0.01, 0.001, x_downstream.shape[0] + x_bell.shape[0]),
    args=(A_ratio[x_upstream.shape[0]:])
)

M_sub = np.hstack((M_upstream.x, M_downstream_sub.x))

p7 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0, 2.1),
    x_range=p6.x_range,
    **opts
)
p7.outline_line_width = 0
p7.xaxis.major_tick_line_color = None
p7.xaxis.minor_tick_line_color = None
p7.xaxis.major_label_text_color = None
p7.xaxis.ticker = [0.0]
p7.yaxis.ticker = [1.0]
p7.line(x, M_sub)

p_ratio_sub = (1 + (gamma - 1)/2 * M_sub**2)**(-gamma/(gamma - 1))
p8 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="p/p_t",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    y_range=(0, 1.1),
    x_range=p6.x_range,
    **opts
)
p8.outline_line_width = 0
p8.xaxis.major_tick_line_color = None
p8.xaxis.minor_tick_line_color = None
p8.xaxis.major_label_text_color = None
p8.xaxis.ticker = [0.0]
p8.yaxis.ticker = [1.0, (2 / (gamma + 1))**(gamma / (gamma - 1))]
p8.line(x, p_ratio_sub)

show(column(p6, p7, p8))
```

Notice that the Mach number reaches exactly 1.0 at the throat, and the static pressure reaches the value specified by Eq. {eq}`p-star-over-p-t` at the throat. For this particular nozzle, the required pressure ratio to reach sonic flow at the throat is very close to one, approximately $p_e/p_t = 0.997$. The larger the expansion ratio from throat to exit, the smaller the required pressure difference to produce sonic flow at the throat.

We can calculate the mass flow rate in the nozzle from the continuity equation. It is most convenient to calculate the mass flow rate at the throat:

```{math}
\dot{m} = \rho^* A^* V^* = \rho^* A^* a^*
```

Now imagine reducing the exit pressure of the nozzle below the value required to obtain sonic flow at the throat. The pressure change is communicated to the rest of the flow by pressure waves that travel at the speed of sound. When the flow reaches the sonic velocity at the throat, downstream pressure changes can no longer be communicated through the throat into the converging section.

Therefore, once sonic flow is reached at the throat, the flow conditions, including the pressure, density, and temperature are fixed no matter what the exit pressure is. Likewise, the conditions in the converging section are fixed (assuming the stagnation conditions are fixed).

From the continuity equation, we see that this results in the mass flow rate becoming constant, regardless of downstream pressure changes! This condition is called **choked flow**. Under this condition, the only way to change the mass flow rate is to change the upstream conditions in the combustion chamber.

Nonetheless, we can continue to change the exit static pressure, for instance, if the nozzle is attached to a rocket ascending through the atmosphere. What happens to the flow in the nozzle in this case?

Remember that the pressure of the flow exiting the nozzle must eventually come to equilibrium with the surrounding pressure. As we change the surrounding pressure, these changes are communicated into the nozzle by sound waves. Once the flow is sonic at the throat, the changes are only communicated partway through the nozzle.

At some location in the nozzle, the velocity of the flow balances the upstream motion of the sound waves. At that location, which depends on the pressure ratio, the sound waves coalesce into a [**normal shock wave**](https://en.wikipedia.org/wiki/Shock_wave#Normal_shocks). A shock wave is an infinitesimally thin region where the flow undergoes an **irreversible** process.

Across the shock wave, the static pressure and temperature are _increased_ and the Mach number is _decreased_ to a subsonic value. The irreversible nature of the process means that the total pressure is _decreased_ and the value of $A^*$ changes across the shock wave as well.

Since the shock wave reduces the Mach number to subsonic values, the remainder of the diverging section downstream of the shock wave functions as a diffuser. This increases the static pressure further until it matches the conditions outside of the exit. An example of this situation is shown in the figure below.

```{code-cell}
:tags: [remove-input]

from bokeh.models import ColumnDataSource, CustomJS, Slider, Dropdown

shock_location = 4
shock_areas = A_ratio[(x >= 0)]
shock_location_idx = np.argmin(np.abs(shock_areas - shock_location)) + len(x[x < 0])
x_shock_loc = x[shock_location_idx]
y_shock_loc = y[shock_location_idx]

source = ColumnDataSource(data=dict(x=[x_shock_loc, x_shock_loc], y=[y_shock_loc, -y_shock_loc]))
nozzle = ColumnDataSource(data=dict(x=x[(x >= 0)].tolist(), y=y[(x >= 0)].tolist(), A=shock_areas.tolist()))
callback = CustomJS(args=dict(source=source,nozzle=nozzle), code="""
    var data = source.data;
    var noz = nozzle.data;
    var nozzle_x = noz['x'];
    var nozzle_y = noz['y'];
    var nozzle_A = noz['A'];
    var f = parseFloat(cb_obj.value);
    var x = data['x'];
    var y = data['y'];
    var val = 1e10;
    var min_i = 0;
    for (var i = 0; i < nozzle_A.length; i++) {
        if (Math.abs(f - nozzle_A[i]) <= val) {
            min_i = i;
            val = Math.abs(f - nozzle_A[i]);
        }
    }
    x[0] = nozzle_x[min_i];
    x[1] = nozzle_x[min_i];
    y[0] = nozzle_y[min_i];
    y[1] = -nozzle_y[min_i];
    source.change.emit();
""")
widget = Slider(start=0.1, end=9, value=shock_location, step=1e-4, title="Shock Location")
widget.js_on_change('value', callback)

p9 = figure(
    title=f"Convergent-Divergent Nozzle, Isentropic Subsonic Flow, 𝛾={gamma}",
    y_range=(-4.1, 4.1),
    **opts
)
p9.outline_line_width = 0
p9.axis.visible = False
p9.xaxis.major_tick_line_color = None
p9.xaxis.minor_tick_line_color = None
p9.xaxis.ticker = [0.0]
p9.ygrid.grid_line_color = None
p9.xaxis.major_label_overrides = {0: "Throat"}

p9.line(x, y)
p9.line(x, -y)
p9.line("x", "y", source=source, line_width=4)

p10 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0, 4.1),
    x_range=p9.x_range,
    **opts
)
p10.outline_line_width = 0
p10.xaxis.major_tick_line_color = None
p10.xaxis.minor_tick_line_color = None
p10.xaxis.major_label_text_color = None
p10.xaxis.ticker = [0.0]
p10.yaxis.ticker = [1.0]

shock_upstream_mask = (A_ratio < shock_location) | (x < 0)
shock_downstream_mask = (A_ratio > shock_location) & (x > 0)

# From compressible flow calculator
# Calculate M_1 from A_shock/A^* = shock_location
# Calculate M_2 from normal shock at M_1
# Calculate A2_A2star from M_2
A2_A2star = 1.38259004
Ae_A2star = epsilon / shock_location * A2_A2star

new_A_ratio = y[shock_downstream_mask]**2 * Ae_A2star / (r_e**2)

M_downstream_shock = np.array([optimize.brentq(area_ratio, 0.01, 0.99, args=(A,)) for A in new_A_ratio])
M_shock = np.hstack((M_sup[shock_upstream_mask], M_downstream_shock))
p10.line(x, M_shock, legend_label="Shock in Nozzle", color=next(colors))
p10.line(x, M_sub, legend_label="Isentropic Deceleration", color=next(colors))
p10.line(x, M_sup, legend_label="Isentropic Acceleration", color=next(colors))
p10.legend.location = "center_right"

# Calculate p_t2/p_t1 from normal shock at M_1
pt2_pt1 = 0.34564750
# p_2/p_t1 = p_2/p_t2 * p_t2/p_t1
p_ratio_downstream_shock = (1 + (gamma - 1)/2 * M_downstream_shock**2)**(-gamma/(gamma - 1)) * pt2_pt1
p_ratio_shock = np.hstack((p_ratio_sup[shock_upstream_mask], p_ratio_downstream_shock))

colors = itertools.cycle(palette[10])
p11 = figure(
    y_axis_label="p/p_t",
    # y_axis_type="log",
    y_range=(0, 1.1),
    x_range=p9.x_range,
    **opts
)
p11.outline_line_width = 0
p11.xaxis.major_tick_line_color = None
p11.xaxis.minor_tick_line_color = None
p11.xaxis.major_label_text_color = None
p11.xaxis.ticker = [0.0]
p11.yaxis.ticker = [1.0, (2 / (gamma + 1))**(gamma / (gamma - 1))]
p11.line(x, p_ratio_shock, legend_label="Shock in Nozzle", color=next(colors))
p11.line(x, p_ratio_sub, legend_label="Isentropic Deceleration", color=next(colors))
p11.line(x, p_ratio_sup, legend_label="Isentropic Acceleration", color=next(colors))
p11.legend.location = "center_right"

# show(column(widget, p9, p10, p11))
show(column(p9, p10, p11))
```

This condition of the nozzle is called **overexpanded** because the flow in the nozzle expands to a pressure below the outside pressure, and requires a shock wave to increase the pressure. If you could cut off the nozzle just upstream of the shock wave, you would have a perfectly expanded nozzle. However, since the nozzle is longer than that, the flow tries to continue expanding and can't.

As the downstream pressure decreases further, the shock moves further and further downstream. Eventually, the normal shock will stand exactly at the exit. The pressure ratio that produces this situation is still larger than the pressure ratio that gives isentropic acceleration throughout the nozzle.

Thus, we can still continue reducing the outside pressure and there will continue to be an irreversible shock that is required to adjust the exit pressure to the outside pressure. When the outside pressure is lower than the pressure that gives a normal shock at the exit, the shock will become angled into an [**oblique shock**](https://en.wikipedia.org/wiki/Oblique_shock).

Oblique shock waves cause the flow to turn, which then requires a [**Prandtl-Meyer expansion fan**](https://en.wikipedia.org/wiki/Prandtl%E2%80%93Meyer_expansion_fan) to turn back to the direction of flight. This pattern repeats in a phenomenon called a [**shock diamond**](https://en.wikipedia.org/wiki/Shock_diamond).

```{figure} ../images/Lockheed_Martin_F-22A_Raptor_JSOH.jpg
---
width: 75%
align: center
---
F-22A Raptor fighter jet with shock diamonds visible in the engine exhaust. Credit: [Wikimedia](https://commons.wikimedia.org/wiki/File:Lockheed_Martin_F-22A_Raptor_JSOH.jpg) under the [CC-BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) license.
```

Finally, continued reduction of the exterior pressure will result in the ratio $p_e/p_t$ dropping below the value for isentropic acceleration. In this case, the flow is called **underexpanded** because the pressure of the flow at the exit plane is higher than the exterior pressure, and it could have been expanded more to match the outside pressure.

To match the exterior pressure, the flow must exit the nozzle through a series of expansion waves to reduce the pressure. These expansion waves turn the flow and to straighten the flow again requires oblique shock waves. Thus, the pattern for underexpanded flow is the same as for overexpanded flow, but it starts with the expansion wave instead of the shock wave.

## Design of Rocket Nozzles

We will now investigate the major factors influencing the design of a rocket nozzle and how to analyze the performance of a given nozzle. To help understand the qualitative behavior of design changes and the inherent tradeoffs, we would like to reduce the problem to an analysis of dimensionless parameters.

### Nozzle Shapes

The flow upstream of the nozzle throat is constant when the flow reaches the sonic velocity at the throat, independent of any downstream changes. Therefore, the nozzle exit conditions are primarily determined by the shape of the nozzle after the throat.

In designing a nozzle, we have two primary goals:

1. Produce a high-velocity flow parallel to the nozzle axis
2. Have as low a weight as possible

Since the nozzle is essentially a thin shell, the weight is proportional to the nozzle surface area. Therefore, minimizing the surface area will give the lowest weight. In addition, a smaller surface area will reduce the effects of frictional drag on the surface and heat loading.

#### Conical Nozzle

The simplest possible design of a nozzle is a [frustum](https://en.wikipedia.org/wiki/Frustum) of a cone. The parameters of the cone are shown in Fig. {numref}`conical-nozzle`.

```{figure} ../images/conical-nozzle.svg
:name: conical-nozzle

A conical nozzle
```

The expansion angle of the cone is determined from the throat radius $r_{\text{th}}$, the exit radius $r_e$ and the length $L$ by:

```{math}
:label: conical-expansion-angle
\alpha = \arctan\left(\frac{r_e - r_{\text{th}}}{L}\right)
```

The **area expansion ratio** is a useful parameter to characterize the nozzle flow:

```{math}
:label: area-expansion-ratio
\varepsilon = \frac{A_e}{A_{\text{th}}} = \frac{r_e^2}{r_{\text{th}}^2}
```

Then we can determine the surface area of the conical frustum:

```{math}
:label: conical-nozzle-surface-area
S = \pi r_e L \left(1 + \frac{1}{\sqrt{\varepsilon}}\right)\sqrt{1 + \left(\frac{r_e}{L}\right)^2\left(1 - \frac{1}{\sqrt{\varepsilon}}\right)^2}
```

Note that the surface area, and thus the weight, is directly proportional to the length of the nozzle. Thus, most of nozzle design is to create the shortest possible nozzle with the highest exit velocity.

The maximum thrust will be produced when the exit pressure equals the ambient pressure. In this situation the thrust is given by:

```{math}
F = \dot{m} \vector{V}_e\cdot\hat{n}
```

where $\hat{n}$ is the surface normal vector to the exit plane. If the flow were parallel to the exit plane, the dot product of the velocity and surface normal would give the magnitude of the exit velocity. However, the angle of the streamlines relative to the centerline in a conical flow varies from 0° at the center line to $\alpha$ at the wall.

If we take a differential area on the exit plane, the differential force is given by:

```{math}
dF = \left(V_e \cos\sigma\right)d\dot{m}
```

where $\sigma$ is the angle from the centerline to the differential area. The differential mass flow rate over the same area is given by:

```{math}
d\dot{m} = \rho_e V_e \left(2\pi \frac{L^2}{\cos^2\alpha}\sin\sigma d\sigma\right)
```

where $d\sigma$ is the angular span of the differential area. The mass flow rate can be found by integrating $\sigma$ from 0 to $\alpha$:

```{math}
:label: conical-mass-flow
\dot{m} = 2\pi \rho_e V_e \frac{L^2}{\cos^2\alpha}\left(1 - \cos\alpha\right)
```

and the force can be found similarly:

```{math}
:label: conical-nozzle-thrust
F = \pi\rho_e V_e^2 \frac{L^2}{\cos^2\alpha}\sin^2\alpha
```

Combining Eqs. {eq}`conical-mass-flow` and {eq}`conical-nozzle-thrust`, we find:

```{math}
:label: corrected-thrust-equation
F = \lambda \dot{m} V_e
```

where $\lambda$ is a correction factor that accounts for the angle of the exhaust flow:

```{math}
:label: thrust-velocity-correction
\lambda = \frac{1}{2} \frac{\sin^2\alpha}{1 - \cos\alpha} = \frac{1 + \cos\alpha}{2}
```

For an expansion angle of 10°, the thrust loss is about 1% while for 20° it is about 3%. Typical conical nozzles have expansion angles of about 15°. Keep in mind the scale of these nozzles. 1% sounds like small loss, until you're talking about hundreds-of-thousands of pounds of thrust, and then a 1% loss can make a big difference in the payload capacity.

#### Bell Nozzles

Conical nozzles have the advantage of being very simple to analyze and build. However, they inherently suffer from thrust loss due to the angularity of the flow. In addition, achieving large area ratios to accelerate the flow requires a long nozzle length, which makes conical nozzles heavy.

To overcome these problems, and achieve parallel flow at the exit in a shorter distance, we can design a reflexive nozzle profile. This nozzle has a rapid expansion immediately after the throat followed by a slower expansion to give nearly parallel flow at the exit, $\alpha\approx 0$. The rapid expansion permits a shorter nozzle and the slow expansion turns the flow while avoiding oblique shock waves.

This kind of nozzle is called a **bell nozzle** due to the shape it takes on.

### Choked Mass Flow Rate

We showed in the last section that the choked mass flow rate is the maximum mass flow rate that a nozzle can pass. In terms of the nozzle and flow properties, we can write the maximum mass flow rate from Eq. {eq}`mass-flow-rate-mach-number` by setting $M = M^* = 1$:

```{math}
:label: choked-mass-flow-rate
\dot{m}_{\text{max}} = \dot{m}^* = \frac{p_c}{\sqrt{T_c}} A_{\text{th}} \sqrt{\frac{\gamma}{R}} \left(\frac{\gamma + 1}{2}\right)^{\frac{-\left(\gamma + 1\right)}{2\left(\gamma - 1\right)}}
```

where $p_c$ and $T_c$ are the combustion chamber pressure and temperature, assumed to be the stagnation conditions, and $A_{\text{th}} = A^*$ is the throat area.

From Eq. {eq}`choked-mass-flow-rate`, we have 5 terms that we can adjust to change the mass flow rate:

1. $p_c$
2. $T_c$
3. $\gamma$
4. $R = R_u/W$
5. $A_{\text{th}}$

The combustion chamber pressure is essentially determined by the design of the pumps supplying propellant to the combustion chamber and by material considerations in the combustion chamber to avoid stress failures. Furthermore, the combustion chamber temperature, the ratio of specific heats, and the specific gas constant are essentially determined by the identity of the propellants.

Note that increasing the chamber pressure, throat area, ratio of specific heats, or the molecular weight, or reducing the chamber temperature will give a higher mass flow rate.

In addition, we can estimate the design mass flow rate by the design of the propellant pumps and the volume of propellant carried on board the rocket. With these parameters all determined, the throat area of the nozzle is fixed.
