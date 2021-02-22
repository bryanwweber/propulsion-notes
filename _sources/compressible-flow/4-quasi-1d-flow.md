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
from bokeh.palettes import Category10 as palette
from bokeh.models import Span, PrintfTickFormatter
from bokeh.layouts import column

import numpy as np
from scipy import optimize

output_notebook(hide_banner=True)
opts = dict(plot_width=500, plot_height=400, min_border=0)
colors = itertools.cycle(palette[10])
```

# Quasi-One-Dimensional Nozzle Flow

Let's now consider a simple nozzle with varying cross-sectional area. We will neglect the influence of skin friction and heat transfer at the nozzle wall, so that the only way that the flow may change is due to the area change. In this nozzle, the flow is adiabatic and reversible, so the entropy is constant.

## Mass Conservation

In steady flow, the mass flow rate is given by the integral relationship:

```{math}
\int \rho \left(\vec{V}\cdot\hat{n}\right) dA = 0
```

If we further simplify to quasi-one-dimensional flow, and define the $z$ axis as the flow direction, then the mass flow rate is:

```{math}
:label: one-d-mass-flow-rate
\dot{m}(z) = \rho(z) A(z) V(z) = \text{const}
```

where $\dot{m}(z)$ is a constant, and the density, area, or velocity may change as a function of axial location. In differential form, this becomes:

```{math}
:label: mass-flow-rate-differential
\frac{d\dot{m}}{\dot{m}} = 0 =\frac{d\rho}{\rho} + \frac{dV}{V} + \frac{dA}{A}
```

At a given station, or axial ($z$) location, the mass flow rate can be related to the local flow conditions by using Eqs. {eq}`ideal-gas-law` and {eq}`speed-of-sound`:

```{math}
\dot{m} = p A M\sqrt{\frac{\gamma}{R T}}
```

where $R = R_u / W$. Using the results from Eqs. {eq}`isentropic-temperature-mach` and {eq}`isentropic-pressure-mach`, we can write the mass flow rate as:

```{math}
:label: mass-flow-rate-mach-number
\dot{m} = \frac{p_t A}{\sqrt{T_t}}\sqrt{\frac{\gamma}{R}}M\left(1 + \frac{\gamma - 1}{2}M^2\right)^{\frac{-\left(\gamma + 1\right)}{2\left(\gamma - 1\right)}}
```

## Momentum Equation

The integral form of the momentum equation for a control volume around the nozzle is:

```{math}
\int_{A} \left(\rho \vec{V}\cdot\hat{n}\right)\vec{V} dA = 0
```

because we are neglecting friction and drag. In the log differential form, this becomes:

```{math}
\frac{dp}{p} + \frac{1}{2}\frac{\rho}{p}\frac{dV^2}{V^2} = 0
```

Replacing $\rho/p$ from the ideal gas law, Eq. {eq}`ideal-gas-law` and multiplying and dividing the second term by $a^2$, we can write:

```{math}
:label: momentum-differential
\frac{dp}{p} + \frac{1}{2}\gamma M^2 \frac{dV^2}{V^2} = 0
```

## Area-Velocity Relation

Using Eq. {eq}`mass-flow-rate-differential` to eliminate the $dp/p$ term from Eq. {eq}`momentum-differential`, we find the **area-velocity relation**:

```{math}
:label: area-velocity-relation
\frac{dA}{A} = \left(M^2 - 1\right) \frac{dV}{V}
```

This important equation gives us the relationship between Mach number, area change, and velocity change. We make a number of observations from this equation:

1. If $M\rightarrow 0$, this tells us that the product of the area and velocity is a constant, which is the continuity equation for incompressible flow.
2. If $M < 1$, the first time on the right-hand side of Eq. {eq}`area-velocity-relation` is negative. This means that if we want the velocity to increase ($dV > 0$), then $dA$ must be negative and the area must decrease. The opposite is also true; if we want velocity to decrease, the area must increase.
3. On the other hand, if $M > 1$, the first time on the right-hand side of Eq. {eq}`area-velocity-relation` is positive. This means that if we want the velocity to increase ($dV > 0$), then $dA$ must be positive and the area must increase. The opposite is also true; if we want velocity to decrease, the area must decrease.
4. If $M = 1$, the area must be constant ($dA = 0$). We can prove that for flow to accelerate from subsonic to supersonic, or to decelerate flow from supersonic to subsonic, this area must be a **minimum**.

## Area-Mach Number Relation

Now let's return to the nozzle. We will consider a **converging-diverging** nozzle, since we know that we want to accelerate the flow from subsonic in the combustion chamber to supersonic exit velocity. From the thrust equation, Eq. {eq}`rocket-momentum`, we know that the thrust is proportional to the nozzle exit velocity, so higher exit velocities will provide more thrust.

The location of the smallest area in the nozzle is called the **throat**. Since the area is at a minimum at this location, the slope must be zero, $dA = 0$. Therefore, the Mach number $M = 1$, and this defines the **characteristic area**, $A^*$.

Let's apply the conservation equations from a point upstream of the throat to the throat. Then:

```{math}
\rho V A = \rho^* V^* A^* \Rightarrow \frac{A}{A^*} = \frac{\rho^*}{\rho} \frac{a^*}{V}
```

Next, multiply and divide the right side by $\rho_t$. This gives us the relationship of $\rho_t/\rho$ and $\rho^*/\rho_t$, which we have developed previously. Finally, using Eq. {eq}`mach-to-m-star`, we find:

```{math}
:label: area-mach-relation
\left(\frac{A}{A^*}\right)^2 = \frac{1}{M^2}\left[\frac{2}{\gamma + 1}\left(1 + \frac{\gamma - 1}{2}M^2\right)\right]^{\frac{\gamma + 1}{\gamma - 1}}
```

This is the **area-Mach number relation** and it is a critically important equation to understand nozzle flows. To help understand why, we will inspect the figure below.

```{code-cell}
:tags: [remove-input]

