# Transmission Line Parameter Calculator
# Calculates inductance, capacitance and reactances
# for a 3-phase transmission line

import math

print("===== Transmission Line Parameter Calculator =====")

D = float(input("Enter GMD between conductors (m): "))
r = float(input("Enter conductor radius (m): "))
f = float(input("Enter frequency (Hz): "))
length = float(input("Enter transmission line length (km): "))

if D <= 0 or r <= 0 or f <= 0 or length <= 0:
    print("Please enter valid positive values.")

elif D <= r:
    print("GMD must be greater than conductor radius.")

else:
    # GMR for a solid conductor
    GMR = 0.7788 * r

    # Inductance per conductor
    L_per_m = 2e-7 * math.log(D / GMR)

    # Capacitance per meter
    C_per_m = (2 * math.pi * 8.854e-12) / math.log(D / r)

    # Total inductance and capacitance
    L_total = L_per_m * length * 1000
    C_total = C_per_m * length * 1000

    # Inductive reactance
    XL = 2 * math.pi * f * L_total

    # Capacitive reactance
    XC = 1 / (2 * math.pi * f * C_total)

    print("\n--- Transmission Line Results ---")
    print(f"GMR: {GMR:.6f} m")
    print(f"Inductance per km: {L_per_m * 1000:.6e} H/km")
    print(f"Capacitance per km: {C_per_m * 1000:.6e} F/km")
    print(f"Total Inductance: {L_total:.6e} H")
    print(f"Total Capacitance: {C_total:.6e} F")
    print(f"Inductive Reactance: {XL:.2f} Ω")
    print(f"Capacitive Reactance: {XC:.2f} Ω")