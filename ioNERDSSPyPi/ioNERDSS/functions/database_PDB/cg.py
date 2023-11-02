# take in the pdb file and output the pdb file with the corse-grained interfaces added

import numpy as np


class Chain:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.residues = []
        self.COM = None
        self.interfaces = []
        self.atoms = []


class Residue:
    def __init__(self, index):
        self.index = index
        self.atoms = []
        self.chain = -1
        self.CA = -1


class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distanceSquare(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        dsquare = dx * dx + dy * dy + dz * dz
        return dsquare


class Atom:
    def __init__(
        self, index, atomType, residueType, chainName, chainIndex, residueIndex, coord
    ):
        self.index = index
        self.atomType = atomType
        self.residueType = residueType
        self.chainName = chainName
        self.chainIndex = chainIndex
        self.resideIndex = residueIndex
        self.coord = coord


class Interface:
    def __init__(self, index, partner):
        self.index = index
        self.partner = partner
        self.coord = None
        self.name = None
        self.chain = -1
        self.energy = 0.0
        self.atomsNum = 0
        self.residuesNum = 0


def cg(filename, cutoff):
    energyTable = {
        "CYS-CYS": 5.44,
        "CYS-MET": 4.99,
        "CYS-PHE": 5.80,
        "CYS-ILE": 5.50,
        "CYS-LEU": 5.83,
        "CYS-VAL": 4.96,
        "CYS-TRP": 4.95,
        "CYS-TYR": 4.16,
        "CYS-ALA": 3.57,
        "CYS-GLY": 3.16,
        "CYS-THR": 3.11,
        "CYS-SER": 2.86,
        "CYS-ASN": 2.59,
        "CYS-GLN": 2.85,
        "CYS-ASP": 2.41,
        "CYS-GLU": 2.27,
        "CYS-HIS": 3.60,
        "CYS-ARG": 2.57,
        "CYS-LYS": 1.95,
        "CYS-PRO": 3.07,
        "MET-MET": 5.46,
        "MET-PHE": 6.56,
        "MET-ILE": 6.02,
        "MET-LEU": 6.41,
        "MET-VAL": 5.32,
        "MET-TRP": 5.55,
        "MET-TYR": 4.91,
        "MET-ALA": 3.94,
        "MET-GLY": 3.39,
        "MET-THR": 3.51,
        "MET-SER": 3.03,
        "MET-ASN": 2.95,
        "MET-GLN": 3.30,
        "MET-ASP": 2.57,
        "MET-GLU": 2.89,
        "MET-HIS": 3.98,
        "MET-ARG": 3.12,
        "MET-LYS": 2.48,
        "MET-PRO": 3.56,
        "PHE-PHE": 7.26,
        "PHE-ILE": 6.84,
        "PHE-LEU": 7.28,
        "PHE-VAL": 6.29,
        "PHE-TRP": 6.16,
        "PHE-TYR": 5.66,
        "PHE-ALA": 4.81,
        "PHE-GLY": 4.13,
        "PHE-THR": 4.28,
        "PHE-SER": 4.02,
        "PHE-ASN": 3.75,
        "PHE-GLN": 4.10,
        "PHE-ASP": 3.48,
        "PHE-GLU": 3.56,
        "PHE-HIS": 4.77,
        "PHE-ARG": 3.98,
        "PHE-LYS": 3.36,
        "PHE-PRO": 4.25,
        "ILE-ILE": 6.54,
        "ILE-LEU": 7.04,
        "ILE-VAL": 6.05,
        "ILE-TRP": 5.78,
        "ILE-TYR": 5.25,
        "ILE-ALA": 4.58,
        "ILE-GLY": 3.78,
        "ILE-THR": 4.03,
        "ILE-SER": 3.52,
        "ILE-ASN": 3.24,
        "ILE-GLN": 3.67,
        "ILE-ASP": 3.17,
        "ILE-GLU": 3.27,
        "ILE-HIS": 4.14,
        "ILE-ARG": 3.63,
        "ILE-LYS": 3.01,
        "ILE-PRO": 3.76,
        "LEU-LEU": 7.37,
        "LEU-VAL": 6.48,
        "LEU-TRP": 6.14,
        "LEU-TYR": 5.67,
        "LEU-ALA": 4.91,
        "LEU-GLY": 4.16,
        "LEU-THR": 4.34,
        "LEU-SER": 3.92,
        "LEU-ASN": 3.74,
        "LEU-GLN": 4.04,
        "LEU-ASP": 3.40,
        "LEU-GLU": 3.59,
        "LEU-HIS": 4.54,
        "LEU-ARG": 4.03,
        "LEU-LYS": 3.37,
        "LEU-PRO": 4.20,
        "VAL-VAL": 5.52,
        "VAL-TRP": 5.18,
        "VAL-TYR": 4.62,
        "VAL-ALA": 4.04,
        "VAL-GLY": 3.38,
        "VAL-THR": 3.46,
        "VAL-SER": 3.05,
        "VAL-ASN": 2.83,
        "VAL-GLN": 3.07,
        "VAL-ASP": 2.48,
        "VAL-GLU": 2.67,
        "VAL-HIS": 3.58,
        "VAL-ARG": 3.07,
        "VAL-LYS": 2.49,
        "VAL-PRO": 3.32,
        "TRP-TRP": 5.06,
        "TRP-TYR": 4.66,
        "TRP-ALA": 3.82,
        "TRP-GLY": 3.42,
        "TRP-THR": 3.22,
        "TRP-SER": 2.99,
        "TRP-ASN": 3.07,
        "TRP-GLN": 3.11,
        "TRP-ASP": 2.84,
        "TRP-GLU": 2.99,
        "TRP-HIS": 3.98,
        "TRP-ARG": 3.41,
        "TRP-LYS": 2.69,
        "TRP-PRO": 3.73,
        "TYR-TYR": 4.17,
        "TYR-ALA": 3.36,
        "TYR-GLY": 3.01,
        "TYR-THR": 3.01,
        "TYR-SER": 2.78,
        "TYR-ASN": 2.76,
        "TYR-GLN": 2.97,
        "TYR-ASP": 2.76,
        "TYR-GLU": 2.79,
        "TYR-HIS": 3.52,
        "TYR-ARG": 3.16,
        "TYR-LYS": 2.60,
        "TYR-PRO": 3.19,
        "ALA-ALA": 2.72,
        "ALA-GLY": 2.31,
        "ALA-THR": 2.32,
        "ALA-SER": 2.01,
        "ALA-ASN": 1.84,
        "ALA-GLN": 1.89,
        "ALA-ASP": 1.70,
        "ALA-GLU": 1.51,
        "ALA-HIS": 2.41,
        "ALA-ARG": 1.83,
        "ALA-LYS": 1.31,
        "ALA-PRO": 2.03,
        "GLY-GLY": 2.24,
        "GLY-THR": 2.08,
        "GLY-SER": 1.82,
        "GLY-ASN": 1.74,
        "GLY-GLN": 1.66,
        "GLY-ASP": 1.59,
        "GLY-GLU": 1.22,
        "GLY-HIS": 2.15,
        "GLY-ARG": 1.72,
        "GLY-LYS": 1.15,
        "GLY-PRO": 1.87,
        "THR-THR": 2.12,
        "THR-SER": 1.96,
        "THR-ASN": 1.88,
        "THR-GLN": 1.90,
        "THR-ASP": 1.80,
        "THR-GLU": 1.74,
        "THR-HIS": 2.42,
        "THR-ARG": 1.90,
        "THR-LYS": 1.31,
        "THR-PRO": 1.90,
        "SER-SER": 1.67,
        "SER-ASN": 1.58,
        "SER-GLN": 1.49,
        "SER-ASP": 1.63,
        "SER-GLU": 1.48,
        "SER-HIS": 2.11,
        "SER-ARG": 1.62,
        "SER-LYS": 1.05,
        "SER-PRO": 1.57,
        "ASN-ASN": 1.68,
        "ASN-GLN": 1.71,
        "ASN-ASP": 1.68,
        "ASN-GLU": 1.51,
        "ASN-HIS": 2.08,
        "ASN-ARG": 1.64,
        "ASN-LYS": 1.21,
        "ASN-PRO": 1.53,
        "GLN-GLN": 1.54,
        "GLN-ASP": 1.46,
        "GLN-GLU": 1.42,
        "GLN-HIS": 1.98,
        "GLN-ARG": 1.80,
        "GLN-LYS": 1.29,
        "GLN-PRO": 1.73,
        "ASP-ASP": 1.21,
        "ASP-GLU": 1.02,
        "ASP-HIS": 2.32,
        "ASP-ARG": 2.29,
        "ASP-LYS": 1.68,
        "ASP-PRO": 1.33,
        "GLU-GLU": 0.91,
        "GLU-HIS": 2.15,
        "GLU-ARG": 2.27,
        "GLU-LYS": 1.80,
        "GLU-PRO": 1.26,
        "HIS-HIS": 3.05,
        "HIS-ARG": 2.16,
        "HIS-LYS": 1.35,
        "HIS-PRO": 2.25,
        "ARG-ARG": 1.55,
        "ARG-LYS": 0.59,
        "ARG-PRO": 1.70,
        "LYS-LYS": 0.12,
        "LYS-PRO": 0.97,
        "PRO-PRO": 1.75,
        "MET-CYS": 4.99,
        "PHE-CYS": 5.80,
        "ILE-CYS": 5.50,
        "LEU-CYS": 5.83,
        "VAL-CYS": 4.96,
        "TRP-CYS": 4.95,
        "TYR-CYS": 4.16,
        "ALA-CYS": 3.57,
        "GLY-CYS": 3.16,
        "THR-CYS": 3.11,
        "SER-CYS": 2.86,
        "ASN-CYS": 2.59,
        "GLN-CYS": 2.85,
        "ASP-CYS": 2.41,
        "GLU-CYS": 2.27,
        "HIS-CYS": 3.60,
        "ARG-CYS": 2.57,
        "LYS-CYS": 1.95,
        "PRO-CYS": 3.07,
        "PHE-MET": 6.56,
        "ILE-MET": 6.02,
        "LEU-MET": 6.41,
        "VAL-MET": 5.32,
        "TRP-MET": 5.55,
        "TYR-MET": 4.91,
        "ALA-MET": 3.94,
        "GLY-MET": 3.39,
        "THR-MET": 3.51,
        "SER-MET": 3.03,
        "ASN-MET": 2.95,
        "GLN-MET": 3.30,
        "ASP-MET": 2.57,
        "GLU-MET": 2.89,
        "HIS-MET": 3.98,
        "ARG-MET": 3.12,
        "LYS-MET": 2.48,
        "PRO-MET": 3.56,
        "ILE-PHE": 6.84,
        "LEU-PHE": 7.28,
        "VAL-PHE": 6.29,
        "TRP-PHE": 6.16,
        "TYR-PHE": 5.66,
        "ALA-PHE": 4.81,
        "GLY-PHE": 4.13,
        "THR-PHE": 4.28,
        "SER-PHE": 4.02,
        "ASN-PHE": 3.75,
        "GLN-PHE": 4.10,
        "ASP-PHE": 3.48,
        "GLU-PHE": 3.56,
        "HIS-PHE": 4.77,
        "ARG-PHE": 3.98,
        "LYS-PHE": 3.36,
        "PRO-PHE": 4.25,
        "LEU-ILE": 7.04,
        "VAL-ILE": 6.05,
        "TRP-ILE": 5.78,
        "TYR-ILE": 5.25,
        "ALA-ILE": 4.58,
        "GLY-ILE": 3.78,
        "THR-ILE": 4.03,
        "SER-ILE": 3.52,
        "ASN-ILE": 3.24,
        "GLN-ILE": 3.67,
        "ASP-ILE": 3.17,
        "GLU-ILE": 3.27,
        "HIS-ILE": 4.14,
        "ARG-ILE": 3.63,
        "LYS-ILE": 3.01,
        "PRO-ILE": 3.76,
        "VAL-LEU": 6.48,
        "TRP-LEU": 6.14,
        "TYR-LEU": 5.67,
        "ALA-LEU": 4.91,
        "GLY-LEU": 4.16,
        "THR-LEU": 4.34,
        "SER-LEU": 3.92,
        "ASN-LEU": 3.74,
        "GLN-LEU": 4.04,
        "ASP-LEU": 3.40,
        "GLU-LEU": 3.59,
        "HIS-LEU": 4.54,
        "ARG-LEU": 4.03,
        "LYS-LEU": 3.37,
        "PRO-LEU": 4.20,
        "TRP-VAL": 5.18,
        "TYR-VAL": 4.62,
        "ALA-VAL": 4.04,
        "GLY-VAL": 3.38,
        "THR-VAL": 3.46,
        "SER-VAL": 3.05,
        "ASN-VAL": 2.83,
        "GLN-VAL": 3.07,
        "ASP-VAL": 2.48,
        "GLU-VAL": 2.67,
        "HIS-VAL": 3.58,
        "ARG-VAL": 3.07,
        "LYS-VAL": 2.49,
        "PRO-VAL": 3.32,
        "TYR-TRP": 4.66,
        "ALA-TRP": 3.82,
        "GLY-TRP": 3.42,
        "THR-TRP": 3.22,
        "SER-TRP": 2.99,
        "ASN-TRP": 3.07,
        "GLN-TRP": 3.11,
        "ASP-TRP": 2.84,
        "GLU-TRP": 2.99,
        "HIS-TRP": 3.98,
        "ARG-TRP": 3.41,
        "LYS-TRP": 2.69,
        "PRO-TRP": 3.73,
        "ALA-TYR": 3.36,
        "GLY-TYR": 3.01,
        "THR-TYR": 3.01,
        "SER-TYR": 2.78,
        "ASN-TYR": 2.76,
        "GLN-TYR": 2.97,
        "ASP-TYR": 2.76,
        "GLU-TYR": 2.79,
        "HIS-TYR": 3.52,
        "ARG-TYR": 3.16,
        "LYS-TYR": 2.60,
        "PRO-TYR": 3.19,
        "GLY-ALA": 2.31,
        "THR-ALA": 2.32,
        "SER-ALA": 2.01,
        "ASN-ALA": 1.84,
        "GLN-ALA": 1.89,
        "ASP-ALA": 1.70,
        "GLU-ALA": 1.51,
        "HIS-ALA": 2.41,
        "ARG-ALA": 1.83,
        "LYS-ALA": 1.31,
        "PRO-ALA": 2.03,
        "THR-GLY": 2.08,
        "SER-GLY": 1.82,
        "ASN-GLY": 1.74,
        "GLN-GLY": 1.66,
        "ASP-GLY": 1.59,
        "GLU-GLY": 1.22,
        "HIS-GLY": 2.15,
        "ARG-GLY": 1.72,
        "LYS-GLY": 1.15,
        "PRO-GLY": 1.87,
        "SER-THR": 1.96,
        "ASN-THR": 1.88,
        "GLN-THR": 1.90,
        "ASP-THR": 1.80,
        "GLU-THR": 1.74,
        "HIS-THR": 2.42,
        "ARG-THR": 1.90,
        "LYS-THR": 1.31,
        "PRO-THR": 1.90,
        "ASN-SER": 1.58,
        "GLN-SER": 1.49,
        "ASP-SER": 1.63,
        "GLU-SER": 1.48,
        "HIS-SER": 2.11,
        "ARG-SER": 1.62,
        "LYS-SER": 1.05,
        "PRO-SER": 1.57,
        "GLN-ASN": 1.71,
        "ASP-ASN": 1.68,
        "GLU-ASN": 1.51,
        "HIS-ASN": 2.08,
        "ARG-ASN": 1.64,
        "LYS-ASN": 1.21,
        "PRO-ASN": 1.53,
        "ASP-GLN": 1.46,
        "GLU-GLN": 1.42,
        "HIS-GLN": 1.98,
        "ARG-GLN": 1.80,
        "LYS-GLN": 1.29,
        "PRO-GLN": 1.73,
        "GLU-ASP": 1.02,
        "HIS-ASP": 2.32,
        "ARG-ASP": 2.29,
        "LYS-ASP": 1.68,
        "PRO-ASP": 1.33,
        "HIS-GLU": 2.15,
        "ARG-GLU": 2.27,
        "LYS-GLU": 1.80,
        "PRO-GLU": 1.26,
        "ARG-HIS": 2.16,
        "LYS-HIS": 1.35,
        "PRO-HIS": 2.25,
        "LYS-ARG": 0.59,
        "PRO-ARG": 1.70,
        "PRO-LYS": 0.97,
    }

    updatedEnergyTable = {key: -value + 2.27 for key, value in energyTable.items()}

    filename = filename + ".pdb"
    chains = []
    residues = []
    atoms = []
    interfaces = []
    with open(filename, "r") as fileName:
        currentChain = ""
        atomIndex = -1
        residueGlobalIndex = -1
        residueLocalIndex = -1
        chainIndex = -1
        for line in fileName:
            # parse one line from the pdb file
            typeName = line[0:4].strip()

            if typeName == "ATOM":
                index = int(line[6:11])
                atomType = line[12:16].strip()
                residueType = line[17:20].strip().upper()
                chainName = line[21]

                # check if it is a new chain
                if chainName != currentChain:
                    chainIndex += 1
                    chain = Chain(chainName, chainIndex)
                    currentChain = chainName
                    chains.append(chain)

                residueIndex = int(line[22:26])

                # check if it is a new residue
                if residueIndex != residueLocalIndex:
                    residueGlobalIndex += 1
                    residueLocalIndex = residueIndex
                    residue = Residue(residueGlobalIndex)
                    residue.chain = chainIndex
                    residues.append(residue)
                    chains[-1].residues.append(residueGlobalIndex)

                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                coord = Coord(x, y, z)
                atomIndex += 1
                atom = Atom(
                    atomIndex,
                    atomType,
                    residueType,
                    chainName,
                    chainIndex,
                    residueGlobalIndex,
                    coord,
                )
                atoms.append(atom)
                residues[-1].atoms.append(atomIndex)
                if atomType == "CA":
                    residues[-1].CA = atomIndex

    # calculate the center of mass for each chain
    for chain in chains:
        x = 0
        y = 0
        z = 0
        count = 0
        for residueIndex in chain.residues:
            residue = residues[residueIndex]
            for atomIndex in residue.atoms:
                chain.atoms.append(atomIndex)
                atom = atoms[atomIndex]
                x += atom.coord.x
                y += atom.coord.y
                z += atom.coord.z
                count += 1
        x /= count
        y /= count
        z /= count
        chain.COM = Coord(x, y, z)

    # calculate the interface
    interfaceIndex = -1
    for chain1 in chains:
        for chain2 in chains:
            if chain1.index < chain2.index:
                ca1 = []
                ca2 = []
                energy = []
                residuesPair = ()
                # loop all the atoms pair between chain1 and chain2
                for a1 in chain1.atoms:
                    for a2 in chain2.atoms:
                        atom1 = atoms[a1]
                        atom2 = atoms[a2]
                        dsquare = atom1.coord.distanceSquare(atom2.coord)
                        if dsquare <= cutoff * cutoff:
                            # ca1.append(residues[atom1.resideIndex].CA)
                            # ca2.append(residues[atom2.resideIndex].CA)
                            ca1.append(a1)
                            ca2.append(a2)
                            residuesPairName = (
                                atom1.chainName
                                + str(atom1.resideIndex)
                                + atom1.residueType
                                + atom2.chainName
                                + str(atom2.resideIndex)
                                + atom2.residueType
                            )
                            if residuesPairName not in residuesPair:
                                residuesPair += (residuesPairName,)
                                bond = atom1.residueType + "-" + atom2.residueType
                                if bond in updatedEnergyTable:
                                    energy.append(updatedEnergyTable[bond])
                if len(ca1) > 0:
                    x, y, z = 0, 0, 0
                    for a in ca1:
                        x += atoms[a].coord.x
                        y += atoms[a].coord.y
                        z += atoms[a].coord.z
                    x /= len(ca1)
                    y /= len(ca1)
                    z /= len(ca1)
                    interfaceIndex += 1
                    interface = Interface(interfaceIndex, chain2.index)
                    interface.name = chain1.name + chain2.name
                    interface.chain = chain1.index
                    interface.coord = Coord(x, y, z)
                    interface.energy = sum(energy)
                    interface.atomsNum = len(ca1)
                    interface.residuesNum = len(residuesPair)
                    interfaces.append(interface)
                    chain1.interfaces.append(interfaceIndex)

                    x, y, z = 0, 0, 0
                    for a in ca2:
                        x += atoms[a].coord.x
                        y += atoms[a].coord.y
                        z += atoms[a].coord.z
                    x /= len(ca2)
                    y /= len(ca2)
                    z /= len(ca2)
                    interfaceIndex += 1
                    interface = Interface(interfaceIndex, chain1.index)
                    interface.name = chain2.name + chain1.name
                    interface.chain = chain2.index
                    interface.coord = Coord(x, y, z)
                    interface.energy = sum(energy)
                    interface.atomsNum = len(ca2)
                    interface.residuesNum = len(residuesPair)
                    interfaces.append(interface)
                    chain2.interfaces.append(interfaceIndex)

    # print the center of mass and interfaces for each chain
    for chain in chains:
        print(
            f"COM of chain {chain.name}: {chain.COM.x / 10.0:.3f}, {chain.COM.y / 10.0:.3f}, {chain.COM.z / 10.0:.3f}"
        )
        print(f"Interfaces of chain {chain.name}: ", end="")
        for interfaceIndex in chain.interfaces:
            print(interfaces[interfaceIndex].name, end=" ")
            print(
                f"partner chain: {chains[interfaces[interfaceIndex].partner].name}",
                end=" ",
            )
            print(
                f"{interfaces[interfaceIndex].coord.x / 10.0:.3f} {interfaces[interfaceIndex].coord.y / 10.0:.3f} {interfaces[interfaceIndex].coord.z / 10.0:.3f}",
                end=" ",
            )
            print(f"energy: {interfaces[interfaceIndex].energy:.3f}")
            print(f"residuesNum: {interfaces[interfaceIndex].residuesNum}")
        print()

    # write the pdb file with the interfaces added
    # Open a PDB file for writing
    with open("output.pdb", "w") as pdb_file:
        atom_serial = 1  # Initialize atom serial number
        residue_serial = 1  # Initialize residue serial number
        conect_records = []  # List to store CONECT records

        for chain in chains:
            com_serial = atom_serial  # Store the atom serial number for the COM

            # Write COM to PDB file
            pdb_file.write(
                f"ATOM  {atom_serial:5d} COM  COM {chain.name}{residue_serial:4d}    {chain.COM.x:8.3f}{chain.COM.y:8.3f}{chain.COM.z:8.3f}\n"
            )
            atom_serial += 1

            for interfaceIndex in chain.interfaces:
                interface = interfaces[interfaceIndex]

                # Write interface to PDB file
                pdb_file.write(
                    f"ATOM  {atom_serial:5d} INT  {interface.name.ljust(3)} {chain.name}{residue_serial:4d}    {interface.coord.x:8.3f}{interface.coord.y:8.3f}{interface.coord.z:8.3f}\n"
                )

                # Add bond between COM and interface
                conect_records.append(f"CONECT{com_serial:5d}{atom_serial:5d}\n")

                atom_serial += 1
            residue_serial += 1

        # Write all the CONECT records to the PDB file
        for conect in conect_records:
            pdb_file.write(conect)
    print("output.pdb has been generated.")

    print("nerdss input parameters:")

    # generate the input parameters for the nerdss simulation
    for chain in chains:
        print(f"mol {chain.name}:")
        print("  com 0.000 0.000 0.000")
        for i in chain.interfaces:
            interface = interfaces[i]
            print(
                f"  {interface.name} [{(interface.coord.x - chain.COM.x) / 10.0:.3f}, {(interface.coord.y - chain.COM.y) / 10.0:.3f}, {(interface.coord.z - chain.COM.z) / 10.0:.3f}]"
            )
            partner = None
            for partnerChain in chains:
                if partnerChain.index == interface.partner:
                    print(f"      partner {partnerChain.name}")
                    for partnerInterface in partnerChain.interfaces:
                        if interfaces[partnerInterface].partner == chain.index:
                            partner = interfaces[partnerInterface]
                            break
            print(f"      partner interface: {partner.name}")
            theta1, theta2, phi1, phi2, omega = calculateAngles(
                np.array([chain.COM.x, chain.COM.y, chain.COM.z]),
                np.array(
                    [
                        chains[interface.partner].COM.x,
                        chains[interface.partner].COM.y,
                        chains[interface.partner].COM.z,
                    ]
                ),
                np.array([interface.coord.x, interface.coord.y, interface.coord.z]),
                np.array([partner.coord.x, partner.coord.y, partner.coord.z]),
                np.array([0, 0, 1]),
                np.array([0, 0, 1]),
            )
            print(
                f"      theta1 {theta1:.3f} theta2 {theta2:.3f} phi1 {phi1:.3f} phi2 {phi2:.3f} omega {omega:.3f}"
            )
            print(
                f"      [{theta1:.3f}, {theta2:.3f}, {phi1:.3f}, {phi2:.3f}, {omega:.3f}]"
            )
            print("      n1 0.000 0.000 1.000")
            print("      n2 0.000 0.000 1.000")
            sigma = np.linalg.norm(
                np.array([interface.coord.x, interface.coord.y, interface.coord.z])
                - np.array([partner.coord.x, partner.coord.y, partner.coord.z])
            )
            print(f"       sigma {sigma / 10.0:.3f}")
            print(f"       energy {interface.energy:.3f}")
            print(f"       residuesNum {interface.residuesNum}")


def calculateAngles(c1, c2, p1, p2, n1, n2):
    """
    Determine the angles of the reaction (theta1, theta2, phi1, phi2, omega) given the coordinates of the two Center of Mass (c1 and c2) and two reaction sites (p1 and p2), and two norm vectors (n1 and n2).

    Parameters
    ----------
    c1 : numpy.array
        Center of Mass vector for the first molecule.
    c2 : numpy.array
        Center of Mass vector for the second molecule.
    p1 : numpy.array
        Reaction site vector for the first molecule.
    p2 : numpy.array
        Reaction site vector for the second molecule.
    n1 : numpy.array
        Norm vector for the first molecule.
    n2 : numpy.array
        Norm vector for the second molecule.

    Returns
    -------
    tuple
        The tuple (theta1, theta2, phi1, phi2, omega), where theta1, theta2, phi1, phi2, omega are the angles in radians.
    """
    v1 = p1 - c1
    v2 = p2 - c2
    sigma1 = p1 - p2
    sigma2 = -sigma1

    theta1 = np.arccos(
        np.dot(v1, sigma1) / (np.linalg.norm(v1) * np.linalg.norm(sigma1))
    )
    theta2 = np.arccos(
        np.dot(v2, sigma2) / (np.linalg.norm(v2) * np.linalg.norm(sigma2))
    )

    t1 = np.cross(v1, sigma1)
    t2 = np.cross(v1, n1)
    norm_t1 = t1 / np.linalg.norm(t1)
    norm_t2 = t2 / np.linalg.norm(t2)
    phi1 = np.arccos(np.dot(norm_t1, norm_t2))

    # the sign of phi1 is determined by the direction of t2 relative to the right-hand rule of cross product of v1 and t1
    if np.dot(np.cross(v1, t1), t2) > 0:
        phi1 = -phi1

    t1 = np.cross(v2, sigma2)
    t2 = np.cross(v2, n2)
    norm_t1 = t1 / np.linalg.norm(t1)
    norm_t2 = t2 / np.linalg.norm(t2)
    phi2 = np.arccos(np.dot(norm_t1, norm_t2))

    # the sign of phi2 is determined by the direction of t2 relative to the right-hand rule of cross product of v2 and t1
    if np.dot(np.cross(v2, t1), t2) > 0:
        phi2 = -phi2

    if not np.isclose(np.linalg.norm(np.cross(v1, sigma1)), 0) and not np.isclose(
        np.linalg.norm(np.cross(v2, sigma2)), 0
    ):
        t1 = np.cross(sigma1, v1)
        t2 = np.cross(sigma1, v2)
    else:
        t1 = np.cross(sigma1, n1)
        t2 = np.cross(sigma1, n2)

    omega = np.arccos(np.dot(t1, t2) / (np.linalg.norm(t1) * np.linalg.norm(t2)))

    # the sign of omega is determined by the direction of t2 relative to the right-hand rule of cross product of sigma1 and t1
    if np.dot(np.cross(sigma1, t1), t2) > 0:
        omega = -omega

    return theta1, theta2, phi1, phi2, omega