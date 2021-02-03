# Rocket Nozzles

The nozzle is the most important component of the rocket engine. The nozzle converts high pressure, and ideally high temperature, gases into low pressure gases with much higher velocity by changing the cross-sectional area of the flow. This momentum transfer then provides the thrust force on the spacecraft.

In principle, nozzles can function with any source of high pressure fluid upstream. As we'll see, the higher the upstream pressure and temperature, the higher the performance of the nozzle. However, this ability to be very flexible and still provide thrust is why nozzles are the most important component.

For most purposes, we will assume the upstream flow is at **nearly zero velocity**. This means that the upstream temperature and pressure are at the **stagnation** conditions, which is a very important state for the analysis of nozzles.

## Stagnation State

For flowing fluids, we define two conditions at which we can evaluate properties:

1. **Static**: What you would measure if you moved along with the flow
2. **Stagnation**: What you would measure if you slowed the fluid to a stop in an adiabatic and reversible (isentropic) process. Also known as the **total** state, with the subscript $t$.

When the fluid is stationary, the static and stagnation properties are equal, by definition. The objective of the nozzle is to produce high velocity flow at the exit using the high stagnation pressure and temperature upstream of the nozzle.

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

The speed of sound is given by the differential:

```{math}
:label: speed-of-sound-differential
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

Note that this differential is specifically and only for an isentropic process, but it meets the definition of the speed of sound earlier. Plugging in Eq. {eq}`ideal-gas-law`, we find:

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

(relations-for-compressible-flow)=
## Relations for Compressible Flow

The flow through rocket nozzles is compressible in general. It will be convenient to relate the static and stagnation properties to each other and to the Mach number. In all of the following equations, we will assume that the process is isentropic.

First, we imagine a process which isentropically slows the flow from the current velocity, where the static pressure is $p$, to a stop, where the static pressure is equal to the total pressure, $p_t$. Likewise, the temperature changes from the static temperature $T$ to the total temperature $T_t$ as a result of this process. Then, the ratio of these properties is given by:

```{math}
:label: p-T-isentropic
\frac{T_t}{T} = \left(\frac{p_t}{p}\right)^{(\gamma - 1)/\gamma}
```

Similarly, the temperature and pressure ratios can be related to the density ratio:

```{math}
:label: rho-p-T-isentropic
\frac{\rho_t}{\rho} = \left(\frac{T_t}{T}\right)^{1/\gamma} = \left(\frac{p_t}{p}\right)^{1/n}
```

The definition of the enthalpy is:

```{math}
:label: enthalpy
h = c_p T
```

where $h$ is the enthalpy. Then, the conservation of energy for this flow is given by:

```{math}
h_t + V_{t}^2/2 = h + V^2/2
```

where $V_{t}$ is zero by definition. Plugging in Eqs. {eq}`enthalpy`, {eq}`mach-number`, and {eq}`speed-of-sound`, we find:

```{math}
:label: isentropic-temperature-mach
\frac{T_t}{T} = 1 + \frac{\gamma - 1}{2}M^2
```

Using Eqs. {eq}`p-T-isentropic` and {eq}`rho-p-T-isentropic`, we can also find:

```{math}
:label: isentropic-pressure-mach
\frac{p_t}{p} = \left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{\gamma}{\gamma - 1}}
```

and

```{math}
:label: isentropic-density-mach
\frac{\rho_t}{\rho} = \left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{1}{\gamma - 1}}
```

## Mass Conservation

In steady flow, the mass flow rate is given by the integral relationship:

```{math}
\int \rho \left(\vec{V}\cdot\hat{n}\right) dA = 0
```

If we further simplify to quasi-one-dimensional flow, and define the $z$ axis as the flow direction, then the mass flow rate is:

```{math}
:label: one-d-mass-flow-rate
\dot{m}(z) = \rho{z} A(z) V(z)
```

where $\dot{m}(z)$ may change as a function of the axial coordinate due to changes in density, area, or velocity. In differential form, this becomes:

```{math}
:label: mass-flow-rate-differential
\frac{d\dot{m}}{\dot{m}} = \frac{d\rho}{\rho} + \frac{dV}{V} + \frac{dA}{A} = 0
```

At a given flow station, or $z$ location, the mass flow rate can be related to the local flow conditions by:

```{math}
\dot{m} = p A M\sqrt{\frac{\gamma}{R T}}
```

where $R = R_u / W$. Using the results from {ref}`relations-for-compressible-flow`, we can write the mass flow rate as:

```{math}
:label: mass-flow-rate-mach-number
\dot{m} = \frac{p_t A}{\sqrt{T_t}}\sqrt{\frac{\gamma}{R}}M\left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{-\left(\gamma + 1\right)}{2\left(\gamma - 1\right)}}
```
