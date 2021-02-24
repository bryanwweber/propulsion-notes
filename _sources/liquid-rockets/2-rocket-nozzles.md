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
from bokeh.models import LinearAxis, Range1d, ColumnDataSource, Arrow, NormalHead
from bokeh.palettes import Category10 as palette
from bokeh.layouts import row

from myst_nb import glue

output_notebook(hide_banner=True)
opts = dict(plot_width=500, plot_height=400, min_border=10)
colors = itertools.cycle(palette[10])
```

# Design of Rocket Nozzles

The nozzle is the most important component of the rocket engine. The nozzle converts high pressure, and ideally high temperature, gases into low pressure gases with much higher velocity by changing the cross-sectional area of the flow. This momentum transfer then provides the thrust force on the spacecraft.

In principle, nozzles can function with any source of high pressure fluid upstream. As we'll see, the higher the upstream pressure and temperature, the higher the performance of the nozzle. However, this ability to be very flexible and still provide thrust is why nozzles are the most important component.

Nearly all rocket nozzles are of the **converging-diverging** type. This means that the flow at the exit of the nozzle is supersonic and it must be treated using compressible flow relations. These equations are derived in a {ref}`separate chapter all about compressible flow <compressible-flow-introduction>`.

We will now investigate the major factors influencing the design of a rocket nozzle and how to analyze the performance of a given nozzle. To help understand the qualitative behavior of design changes and the inherent tradeoffs, we would like to reduce the problem to an analysis of dimensionless parameters. First, we will discuss the various shape of nozzle designs before returning to some equations.

(nozzle-shapes)=
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
:label: Gamma-function
\Gamma_c = \sqrt{\gamma_c}\left(\frac{2}{\gamma_c + 1}\right)^{\frac{\gamma_c + 1}{2\left(\gamma_c - 1\right)}}
```

where $\gamma_c$ is the specific heat ratio in the combustion chamber. The bottom of the fraction in Eq. {eq}`ideal-nozzle-mass-flow-rate` has dimensions of velocity, so it can be used to define a **characteristic velocity** of the nozzle:

```{math}
:label: nozzle-characteristic-velocity
c^* = \frac{1}{\Gamma}\sqrt{\frac{R_u T_c}{W_c}} = \frac{a_c}{\Gamma \sqrt{\gamma}}
```

where $a_c$ is the speed of sound in the combustion chamber. The characteristic velocity is a figure of merit for the effectiveness of the combustion products to produce thrust from the nozzle. The characteristic velocity is large when $T_c$ is large, or $\gamma$ or $W_c$ are small.

For the case of LH2/LOX combustion, the combustion temperature is approximately 3,900 K, the products' molecular weight is approximately 13 kg/kmol, and the ratio of specific heats is approximately 1.16. This gives a characteristic velocity of about 2,500 m/s.

For the case of RP1/LOX combustion, the combustion temperature is about 3,700 K, the products' molecular weight is approximately 23 kg/kmol, and the ratio of specific heats is approximately 1.14. This gives a characteristic velocity of about 1,800 m/s.

These values give an approximate range typical of most propellants, 1,500 m/s < $c^*$ < 2,500 m/s. In a subsequent section, we will discuss the effect of propellant choice on $c^*$ more directly.

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

### Nozzle Exit Velocity

To determine the ideal nozzle exit velocity, we can apply conservation of energy across the nozzle, noting that $V_c\approx 0$:

```{math}
\frac{1}{2} V_e^2 + c_p T_e = c_p T_c
```

Solving for $V_e$ and substituting Eqs. {eq}`cp-cv-relationships` and {eq}`p-T-isentropic`, where $T_c = T_t$, we find:

```{math}
:label: ideal-exit-velocity
V_e = \sqrt{\frac{2\gamma}{\gamma - 1} \frac{R_u T_c}{W_c} \left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma - 1}{\gamma}}\right]}
```

From Eq. {eq}`ideal-exit-velocity`, we have four factors that we control to adjust the exit velocity:

