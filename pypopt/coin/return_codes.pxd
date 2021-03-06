cdef extern from "<coin/IpReturnCodes.hpp>" namespace "Ipopt":
    cdef enum ApplicationReturnStatus:
        Solve_Succeeded = 0
        Solved_To_Acceptable_Level = 1
        Infeasible_Problem_Detected = 2
        Search_Direction_Becomes_Too_Small = 3
        Diverging_Iterates = 4
        User_Requested_Stop = 5
        Feasible_Point_Found = 6
        Maximum_Iterations_Exceeded = -1
        Restoration_Failed = -2
        Error_In_Step_Computation = -3
        Maximum_CpuTime_Exceeded = -4
        Not_Enough_Degrees_Of_Freedom = -10
        Invalid_Problem_Definition = -11
        Invalid_Option = -12
        Invalid_Number_Detected = -13
        Unrecoverable_Exception = -100
        NonIpopt_Exception_Thrown = -101
        Insufficient_Memory = -102
        Internal_Error = -199

    cdef enum AlgorithmMode:
        RegularMode
        RestorationPhaseMode
