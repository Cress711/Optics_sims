from Diffraction.OneSlitDiff import compute_field_D
from Intereference.interference_2D import compute_field_I
import numpy as np
import matplotlib.pyplot as plt

def wavelength_to_rgb(wavelength_nm, gamma=0.8):
    if wavelength_nm < 380 or wavelength_nm > 770:
        return (1, 1, 1) #biały dla niewidzialnych długości fal

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
    Wavelength = 420 #nm
    Slit_width = 50 #um
    Grid_size = 1000
    Intensity_plot = False
    Amplitude_plot = False


    ###Tu zmieniamy co chcemy rysować###
    ###Zakomentować czego nie chcemy###

    #E = compute_field_I(wavelength=Wavelength, grid_size=1000) #interferencja
    E = compute_field_D(wavelength=Wavelength*1e-9, slit_width=Slit_width*1e-6, grid_size=Grid_size) #dyfrakcja

    Intensity_plot = True
    #Amplitude_plot = True

    #####################################

    if Intensity_plot:
        I = np.abs(E)**2
        #normalizacja jasności
        I_norm = I/ I.max()

        #kolor z długości fali
        rgb = wavelength_to_rgb(Wavelength)

        #tworzenie obrazu RGB
        image = np.zeros(I.shape + (3,))
        for i in range(3):
            image[..., i] = I_norm * rgb[i]

        plt.imshow(image)
        plt.title(f"{Wavelength:.0f} nm")
        plt.axis("off")
        plt.show()
    elif Amplitude_plot:
        #E = E.real
        E = np.abs(E)
        E_norm = E/ E.max()
        #kolor z długości fali
        rgb = wavelength_to_rgb(Wavelength)

        #tworzenie obrazu RGB
        image = np.zeros(E.shape + (3,))
        for i in range(3):
            image[..., i] = E_norm * rgb[i]

        plt.imshow(image)
        plt.title(f"{Wavelength:.0f} nm")
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    main()