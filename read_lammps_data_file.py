import numpy as np

def read_lammps_data_file(file_path):
	atoms, bonds, angles, dihedrals, impropers = [], [], [], [], []

	is_atom, is_bond, is_angle, _is_dihedral, is_improper = False

	with open(file_path, 'r') as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			parts = line.split()

			if parts[0] == 'Atoms':
				is_atom, is_bond, is_angle, _is_dihedral, is_improper = True, False, False, False, False
				continue
			elif parts[0] == 'Bonds':
				is_atom, is_bond, is_angle, _is_dihedral, is_improper = False, True, False, False, False
				continue
			elif parts[0] == 'Angles':
				is_atom, is_bond, is_angle, _is_dihedral, is_improper = False, False, True, False, False
				continue
			elif parts[0] == 'Dihedrals':
				is_atom, is_bond, is_angle, _is_dihedral, is_improper = False, False, False, True, False
				continue
			elif parts[0] == 'Impropers':
				is_atom, is_bond, is_angle, _is_dihedral, is_improper = False, False, True, False, True
				continue

			if is_atoms:
                atoms.append(parts)
            elif is_bonds:
                bonds.append(parts)
            elif is_angles:
                angles.append(parts)
            elif is_dihedrals:
                dihedrals.append(parts)
            elif is_impropers:
                impropers.append(parts)

	atoms = np.array(atoms, dtype=float) if atoms else np.empty((0, 9))
    bonds = np.array(bonds, dtype=int) if bonds else np.empty((0, 4), dtype=int)
    angles = np.array(angles, dtype=int) if angles else np.empty((0, 5), dtype=int)
    dihedrals = np.array(dihedrals, dtype=int) if dihedrals else np.empty((0, 6), dtype=int)
    impropers = np.array(impropers, dtype=int) if impropers else np.empty((0, 6), dtype=int)

    return atoms, bonds, angles, dihedrals, impropers
