#This code will demonstrate quantum entanglement and give a basic idea of what is happening
import math
import random

class EntangledPhotonSimulator:
    def __init__(self):
        # Our entangled state: |Ψ⟩ = 1/√2 (|00⟩ + |11⟩) (The bell state)
        
        self.p00 = 1 / math.sqrt(2)  # amplitude of |00⟩
        self.p11 = 1 / math.sqrt(2)  # amplitude of |11⟩
        
        self.p01 = 0                 # amplitude of |01⟩
        self.p10 = 0                 # amplitude of |10⟩
    
    def measure(self):
        """
        Simulates the quantum measurement of two photon system.
        The outcome is probabilistic in nature and is the square of amplitudes
        """
    def measure(self):
        """
        Simulates a quantum measurement of the two-photon system.
        The outcome is probabilistic based on the square of amplitude.
        """

        # Compute probabilities of each basis state (square of amplitudes)
        prob_00 = self.p00 ** 2
        prob_01 = self.p01 ** 2
        prob_10 = self.p10 ** 2
        prob_11 = self.p11 ** 2
        
        print(f"Probabilities before measurement:")
        print(f"  P(|00⟩) = {prob_00:.2f}")
        print(f"  P(|01⟩) = {prob_01:.2f}")
        print(f"  P(|10⟩) = {prob_10:.2f}")
        print(f"  P(|11⟩) = {prob_11:.2f}")
        
        # This will act as the measurement apparatus
        r = random.random()
        if r < prob_00:
            outcome = "00"
        elif r < prob_00 + prob_01:
            outcome = "01"
        elif r < prob_00 + prob_01 + prob_10:
            outcome = "10"
        else:
            outcome = "11"

        # After measurement, wavefunction collapses!
        # Now the system becomes a definite product state.
        if outcome == "00":
            self.set_product_state(0, 0)
        elif outcome == "01":
            self.set_product_state(0, 1)
        elif outcome == "10":
            self.set_product_state(1, 0)
        else:  # "11"
            self.set_product_state(1, 1)
    
    def set_product_state(self, bit1, bit2):
        """
        After measurement, the state becomes a classical product state.
        Only one amplitude is 1; the rest are zero.
        """
        self.p00 = 1.0 if (bit1 == 0 and bit2 == 0) else 0.0
        self.p01 = 1.0 if (bit1 == 0 and bit2 == 1) else 0.0
        self.p10 = 1.0 if (bit1 == 1 and bit2 == 0) else 0.0
        self.p11 = 1.0 if (bit1 == 1 and bit2 == 1) else 0.0

        print(f"\n🧩 State after measurement collapse:")
        print(f"  New state = |{bit1}{bit2}⟩ (pure product state)\n")
        print(f"  Amplitudes:")
        print(f"    |00⟩: {self.p00}")
        print(f"    |01⟩: {self.p01}")
        print(f"    |10⟩: {self.p10}")
        print(f"    |11⟩: {self.p11}")

for i in range(5):
    print(f"\n========= Trial {i+1} =========")
    sim = EntangledPhotonSimulator()  # reset to entangled state
    sim.measure()


        
# The first measurement collapses the other states and the entanglement too. This is because, once you get 11 (suppose) after first measurement,
# the other measurements will yeild same result. Had there been no collapse, there would have been equal probabilities for 00 or 11.