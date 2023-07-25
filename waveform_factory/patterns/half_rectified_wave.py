import numpy as np

def generate_half_rectified_wave(frequency: float, amplitude: float, length: float, sample_rate: int = 44100,
                                 phase_shift: float = 0.0, offset: float = 0.0, invert: bool = False) -> np.ndarray:
    """
    Generates a half-wave rectified sine wave.

    :param frequency: The frequency of the wave in Hz.
    :param amplitude: The amplitude of the wave.
    :param length: The length of the wave in seconds.
    :param sample_rate: The sample rate for the wave. Default is 44100Hz (standard audio CD sample rate).
    :param phase_shift: The phase shift of the wave in radians. Default is 0.0.
    :param offset: The DC offset of the wave. Default is 0.0.
    :param invert: A boolean indicating whether the wave should be inverted or not. Default is False.
    :return: A numpy array representing the generated wave.
    """

    t = np.linspace(0, length, int(sample_rate * length), False)  # time variable
    waveform = np.sin(2 * np.pi * frequency * t + phase_shift)
    waveform[waveform < 0] = 0  # half-wave rectification

    if invert:
        waveform = -waveform

    waveform = amplitude * waveform + offset

    return waveform
