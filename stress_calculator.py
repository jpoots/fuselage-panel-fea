p = 0.0607
r = 1345
t = 1.0

hoop_stress = p * r / t

# assuming closed
longitudinal_stress = p * r / (2 * t)

# no shear in the baseline cylinder
shear_stress = 0

# simplified to ignore radial stress (thin walled)
von_mises_stress = (
    0.5
    * (
        (hoop_stress - longitudinal_stress) ** 2
        + longitudinal_stress**2
        + hoop_stress**2
    )
    + 3 * shear_stress**2
) ** 0.5

print("Stress calculations, units: mm, N, MPa")
print(f"Pressure: {p}")
print(f"Radius: {r}")
print(f"Wall thickness: {t}")
print(f"Hoop stress: {hoop_stress}")
print(f"Longitudinal stress: {longitudinal_stress}")
print(f"Von Mises stress: {von_mises_stress}")
