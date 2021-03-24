import numpy as np
import shapely.geometry as sg
import shapely.ops as so
import matplotlib.pyplot as plt
import shapely.affinity as sa
from matplotlib.patches import FancyArrowPatch as Arrow

plt.rc('font', size=24)          # controls default text sizes
plt.rc('axes', titlesize=24)     # fontsize of the axes title
plt.rc('axes', labelsize=24)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=24)    # fontsize of the tick labels
plt.rc('ytick', labelsize=24)    # fontsize of the tick labels
plt.rc('legend', fontsize=24)    # legend fontsize
plt.rc('figure', titlesize=24)  # fontsize of the figure title

exam = 0
sol = 0
if exam:
    fig, axs2 = plt.subplots(1,2)
    axs = axs2[0]
    axs2 = axs2[1]

    #plot obstacles
    rect = sg.Polygon([(-10,0),(-10,-10),(10,-10),(10,0)])
    circle = sg.Point((0,0)).buffer(6)
    t = sg.Polygon([(6.5,0),(10,-4),(10,0)])
    t2 = sg.Polygon([(-10,-6),(-10,-10),(0,-10)])
    obs_bottom = rect.difference(circle).difference(t).difference(t2)
    xs, ys = obs_bottom.exterior.xy
    axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')
    s = sg.Polygon([(-10,10),(10,10),(10,7),(0,8),(-5,9),(-7,7)])
    xs, ys = s.exterior.xy
    axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')
    s = sg.Polygon([(-7,3),(-7,5),(-9,6),(-10,4)])
    xs, ys = s.exterior.xy
    axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')

    #plot robot
    arm_c = sg.Point((0,0)).buffer(0.2)
    xs, ys = arm_c.exterior.xy
    axs.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    arm = sg.Polygon([(0,0.2),(0,-0.2),(5,-0.2),(5,0.2)])
    arm = sa.rotate(arm,36.87,origin=(0,0),use_radians=False)
    xs, ys = arm.exterior.xy
    axs.fill(xs, ys, alpha=0.5, fc='b', ec='none')
    arm_c2 = sg.Point((4,3)).buffer(0.2)
    xs, ys = arm_c2.exterior.xy
    axs.fill(xs, ys, alpha=1.0, fc='k', ec='none')

    # add angle and distance markers
    x = np.linspace(0, 4, 500)
    y = 0*x
    axs.plot(x, y, 'k', dashes=[2, 2])
    x = np.linspace(4, 6, 500)
    y = np.linspace(3, 4.5, 500)
    axs.plot(x, y, 'k', dashes=[2, 2])
    style="Simple,tail_width=0.5,head_width=4,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    a = Arrow((1.5,0), (1,1),connectionstyle="arc3,rad=.5", **kw)
    axs.add_patch(a)
    a = Arrow((4.5,3), (5.5,3.75), **kw)
    axs.add_patch(a)
    axs.text(5, 2.8, "d", fontsize=24)
    axs.text(1.6, 0.4, r"$\theta$", fontsize=24)

    # format
    xrange = [-10, 10]
    yrange = [-10, 10]
    axs.set_xlim(*xrange)
    axs.set_xticks(range(*xrange) + [xrange[-1]])
    axs.set_ylim(*yrange)
    axs.set_yticks(range(*yrange) + [yrange[-1]])
    axs.set_aspect(1)
    axs.grid(True)
    axs.set_ylabel("y (meters)")
    axs.set_xlabel("x (meters)")

    # plot grid for solution (and sol if asked) and format
    if sol:
        s = sg.Polygon([(1,0),(2,0),(2,-np.pi),(1,-np.pi)])
        xs, ys = s.exterior.xy
        axs2.fill(xs, ys, alpha=0.5, fc='k', ec='none')
    unit   = 0.25
    r_tick = np.arange(-1, 1+unit, unit)
    r_label = [r"$-\pi$", r"$-\frac{3\pi}{4}$", r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$",r"$+\frac{\pi}{4}$",r"$+\frac{\pi}{2}$", r"$+\frac{3\pi}{4}$", r"$\pi$"]
    axs2.set_yticks(r_tick*np.pi)
    axs2.set_yticklabels(r_label, fontsize=24)
    unit = 0.2
    axs2.set_xticks(np.arange(0, 2+unit, unit))
    xrange = [0, 2]
    yrange = [-np.pi, np.pi]
    axs2.set_xlim(*xrange)
    axs2.set_ylim(*yrange)
    # axs2.set_aspect(1)
    axs2.grid(True)
    axs2.set_ylabel(r"$\theta$" + " (radians)")
    axs2.set_xlabel("d (meters)")

else:
    fig, axs2 = plt.subplots(1,2)
    axs = axs2[0]
    axs2 = axs2[1]

    #plot obstacle
    rect = sg.Polygon([(3,-3),(8,-3),(8,3),(3,3)])
    t = sg.Polygon([(8,3),(8,-3),(5,0)])
    obs_bottom = rect.difference(t)
    xs, ys = obs_bottom.exterior.xy
    axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')

    #plot robot
    arm_c = sg.Point((0,0)).buffer(0.2)
    xs, ys = arm_c.exterior.xy
    axs.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    arm = sg.Polygon([(0,0.2),(0,-0.2),(3*np.sqrt(2),-0.2),(3*np.sqrt(2),0.2)])
    arm = sa.rotate(arm,135,origin=(0,0),use_radians=False)
    xs, ys = arm.exterior.xy
    axs.fill(xs, ys, alpha=0.5, fc='b', ec='none')
    x = np.cos(135.0/180*np.pi)*3*np.sqrt(2)
    y = np.sin(135.0/180*np.pi)*3*np.sqrt(2)
    arm_c2 = sg.Point((x,y)).buffer(0.2)
    xs, ys = arm_c2.exterior.xy
    axs.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    arm2 = sg.Polygon([(x,y+0.2),(x,y-0.2),(x+np.sqrt(8),y-0.2),(x+np.sqrt(8),y+0.2)])
    arm2 = sa.rotate(arm2,180,origin=(x,y),use_radians=False)
    xs, ys = arm2.exterior.xy
    axs.fill(xs, ys, alpha=0.5, fc='b', ec='none')

    # add angle markers
    xs = np.linspace(0, 3, 500)
    ys = 0*xs
    axs.plot(xs, ys, 'k', dashes=[2, 2])
    xs = np.linspace(x, x-1.3, 500)
    ys = np.linspace(y, y+1.3, 500)
    axs.plot(xs, ys, 'k', dashes=[2, 2])
    axs.set_ylabel("y (meters)")
    axs.set_xlabel("x (meters)")
    style="Simple,tail_width=0.5,head_width=4,head_length=8"
    kw = dict(arrowstyle=style, color="k")
    a = Arrow((0.5,0), (-0.5,0.5),connectionstyle="arc3,rad=.5", **kw)
    axs.add_patch(a)
    a = Arrow((-4,4), (-4,3),connectionstyle="arc3,rad=.5", **kw)
    axs.add_patch(a)

    # format
    xrange = [-8, 8]
    yrange = [-8, 8]
    axs.set_xlim(*xrange)
    axs.set_xticks(range(*xrange) + [xrange[-1]])
    axs.set_ylim(*yrange)
    axs.set_yticks(range(*yrange) + [yrange[-1]])
    axs.set_aspect(1)
    axs.grid(True)
    axs.text(0.3, 0.5, r"$\theta_1$", fontsize=24)
    axs.text(-4.8, 3.5, r"$\theta_2$", fontsize=24)

    # plot grid for solution and solution cirlces
    a = sg.Point((np.pi/6,np.pi/6))
    b = sg.Point((-np.pi/5,-np.pi/7))
    c = sg.Point((9*np.pi/10,0.1))
    d = sg.Point((np.pi/4+0.2,-np.pi/2))
    e = sg.Point((-3*np.pi/4,3*np.pi/4))
    xs, ys = a.buffer(0.1).exterior.xy
    axs2.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    axs2.text(a.x+0.1, a.y+0.1, "a", fontsize=24)
    xs, ys = b.buffer(0.1).exterior.xy
    axs2.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    axs2.text(b.x+0.1, b.y+0.1, "b", fontsize=24)
    xs, ys = c.buffer(0.1).exterior.xy
    axs2.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    axs2.text(c.x+0.1, c.y+0.1, "c", fontsize=24)
    xs, ys = d.buffer(0.1).exterior.xy
    axs2.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    axs2.text(d.x+0.1, d.y+0.1, "d", fontsize=24)
    xs, ys = e.buffer(0.1).exterior.xy
    axs2.fill(xs, ys, alpha=1.0, fc='k', ec='none')
    axs2.text(e.x+0.1, e.y+0.1, "e", fontsize=24)
    unit   = 0.25
    r_tick = np.arange(-1, 1+unit, unit)
    r_label = [r"$-\pi$", r"$-\frac{3\pi}{4}$", r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$",r"$+\frac{\pi}{4}$",r"$+\frac{\pi}{2}$", r"$+\frac{3\pi}{4}$", r"$\pi$"]
    axs2.set_yticks(r_tick*np.pi)
    axs2.set_yticklabels(r_label, fontsize=24)
    axs2.set_xticks(r_tick*np.pi)
    axs2.set_xticklabels(r_label, fontsize=24)
    xrange = [-np.pi, np.pi]
    yrange = [-np.pi, np.pi]
    axs2.set_xlim(*xrange)
    axs2.set_ylim(*yrange)
    axs2.set_aspect(1)
    axs2.grid(True)
    axs2.set_xlabel(r"$\theta_1$" + " (radians)")
    axs2.set_ylabel(r"$\theta_2$" + " (radians)")

plt.show()