1. $p_e/p_c$: This is the ratio of the nozzle exit pressure to the combustion chamber (stagnation) pressure. Decreasing this ratio will increase the exit velocity. However, since the exit pressure must equilibrate with the ambient, we do not have direct control over that parameters. We can control the combustion chamber pressure, but we are limited by the strength of the materials required for the combustion chamber.
2. $T_c$: Increasing the combustion chamber temperature will increase the exit velocity. However, it also increases the requirements for cooling in the combustor and nozzle. Systems for cooling these components will add weight to the engine, tending to offset the increased thrust.
3. $W_c$: Decreasing the molecular weight of the combustion products is very effective at increasing the exit velocity. The most efficient combination is LH2/LOX, but this requires expensive and heavy cryogenic equipment on-board the engine.
4. $\gamma$: Decreasing the ratio of specific heats (which is a function of the temperature and composition, so not truly independent) will increase the exit velocity. However, $\gamma$ can never be less than one.

## Nozzle Thrust Coefficient

We have now reached the point where we can relate both of our design variables, the choice of propellant and the design of the nozzle, to the thrust produced by the rocket. The thrust of the rocket is given by Eq. {eq}`rocket-thrust`. Using the discharge coefficient, Eq. {eq}`nozzle-discharge-coefficient`, and the velocity coefficient, Eq. {eq}`nozzle-velocity-coefficient`, we can rewrite the thrust equation in terms of the ideal exit velocity and mass flow rate:

```{math}
F = \lambda c_d c_V \dot{m}_i V_{e,i} + A_e\left(p_e - p_0\right)
```

Further plugging in for the ideal mass flow rate and ideal exit velocity, we find:

```{math}
F = \lambda c_d c_V \Gamma p_c A_{\text{th}} \sqrt{\frac{2\gamma}{\gamma - 1}\left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma - 1}{\gamma}}\right]} + A_e \left(p_e - p_0\right)
```

This equation can be divided by the chamber pressure and throat area to define the **nozzle thrust coefficient**:

```{math}
:label: nozzle-thrust-coefficient
c_F = \frac{F}{p_c A_{\text{th}}} = \lambda c_d c_V \Gamma \sqrt{\frac{2\gamma}{\gamma - 1}\left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma - 1}{\gamma}}\right]} + \frac{A_e}{A_{\text{th}}} \left(\frac{p_e}{p_c} - \frac{p_0}{p_c}\right)
```

When there are no losses in the nozzle, then $\lambda = c_V = c_d = 1$ and the thrust coefficient is called the **ideal thrust coefficient**, denoted by $c_{F,i}$:

```{math}
:label: ideal-nozzle-thrust-coefficient
c_{F,i} = \Gamma \sqrt{\frac{2\gamma}{\gamma - 1}\left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma - 1}{\gamma}}\right]}
```

The general thrust coefficient $c_F$ is given in terms of the ideal thrust coefficient as:

```{math}
c_F = c_{F,i} + \varepsilon\left(\frac{p_e}{p_c} - \frac{p_0}{p_c}\right)
```

Furthermore, if we set $p_0 = 0$ then the nozzle is exhausting into a vacuum and we can define the **vacuum thrust coefficient**, $c_{F,\text{vac}}$. Then, the normal thrust coefficient and the vacuum thrust coefficient are related by the area expansion ratio $\varepsilon$:

```{math}
:label: nozzle-thrust-coefficient-vacuum
c_F = c_{F,\text{vac}} - \varepsilon \frac{p_0}{p_c}
```

Although the thrust coefficient is non-dimensional, there are no specific restrictions on the values it can take on. Larger values of the thrust coefficient mean that the nozzle is more effective at turning high-pressure, high-temperature gases in the combustion chamber into acceleration of the engine via the thrust force. This is further emphasized by introducing the ideal mass flow rate and the characteristic velocity into Eq. {eq}`rocket-thrust`:

```{math}
:label: rocket-thrust-characteristic-velocity
F = c_F p_c A_{\text{th}} = c_F \dot{m}_i c^* = c_F \frac{\dot{m}}{c_d} c^*
```

Equation {eq}`rocket-thrust-characteristic-velocity` is made of two terms multiplying the mass flow rate:

1. $c^*$: the characteristic velocity
2. $c_F$: the thrust coefficient

The characteristic velocity is a measure of the propellant performance and the thrust coefficient is a measure of the nozzle performance. Remember that the discharge coefficient is ideally 1, so it does not factor into this analysis.

