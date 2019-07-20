import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_expsum(z):
    """
    Plot the exponential sum function.
    """
    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(z.real, z.imag, 'k')
    ax.grid(color='0.9')
    ax.set_aspect('equal')
    ax.set_frame_on(False)
    ax.tick_params(color='0.9')


def animate_expsum(z):
    """
    Animate the exponential sum function.
    """
    fig, ax = plt.subplots(tight_layout=True)
    ax.grid(color='0.9')
    ax.set_aspect('equal')
    ax.set_xlim(min(z.real) * 1.1, max(z.real) * 1.1)
    ax.set_ylim(min(z.imag) * 1.1, max(z.imag) * 1.1)
    ax.set_frame_on(False)
    ax.tick_params(color='0.9')
    ln, = ax.plot([], [], 'm')

    x, y = [], []

    def animate(i):
        x.append(z.real[i])
        y.append(z.imag[i])
        ln.set_data(x, y)
        return ln,

    anim = FuncAnimation(fig, animate, interval=2, blit=True)   # noqa: F841


def show():
    """
    Display Matplotlib figure.
    """
    plt.show()
