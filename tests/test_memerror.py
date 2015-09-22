from __future__ import print_function
import pytraj as pt
import unittest
from pytraj.base import *
from pytraj import allactions
from pytraj.datasets import cast_dataset
from pytraj import adict, analdict
from pytraj.utils.check_and_assert import assert_almost_equal

farray = TrajectoryIterator(top=pt.load_topology("./data/Tc5b.top"),
                            filename='data/md1_prod.Tc5b.x', )


class TestRadgyr(unittest.TestCase):
    def test_0(self):
        # just want to go over the list of cpptraj Action
        # and try to create Action object.
        # used to get memory error for some actions.
        # failed_action_list: is the list of failed Action objects

        failed_action_list = ['createreservoir']
        #failed_action_list = []
        failed_anal_list = []

        def test_all():
            n_actions = 0
            n_anals = 0
            for key in adict.keys():
                if key not in failed_action_list:
                    n_actions += 1
                    #print(adict[key])
                    #print(key)

            for key in analdict.keys():
                if key not in failed_anal_list:
                    n_anals += 1
                    #print(analdict[key])
                    #print(key)
                    #print("n_actions = %s, n_anals = %s" % (n_actions, n_anals))

        test_all()

    def test_1(self):
        # try creating failed Action

        failed_action_list = ['createreservoir']
        for key in failed_action_list:
            adict[key]


if __name__ == "__main__":
    unittest.main()
