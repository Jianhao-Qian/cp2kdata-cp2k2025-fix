import dpdata
import numpy as np

dp1 = dpdata.LabeledSystem("SSE_V202501.out", fmt="cp2kdata/e_f")
dp2 = dpdata.LabeledSystem("SSE_V202301.out", fmt="cp2kdata/e_f")

def compare_array(name, a1, a2):
    if a1 is None and a2 is None:
        print(f"{name}: both None, skipping")
        return
    if a1 is None or a2 is None:
        print(f"{name}: one of them is None")
        return
    diff = np.abs(a1 - a2)
    print(f"{name}:")
    print(f"  max abs diff : {diff.max():.6e}")
    print(f"  mean abs diff: {diff.mean():.6e}")
    print(f"  V202501 mean : {np.mean(a1):.6e}")
    print(f"  V202301 mean : {np.mean(a2):.6e}")

print("=" * 50)
print("V202501:", dp1)
print("V202301:", dp2)
print("=" * 50)

compare_array("cell      [Angstrom]", dp1["cells"],  dp2["cells"])
compare_array("coords    [Angstrom]", dp1["coords"], dp2["coords"])
compare_array("forces    [eV/Ang]  ", dp1["forces"], dp2["forces"])
compare_array("energies  [eV]      ", dp1["energies"].reshape(-1,1), dp2["energies"].reshape(-1,1))

v1 = dp1.data.get("virials", None)
v2 = dp2.data.get("virials", None)
compare_array("virials   [eV]      ", v1, v2)