from __future__ import print_function
import unittest
from pytraj.base import *
from pytraj import adict
from pytraj import io as mdio
from pytraj.utils.check_and_assert import assert_almost_equal
from pytraj import set_world_silent, set_error_silent

class Test(unittest.TestCase):
    def test_0(self):
        print ("turn-on set_world_silent")
        # just want to test for not printing out cpptraj warning
        top = Topology("./data/saxs_test/test.pdb")
        print ("you should not see anything from cpptraj before")

    def test_1(self):
        print ()
        print ()
        print ()
        print ("turn-off set_world_silent")
        set_world_silent(False)
        set_error_silent(False)
        print ("you should see a bunch of cpptraj's messages after this line")
        top = Topology("./data/saxs_test/test.pdb")

if __name__ == "__main__":
    unittest.main()
