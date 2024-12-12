import matplotlib.pyplot as plt
import numpy as np

def amdahl_law(P, N):
    """Amdahl Yasasına göre hızlanmayı hesaplar."""
    return 1 / ((1 - P) + (P / N))

# Kullanıcıdan girdi alma
P = float(input("Paralel çalışabilir kısım oranını (0 ile 1 arasında) girin (P): "))
max_processors = int(input("Maksimum işlemci sayısını girin (N): "))

# İşlemci sayıları ve hızlanmaları hesaplama
processors = np.arange(1, max_processors + 1)  # 1'den max_processors'a kadar bir dizi
speedups = amdahl_law(P, processors)  # Her bir işlemci sayısı için hızlanmayı hesapla

# Sonuçları çizdirme
plt.figure(figsize=(10, 6))
plt.plot(processors, speedups, marker='o', color='b', label=f'Paralel Kısım (P) = {P}')
plt.xlabel('İşlemci Sayısı (N)')
plt.ylabel('Hızlanma (Speedup)')
plt.title('Amdahl Yasası ile Hızlanma Grafiği')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
