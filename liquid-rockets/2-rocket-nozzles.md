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

### Critical Properties

Ch. 3.4, Anderson to define the * conditions. Then Ch. 5 to get to the area relationship based on the momentum equation (which might need to go somewhere?).

Let's now consider a simple nozzle with varying cross-sectional area. We will neglect the influence of skin friction and heat transfer at the nozzle wall, so that the only way that the flow may change is due to the area change. In this nozzle, the flow is adiabatic and reversible, so the entropy is constant.

## Mass Conservation

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
