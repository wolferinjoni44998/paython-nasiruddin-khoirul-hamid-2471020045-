
import csv

with open("nilai.csv", newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f))

for d in data:
    d["nilai"] = int(d["nilai"])

rekap = {}

for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")

for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")