p1 = figure(
    x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    title="Area-Mach Number Relation",
    y_axis_type="log",
    x_range=(0, 10), y_range=(0.05, 4.25),
    **opts
)
mach_number = np.hstack((np.logspace(-2, 0), np.linspace(1, 5)))
gamma = 1.4
first_term = 2 / (gamma + 1)
second_term = 1 + (gamma - 1)/2 * mach_number**2
power = (gamma + 1) / (gamma - 1)
area_ratio = np.sqrt(1/mach_number**2 * (first_term * second_term)**(power))
p1.line(area_ratio, mach_number, line_width=2)
p1.add_layout(Span(location=1.0, dimension="width"))
p1.add_layout(Span(location=1.0, dimension="height"))
p1.yaxis[0].formatter = PrintfTickFormatter(format="%2f")
show(p1)
```

From the graph, we can see two things immediately:

1. There are no solutions for $A/A^*$ less than 1.0. In other words, for isentropic flow, the area at any cross section must be greater than or equal to the characteristic area.
2. There are two values of $M$ that correspond to a given $A/A^*$ value, a subsonic and a supersonic solution. The only exception is at the point (1.0, 1.0), where the area is minimum and the flow is exactly sonic.

Assume that a convergent-divergent nozzle looks like the figure below. At the inlet, the area ratio goes to infinity, such that the Mach number goes to zero and the conditions are stagnated. The Mach number cannot be identically zero, because then there'd be no flow. In the case of isentropic flow through the nozzle, the flow will be accelerated through the subsonic Mach numbers, to the sonic condition at the throat, and then continue accelerating to supersonic Mach numbers.

The static pressure and temperature will also experience continuous decreases over the nozzle. At the inlet, the ratio of the static property to the stagnation property is one. At the throat, the ratios take on the values of the static property over the characteristic property.

```{code-cell}
:tags: [remove-input]
gamma = 1.4
opts["plot_height"] = 300
p2 = figure(
    title=f"Convergent-Divergent Nozzle, Isentropic Acceleration, 𝛾={gamma}",
    y_range=(-4.1, 4.1),
    **opts
)
p2.outline_line_width = 0
p2.axis.visible = False
p2.xaxis.major_tick_line_color = None
p2.xaxis.minor_tick_line_color = None
p2.xaxis.ticker = [0.0]
p2.ygrid.grid_line_color = None
p2.xaxis.major_label_overrides = {0: "Throat"}

r_t = 1
epsilon = 9
r_e = r_t * np.sqrt(epsilon)
theta_n = np.radians(35)
theta_e = np.radians(0.0)

