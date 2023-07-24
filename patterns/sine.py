import numpy as np

def generate_sine_wave(frequency: float, amplitude: float, length: float, sample_rate: int = 44100,
                        phase_shift: float = 0.0, offset: float = 0.0, invert: bool = False):
    """
    Generates a sine wave.

    :param frequency: The frequency of the sine wave in Hz
    :param amplitude: The amplitude of the sine wave
    :param length: The length of the sine wave in seconds
    :param sample_rate: The sample rate for the sine wave. Default is 44100Hz (standard audio CD sample rate)
    :param phase_shift: Phase shift for the sine wave in radians. Default is 0.
    :param offset: Offset to be added to the sine wave. Default is 0.
    :param invert: If True, the sine wave will be inverted. Default is False.
    :return: A numpy array representing the generated sine wave
    """
    t = np.linspace(0, length, int(sample_rate * length), False)  # time variable
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
    sine_wave += offset
    if invert:
        sine_wave *= -1

    return sine_wave
