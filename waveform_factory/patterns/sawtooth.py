import numpy as np
from scipy.signal import sawtooth

def generate_sawtooth(frequency: float, amplitude: float, length: float, sample_rate: int,
                      phase_shift: float = 0, offset: float = 0, invert: bool = False):
    """
    Generates a sawtooth wave.

    :param frequency: The frequency of the sawtooth wave in Hz
    :param amplitude: The amplitude of the sawtooth wave
    :param length: The length of the sawtooth wave in seconds
    :param sample_rate: The sample rate for the sawtooth wave in Hz. Default is 44100Hz (standard audio CD sample rate)
    :param phase_shift: The phase shift for the sawtooth wave in radians. Default is 0
    :param offset: The constant to be added to the waveform to move it up or down along the amplitude axis
    :param invert: A boolean indicating whether to invert the waveform. If True, the waveform is inverted. Default is False
    :return: A numpy array representing the generated sawtooth wave
    """

    # Calculate the time variable
    t = np.linspace(0, length, int(sample_rate * length), False)

    # Generate the sawtooth wave
    sawtooth_wave = amplitude * sawtooth(2 * np.pi * (frequency * t + phase_shift/ (2*np.pi)))

    # Add the offset
    sawtooth_wave += offset

    # Invert the waveform if the invert parameter is True
    if invert:
        sawtooth_wave = -sawtooth_wave

    return sawtooth_wave