## Specific Impulse

Another figure of merit for rocket engines is the **specific impulse**. We discussed the specific impulse in the {ref}`introductory chapter <intro-specific-impulse>`. Here, we will place the specific impulse in the context of the variables we have described so far.

Recall that the definition of the specific impulse is the impulse per unit mass, or the thrust per unit _weight_ flow of propellants. Assuming constant thrust and mass flow rate of the propellants, this is:

```{math}
:label: specific-impulse
\Isp = \frac{F}{\dot{m} g} = \frac{V_e}{g} + \frac{A_e}{\dot{m}_e g}\left(p_e - p_0\right)
```

where $g$ is the gravitational acceleration at the Earth's surface, 32.174 ft/s{superscript}`2` or 9.81 m/s{superscript}`2` depending on the units. Note that the Earth's gravitational acceleration is always used regardless of where the rocket engine is physically located. The dimensions of $\Isp$ are time, usually quoted in seconds. This similarly suggests the definition of a related figure of merit, called the **effective exhaust velocity**:

```{math}
:label: effective-exhaust-velocity
V_{\text{eff}} = \frac{F}{\dot{m}}
```

which has dimensions of velocity. The effective velocity is, like the characteristic velocity, not an actual velocity that is required to be present in the system. Rather, it is the velocity of the exhaust that gives the equivalent thrust as the sum of the momentum and pressure thrust.

The effective exhaust velocity, specific impulse, thrust coefficient, and characteristic velocity are all related to each other by the thrust:

```{math}
c^* c_{F} = V_{\text{eff}} = \Isp g
```

Next, taking the specific impulse in Eq. {eq}`specific-impulse` and noting that $\dot{m} = \rho_e A_e V_e$ and $\rho_e V_e^2 = \gamma_e p_e M_e^2$, we find:

```{math}
\Isp = \frac{V_e}{g}\left[1 + \left(1 - \frac{p_0}{p_e}\right)\frac{1}{\gamma_e M_e^2}\right]
```

We have seen previously that the exit Mach number and exit velocity depend only on the chamber conditions and the expansion ratio, $\varepsilon$. Thus, the specific impulse for a given engine, with a particular choice of propellant, chamber, and nozzle, will vary only with the altitude.

We define the vacuum specific impulse, with $p_0 = 0$, as:

```{math}
:label: vacuum-specific-impulse
I_{\text{sp},\text{vac}} = \frac{V_e}{g}\left(1 + \frac{1}{\gamma_e M_e^2}\right)
```

Taking the ratio of the actual $\Isp$ to the vacuum $\Isp$, we find:

```{math}
:label: specific-impulse-ratio
\frac{\Isp}{I_{\text{sp},\text{vac}}} = 1 - \frac{1}{1 + \gamma M_e^2}\frac{p_0}{p_e} \leq 1
```

where since the second term on the right hand side is between 0 and 1, the entire fraction must be less than one. This means that the vacuum specific impulse is the largest that a given rocket engine can produce. In general, references to a particular rocket engine will quote either the vacuum specific impulse or the sea-level specific impulse, with a slight preference for the vacuum specific impulse since it is larger.

For a given rocket engine, one possible procedure to determine the specific impulse at any altitude is to calculate the vacuum specific impulse from Eq. {eq}`vacuum-specific-impulse`, which depends only on the exit velocity and the exit Mach number, which in turn depend only on the expansion ratio and combustion chamber conditions. Then, the ratio in Eq. {eq}`specific-impulse-ratio` is used to account for the effect of the varying pressure with altitude.

Let's consider two rocket engines with the same chamber temperature, $T_c$ = 5000 °R, chamber pressure, $p_c$ = 1000 psia, $W$ = 28.95 kg/kmol, and $\gamma$ = 1.4. Assume that both engines are ideal, such that $\lambda = c_V = c_d = 1$, and the process through both nozzles is isentropic. The two nozzles have differing expansion ratios giving them different values of $p_e$, and thus $M_e$ and $V_e$:

1. **Nozzle 1**: $\varepsilon$ = 10
2. **Nozzle 2**: $\varepsilon$ = 25

