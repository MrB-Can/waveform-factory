import numpy as np
from scipy.signal import sawtooth

def generate_triangle_wave(frequency: float, amplitude: float, length: float, sample_rate: int = 44100,
                           phase_shift: float = 0.0, offset: float = 0.0, width: float = 0.5, invert: bool = False) -> np.ndarray:
    """
    Generates a triangle wave.

    :param frequency: The frequency of the triangle wave in Hz.
    :param amplitude: The amplitude of the triangle wave.
    :param length: The length of the triangle wave in seconds.
    :param sample_rate: The sample rate for the triangle wave. Default is 44100Hz (standard audio CD sample rate).
    :param phase_shift: The phase shift of the triangle wave in radians. Default is 0.0.
    :param offset: The DC offset of the triangle wave. Default is 0.0.
    :param width: Determines the point at which the waveform reaches its maximum value. Default is 0.5 (symmetric triangle).
    :param invert: A boolean indicating whether the triangle wave should be inverted or not. Default is False.
    :return: A numpy array representing the generated triangle wave.
    """

    t = np.linspace(0, length, int(sample_rate * length), False)  # time variable
    waveform = sawtooth(2 * np.pi * frequency * t + phase_shift, width)

    if invert:
        waveform *= -1

    waveform = amplitude * waveform + offset

    return waveform
