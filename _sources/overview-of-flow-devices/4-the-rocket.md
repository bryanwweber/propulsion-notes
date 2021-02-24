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
# The Rocket

In the {ref}`previous section <no-net-power>`, we discussed devices with heat transfer input, no net power input, and a finite inlet area. In this section, we will keep the first two assumptions but remove the inlet. This requires all of the fluids to be stored on-board the flow machine.

This kind of device is called a **rocket**. The main advantage of a rocket is that it does not require any fluid from the environment to operate. As such, it can operate in space, without an atmosphere.

The propellants can be carried in **gaseous**, **liquid**, or **solid** form on the rocket. Gaseous propellants tend to be used for low-thrust rockets, since they take up a lot of volume.

Liquid and solid propellants are more commonly used. Liquid propellants can be directly introduced into a combustion chamber where they are ignited and burned. Solid propellants must be gasified from the surface before they are burned.

The advantage of liquid propellants is that they can be pumped, and therefore the thrust can be turned on or off by changing the flow of propellants. Solid propellants are very difficult to extinguish once ignited.

On the other hand, liquid propellants must often be stored at cryogenic temperatures, requiring sophisticated handling equipment and storage tanks to prevent accidental releases. Solid propellants are usually much easier to handle and store.

## Thrust Variation

```{margin}
**Note:** The book specifies that $V_0 = 0$ here, to indicate that there is no inlet velocity. However, $V_0$ is not truly zero, because the rocket is still moving.
```

For the rocket, there is no air taken on board during flight. Therefore, the inlet velocity is zero and the mass flow rate in the engine is given by:

```{math}
:label: rocket-mdot
\dot{m} = \rho_e A_e V_e
```

In addition, the momentum equation simplifies to:

```{math}
:label: rocket-momentum
F = \dot{m}V_e
```

Finally, the energy equation can be simplified to:

```{math}
:label: rocket-energy
F = \frac{2\dot{m}}{V_e}\left[Q - \left(h_e - h_i\right)\right] = 2 \rho_e A_e \left[Q - \left(h_e - h_i\right)\right]
```

where $h_i$ is the initial enthalpy of the reactants. From these equations, we see that the thrust is independent of the flight velocity, $V_0$.

(intro-specific-impulse)=
## Fuel Efficiency and Specific Impulse

Rockets use a different fuel efficiency metric than jet engines. The TSFC for a jet engine is the ratio of the propellant carried on board the aircraft to the thrust produced. The bulk of the mass flow in the engine is available for free from the environment, captured simply by the motion of the aircraft.

```{margin}
There's that word _specific_ again. With no modifier, it usually means _mass_ specific.
```

Rockets carry all their propellant with them. Therefore, the fuel efficiency metric for a rocket is the ratio of the impulse delivered to the rocket during a time interval to the amount of propellant consumed during that same time interval. This metric is called the **specific impulse**, $\Isp$:

```{math}
\Isp = \frac{\int_{t_1}^{t_2} F dt}{\int_{t_1}^{t_2} \dot{m} dt}
```

In most cases, we will consider the thrust and mass flow rate to be constant, such that the specific impulse can be represented by:

```{math}
:label: rocket-Isp
\Isp = \frac{F}{\dot{m}} = \frac{\dot{m} V_e}{\dot{m}} = V_e
```

Therefore, the units of specific impulse in the SI system are m/s, and the fundamental property related to $\Isp$ is the exhaust velocity. In English units, $\Isp$ is given by:

```{math}
:label: rocket-Isp-EE
\Isp = \frac{F}{\dot{m}} \left\lvert\frac{1g\cdot\text{lbm}}{\text{lbf}}\right\rvert \frac{1}{1g} = \frac{V_e}{g}
```

Therefore, the units of specific impulse in the English system are seconds, and this is the typical parameter quoted for rocket engines. You can see that the definitions differ by $g$, the standard gravitational acceleration, 32.174 ft/s{superscript}`2` in English units and 9.81 m/s{superscript}`2` in SI units.

For a jet engine, we can also define a specific impulse, which is essentially the inverse of the TSFC. However, because the consumable quantity is only the fuel flow in the jet engine, the specific impulse of jet engines tends to be much higher than rockets.

## Example

The German [V-2 rocket](https://en.wikipedia.org/wiki/V-2_rocket) was used in World War II to bomb Allied cities. It burned 3,810 kg of 75% ethanol + water as the fuel and 4,910 kg of liquid oxygen as the oxidizer in an oxidizer-to-fuel ratio of 1.25. The burn time was 65 s and the nozzle exhaust velocity was approximately 2,200 m/s [Source](https://history.nasa.gov/SP-4404/app-b8.htm). Find the thrust produced, the power produced at a flight velocity of 2,000 m/s, the specific impulse, and the overall efficiency.

```{code-cell}
import pint
units = pint.UnitRegistry()

fuel = 3_810 * units.kg
oxid = 4_910 * units.kg
O_to_F = 1.25 * units.dimensionless
t_burn = 65 * units.s
V_e = 2_200 * units.m / units.s
V_0 = 2_000 * units.m / units.s
Q_f = 0.75 * 2.723E4 * units.kJ / units.kg

mdot = (fuel + oxid) / t_burn
F = (mdot * V_e).to("ton_force")
P = (F * V_0).to("MW")
I_sp = (V_e / units.standard_gravity).to("s")
eta_o = (F * V_0 / (mdot / (1 + O_to_F) * Q_f)).to("dimensionless")
print(*(f"{v:.2F~P}" for v in (F, P, I_sp, eta_o)), sep="\n")
```

The thrust force in this calculation of 33.17 tons exceeds the listed design thrust of 25 tons quite substantially. This is likely due to our simplistic assumptions related to the mass flow rate.
