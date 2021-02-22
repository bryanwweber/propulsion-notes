# Design of Rocket Nozzles

The nozzle is the most important component of the rocket engine. The nozzle converts high pressure, and ideally high temperature, gases into low pressure gases with much higher velocity by changing the cross-sectional area of the flow. This momentum transfer then provides the thrust force on the spacecraft.

In principle, nozzles can function with any source of high pressure fluid upstream. As we'll see, the higher the upstream pressure and temperature, the higher the performance of the nozzle. However, this ability to be very flexible and still provide thrust is why nozzles are the most important component.

Nearly all rocket nozzles are of the **converging-diverging** type. This means that the flow at the exit of the nozzle is supersonic and it must be treated using compressible flow relations. These equations are derived in a {ref}`separate chapter all about compressible flow <compressible-flow-introduction>`.

We will now investigate the major factors influencing the design of a rocket nozzle and how to analyze the performance of a given nozzle. To help understand the qualitative behavior of design changes and the inherent tradeoffs, we would like to reduce the problem to an analysis of dimensionless parameters. First, we will discuss the various shape of nozzle designs before returning to some equations.

## Nozzle Shapes

The flow properties upstream of the nozzle throat are fixed when the flow reaches the sonic velocity at the throat, independent of any downstream changes. Therefore, the nozzle exit conditions are primarily determined by the shape of the nozzle after the throat.

In designing a nozzle, we have two primary goals:

1. Produce a high-velocity flow parallel to the nozzle axis
2. Have as low a weight as possible

Since the nozzle is essentially a thin shell, the weight is proportional to the nozzle surface area. Therefore, minimizing the surface area will give the lowest weight. In addition, a smaller surface area will reduce the effects of frictional drag on the surface and heat loading. Thus, the primary goal of a rocket nozzle is to have the optimal area expansion in the smallest length, without introducing irreversibilities.

### Conical Nozzle

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