r_upstream = 1.5 * r_t
upstream_center = r_t + r_upstream
x_upstream = np.linspace(-r_upstream + 0.01, 0, 200)
y_upstream = -np.sqrt(r_upstream**2 - x_upstream**2) + upstream_center

r_downstream = 0.382 * r_t
downstream_center = r_t + r_downstream
downstream_stop = r_downstream*np.cos(np.radians(270) + theta_n)
x_downstream = np.linspace(0, downstream_stop, 200)
y_downstream = -np.sqrt(r_downstream**2 - x_downstream**2) + downstream_center

x_n, y_n = x_downstream[-1], y_downstream[-1]
L = r_e / np.tan(np.radians(15))
l = r_t / np.tan(np.radians(15))
L_n = L - l
x_e, y_e = x_n + L_n, r_e

A = np.array([[x_n**2, x_n, 1.0], [x_e**2, x_e, 1.0], [2 * x_e, 1.0, 0.0]])
b = np.array([y_n, y_e, np.tan(theta_e)])
a, b, c = np.linalg.solve(A, b)

x_bell = np.linspace(x_n, x_e, 200)
y_bell = a * x_bell**2 + b * x_bell + c

x = np.hstack((x_upstream, x_downstream, x_bell))
y = np.hstack((y_upstream, y_downstream, y_bell))
p2.line(x, y)
p2.line(x, -y)

A_t = np.pi * r_t**2

A_ratio = np.pi * y**2 / A_t

def area_ratio(M, A_ratio):
    first_term = 2 / (gamma + 1)
    power = (gamma + 1) / (gamma - 1)
    second_term = 1 + (gamma - 1) / 2 * M**2
    return 1 / M**2 * (first_term * second_term)**(power) - A_ratio**2

M_upstream = optimize.root(
    area_ratio,
    x0=np.linspace(0.15, 1.0, x_upstream.shape[0]),
    args=(A_ratio[:x_upstream.shape[0]],)
)
M_downstream_sup = optimize.root(
    area_ratio,
    x0=np.linspace(1.0, 5.0, x_downstream.shape[0] + x_bell.shape[0]),
    args=(A_ratio[x_upstream.shape[0]:])
)

M_sup= np.hstack((M_upstream.x, M_downstream_sup.x))

p3 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0, 4.1),
    x_range=p2.x_range,
    **opts
)
p3.outline_line_width = 0
p3.xaxis.major_tick_line_color = None
p3.xaxis.minor_tick_line_color = None
p3.xaxis.major_label_text_color = None
p3.xaxis.ticker = [0.0]
p3.yaxis.ticker = [1.0]
p3.line(x, M_sup)

p_ratio_sup = (1 + (gamma - 1)/2 * M_sup**2)**(-gamma/(gamma - 1))
p4 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="p/p_t",
    # title="Area-Mach Number Relation",
    y_axis_type="log",
    y_range=(0.008, 1.1),
    x_range=p2.x_range,
    **opts
)
p4.outline_line_width = 0
p4.xaxis.major_tick_line_color = None
p4.xaxis.minor_tick_line_color = None
p4.xaxis.major_label_text_color = None
p4.xaxis.ticker = [0.0]
p4.yaxis.ticker = [1.0, (2 / (gamma + 1))**(gamma / (gamma - 1))]
p4.line(x, p_ratio_sup)

T_ratio_sup = (1 + (gamma - 1)/2 * M_sup**2)**(-1)
p5 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="T/T_t",
    # title="Area-Mach Number Relation",
    y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0.2, 1.1),
    x_range=p2.x_range,
    **opts
)
p5.outline_line_width = 0
p5.xaxis.major_tick_line_color = None
p5.xaxis.minor_tick_line_color = None
p5.xaxis.major_label_text_color = None
p5.xaxis.ticker = [0.0]
p5.yaxis.ticker = [1.0, (2 / (gamma + 1))]
p5.line(x, T_ratio_sup)

show(column(p2, p3, p4, p5))
```

```{note}
There is exactly one value of the pressure ratio $p_e/p_t$ that gives an isentropic acceleration from subsonic to supersonic flow. Under these conditions, the static pressure outside the nozzle must be equal to the static pressure of the flow at the exit plane.

