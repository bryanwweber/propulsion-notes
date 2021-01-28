# Combined Heat and Power Addition: The Turbofan

We saw from our analysis of the propeller that the efficiency is improved by accelerating a large mass of fluid only a little. However, propellers have the disadvantage of speed limitations due to the power input requirements.

The speed limitation is removed by switching to a jet engine, but the efficiency is reduced. It is possible to combine the turbojet and the propeller to gain advantages of both. The resulting device is called a **turbofan** engine.

In the turbofan engine, the incoming airstream is divided between a **cold outer flow**, which is accelerated by the fan by power addition, and a **hot inner flow** which proceeds through a turbojet cycle and has heat addition. These flows are shown in {numref}`turbofan`.

```{figure} ../images/turbofan.svg
:name: turbofan

Schematic of a turbofan engine.
```

## Conservation Equations

The total mass flow rate coming in to the inlet, $\dot{m}_0$ is split at the fan into two components:

1. The cold flow, $\dot{m}_c$
2. The hot floe, $\dot{m}_h$

Applying mass conservation, we find:

```{math}
\dot{m}_0 = \dot{m}_c + \dot{m}_h = \dot{m}_h\left(1 + \beta\right)
```

where $\beta$ is the **bypass ratio**, defined as $\dot{m}_c/\dot{m}_h$. The force on the fluid from the momentum equation is the sum of the force due to the fan on the cold flow and the nozzle on the hot flow:

```{math}
F = F_h + F_c = \frac{\dot{m}_0}{1 + \beta}\left(V_{e,h} - V_0\right) + \frac{\dot{m}_0 \beta}{1 + \beta}\left(V_{e,c} - V_0\right)
```

Finally, we can apply the energy equation to the cold and hot flows independently. For the cold flow, there is no heat addition and only power addition. Therefore, the energy equation reduces to the same as the propeller case:

```{math}
P_c = F_c V_{c,\text{avg}}
```

For the hot flow, there is no net power addition and only heat addition. However, part of the energy extracted in the turbine is used to drive the fan and provide power input to the cold flow. If we include both the hot and cold flow in the energy equation, we can assume that there is no net power addition:

```{math}
\dot{m}_c\left[\left(h_{e,c} - h_0\right) + \frac{1}{2}\left(V_{e,c}^2 - V_0^2\right)\right] + \dot{m}_h\left[\left(h_{e,h} - h_0\right) + \frac{1}{2}\left(V_{e,h}^2 - V_0^2\right)\right] = \dot{m}_h Q
```

We will also assume that the temperature change of the cold flow is negligible, such that $h_{e,c}\approx h_0$. Simplifying the energy equation, and solving for the thrust, we find:

```{math}
F = \frac{\dot{m}_h Q \eta_{\text{th}}}{V_{\text{avg},h}} + \frac{\dot{m}_0 \beta}{1 + \beta}\left[\frac{1}{2}\left(V_{e,c}^2 - V_0^2\right)\left(\frac{1}{V_{\text{avg},c}} - \frac{1}{v_{\text{avg}, h}}\right)\right]
```

Thus, the specific fuel consumption is:

```{math}
c_{\text{j}} = \frac{\dot{m}_\text{f}}{F} = \left\{\frac{\eta_{\text{th}}\eta_{\text{b}}Q_{\text{f}}}{V_{\text{avg},h}} + \frac{\beta}{\left(f/a\right)}\left[\frac{1}{2}\left(V_{e,c}^2 - V_0^2\right)\left(\frac{1}{V_{\text{avg},c}} - \frac{1}{V_{\text{avg}, h}}\right)\right]\right\}^{-1}
```

Note that as $\beta\rightarrow 0$, we recover the turbojet result. For $\beta > 0$, the TSFC is reduced as compared to the turbojet case, showing why the turbofan is worth the additional complexity. The larger that $\beta$ is, the lower the fuel consumption. Note that the value of $\beta$ cannot grow infinitely, because the hot core flow is needed to provide power to the fan.

Modern turbofan bypass ratios can reach as high as approximately 10. Currently, the primary limitation on increasing $\beta$ for turbofan engines is the larger drag and structural weight they incur on the aircraft. This offsets the benefit provided by the turbofan.

## Turboprop

Although turbofan engines cannot have $\beta$ values larger than about 10, removing the cowling around the fan blades removes many of the drag and weight problems. This converts the engine into a **turboprop** engine, where nearly all the heat transfer is used to provide power to the propeller and none is used for jet thrust.

For the turboprop, the input power is then approximately given by:

```{math}
P_c = \dot{m}_h Q \eta_{\text{th}}
```

and the total thrust is given by:

```{math}
F = \frac{P_c}{V_{\text{avg},c}}
```

These are the same equations we developed for the propeller earlier. Thus, the turboprop has the same speed disadvantages as the standard propeller, making it unsuitable for long-range flights. However, the specific fuel consumption is the lowest among the turbomachinery-based engines we have discussed:

```{math}
c_{\text{j}} = \frac{V_{\text{avg},c}}{\eta_b \eta_{\text{th}}Q_{\text{f}}}
```
