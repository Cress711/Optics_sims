from Diffraction.field_sim import compute_field
import numpy as np
import matplotlib.pyplot as plt

def wavelength_to_rgb(wavelength_nm, gamma=0.8):
    if wavelength_nm < 380 or wavelength_nm > 770:
        return (0, 0, 0)

    w = wavelength_nm
    if w < 440:
        r, g, b = -(w - 440)/(440-380), 0, 1
    elif w < 490:
        r, g, b = 0, (w-440)/(490-440), 1
    elif w < 510:
        r, g, b = 0, 1, -(w-510)/(510-490)
    elif w < 580:
        r, g, b = (w-510)/(580-510), 1, 0
    elif w < 645:
        r, g, b = 1, -(w-645)/(645-580), 0
    else:
        r, g, b = 1, 0, 0

    if w < 420:
        factor = 0.3 + 0.7*(w-380)/(420-380)
    elif w < 645:
        factor = 1
    else:
        factor = 0.3 + 0.7*(770-w)/(770-645)

    return tuple((np.array([r, g, b]) * factor) ** gamma)


def main():
    Wavelength = 1550e-9

    E = compute_field(wavelength=Wavelength)
    I = np.abs(E)**2

    #normalizacja jasności
    I_norm = I / I.max()

    #kolor z długości fali
    rgb = wavelength_to_rgb(Wavelength * 1e9)

    image = np.zeros(I.shape + (3,))
    for i in range(3):
        image[..., i] = I_norm * rgb[i]

    plt.imshow(image)
    plt.title(f"Dyfrakcja – {Wavelength*1e9:.0f} nm")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()