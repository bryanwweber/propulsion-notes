(conservation_equations_review)=
# Conservation Equations

There are three conservation laws that are relevant for propulsion engines:

1. Conservation of Mass
2. Conservation of Momentum
3. Conservation of Energy

## Assumptions

Before discussing these equations, we must describe the assumptions we will use to simplify them. We can think of an ideal flow machine as a device that operates on a stream of a fluid in some way and ejects the processed fluid into the surroundings. The device may or may not intake a stream of fluid as well. This kind of simplified flow machine is shown in {numref}`ideal-flow-machine`.

```{figure} ../images/ideal-flow-machine.svg
:name: ideal-flow-machine

An ideal flow machine.
```

**Assumption 1:** Draw an imaginary surface in front of the flow machine. Inside the surface are all the molecules of fluid that will enter the flow machine. A similar surface containing all the molecules that have been processed by the flow machine is drawn from the exit. This surface is called a **streamtube**, and no mass can cross the streamtube surface. The shape of the streamtube may be as shown in {numref}`ideal-flow-machine`, or it may be different. The combination of the streamtubes and the flow machine create a **control volume** to which we will apply the conservation laws.

**Assumption 2:** The fluid flow is at steady state. This means that there can be no unbalanced forces on the flow machine. Due to the aerodynamic drag, there must be a corresponding applied force to maintain constant velocity. The power required to maintain constant velocity is therefore given by

```{math}
:label: power-required-steady-state

D V_0 = F V_0
```

where $D$ is the drag force and $F$ is the applied force by the flow machine.

**Assumption 3:** The fluid flow is quasi-one-dimensional. This means that at any cross section of the flow, the properties are constant, and we refer to the properties **at a location** or **at a station**. In the freestream, the properties of the fluid flow are subscripted with $0$; at the exit, the properties are subscripted with $e$.

**Assumption 4:** The freestream and exit stations are sufficiently far away from the flow machine that the pressures are equal, $p_e = p_0$, and are in equilibrium with the surroundings.

**Assumption 5:** There is no stray heat transfer from the flow machine to the surroundings, or across the streamtube boundaries.

**Assumption 6:** We can neglect frictional forces across the streamtube boundary.

**Assumption 7:** The only mass entering and leaving the flow machine are within the inlet streamtube. Any other mass flows, for instance, of fuel are negligible in comparison to this flow. Assuming the stoichiometric mass-basis air-fuel ratio of jet fuel is 15, and assuming the entire flow is used for combustion, neglecting the fuel flow results in about a 5% error in the mass flow rate. However, part of the inlet air flow is used for cooling in the engine, so the actual ratio of incoming air to incoming fuel is much higher than 15, resulting in a smaller error.

(conservation_of_mass)=
## Conservation of Mass

For the control volume described in **Assumption 1**, according to **Assumption 7** the only mass entering is at the freestream (station $0$) and the only mass exiting is at the exit (station $e$). Second, because the control volume is at steady state (**Assumption 2**), the amount of matter inside the control volume is constant. Finally, according to **Assumption 3**, the flow is quasi-one-dimensional and the properties of the flow at a given station are constant.

Therefore, we can represent the mass flow rate of the fluid at the freestream as:

```{math}
:label: mass-flow-rate-freestream

\dot{m}_0 = \rho_0 A_0 V_0
```

and the mass flow rate of the fluid at the exit as:

```{math}
:label: mass-flow-rate-exit

\dot{m}_e = \rho_e A_e V_e
```

where $\dot{m}$ is the mass flow rate, $\rho$ is the density of the fluid, $A$ is the cross-sectional area of the streamtube at that station, and $V$ is the fluid velocity.

According to the Law of Conservation of Mass, mass cannot be created or destroyed. In general, for one-dimensional flow, the Law of Conservation of Mass can be written as:

$$-\sum_i \dot{m}_i + \sum_e \dot{m}_e = -\frac{dm_{cv}}{dt}$$

where subscript $i$ indicates an inlet, and $m_{cv}$ is the mass inside the control volume. At steady state, the right-hand-side is zero by definition, such that the Law of Conservation of Mass simplifies to:

```{math}
:label: ideal-conservation-of-mass

\dot{m}_0 = \dot{m}_e = \rho_0 A_0 V_0 = \rho_e A_e V_e = \dot{m}
```

## Conservation of Momentum

Newton's second law of motion can be written as:

$$\frac{d\left(mV\right)}{dt} = \sum F$$

or, the change of momentum of the fluid is equal to the net force acting on it. For this control volume, we will only consider one net force on the fluid. Newton's second law can therefore be written as:

$$\left(-\rho_0 A_0 V_0\right)V_0 + \left(\rho_e A_e V_e\right)V_e = F$$

where we have used the sign convention established in {ref}`conservation_of_mass`. Since the mass flow rate is constant ($\rho_0 A_0 V_0 = \rho_e A_e V_e$), this can be rewritten as:

```{math}
:label: ideal-conservation-of-momentum

\dot{m}\left(V_e - V_0\right) = F
```

Note that the force $F$ is the force on the fluid. Therefore, the force on the flow machine by the fluid is $-F$.

## Conservation of Energy

The First Law of Thermodynamics, applied to this control volume, states that the **total enthalpy** of the flowing fluid can only be changed by heat transfer or power transfer. The total enthalpy is given by:

```{math}
:label: total-enthalpy

h_t = h + \frac{1}{2} V^2
```

where $h_t$ is the total enthalpy and $h$ is the **static enthalpy**. Therefore, the Law of Conservation of Energy can be stated as:

```{math}
:label: conservation-of-energy

\dot{m}\left[\left(h_e - h_0\right) + \frac{1}{2}\left(V_e^2 - V_0^2\right)\right] = \dot{m} Q + P
```

where $h$ and $Q$ (the heat transfer) have units of kJ/kg in the SI system, and $P$ (the power) has units of kW. Beware of the kinetic energy term, though, because it does not have consistent units in this system.
