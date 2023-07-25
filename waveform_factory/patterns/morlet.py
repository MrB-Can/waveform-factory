import numpy as np
from matplotlib import pyplot as plt

def generate_morlet_wave(frequency: float, amplitude: float, length: float, sample_rate: int = 44100,
                         phase_shift: float = 0.0, offset: float = 0.0, invert: bool = False) -> np.ndarray:
    """
    Generates a Morlet wavelet.

    :param frequency: The central frequency of the cosine wave in the Morlet wavelet in Hz.
    :param amplitude: The amplitude of the Morlet wavelet.
    :param length: The length of the Morlet wavelet in seconds.
    :param sample_rate: The sample rate for the Morlet wavelet. Default is 44100Hz (standard audio CD sample rate).
    :param phase_shift: The phase shift of the Morlet wavelet in radians. Default is 0.0.
    :param offset: The DC offset of the Morlet wavelet. Default is 0.0.
    :param invert: A boolean indicating whether the Morlet wavelet should be inverted or not. Default is False.
    :return: A numpy array representing the generated Morlet wavelet.
    """

    t = np.linspace(0, length, int(sample_rate * length), False)  # time variable
    morlet_wave = amplitude * np.exp(1j * 2 * np.pi * frequency * t + phase_shift)  # Complex sinusoid
    morlet_wave *= np.exp(-((t - length / 2) ** 2) / (2 * (length / 8) ** 2))  # Gaussian window

    if invert:
        morlet_wave = -morlet_wave

    morlet_wave += offset  # Apply DC offset

    return morlet_wave
