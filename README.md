#ProtChemExperimentalOrder – Add Experimental Binding Energy to Molecule Set

##Overview:

This protocol allows users to annotate a set of small molecules in Scipion-chem with corresponding experimental binding energy values (e.g., ΔG) using a provided CSV file. This is particularly useful for benchmarking virtual screening workflows or comparing computational predictions with known experimental results.

##Purpose:

The goal is to enrich molecular datasets with experimental affinity data to:

    Enable downstream analysis of prediction accuracy.

    Facilitate correlation between docking/rescoring outputs and real-world bioactivity.

    Support visualization or ranking workflows that integrate experimental benchmarks.

Input Parameters:

    Experimental Data CSV File: A path to the CSV file containing the reference values. The file must contain at least two columns:

        molName: The name of the molecule (must match mol.getMolName() in Scipion).

        experimental_energy: The experimental binding energy value (e.g., in kcal/mol).

    Experimental Data CSV Delimiter: Specifies the delimiter used in the CSV file (e.g., , for comma or \t for tab-separated files).

    Molecule Set: A SetOfSmallMolecules object containing the molecules to be annotated with experimental values.

How It Works:

    Reads the experimental CSV file and creates a mapping of molecule names to energy values.

    Iterates over the molecules in the input set and adds an experimental_energy attribute to those found in the CSV.

    Returns a new molecule set with the experimental values embedded for use in scoring, filtering, or plotting workflows.

Output:

    A new SetOfSmallMolecules with the experimental_energy attribute added to the corresponding molecules.

Notes:

    Molecule names in the CSV must exactly match the names in the input set.

    Only molecules present in both the input set and the CSV will be updated.

    This protocol does not modify docking or scoring results—only enriches the metadata for further correlation or benchmarking.
