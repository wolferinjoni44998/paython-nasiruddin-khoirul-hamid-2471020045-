
import csv

with open("nilai.csv", newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f))

for d in data:
    d["nilai"] = int(d["nilai"])

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)

print(f"Rata-rata: {rata:.1f}")

lulus = [
    d["nama"] for d in data
    if d["nilai"] >= 75
]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