The particular value of $p_e/p_t$ that gives isentropic acceleration depends on the expansion ratio of the nozzle, $A_e/A^*$.
```

## Effect of Pressure Ratio

So, what happens when the pressure ratio over the nozzle is not equal to the value that gives isentropic acceleration? There are a few different cases. The trivial case is that the outlet pressure is equal to the inlet pressure and there is no flow. Not super useful.

Now, imagine reducing the pressure ratio slightly, say to 0.9999. The flow accelerates in the converging section, but for this nozzle it _does not reach $M=1$ at the throat_. If the flow does not reach sonic velocity at the throat, the diverging section acts as a diffuser according to Eq. {eq}`area-velocity-relation`, and the flow is subsonic throughout.

Next, imagine that we continue to reduce the pressure ratio. Eventually, the pressure ratio will be at some value such that the sonic velocity is reached in the throat. However, the static pressure at the throat, given by Eq. {eq}`p-star-over-p-t`, is lower than the static pressure at the exit. Therefore, the diverging section must act as a diffuser and increase the pressure until the outlet.

This second case is shown in the figure below.

```{code-cell}
:tags: [remove-input]
gamma = 1.4
opts["plot_height"] = 300
p6 = figure(
    title=f"Convergent-Divergent Nozzle, Isentropic Subsonic Flow, 𝛾={gamma}",
    y_range=(-4.1, 4.1),
    **opts
)
p6.outline_line_width = 0
p6.axis.visible = False
p6.xaxis.major_tick_line_color = None
p6.xaxis.minor_tick_line_color = None
p6.xaxis.ticker = [0.0]
p6.ygrid.grid_line_color = None
p6.xaxis.major_label_overrides = {0: "Throat"}

p6.line(x, y)
p6.line(x, -y)

M_downstream_sub = optimize.root(
    area_ratio,
    x0=np.linspace(0.01, 0.001, x_downstream.shape[0] + x_bell.shape[0]),
    args=(A_ratio[x_upstream.shape[0]:])
)

M_sub = np.hstack((M_upstream.x, M_downstream_sub.x))

p7 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0, 2.1),
    x_range=p6.x_range,
    **opts
)
p7.outline_line_width = 0
p7.xaxis.major_tick_line_color = None
p7.xaxis.minor_tick_line_color = None
p7.xaxis.major_label_text_color = None
p7.xaxis.ticker = [0.0]
p7.yaxis.ticker = [1.0]
p7.line(x, M_sub)

p_ratio_sub = (1 + (gamma - 1)/2 * M_sub**2)**(-gamma/(gamma - 1))
p8 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="p/p_t",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    y_range=(0, 1.1),
    x_range=p6.x_range,
    **opts
)
p8.outline_line_width = 0
p8.xaxis.major_tick_line_color = None
p8.xaxis.minor_tick_line_color = None
p8.xaxis.major_label_text_color = None
p8.xaxis.ticker = [0.0]
p8.yaxis.ticker = [1.0, (2 / (gamma + 1))**(gamma / (gamma - 1))]
p8.line(x, p_ratio_sub)

