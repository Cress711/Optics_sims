import numpy as np

def compute_field_I(
    wavelength,
    x1=-0.5, y1=0.0,
    x2=0.5, y2=0.0,
    grid_size=2000,
    screen_size=0.1
    #domyślnie źródła poza ekranem!!! - najlepszy efekt
):
    x = np.linspace(-screen_size, screen_size, grid_size)
    y = np.linspace(-screen_size, screen_size, grid_size)
    X, Y = np.meshgrid(x, y)

    k = 2 * np.pi / wavelength

    r1 = np.sqrt((X - x1)**2 + (Y - y1)**2)
    r2 = np.sqrt((X - x2)**2 + (Y - y2)**2)

    E1 = np.exp(1j * k * r1)
    E2 = np.exp(1j * k * r2)

    return E1 + E2