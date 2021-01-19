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

Under our assumption of steady state, the drag is equal to the thrust, $D = F$. The **required power**, also called the **useful power**, is the power required to overcome the drag, $P_u = D V_0 = FV_0$. Then, it is useful to divide the total power provided by the propeller into the useful portion and the portion accounting for losses. This will allow us to define a **propulsive efficiency**.

```{math}
P = P_u + P_l = F V_0 + P_l
```

where $P_l$ is the power loss and $P_u$ is the useful power. Solving for the loss term, and plugging in Eq. {eq}`simplified-no-heat-energy`:

```{math}
:label: propeller-power-loss

P_l = \frac{1}{2}\dot{m}\left(V_e^2 - V_0^2\right) - \dot{m}\left(V_e - V_0\right)V_0 = \frac{1}{2}\dot{m}\left(V_e - V_0\right)^2
```