show(column(p6, p7, p8))
```

Notice that the Mach number reaches exactly 1.0 at the throat, and the static pressure reaches the value specified by Eq. {eq}`p-star-over-p-t` at the throat. For this particular nozzle, the required pressure ratio to reach sonic flow at the throat is very close to one, approximately $p_e/p_t = 0.997$. The larger the expansion ratio from throat to exit, the smaller the required pressure difference to produce sonic flow at the throat.

(choked-mass-flow-rate)=
## Choked Mass Flow Rate

We can calculate the mass flow rate in the nozzle for this exit pressure condition from the continuity equation. It is most convenient to calculate the mass flow rate at the throat:

```{math}
\dot{m} = \rho^* A^* V^* = \rho^* A^* a^*
```

Now imagine reducing the exit pressure of the nozzle below the value required to obtain sonic flow at the throat. The pressure change is communicated to the rest of the flow by pressure waves that travel at the speed of sound. When the flow reaches the sonic velocity at the throat, downstream pressure changes can no longer be communicated through the throat into the converging section.

Therefore, once sonic flow is reached at the throat, the flow conditions, including the pressure, density, and temperature are fixed no matter what the exit pressure is. Likewise, the conditions in the converging section are fixed (assuming the stagnation conditions are fixed).

From the continuity equation, we see that this results in the mass flow rate becoming constant, regardless of downstream pressure changes! This condition is called **choked flow**. Under this condition, the only way to change the mass flow rate is to change the upstream conditions in the combustion chamber.

## Overexpanded and Underexpanded Flow

Nonetheless, we can continue to change the exit static pressure, for instance, if the nozzle is attached to a rocket ascending through the atmosphere. What happens to the flow in the nozzle in this case?

Remember that the pressure of the flow exiting the nozzle must eventually come to equilibrium with the surrounding pressure. As we change the surrounding pressure, these changes are communicated into the nozzle by sound waves. Once the flow is sonic at the throat, the changes are only communicated partway through the nozzle.

At some location in the nozzle, the velocity of the flow balances the upstream motion of the sound waves. At that location, which depends on the pressure ratio, the sound waves coalesce into a [**normal shock wave**](https://en.wikipedia.org/wiki/Shock_wave#Normal_shocks). A shock wave is an infinitesimally thin region where the flow undergoes an **irreversible** process.

Across the shock wave, the static pressure and temperature are _increased_ and the Mach number is _decreased_ to a subsonic value. The irreversible nature of the process means that the total pressure is _decreased_ and the value of $A^*$ changes across the shock wave as well.

Since the shock wave reduces the Mach number to subsonic values, the remainder of the diverging section downstream of the shock wave functions as a diffuser. This increases the static pressure further until it matches the conditions outside of the exit. An example of this situation is shown in the figure below.

```{code-cell}
:tags: [remove-input]

from bokeh.models import ColumnDataSource, CustomJS, Slider, Dropdown
from textwrap import dedent

shock_location = 4
shock_areas = A_ratio[(x >= 0)]
shock_location_idx = np.argmin(np.abs(shock_areas - shock_location)) + len(x[x < 0])
x_shock_loc = x[shock_location_idx]
y_shock_loc = y[shock_location_idx]

shock_upstream_mask = (A_ratio < shock_location) | (x < 0)
shock_downstream_mask = (A_ratio > shock_location) & (x > 0)

# From compressible flow calculator
# Calculate M_1 from A_shock/A^* = shock_location
# Calculate M_2 from normal shock at M_1
# Calculate A2_A2star from M_2
A2_A2star = 1.38259004
Ae_A2star = epsilon / shock_location * A2_A2star

new_A_ratio = y[shock_downstream_mask]**2 * Ae_A2star / (r_e**2)

M_downstream_shock = np.array([optimize.brentq(area_ratio, 0.01, 0.99, args=(A,)) for A in new_A_ratio])
M_shock = np.hstack((M_sup[shock_upstream_mask], M_downstream_shock))

# Calculate p_t2/p_t1 from normal shock at M_1
pt2_pt1 = 0.34564750
# p_2/p_t1 = p_2/p_t2 * p_t2/p_t1
p_ratio_downstream_shock = (1 + (gamma - 1)/2 * M_downstream_shock**2)**(-gamma/(gamma - 1)) * pt2_pt1
p_ratio_shock = np.hstack((p_ratio_sup[shock_upstream_mask], p_ratio_downstream_shock))

shock = ColumnDataSource(
    data=dict(
        x=[x_shock_loc, x_shock_loc],
        y=[y_shock_loc, -y_shock_loc]
    )
)
nozzle = ColumnDataSource(
    data=dict(
        x=x[(x >= 0)].tolist(),
        y=y[(x >= 0)].tolist(),
        A=shock_areas.tolist()
    )
)

shock_data = ColumnDataSource(
    data=dict(
        x=x.tolist(),
        M=M_shock.tolist(),
        M_sup=M_sup.tolist(),
        p_ratio_sup=p_ratio_sup.tolist(),
        p_ratio=p_ratio_shock.tolist(),
    )
)