For instance, the sea-level thrust of the [Falcon 9 Full Thrust model](https://en.wikipedia.org/wiki/Falcon_9_Full_Thrust) is approximately 1.71 million pounds of thrust and its payload capacity is approximately 50,000 pounds. A 1% reduction in the thrust would lead to a loss of 17,100 pounds of thrust, on the same order of magnitude as the payload mass!

### Bell Nozzles

Conical nozzles have the advantage of being very simple to analyze and build. However, they inherently suffer from thrust loss due to the angularity of the flow. In addition, achieving large area ratios to accelerate the flow requires a long nozzle length, which makes conical nozzles heavy.

To overcome these problems, and achieve parallel flow at the exit in a shorter distance, we can design a reflexive nozzle profile. This nozzle has a rapid expansion immediately after the throat followed by a slower expansion to give nearly parallel flow at the exit, $\alpha\approx 0$. The rapid expansion permits a shorter nozzle and the slow expansion turns the flow while avoiding oblique shock waves.

This kind of nozzle is called a **bell nozzle**, because the rapid expansion and slow turn look like a bell. The bell nozzle is shown schematically in {numref}`rocket-engine`, repeated here for reference.

```{image} ../images/rocket-engine.svg
```

The design of bell nozzles has been well studied since the middle of the 20th century. G.V.R. Rao {cite}`Rao1958,Rao1961` developed a methodology to optimize the thrust from bell nozzles that results in nozzles about 75% the length of conical nozzles with the same $A_e/A_{\text{th}}$ ratio.

### Plug Nozzles

In an effort to further reduce the nozzle length, several alternative designs have been developed although not applied in practice. The primary of these alternatives is called the **plug nozzle**.

In a plug nozzle, the diverging section is removed and a plug is placed into the center of the converging section. The plug extends past the end of the converging section. The flow reaches sonic velocity at the end of the converging section and continues expanding after leaving the converging section due to the shape of the plug.

The advantage of plug nozzles is that they are less sensitive to the ambient pressure. Bell nozzles are very sensitive to the ambient pressure; as we saw, off-design pressure ratios can lead to shock wave formation, which results in a loss of thrust.

The disadvantage of plug nozzles is that they are more difficult to manufacture, which is probably why they haven't been put into practice.

### Extendable Nozzles

One final design that has been proposed to alleviate problems with ambient pressure changes is an [extendable nozzle](https://en.wikipedia.org/wiki/Expanding_nozzle). Lower ambient pressures require a longer nozzle to avoid underexpansion. The diverging portion of a bell nozzle is split into two pieces, and the lower piece is able to move in the axial direction. At high altitudes, the lower portion is moved into place mechanically to extend the nozzle.

An extendable nozzle was proposed for the Space Shuttle, but scrapped due to cost considerations.

## Nozzle Design Equations

The thrust from a rocket nozzle is ideally given by Eq. {eq}`rocket-momentum`. This assumes that the exit pressure is matched to the ambient pressure. If the pressures do not match, we must add an additional term to the thrust equation to account for the pressure difference:

```{math}
:label: rocket-thrust
F = \dot{m} V_e + A_e \left(p_e - p_0\right)
```

As we can see in Eq. {eq}`rocket-thrust`, there are two primary terms that make up the thrust:

1. **Momentum thrust**: $\dot{m} V_e$ is due to the change in momentum of the fluid
2. **Pressure thrust**: $A_e \left(p_e - p_0\right)$ is due to the pressure difference from the ambient

We note that the mass flow rate for a converging-diverging nozzle is fixed at the choked flow value, so only the exit velocity can be changed by changing the downstream conditions. When the exit pressure is larger than the ambient pressure, the pressure thrust is positive but the exit velocity and the momentum thrust are low. When the exit pressure is less than the ambient pressure, the pressure thrust is negative but the exit velocity and momentum thrust are high. Since momentum thrust and pressure thrust are inversely proportional, the maximum total thrust occurs when the nozzle is perfectly expanded, $p_e = p_0$.

## Nozzle Mass Flow Rate

We showed in the {ref}`nozzle flow section <choked-mass-flow-rate>` that the choked mass flow rate is the ideal maximum mass flow rate that a nozzle can pass. In terms of the nozzle and flow properties, we can write the maximum mass flow rate from Eq. {eq}`mass-flow-rate-mach-number` by setting $M = M^* = 1$:

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

## Nozzle Discharge Coefficient

Now we would like to characterize the performance of a real nozzle relative to the ideal case. In the ideal flow, we assume quasi-1-dimensional, steady, isentropic, constant-specific-heat-ratio and constant-composition flow. In a real flow, the flow may be 3-dimensional, unsteady, non-isentropic, and have varying specific heat ratio and composition.

To characterize the performance of the real nozzle, we define the **nozzle discharge coefficient**:

```{math}
c_d = \frac{\dot{m}}{\dot{m}_i}
```

where $\dot{m}$ is the real mass flow rate and $\dot{m}_i$ is the ideal mass flow rate. In general, the actual mass flow rate can be measured from flow meters on the propellant pumps. In addition, the combustion chamber pressure and the throat area can be easily measured, so that we can define a **mass flow rate coefficient**:

```{math}
:label: nozzle-mass-flow-rate-coefficient
c_m = \frac{\dot{m}}{p_c A_{\text{th}}}
```

Equation {eq}`nozzle-mass-flow-rate-coefficient` says that the mass flow rate is directly proportional to the chamber pressure and throat area, with the proportionality constant depending on factors such as the chamber temperature and combustion products. The dimensions of $c_m$ are inverse velocity.

The ideal mass flow rate is given by Eq. {eq}`choked-mass-flow-rate`, which can be rearranged to be:

```{math}
:label: ideal-nozzle-mass-flow-rate
\dot{m}_i = \frac{p_c A_{\text{th}}}{\frac{1}{\Gamma_c}\sqrt{\frac{R_u T_c}{W_c}}}
```

where $p_c$, $T_c$, and $W_c$ are the pressure, temperature, and molecular weight in the combustion chamber, and $\Gamma_c$ is a combination term involving the (constant) specific heat ratio:

```{math}
\Gamma_c = \sqrt{\gamma_c}\left(\frac{2}{\gamma_c + 1}\right)^{\frac{\gamma_c + 1}{2\left(\gamma_c - 1\right)}}
```

where $\gamma_c$ is the specific heat ratio in the combustion chamber. The bottom of the fraction in Eq. {eq}`ideal-nozzle-mass-flow-rate` has dimensions of velocity, so it can be used to define a **characteristic velocity** of the nozzle:

```{math}
:label: nozzle-characteristic-velocity
c^* = \frac{1}{\Gamma_c}\sqrt{\frac{R_u T_c}{W_c}}
```

This velocity characterizes the effectiveness of the combustion products to produce thrust from the nozzle. The characteristic velocity is large when $T_c$ is large, or $\gamma_c$ or $W_c$ are small.

For the case of LH2/LOX combustion, the combustion temperature is approximately 3,900 K, the products' molecular weight is approximately 13 kg/kmol, and the ratio of specific heats is approximately 1.16. This gives a characteristic velocity of about 2,500 m/s.

For the case of RP1/LOX combustion, the combustion temperature is about 3,700 K, the products' molecular weight is approximately 23 kg/kmol, and the ratio of specific heats is approximately 1.14. This gives a characteristic velocity of about 1,800 m/s.

These values give an approximate range typical of most propellants, 1,500 m/s < $c^*$ < 2,500 m/s.

With this definition of the characteristic velocity, we can rewrite the ideal mass flow rate:

```{math}
:label: ideal-mass-flow-rate-characteristic-velocity
\dot{m}_i = \frac{p_c A_{\text{th}}}{c^*}
```

Combining Eqs. {eq}`nozzle-mass-flow-rate-coefficient` and {eq}`ideal-mass-flow-rate-characteristic-velocity`, we find that the discharge coefficient becomes:

```{math}
:label: nozzle-discharge-coefficient
c_d = c_m c^*
```

In this equation, both $c_m$ and $c^*$ are essentially functions of the propellant combination, so that the discharge coefficient is mostly a function of the propellant combination.

For most nozzles, the discharge coefficient is very close to one. This means that the mass flow rate coefficient is nearly inversely proportional to the characteristic velocity. We will see later that the characteristic velocity of the nozzle can be used in other calculations, so being able to approximate it by measuring the actual mass flow rate of the nozzle, as well as the chamber pressure and throat area is very useful.

```{note}
**Note:** Interestingly, the discharge coefficient can be larger than 1! This unusual situation can occur because the actual mass flow rate is larger than the ideal case due to varying temperature, pressure, and composition in the converging portion of the nozzle.

Nonetheless, in early design stages before experimental data are available, it is reasonable to assume $c_d = 1$.
```

## Nozzle Velocity Coefficient

Measuring the true exit velocity of the combustion products from the nozzle is very difficult. Therefore, we would like to find a method to estimate the true velocity from other known information. As before, we are interested in a dimensionless coefficient that can be used to describe the velocity variation from the ideal.

We can define the isentropic efficiency of the nozzle as:

```{math}
:label: nozzle-isentropic-efficiency
\eta_n = \frac{h_c - h_e}{h_c - h_{e,i}} = \frac{V_e^2}{V_{e,i}^2}
```

where $h_c = h_t$ is the enthalpy in the combustion chamber, equal to the stagnation enthalpy, $h_e$ is the true exit enthalpy, and $h_{e,i}$ is the ideal exit enthalpy. The isentropic nozzle efficiency is restricted to be between 0 and 1, since $h_e < h_{e,i}$.

From the energy equation, the difference in the enthalpy over the nozzle is equal to the square of the change in velocity, so we can define the isentropic efficiency in terms of the velocity as well. This suggests a definition for the **nozzle velocity coefficient**:

```{math}
:label: nozzle-velocity-coefficient
c_V = \frac{V_e}{V_{e,i}} = \sqrt{\eta_n}
```

$c_V$ is also restricted to lie between 0 and 1. For well-designed nozzles, $c_V$ is typically in excess of 0.95.

Whereas $c_m$, $c^*$, and $c_d$ are related to the choice of propellant, $c_V$ is related to the design of the nozzle. The reason for this is because the isentropic efficiency is essentially determined by the increase in entropy of the flow over the nozzle. Better designed nozzles that minimize the effect of the boundary layer and avoid shock waves have smaller entropy increases, and therefore higher values of $c_V$.

### Nozzle Thrust Coefficient

We have now reached the point where we can relate both of our design variables, the choice of propellant and the design of the nozzle, to the thrust produced by the rocket. The thrust of the rocket is given by Eq. {eq}`rocket-thrust`. Using the discharge coefficient, Eq. {eq}`nozzle-discharge-coefficient`, and the velocity coefficient, Eq. {eq}`nozzle-velocity-coefficient`, we can rewrite the thrust equation in terms of the ideal exit velocity and mass flow rate:

```{math}
F = \lambda c_d c_V \dot{m}_i V_{e,i} + A_e\left(p_e - p_0\right)
```

Further plugging in for the ideal mass flow rate and ideal exit velocity, we find:

```{math}
F = \lambda c_d c_V \Gamma_c p_c A_{\text{th}} \sqrt{\frac{2\gamma_c}{\gamma_c - 1}\left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma_c - 1}{\gamma_c}}\right]} + A_e \left(p_e - p_0\right)
```

This equation can be divided by the chamber pressure and throat area to define the **nozzle thrust coefficient**:

```{math}
:label: nozzle-thrust-coefficient
c_F = \frac{F}{p_c A_{\text{th}}} = \lambda c_d c_V \Gamma_c \sqrt{\frac{2\gamma_c}{\gamma_c - 1}\left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma_c - 1}{\gamma_c}}\right]} + \frac{A_e}{A_{\text{th}}} \left(\frac{p_e}{p_c} - \frac{p_0}{p_c}\right)
```
