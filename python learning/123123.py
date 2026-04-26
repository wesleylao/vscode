import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]
core_cpi_yoy = [0.36, 1.33, 2.61, 2.58, 1.88, 1.77, 1.95, 2.00, 2.00, 2.00]

plt.figure(figsize=(10, 6))
plt.plot(years, core_cpi_yoy, marker='o', color='orange', linewidth=2)
plt.title("cpi_trend(2020–2029)", fontsize=14)
plt.xlabel("year")
plt.ylabel("core_cpi_grewth_rate (%)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.ylim(0, 3)
plt.show()