For both engines, we can calculate the vacuum specific impulse from Eq. {eq}`vacuum-specific-impulse` if we can determine $V_e$ and $M_e$. The exit Mach number is determined by the area-Mach-number relation, Eq. {eq}`area-mach-relation`, where we will assume that the solution is supersonic. The exit velocity is determined by Eq. {eq}`ideal-exit-velocity`. The exit properties and vacuum $\Isp$ for both engines are shown in {numref}`varying-expansion-ratio-Isp`.

```{code-cell}
:tags: [remove-output]

from pint import UnitRegistry
from scipy import optimize
import numpy as np

units = UnitRegistry()

T_c = 5000 * units.degR
p_c = 1000 * units.psi
gamma = 1.4 * units.dimensionless
W = 28.95 * units.kg / units.kmol
R = units.molar_gas_constant / W
epsilon_1 = 10 * units.dimensionless
epsilon_2 = 25 * units.dimensionless

def area_ratio(M, A_ratio, gamma):
    first_term = 2 / (gamma + 1)
    power = (gamma + 1) / (gamma - 1)
    second_term = 1 + (gamma - 1) / 2 * M**2
    return 1 / M**2 * (first_term * second_term)**(power) - A_ratio**2

M_e1 = optimize.brentq(area_ratio, 1.01, 10, args=(epsilon_1.magnitude, gamma.magnitude)) * units.dimensionless
T_e1 = T_c / (1 + (gamma - 1) / 2 * M_e1**2)
p_e1 = p_c / (T_c / T_e1)**(gamma / (gamma - 1))
V_e1 = (np.sqrt(2 * gamma / (gamma - 1) * R * T_c * (1 - (p_e1 / p_c)**((gamma - 1) / gamma)))).to("ft/s")
vIsp_1 = (V_e1 / units.gravity * (1 + 1 / (gamma * M_e1**2))).to("s")

M_e2 = optimize.brentq(area_ratio, 1.01, 10, args=(epsilon_2.magnitude, gamma.magnitude)) * units.dimensionless
T_e2 = T_c / (1 + (gamma - 1) / 2 * M_e2**2)
p_e2 = p_c / (T_c / T_e2)**(gamma / (gamma - 1))
V_e2 = (np.sqrt(2 * gamma / (gamma - 1) * R * T_c * (1 - (p_e2 / p_c)**((gamma - 1) / gamma)))).to("ft/s")
vIsp_2 = (V_e2 / units.gravity * (1 + 1 / (gamma * M_e2**2))).to("s")
```

```{code-cell}
:tags: [remove-cell]

for property in ["M_e" , "T_e", "p_e", "V_e", "vIsp_"]:
    for nozzle in ["1", "2"]:
        var = property + nozzle
        glue(var, f"{locals()[var]:.2F~P}", display=False)
```

```{table} Effect of varying expansion ratio on rocket engine vacuum performance
:name: varying-expansion-ratio-Isp

| Property                     | Nozzle 1            | Nozzle 2            |
|------------------------------|---------------------|---------------------|
| $M_e$                        | {glue:text}`M_e1`   | {glue:text}`M_e2`   |
| $V_e$                        | {glue:text}`V_e1`   | {glue:text}`V_e2`   |
| $p_e$                        | {glue:text}`p_e1`   | {glue:text}`p_e2`   |
| $T_e$                        | {glue:text}`T_e1`   | {glue:text}`T_e2`   |
| $I_{\text{sp},{\text{vac}}}$ | {glue:text}`vIsp_1` | {glue:text}`vIsp_2` |
```

We can see that the larger expansion ratio nozzle has higher specific impulse under the vacuum conditions. This makes sense, because it is not possible to overexpand the nozzle when the backpressure is a vacuum, and the ideal expansion ratio would be infinite. Thus, the larger expansion ratio is able to expand the flow closer to the vacuum.

Now, we can plot the variation of the specific impulse with altitude for the two engines.

```{code-cell}
:tags: [remove-output]

from ambiance import Atmosphere

heights = np.linspace(0, 200E3) * units.ft
atmos = Atmosphere(heights.to("m").magnitude)
p_0 = atmos.pressure * units.Pa

Isp_1 = ((1 - p_0 / ((1 + gamma * M_e1**2) * p_e1)) * vIsp_1).to("s")
Isp_2 = ((1 - p_0 / ((1 + gamma * M_e2**2) * p_e2)) * vIsp_2).to("s")
```

