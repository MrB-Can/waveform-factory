import numpy as np

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
    waveform = np.exp(1j * 2 * np.pi * frequency * t + phase_shift)
    waveform *= np.exp(-t**2 / 2)

    if invert:
        waveform = waveform.conjugate()

    waveform = amplitude * np.real(waveform) + offset

    return waveform
