# The Mach Number

As we alluded to in the introduction to this chapter, the **Mach number** plays a critical role in the behavior of compressible flows. In this section, we define the Mach number and relate it to the static and stagnation property ratios.

## Speed of Sound

The speed of sound is the speed at which an infinitesimal pressure disturbance propagates through a fluid. The disturbance is of such a small magnitude that the process that the gas goes through is reversible, and the process is adiabatic. Therefore, sound waves are isentropic processes.

The speed of sound is defined by the differential:

```{math}
:label: speed-of-sound-definition
a^2 = \left(\frac{\partial p}{\partial \rho}\right)_{s}
```

where $a$ is the speed of sound and the subscript $s$ indicates the partial derivative is to be taken for a constant entropy process.

The entropy of the ideal gas can be determined from the second Gibbs relation (modified here from Eq. {eq}`gibbs-relations`):

```{math}
:label: second-gibbs
ds = c_p \frac{dT}{T} - \frac{dp}{\rho T}
```

Introducing Eq. {eq}`ideal-gas-differential`, we find:

```{math}
:label: entropy-differential
\frac{ds}{c_v} = \frac{dp}{p} - \gamma \frac{d\rho}{\rho} + \gamma \frac{dW}{W}
```

If we assume the change in molecular weight is zero, and the process is isentropic, then we can relate the pressure to the density using Eq. {eq}`entropy-differential`:

```{math}
\frac{dp}{p} = \gamma \frac{d\rho}{\rho}
```

or, rearranging:

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
