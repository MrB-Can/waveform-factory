import numpy as np
from scipy.signal import sawtooth

def generate_sawtooth_wave(frequency: float, amplitude: float, length: float, sample_rate: int = 44100,
                           phase_shift: float = 0.0, offset: float = 0.0, invert: bool = False) -> np.ndarray:
    """
    Generates a sawtooth wave.

    :param frequency: The frequency of the sawtooth wave in Hz.
    :param amplitude: The amplitude of the sawtooth wave.
    :param length: The length of the sawtooth wave in seconds.
    :param sample_rate: The sample rate for the sawtooth wave. Default is 44100Hz (standard audio CD sample rate).
    :param phase_shift: The phase shift of the sawtooth wave in radians. Default is 0.0.
    :param offset: The DC offset of the sawtooth wave. Default is 0.0.
    :param invert: A boolean indicating whether the sawtooth wave should be inverted or not. Default is False.
    :return: A numpy array representing the generated sawtooth wave.
    """

    t = np.linspace(0, length, int(sample_rate * length), False)  # time variable
    waveform = sawtooth(2 * np.pi * frequency * t + phase_shift)

    if invert:
        waveform *= -1

    waveform = amplitude * waveform + offset

    return waveform
