import numpy as np
from matplotlib import pyplot as plt
from patterns.sine import generate_sine_wave

class SineWaveTest:
    def run_tests(self):
        self.test_generate_sine_wave()

    def test_generate_sine_wave(self):
        frequency = 440
        amplitude = 1.0
        length = 2.0
        sample_rate = 44100

        # Generate the sine wave
        generated_wave = generate_sine_wave(frequency, amplitude, length, sample_rate)

        # Check if the generated wave has the correct length
        assert len(generated_wave) == int(sample_rate * length)

        plt.figure(figsize=(18, 12))  # Adjust the figure size to maintain the same ratio and increase the resolution
        plt.plot(generated_wave[:1000])
        plt.title('Sine Wave')
        plt.show()


class SineWaveInvertTest:
    def run_tests(self):
        self.test_generate_sine_wave_invert()

    def test_generate_sine_wave_invert(self):
        frequency = 440
        amplitude = 1.0
        length = 2.0
        sample_rate = 44100

        for invert in [False, True]:
            generated_wave = generate_sine_wave(frequency, amplitude, length, sample_rate, invert=invert)

            plt.figure(figsize=(18, 12))
            plt.plot(generated_wave[:1000])
            plt.title(f'Sine Wave Invert: {invert}')
            plt.show()


class SineWaveOffsetTest:
    def run_tests(self):
        self.test_generate_sine_wave_offset()

    def test_generate_sine_wave_offset(self):
        frequency = 440
        amplitude = 1.0
        length = 2.0
        sample_rate = 44100

        for offset in [-0.5, 0, 0.5]:
            generated_wave = generate_sine_wave(frequency, amplitude, length, sample_rate, offset=offset)

            plt.figure(figsize=(18, 12))
            plt.plot(generated_wave[:1000])
            plt.title(f'Sine Wave Offset: {offset}')
            plt.show()


class SineWavePhaseShiftTest:
    def run_tests(self):
        self.test_generate_sine_wave_phase_shift()

    def test_generate_sine_wave_phase_shift(self):
        frequency = 440
        amplitude = 1.0
        length = 2.0
        sample_rate = 44100

        for phase_shift in [0, np.pi / 2, np.pi]:
            generated_wave = generate_sine_wave(frequency, amplitude, length, sample_rate, phase_shift=phase_shift)

            plt.figure(figsize=(18, 12))
            plt.plot(generated_wave[:1000])
            plt.title(f'Sine Wave Phase Shift: {phase_shift}')
            plt.show()


class SineWaveSampleRateTest:
    def run_tests(self):
        self.test_generate_sine_wave_sample_rate()

    def test_generate_sine_wave_sample_rate(self):
        frequency = 440
        amplitude = 1.0
        length = 2.0

        for sample_rate in [22050, 44100, 88200]:
            generated_wave = generate_sine_wave(frequency, amplitude, length, sample_rate)

            plt.figure(figsize=(18, 12))
            plt.plot(generated_wave[:1000])
            plt.title(f'Sine Wave Sample Rate: {sample_rate}')
            plt.show()


class SineWaveFrequencyTest:
    def run_tests(self):
        self.test_generate_sine_wave_frequency()

    def test_generate_sine_wave_frequency(self):
        amplitude = 1.0
        length = 2.0
        sample_rate = 44100

        for frequency in [220, 440, 880]:
            generated_wave = generate_sine_wave(frequency, amplitude, length, sample_rate)

            plt.figure(figsize=(18, 12))
            plt.plot(generated_wave[:1000])
            plt.title(f'Sine Wave Frequency: {frequency}Hz')
            plt.show()


# Create an instance of each test class and run the tests
sine_wave_test = SineWaveTest()
sine_wave_test.run_tests()

sine_wave_invert_test = SineWaveInvertTest()
sine_wave_invert_test.run_tests()

sine_wave_offset_test = SineWaveOffsetTest()
sine_wave_offset_test.run_tests()

sine_wave_phase_shift_test = SineWavePhaseShiftTest()
sine_wave_phase_shift_test.run_tests()

sine_wave_sample_rate_test = SineWaveSampleRateTest()
sine_wave_sample_rate_test.run_tests()

sine_wave_frequency_test = SineWaveFrequencyTest()
sine_wave_frequency_test.run_tests()
