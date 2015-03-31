import unittest
from pytraj.six_2 import izip
from pytraj.base import *
from pytraj import adict
from pytraj import io as mdio
from pytraj.utils.check_and_assert import assert_almost_equal
from pytraj.trajs.Trajin import Trajin

class Test(unittest.TestCase):
    def test_0(self):
        top = Topology("./data/Test_RemdTraj/ala2.99sb.mbondi2.parm7")

        # load regular traj
        straj = mdio.load("./data/Test_RemdTraj/rem.nc.000", top)

        # load all traj and extract frames having 300.0 K
        traj = mdio.load_remd("./data/Test_RemdTraj/rem.nc.000", top, "300.0")

        print (traj)
        assert isinstance(traj, Trajin) == True
        print (traj, traj.top, traj.n_frames)

        # make sure to get 300.0 K for all frames
        for T in traj.temperatures:
            assert_almost_equal([T], [300.0,])

        # make sure to reproduce cpptraj output
        saved_traj = mdio.load("data/Test_RemdTraj/temp0.crd.300.00", 
                               "./data/Test_RemdTraj/ala2.99sb.mbondi2.parm7")

        print (traj.n_frames)
        for f0, f1 in izip(traj, straj):
            print (f0[0], f1[0])

if __name__ == "__main__":
    unittest.main()