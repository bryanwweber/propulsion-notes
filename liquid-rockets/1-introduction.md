# Liquid Propellant Rocket Engines

Liquid propellant rocket engines are a critical piece of a launch vehicle. Many rockets destined for low Earth orbit and beyond are launched from the surface of the Earth using liquid propellant-fueled rockets.

As we discussed previously, liquid propellant rockets have two big advantages over solid-propellant rockets:

1. They can be turned on and off
2. They can be throttled to adjust the thrust level

Both of these characteristics are due to the use of liquid propellants, and in particular, the ability of liquid propellants to be pumped into a combustion chamber. Controlling the flow rate through the pump(s), or turning them off, provides both of the functions described above.

The most common liquid propellant combinations for launch vehicles are LH<sub>2</sub>/LOX, RP-1/LOX, and LCH<sub>4</sub>/LOX. The _L_ indicates the propellants are in a liquid state, and _OX_ means oxygen in this case. RP-1 is a kerosene-based fuel similar to jet fuel. These combinations are **bipropellants**, or binary propellants, because they require both a fuel and an oxidizer to function.

Other common fuels include **monopropellants** such as [hydrazine](https://en.wikipedia.org/wiki/Hydrazine#Rocket_fuel), which are able to react by themselves or with the help of a catalyst.

```{note}
For an hilarious and insightful read about the early history of rocket fuel development, check out _Ignition_ by John D. Clark. You can buy a new printing of it, but it's old enough that it's in the public domain and you can find [PDFs and epubs of _Ignition_ online](https://archive.org/details/ignition_201612). Sample quote:

> If, however, this coat is melted or scrubbed off, and has no chance to reform, the operator is confronted with the problem of coping with a metal-fluorine fire. For dealing with this situation, I have always recommended a good pair of running shoes. John D. Clark, _Ignition_, pg. 74. {cite}`clark2018ignition`
```

## Rocket Motor Components

```{figure} ../images/rocket-engine.svg
:name: rocket-engine
A schematic of a simple rocket engine, showing the injector, combustion chamber, and nozzle.
```

The rocket motor has three primary components, as shown in {numref}`rocket-engine`:

1. The injector
2. The combustion chamber
3. The nozzle

Propellants are injected into the combustion chamber, where they react at nearly zero velocity. After reacting, the propellants enter the **converging-diverging** nozzle, which accelerates them to supersonic speed at the exit.

There are a few important dimensions on the nozzle we should be aware of. In general, rocket motors are axisymmetric, as shown by the centerline drawn on {numref}`rocket-engine`:

1. $r_c$ - the radius of the combustion chamber
2. $r_t$ - the radius of the nozzle throat, the smallest radius in the nozzle
3. $r_e$ - the radius of the nozzle exit
4. $\alpha$ - the expansion angle of the nozzle at the exit

The converging section of the nozzle accelerates the flow to $M = 1$. At the throat, the Mach number is exactly equal to one, and the flow is said to be **choked**. This means that changing the pressure at the nozzle exit will not change the mass flow rate. After the throat, the nozzle diverges. This further accelerates the flow into supersonic speeds.

```{margin}
Additional mass for the nozzle requires additional mass of propellant to launch it. That mass of propellant requires more mass of propellant to launch it, and so on. This is called the [_tyranny of the rocket equation_](https://www.nasa.gov/mission_pages/station/expeditions/expedition30/tryanny.html). Or, you can [watch Chris Hadfield](https://www.youtube.com/watch?v=V_brZ-KWY3g) explain the equation on Stand Up Maths.
```

Ideally, the flow will leave the nozzle parallel to the axis. However, this often requires additional length of the nozzle, translating to additional mass that must be carried. There is a significant penalty for any additional mass on a rocket, so the nozzle may be cut short, and the flow may leave at some angle relative to the axis, given by $\alpha$.
