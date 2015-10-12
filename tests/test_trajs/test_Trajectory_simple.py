from __future__ import print_function
import unittest
import pytraj as pt
from pytraj.base import *
from pytraj import adict
from pytraj import io as mdio
from pytraj.utils import eq, aa_eq
from pytraj.testing import cpptraj_test_dir
import pytraj.common_actions as pyca
from pytraj.compat import zip


class Test(unittest.TestCase):
    def test_0(self):
        from pytraj import Trajectory
        traj = mdio.iterload("./data/md1_prod.Tc5b.x", "./data/Tc5b.top")

        # test slice
        fa0 = traj[:]
        for f0, f1 in zip(fa0, traj):
            pass
        try:
            from rmsd import rmsd
        except:
            pass

        aa_eq(fa0.xyz, traj.xyz, decimal=5)

        # test append
        fa = Trajectory()
        fa.top = traj.top.copy()

        for frame in traj:
            fa.append(frame.copy())
        assert (fa.n_frames == traj.n_frames)
        assert (fa.top.n_atoms == traj.top.n_atoms)

        # test memview for slicing
        fa2 = fa[2:]
        mylist = [1., 2., 3.]
        fa2[0, 0] = mylist
        aa_eq(fa[2, 0], mylist)

        #
        fa3 = traj[:]


if __name__ == "__main__":
    unittest.main()