update_shock_location = CustomJS(
    args=dict(
        shock=shock,
        nozzle=nozzle,
        g=gamma,
        e=epsilon,
        r_e=r_e,
        shock_data=shock_data,
    ),
    code=dedent("""\
    var nozzle_x = nozzle.data['x'];
    var nozzle_y = nozzle.data['y'];
    var nozzle_A = nozzle.data['A'];
    var f = parseFloat(cb_obj.value);
    var x = shock.data['x'];
    var y = shock.data['y'];
    var val = 1e10;
    var min_i = 0;
    for (var i = 0; i < nozzle_A.length; i++) {
        if (Math.abs(f - nozzle_A[i]) <= val) {
            min_i = i;
            val = Math.abs(f - nozzle_A[i]);
        }
    }
    x[0] = nozzle_x[min_i];
    x[1] = nozzle_x[min_i];
    y[0] = nozzle_y[min_i];
    y[1] = -nozzle_y[min_i];

    shock.change.emit();

    /*
    Much of the following code is adapted from the compressible
    flow calculator by W. Devenport et al., 
    http://www.dept.aoe.vt.edu/~devenpor/aoe3114/calc.html
    */
    function tt0(g,m) {
        return Math.pow((1.+(g-1.)/2.*m*m),-1.)
    }

    function pp0(g,m) {
        return Math.pow((1.+(g-1.)/2.*m*m),-g/(g-1.))
    }

    function rr0(g,m) {
        return Math.pow((1.+(g-1.)/2.*m*m),-1./(g-1.))
    }

    function tts(g,m) {
        return tt0(g,m)*(g/2. + .5)
    }

    function pps(g,m) {
        return pp0(g,m)*Math.pow((g/2. + .5),g/(g-1.))
    }

    function rrs(g,m) {
        return rr0(g,m)*Math.pow((g/2. + .5),1./(g-1.))
    }

    function aas(g,m) {
        return 1./rrs(g,m)*Math.sqrt(1./tts(g,m))/m;
    }

    function m2(g,m1) {
        return Math.sqrt((1. + .5 * (g - 1.) * m1 * m1) / (g * m1 * m1 - .5 * (g - 1.)))
    }

    var mnew=2.0;
    var m=0.0;
    var phi;
    var s=(3. - g) / (1. + g);
    while( Math.abs(mnew-m) > 0.000001) {
        m=mnew;
        phi=aas(g,m);
        mnew=m - (phi - f) / (Math.pow(phi * m,s) - phi / m);
    }
    var M1 = mnew;
    var M2 = m2(g,M1);
    var p2p1=1.+2.*g/(g+1.)*(M1*M1-1.)
    var p02p01=pp0(g,M1)/pp0(g,M2)*p2p1
    var AAS2 = aas(g,M2);
    var AeAs2 = e / f * AAS2;
    var shock_M = shock_data.data['M'];
    var shock_pratio = shock_data.data['p_ratio'];
    var shock_M_sup = shock_data.data['M_sup'];
    var shock_pratio_sup = shock_data.data['p_ratio_sup'];
    var extra_elements = shock_M.length - nozzle_y.length;
    var shock_data_index;
    var A_ratio2;
    var temp_A_ratio = AeAs2 / Math.pow(r_e, 2);
    for (var i = 0; i < nozzle_y.length; i++) {
        shock_data_index = i + extra_elements;
        if (i <= min_i) {
            shock_M[shock_data_index] = shock_M_sup[shock_data_index];
            shock_pratio[shock_data_index] = shock_pratio_sup[shock_data_index];
        } else {
            A_ratio2 = Math.pow(nozzle_y[i], 2) * temp_A_ratio;
            mnew=0.00001;
            m=0.0;
            while( Math.abs(mnew-m) > 0.000001) {
                m=mnew;
                phi=aas(g,m);
                mnew=m - (phi - A_ratio2) / (Math.pow(phi * m,s) - phi / m);
            }
            shock_M[shock_data_index] = mnew;
            shock_pratio[shock_data_index] = p02p01 * pp0(g,mnew);
        }
    }
    shock_data.change.emit()
    """)
)

widget = Slider(start=1, end=9, value=shock_location, step=1e-4, title="Shock Location")
widget.js_on_change('value', update_shock_location)

p9 = figure(
    title=f"Convergent-Divergent Nozzle, Isentropic Subsonic Flow, 𝛾={gamma}",
    y_range=(-4.1, 4.1),
    **opts
)
p9.outline_line_width = 0
p9.axis.visible = False
p9.xaxis.major_tick_line_color = None
p9.xaxis.minor_tick_line_color = None
p9.xaxis.ticker = [0.0]
p9.ygrid.grid_line_color = None
p9.xaxis.major_label_overrides = {0: "Throat"}

