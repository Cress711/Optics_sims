import numpy as np

def compute_field(
    wavelength,
    slit_width=50e-6,
    screen_distance=0.1,
    grid_size=200,
    screen_size=0.01,
    aperture_points=100
):
    k = 2 * np.pi / wavelength

    x = np.linspace(-screen_size/2, screen_size/2, grid_size)
    y = np.linspace(-screen_size/2, screen_size/2, grid_size)
    X, Y = np.meshgrid(x, y)

    #dzielimy szczeliny na konkretną ilość punktów z których powstają nowe fale
    xs = np.linspace(-slit_width/2, slit_width/2, aperture_points)

    #zespolona tablica
    E = np.zeros((grid_size, grid_size), dtype=complex)

    dx = slit_width / aperture_points  # element całki

    #dla każdego elementu xs liczymy całkę
    for x_s in xs:
        #odległość punktu na szczelinie od punktu na ekranie
        r = np.sqrt((X - x_s)**2 + Y**2 + screen_distance**2)

        #dodajemy policzony element pola do tablicy E
        E += np.exp(1j * k * r) / r * dx

    return E