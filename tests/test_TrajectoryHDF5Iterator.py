from __future__ import print_function
import unittest
from pytraj.base import *
from pytraj import adict
from pytraj import io
from pytraj.utils import eq, aa_eq
from pytraj.decorators import no_test, test_if_having, test_if_path_exists
from pytraj.testing import cpptraj_test_dir, duplicate_traj
import pytraj.common_actions as pyca
from pytraj.compat import zip


class Test(unittest.TestCase):

    @test_if_having("h5py")
    def test_0(self):
        from pytraj.trajs.TrajectoryHDF5Iterator import TrajectoryHDF5Iterator
        t = TrajectoryHDF5Iterator("./data/ala2.h5")
        print(t.xyz)
        print(t)

        for frame in t:
            print(frame)

    @test_if_having("h5py")
    @test_if_having("mdtraj")
    def test_0(self):
        from pytraj.trajs.TrajectoryHDF5Iterator import TrajectoryHDF5Iterator
        from mdtraj.testing import get_fn
        traj = io.load_hdf5(get_fn("frame0.h5"), autoconvert=False)

        namelist = "frame0.h5  frame0.xtc.h5 frame0.dcd.h5 traj.h5"
        for x in namelist.split():
            print(x)
            fn = get_fn(x)
            t = TrajectoryHDF5Iterator(fn, top=traj.top)
            print(t.top.box)
            print(t.has_box())
            for frame in t:
                pass

            print(t[:2])


if __name__ == "__main__":
    unittest.main()