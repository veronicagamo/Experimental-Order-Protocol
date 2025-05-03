# ProtChemExperimentalOrder – Add Experimental Binding Energy to Molecule Set

## Overview
This protocol allows users to annotate a set of small molecules in Scipion-chem with corresponding **experimental binding energy values** using a provided CSV file. It is particularly useful for benchmarking virtual screening workflows or validating computational predictions.

## Purpose
The protocol enriches molecular datasets with experimental affinity data to:
- Compare predicted scores with experimental results.
- Evaluate workflow accuracy and consistency.
- Visualize or rank compounds based on real-world performance.

## Input Parameters
- **Experimental Data CSV File**: Path to a CSV file containing:
  - `molName`: Molecule name (must match `mol.getMolName()` in Scipion).
  - `experimental_energy`: Experimental binding energy (e.g., in kcal/mol).
- **Experimental Data CSV Delimiter**: Delimiter used in the CSV (e.g., `,` or `\t`).
- **Molecule Set**: A `SetOfSmallMolecules` object to be annotated.

## How It Works
1. Loads and parses the experimental data CSV.
2. Matches entries by molecule name.
3. Annotates matching molecules with a new attribute: `experimental_energy`.
4. Returns a new molecule set containing the updated entries.

## Output
- A new `SetOfSmallMolecules` with each matching molecule annotated with an `experimental_energy` attribute.

## Notes
- Molecule names must match exactly between the CSV and the molecule set.
- Only molecules found in both sources will be updated.
- This protocol adds metadata for analysis but does not modify docking or scoring outputs.

