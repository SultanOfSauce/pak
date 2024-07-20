from pymol import cmd
from pandas import read_csv

def set_phipsi(selection, phi=None, psi=None):
    '''
DESCRIPTION

    Set phi/psi angles for all residues in selection.

SEE ALSO

    set_phi, set_psi, set_dihedral, phi_psi, cmd.get_phipsi, DynoPlot
    '''
    for model, index in cmd.index('byca (' + selection + ')'):
        atsele = [
            'first ((%s`%d) extend 2 and name C)' % (model, index), # prev C
            'first ((%s`%d) extend 1 and name N)' % (model, index), # this N
            '(%s`%d)' % (model, index),                             # this CA
            'last ((%s`%d) extend 1 and name C)' % (model, index),  # this C
            'last ((%s`%d) extend 2 and name N)' % (model, index),  # next N
        ]
        try:
            if phi is not None:
                cmd.set_dihedral(atsele[0], atsele[1], atsele[2], atsele[3], phi)
            if psi is not None:
                cmd.set_dihedral(atsele[1], atsele[2], atsele[3], atsele[4], psi)
        except:
            print (' Error: cmd.set_dihedral failed')

def set_phi(selection, phi):
    set_phipsi(selection, phi=phi)

def set_psi(selection, psi):
    set_phipsi(selection, psi=psi)

def load_angles(csv):
    angles = read_csv(csv)

    no_angles = len(angles.columns)//2

    for i in range(no_angles):
        phi = angles.iloc[0,i]
        psi = angles.iloc[0,i+no_angles]

        set_phipsi(selection = f"resi {i+1}", phi = phi * -1, psi = psi * -1)



cmd.extend('set_phipsi', set_phipsi)
cmd.extend('set_phi', set_phi)
cmd.extend('set_psi', set_psi)
cmd.extend('load_angles', load_angles)



# vi:expandtab:smarttab:sw=4