p9.line(x, y)
p9.line(x, -y)
p9.line("x", "y", source=shock, line_width=4)

p10 = figure(
    # x_axis_label="Area Ratio, A/A*",
    y_axis_label="Mach Number, M",
    # title="Area-Mach Number Relation",
    # y_axis_type="log",
    # x_range=(0, 10), y_range=(0.05, 4.25),
    y_range=(0, 4.1),
    x_range=p9.x_range,
    **opts
)
p10.outline_line_width = 0
p10.xaxis.major_tick_line_color = None
p10.xaxis.minor_tick_line_color = None
p10.xaxis.major_label_text_color = None
p10.xaxis.ticker = [0.0]
p10.yaxis.ticker = [1.0]

p10.line('x', 'M', source=shock_data, legend_label="Shock in Nozzle", color=next(colors))
p10.line(x, M_sub, legend_label="Isentropic Deceleration", color=next(colors))
p10.line(x, M_sup, legend_label="Isentropic Acceleration", color=next(colors))
p10.legend.location = "center_right"

colors = itertools.cycle(palette[10])
p11 = figure(
    y_axis_label="p/p_t",
    # y_axis_type="log",
    y_range=(0, 1.1),
    x_range=p9.x_range,
    **opts
)
p11.outline_line_width = 0
p11.xaxis.major_tick_line_color = None
p11.xaxis.minor_tick_line_color = None
p11.xaxis.major_label_text_color = None
p11.xaxis.ticker = [0.0]
p11.yaxis.ticker = [1.0, (2 / (gamma + 1))**(gamma / (gamma - 1))]
p11.line('x', 'p_ratio', source=shock_data, legend_label="Shock in Nozzle", color=next(colors))
p11.line(x, p_ratio_sub, legend_label="Isentropic Deceleration", color=next(colors))
p11.line(x, p_ratio_sup, legend_label="Isentropic Acceleration", color=next(colors))
p11.legend.location = "center_right"

show(column(widget, p9, p10, p11))
# show(column(p9, p10, p11))
```

This condition of the nozzle is called **overexpanded** because the flow in the nozzle expands to a pressure below the outside pressure, and requires a shock wave to increase the pressure. If you could cut off the nozzle just upstream of the shock wave, you would have a perfectly expanded nozzle. However, since the nozzle is longer than that, the flow tries to continue expanding and can't.

As the downstream pressure decreases further, the shock moves further and further downstream. Eventually, the normal shock will stand exactly at the exit. The pressure ratio that produces this situation is still larger than the pressure ratio that gives isentropic acceleration throughout the nozzle.

Thus, we can still continue reducing the outside pressure and there will continue to be an irreversible shock that is required to adjust the exit pressure to the outside pressure. When the outside pressure is lower than the pressure that gives a normal shock at the exit, the shock will become angled into an [**oblique shock**](https://en.wikipedia.org/wiki/Oblique_shock).

Oblique shock waves cause the flow to turn, which then requires a [**Prandtl-Meyer expansion fan**](https://en.wikipedia.org/wiki/Prandtl%E2%80%93Meyer_expansion_fan) to turn back to the direction of flight. This pattern repeats in a phenomenon called a [**shock diamond**](https://en.wikipedia.org/wiki/Shock_diamond).

```{figure} ../images/Lockheed_Martin_F-22A_Raptor_JSOH.jpg
---
width: 75%
align: center
---
F-22A Raptor fighter jet with shock diamonds visible in the engine exhaust. Credit: [Wikimedia](https://commons.wikimedia.org/wiki/File:Lockheed_Martin_F-22A_Raptor_JSOH.jpg) under the [CC-BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) license.
```

Finally, continued reduction of the exterior pressure will result in the ratio $p_e/p_t$ dropping below the value for isentropic acceleration. In this case, the flow is called **underexpanded** because the pressure of the flow at the exit plane is higher than the exterior pressure, and it could have been expanded more to match the outside pressure.

To match the exterior pressure, the flow must exit the nozzle through a series of expansion waves to reduce the pressure. These expansion waves turn the flow and to straighten the flow again requires oblique shock waves. Thus, the pattern for underexpanded flow is the same as for overexpanded flow, but it starts with the expansion wave instead of the shock wave.
