# Properties of Compressible Flow

In this section, we introduce the idea of **static** and **stagnation** properties, as well as equations to determine how the properties are related to each other.

## Stagnation State

For flowing fluids, we define two conditions at which we can evaluate properties:

1. **Static**: What you would measure if you moved along with the flow
2. **Stagnation**: What you would measure if you slowed the fluid to a stop in an adiabatic and reversible (isentropic) process. Also known as the **total** state, with the subscript $t$.

For most purposes, we will assume the fluid upstream of the nozzle inlet is at **nearly zero velocity**. This means that the upstream temperature and pressure are at the **stagnation** conditions, which is a very important state for the analysis of nozzles.

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

## Caloric Equations of State

The ideal gas law gives the relationship among $p$, $\rho$, and $T$ for an ideal gas. In addition to these properties, we need definitions of the internal energy, enthalpy, and entropy of the flow.

In an ideal gas, the internal energy, $u$, and the enthalpy, $h = u + pv$, are functions of temperature and composition only.

We define three other properties, which are also functions of temperature and composition only:

1. **Specific heat at constant pressure**: $c_p = dh/dT$
2. **Specific heat at constant volume**: $c_v = du/dT$
3. **Ratio of specific heats**: $\gamma = c_p/c_v$

The specific heats represent the amount of energy/enthalpy input required to change the temperature of the gas by one degree. Using these definitions, we can determine the change in enthalpy:

```{math}
:label: ideal-gas-delta-h
dh = c_p dT \quad \Rightarrow \quad \int_{h_1}^{h_2} dh = \int_{T_1}^{T_2} c_p dT \quad \Rightarrow \quad \Delta h = c_p \Delta T
```

where the last equation assumes _constant specific heat_. As a shortcut, we will often assume that $T_1 = h_1 = 0$ and write:

```{math}
h = c_p T
```

Similarly, we can write the change in internal energy:

```{math}
:label: ideal-gas-delta-u
du = c_v dT \quad \Rightarrow \quad \int_{u_1}^{u_2} du = \int_{T_1}^{T_2} c_v dT \quad \Rightarrow \quad \Delta u = c_v \Delta T
```

where the last equation assumes _constant specific heat_. As a shortcut, we will often assume that $T_1 = u_1 = 0$ and write:

```{math}
u = c_v T
```

````{attention}
**Note**: The _constant pressure_ or _constant volume_ in the name of the specific heats has absolutely nothing to do with the types of processes to which the properties can be applied. It is an artifact of the definition of the specific heats. If you want the gory details, expand the box below.

```{dropdown}
For a general substance, the enthalpy and internal energy are functions of _two_ independent, intensive properties, plus the composition. Therefore, the specific heats must be defined by **partial derivatives**. For example, the enthalpy of a pure substance (constant composition) is a natural function of $T$ and $p$, $h = h(T, p)$. To calculate the total derivative of $h$, we must take the partial derivative with respect to both properties:

```{math}
dh = \left(\frac{\partial h}{\partial T}\right)_{p} dT + \left(\frac{\partial h}{\partial p}\right)_{T} dp
```

where the subscript $p$ or $T$ indicates that the derivative is taken while mathematically holding that property constant.
```
````

For an ideal gas, the specific heats are related to the specific gas constant:

```{math}
:label: cp-cv-R
c_p - c_v = \frac{R_u}{W} = R
```

Equation {eq}`cp-cv-R` shows that $c_p > c_v$ and therefore that $\gamma > 1.0$. It also allows us to determine a value for $c_p$ or $c_v$ given $\gamma$:

```{math}
\begin{aligned}
c_p &= \frac{\gamma R}{\gamma - 1} & c_v &= \frac{R}{\gamma - 1}
\end{aligned}
```

Finally, the entropy is defined from the Gibbs relations:

```{math}
:label: gibbs-relations
\begin{aligned}
T ds &= du + p dv & T ds &= dh - v dp
\end{aligned}
```

Integrating these relationships, we find:

```{math}
:label: entropy
\Delta s = \int_{T_1}^{T_2} c_v \frac{dT}{T} + R \ln\frac{\rho_1}{\rho_2} = \int_{T_1}^{T_2} c_p \frac{dT}{T} - R \ln\frac{p_2}{p_1}
```

and for constant specific heats:

```{math}
:label: constant-specific-heat-entropy
\Delta s = c_v \ln\frac{T_2}{T_1} + R \ln\frac{\rho_1}{\rho_2} = c_p \ln\frac{T_2}{T_1} - R \ln\frac{p_2}{p_1}
```

## Static and Stagnation Property Ratios

First, we imagine a process which isentropically slows the flow from the current velocity, where the static pressure is $p$, to a stop, where the static pressure is equal to the total pressure, $p_t$. Likewise, the temperature changes from the static temperature $T$ to the total temperature $T_t$ as a result of this process and the density changes from the static density $\rho$ to the total density $\rho_t$.

For any isentropic process of an ideal gas with constant specific heats, we can use Eq. {eq}`constant-specific-heat-entropy` to show that the pressure and density have the following relationship {cite}`Hall2018`:

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
