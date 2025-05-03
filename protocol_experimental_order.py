import os, csv
from pwem.protocols import EMProtocol
from pyworkflow.protocol.params import PathParam, StringParam, PointerParam
from pwchem.objects import SmallMolecule, SetOfSmallMolecules
import pyworkflow.object as pwobj

class ProtChemExperimentalOrder(EMProtocol):
    """Correlate the experimental order with the different scores appearing throughout the workflow."""
    _label = 'experimental order'

    def _defineParams(self, form):
        form.addSection(label='Input')

        form.addParam('experimentalFile', PathParam, label='Experimental Data CSV File:', allowsNull=False,
                      help='Path to the CSV file containing experimental energies and molecule names.')
        
        form.addParam('experimentalDelimiter', StringParam, default=',', label='Experimental Data CSV Delimiter:',
                      help='Specify the delimiter used in the experimental data CSV file (e.g., "," or "\\t").')
        
        form.addParam('inputMoleculeSet', PointerParam, label='Molecule Set:',
                      allowsNull=False, pointerClass='SetOfSmallMolecules',
                      help='The set of molecules to which experimental energy will be added.')

    def _insertAllSteps(self):
        self._insertFunctionStep('updateMoleculesWithExperimentalData')

    def updateMoleculesWithExperimentalData(self):
        """Update input molecules with experimental energy data."""
        expFile = os.path.abspath(self.experimentalFile.get())
        expDelimiter = self.experimentalDelimiter.get()

        # Read and validate experimental data
        expData = []
        with open(expFile, 'r') as ef:
            reader = csv.DictReader(ef, delimiter=expDelimiter)
            headers = reader.fieldnames
            if not headers:
                raise ValueError("The experimental data CSV file is empty or malformed.")

            # Validate required columns
            if 'molName' not in headers or 'experimental_energy' not in headers:
                raise ValueError("Experimental data CSV must contain 'molName' and 'experimental_energy' columns.")

            expData = [row for row in reader]

        expDict = {row['molName']: row['experimental_energy'] for row in expData}

        # Get input molecule set and update molecules with experimental data
        inputMoleculeSet = self.inputMoleculeSet.get()
        updatedMoleculeSet = inputMoleculeSet.createCopy(self._getPath(), copyInfo=True)

        for mol in inputMoleculeSet:
            molName = mol.getMolName()
            if molName in expDict:
                setattr(mol, 'experimental_energy', pwobj.Float(float(expDict[molName])))
                updatedMoleculeSet.append(mol.clone())

        self._defineOutputs(updatedMoleculeSet=updatedMoleculeSet)
        self.info(f"Updated {len(updatedMoleculeSet)} molecules with experimental data.")

    def _validate(self):
        """Ensure input files exist."""
        errors = []
        if not os.path.exists(self.experimentalFile.get()):
            errors.append(f"File not found: {self.experimentalFile.get()}")
        return errors



