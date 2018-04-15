cdef extern from "coin/IpAlgTypes.hpp" namespace "Ipopt":
    cdef enum SolverReturn:
        SUCCESS
        MAXITER_EXCEEDED
        CPUTIME_EXCEEDED
        STOP_AT_TINY_STEP
        STOP_AT_ACCEPTABLE_POINT
        LOCAL_INFEASIBILITY
        USER_REQUESTED_STOP
        FEASIBLE_POINT_FOUND
        DIVERGING_ITERATES
        RESTORATION_FAILURE
        ERROR_IN_STEP_COMPUTATION
        INVALID_NUMBER_DETECTED
        TOO_FEW_DEGREES_OF_FREEDOM
        INVALID_OPTION
        OUT_OF_MEMORY
        INTERNAL_ERROR
        UNASSIGNED
