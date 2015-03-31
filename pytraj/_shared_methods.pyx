# distutils: language = c++
#
cimport cython
from pytraj.Frame cimport _Frame, Frame
from pytraj.AtomMask cimport AtomMask
from pytraj.trajs.Trajout import Trajout
from pytraj.six_2 import set

def _savetraj(self, filename="", fmt='unknown', overwrite=False):
    if fmt == 'unknown':
        # convert to "UNKNOWN_TRAJ"
        fmt = fmt.upper() + "_TRAJ"
    else:
        fmt = fmt.upper()

    with Trajout(filename=filename, top=self.top, fmt=fmt, 
                 overwrite=overwrite, more_args=None) as trajout:
        for idx, frame in enumerate(self):
            trajout.writeframe(idx, frame, self.top)

def _get_temperature_set(self):
    return set(self.temperatures) 

def my_str_method(self):
    name = self.__class__.__name__
    n_atoms = 0 if self.top.is_empty() else self.top.n_atoms
    tmps = """%s instance with %s frames, %s atoms/frame
           """ % (
            name, self.size, n_atoms,
            )
    return tmps

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.infer_types(True)
def _frame_iter(self, int start=0, int stop=-1, int stride=1, mask=None):
    """iterately get Frames with start, stop, stride 
    Parameters
    ---------
    start : int (default = 0)
    stop : int (default = max_frames - 1)
    """
    cdef int i
    cdef Frame frame = Frame(self.n_atoms)
    cdef Frame frame2
    cdef AtomMask atm
    cdef int _end

    if stop == -1:
        _end = <int> self.n_frames
    else:
        _end = stop + 1

    i = start
    while i < _end:
        frame = self[i]
        if mask is not None:
            atm = self.top(mask)
            frame2 = Frame(atm.n_atoms)
            frame2.thisptr.SetCoordinates(frame.thisptr[0], atm.thisptr[0])
            yield frame2
        else:
            yield frame

        i += stride