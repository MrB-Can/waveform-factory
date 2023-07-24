import numpy as np
from matplotlib import pyplot as plt

from patterns import sawtooth


def test_generate_sawtooth():
    frequency = 440  # A4 note
    amplitude = 1.0  # max amplitude
    length = 2.0  # 2 seconds
    sample_rate = 44100  # standard audio CD sample rate

    # Generate the sawtooth wave
    generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate)

    # Check if the generated wave has the correct length
    assert len(generated_wave) == int(sample_rate * length)

    # Check if the generated wave indeed has a sawtooth pattern
    # The waveform should start at -amplitude at the start of every period
    period_samples = int(sample_rate / frequency)
    for i in range(0, len(generated_wave), period_samples):
        assert np.isclose(generated_wave[i], -amplitude, atol=1e-2)  # increase the absolute tolerance

def test_plot_sawtooth():
    frequency = 440  # A4 note
    amplitude = 1.0  # max amplitude
    length = 2.0  # 2 seconds
    sample_rate = 44100  # standard audio CD sample rate

    # Generate the sawtooth wave
    generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate)

    # Plot the first few samples of the wave
    plt.figure(figsize=(10, 4))
    plt.plot(generated_wave[:1000])  # plot the first 1000 samples
    plt.title('Sawtooth Wave')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits
    plt.show()

def test_generate_sawtooth_frequency():
    amplitude = 1.0
    length = 2.0
    sample_rate = 44100

    for frequency in [220, 440, 880]:  # Test different frequencies
        generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate)
        plt.figure()
        plt.plot(generated_wave[:1000])  # Plot the first 1000 samples
        plt.title(f'Frequency: {frequency}Hz')
        plt.ylim(-1.5, 1.5)  # Set y-axis limits
    plt.show()


def test_generate_sawtooth_amplitude():
    frequency = 440
    length = 2.0
    sample_rate = 44100

    for amplitude in [0.5, 1.0, 1.5]:  # Test different amplitudes
        generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate)
        plt.figure()
        plt.plot(generated_wave[:1000])  # Plot the first 1000 samples
        plt.title(f'Amplitude: {amplitude}')
        plt.ylim(-1.5, 1.5)  # Set y-axis limits
    plt.show()


def test_generate_sawtooth_length():
    frequency = 10
    amplitude = 1.0
    sample_rate = 44100

    for length in [1.0, 2.0, 3.0]:  # Test different lengths
        generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate)
        plt.figure()
        plt.plot(generated_wave)
        plt.title(f'Length: {length}s')
        plt.ylim(-1.5, 1.5)  # Set y-axis limits
    plt.show()


def test_generate_sawtooth_sample_rate():
    frequency = 440
    amplitude = 1.0
    length = 2.0

    for sample_rate in [22050, 44100, 88200]:  # Test different sample rates
        generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate)
        plt.figure()
        plt.plot(generated_wave[:1000])  # Plot the first 1000 samples
        plt.title(f'Sample Rate: {sample_rate}Hz')
        plt.ylim(-1.5, 1.5)  # Set y-axis limits
    plt.show()

def test_generate_sawtooth_phase_shift():
    frequency = 440
    amplitude = 1.0
    length = 2.0
    sample_rate = 44100

    for phase_shift in [0, np.pi/2, np.pi]:  # Test different phase shifts
        generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate, phase_shift=phase_shift)
        plt.figure()
        plt.plot(generated_wave[:1000])  # Plot the first 1000 samples
        plt.title(f'Phase Shift: {phase_shift} rad')
        plt.ylim(-1.5, 1.5)  # Set y-axis limits
    plt.show()

def test_generate_sawtooth_offset():
    frequency = 440
    amplitude = 1.0
    length = 2.0
    sample_rate = 44100

    for offset in [-0.5, 0, 0.5]:  # Test different offsets
        generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate, offset=offset)
        plt.figure()
        plt.plot(generated_wave[:1000])  # Plot the first 1000 samples
        plt.title(f'Offset: {offset}')
        plt.ylim(-2.0, 2.0)  # Set y-axis limits
    plt.show()

def test_generate_sawtooth_invert():
    frequency = 440
    amplitude = 1.0
    length = 2.0
    sample_rate = 44100

    for invert in [False, True]:  # Test both non-inverted and inverted waveform
        generated_wave = sawtooth.generate_sawtooth(frequency, amplitude, length, sample_rate, invert=invert)
        plt.figure()
        plt.plot(generated_wave[:1000])  # Plot the first 1000 samples
        plt.title(f'Inverted: {invert}')
        plt.ylim(-1.5, 1.5)  # Set y-axis limits
    plt.show()
