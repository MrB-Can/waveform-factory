import numpy as np

def generate_stepped_wave(step_height: float, step_length: int, total_steps: int, steps_up_ratio: float,
                          length: float, sample_rate: int = 44100, offset: float = 0.0, smoothing_factor: float = 0.0):
    """
    Generates a stepped wave (staircase) with added features.

    :param step_height: The height of each step in the wave.
    :param step_length: The length (in samples) of each step in the wave.
    :param total_steps: The total number of steps in each cycle.
    :param steps_up_ratio: The ratio of upward steps to the total number of steps.
    :param length: The total length of the wave in seconds.
    :param sample_rate: The sample rate for the wave. Default is 44100Hz (standard audio CD sample rate).
    :param offset: The DC offset of the wave. Default is 0.0.
    :param smoothing_factor: The smoothing factor for the edges of the steps. Default is 0.0 (no smoothing).
    :return: A generator that yields samples of the generated wave.
    """

    steps_up = int(total_steps * steps_up_ratio)
    steps_down = total_steps - steps_up

    total_samples = int(sample_rate * length)
    num_cycles = total_samples // (step_length * total_steps)
    remaining_samples = total_samples % (step_length * total_steps)

    single_step = np.concatenate([
        np.linspace(i * step_height, (i + 1) * step_height, step_length) for i in range(steps_up)] +
        [np.linspace((total_steps - i - 1) * step_height, total_steps * step_height - i * step_height, step_length)
         for i in range(steps_down)]
    )

    # Apply smoothing to the edges of the steps
    if smoothing_factor > 0.0:
        smooth_samples = int(smoothing_factor * step_length)
        smooth_window = np.hanning(smooth_samples * 2)[:smooth_samples]  # Hanning window for smoothing
        smooth_window /= np.sum(smooth_window)  # Normalize the window

        for i in range(1, steps_up + steps_down):
            single_step[(i * step_length) - smooth_samples:i * step_length] *= smooth_window
            single_step[i * step_length:(i * step_length) + smooth_samples] *= smooth_window[::-1]

    waveform = np.tile(single_step, num_cycles)
    waveform = np.concatenate((waveform, single_step[:remaining_samples]))  # Add remaining samples

    waveform += offset  # Apply DC offset

    return waveform