```{code-cell}
:tags: [remove-input]

data = ColumnDataSource(
    data=dict(
        h=heights.to("kft").magnitude,
        Isp_1=Isp_1.magnitude,
        Isp_2=Isp_2.magnitude,
        p_e1=(p_e1 - p_0).to("psi").magnitude,
        p_e2=(p_e2 - p_0).to("psi").magnitude,
    )
)

colors = itertools.cycle(palette[10])
p1 = figure(
    y_axis_label="I_sp, s",
    x_axis_label="Altitude, kft",
    y_range=(150, 230),
    x_range=(0, 200),
    **opts
)
p1.line("h", "Isp_1", source=data, color=next(colors), line_width=2, legend_label=f"𝜀 = {epsilon_1:~P}")
p1.line("h", "Isp_2", source=data, color=next(colors), line_width=2, legend_label=f"𝜀 = {epsilon_2:~P}")

colors = itertools.cycle(palette[10])
p1.extra_y_ranges["pressure"] = Range1d(-15, 15)
p1.line("h", "p_e1", source=data, y_range_name="pressure", line_width=2, line_dash="dashed", color=next(colors), legend_label=f"𝜀 = {epsilon_1:~P}")
p1.line("h", "p_e2", source=data, y_range_name="pressure", line_width=2, line_dash="dashed", color=next(colors), legend_label=f"𝜀 = {epsilon_2:~P}")
ax2 = LinearAxis(y_range_name="pressure", axis_label="Pressure difference, p_e - p_0, psia")
p1.add_layout(ax2, "right")

p1.add_layout(Arrow(end=NormalHead(size=7), x_start=26, y_start=212, x_end=5, y_end=212, line_width=2))
p1.add_layout(Arrow(end=NormalHead(size=7), x_start=47, y_start=220, x_end=25, y_end=220, line_width=2))
p1.add_layout(Arrow(end=NormalHead(size=7), y_range_name="pressure", x_start=35, y_start=3.9, x_end=55, y_end=3.9, line_width=2))
p1.add_layout(Arrow(end=NormalHead(size=7), y_range_name="pressure", x_start=35, y_start=-1.9, x_end=55, y_end=-1.9, line_width=2))

p1.legend.location = "bottom_right"

show(p1)
```

On this graph, the left axis shows the specific impulse and the right axis shows the pressure difference $p_e - p_0$.

On the far right of the graph, the specific impulse approaches the vacuum specific impulse and pressure difference approaches the exit pressure as the ambient pressure trends towards zero. As altitude decreases moving left, the ambient pressure increases, and the specific impulse of both engines decreases.

The drop off of specific impulse with altitude is fairly steep, and the slope is larger with the larger expansion ratio! This means that there is a crossover point where the smaller expansion ratio engine is more efficient than the larger expansion ratio.

As we pointed out before, the larger expansion ratio is more efficient in a vacuum because it expands the flow closer to the ambient pressure. In other words, $p_e - p_0$ is smaller under vacuum conditions for the larger expansion ratio, getting closer to the ideal case of $p_e = p_0$. However, this additional expansion means that at sea level, the pressure difference is larger for the larger expansion ratio than the smaller expansion ratio. This results in a less efficient engine with the larger expansion ratio!

This trend suggests that a nozzle which is able to adapt to the changing ambient pressure would be advantageous. As we discussed in the {ref}`Nozzle Shapes section <nozzle-shapes>`, the plug, aerospike, and extendable nozzles can all help reduce the effect of the changing ambient pressure. However, none of these engines are used in practice.

As it turns out, most rocket launch vehicles are **staged**. This means that portions of the structure of the rocket (the fuel tanks and support structures) are discarded when the fuel tanks are empty. Staging rockets helps to work around the tyranny of the rocket equation problem, as we'll show later on.

Since the rocket is staged, it will have different engines with different nozzles operating at different altitude ranges! This means that a fixed expansion ratio converging-diverging nozzle can be designed which operates well at low altitude for the first stage of the rocket, and later stages that operate higher in the atmosphere or in space use nozzles optimized for those conditions.
