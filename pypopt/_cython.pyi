# pylint: skip-file
from typing import Any, Optional, List, Dict


class IpoptApplication(Any):
    def initialize(self, allow_clobber: bool = False, params_file: Optional[str] = None) -> ApplicationReturnStatus: ...
    def print_copyright_message(self) -> None: ...
    def rethrow_non_ipopt_exception(self, dorethrow: bool) -> bool: ...
    def optimize_tnlp(self, tnl: TNLP) -> ApplicationReturnStatus: ...
    def journalist(self) -> Journalist: ...
    def options(self) -> OptionsList: ...
    def statistics(self) -> SolveStatistics: ...


class OptionsList(Any):
    def clear(self) -> None: ...
    def get_list(self) -> List[Dict[str, Any]]: ...
    def set_string_value(self, tag: str, value: str, allow_clobber: bool, dont_print: bool) -> bool: ...
    def set_numeric_value(self, tag: str, value: float, allow_clobber: bool, dont_print: bool) -> bool: ...
    def set_integer_value(self, tag: str, value: int, allow_clobber: bool, dont_print: bool) -> bool: ...
    def set_string_value_if_unset(self, tag: str, value: str, allow_clobber: bool, dont_print: bool) -> bool: ...
    def set_numeric_value_if_unset(self, tag: str, value: float, allow_clobber: bool, dont_print: bool) -> bool: ...
    def set_integer_value_if_unset(self, tag: str, value: int, allow_clobber: bool, dont_print: bool) -> bool: ...
    def get_string_value(self, tag: str, prefix: str) -> str: ...
    def get_numeric_value(self, tag: str, prefix: str) -> float: ...
    def get_integer_value(self, tag: str, prefix: str) -> int: ...
    def get_bool_value(self, tag: str, prefix: str) -> bool: ...


class TNLP(Any):
    def get_nlp_info(self) -> NLPInfo: ...
    def fill_bounds_info(self, x_l: Optional[memoryview], x_u: Optional[memoryview],
                         g_l: Optional[memoryview], g_u: Optional[memoryview]) -> bool: ...
    def fill_starting_point(self, init_x: bool, x: Optional[memoryview],
                            init_z: bool, z_l: Optional[memoryview], z_u: Optional[memoryview],
                            init_lambda: bool, lambda_: Optional[memoryview]) -> bool: ...
    def eval_f(self, x: memoryview, new_x: bool) -> float: ...
    def eval_grad_f(self, x: memoryview, new_x: bool, grad_f: memoryview) -> bool: ...
    def fill_jacobian_g_structure(self, row: Optional[memoryview], col: Optional[memoryview]) -> bool: ...
    def eval_jacobian_g(self, x: memoryview, new_x: bool, values: Optional[memoryview]) -> bool: ...
    def fill_hessian_structure(self, row: Optional[memoryview], col: Optional[memoryview]) -> bool: ...
    def eval_hessian(self, x: memoryview, new_x: bool, obj_factor: float,
                     lambda_: Optional[memoryview], new_lambda: bool, value: memoryview) -> bool: ...
    def finalize_solution(self, x: memoryview, z_l: memoryview, z_u: memoryview, g: Optional[memoryview],
                          lambda_: Optional[memoryview], value: float) -> None: ...


class Journal(Any):
    def name(self) -> str: ...
    def set_print_level(self, category: EJournalCategory, level: EJournalLevel) -> None: ...
    def set_all_print_levels(self, level: EJournalLevel) -> None: ...
    def is_accepted(self,  category: EJournalCategory, level: EJournalLevel) -> bool: ...
    def print_(self, category: EJournalCategory, level: EJournalLevel, str_: bytes) -> None: ...
    def flush_buffer(self) -> None: ...


class PythonJournal(Journal):
    def __init__(self, level: EJournalLevel, out_stream: Any) -> None: ...


class Journalist(Any):
    def printf(self, level: EJournalLevel, category: EJournalCategory, fmt: str, *args: Any, **kwargs: Any) -> None: ...
    def print_string_over_lines(self, level: EJournalLevel, category: EJournalCategory, indent_level: int,
                                max_length: int, line: str) -> None: ...
    def printf_indented(self, level: EJournalLevel, category: EJournalCategory, indent_level: int,
                        fmt: str, *args: Any, **kwargs: Any) -> None: ...
    def can_produce_output(self, level: EJournalLevel, category: EJournalCategory) -> bool: ...
    def flush_buffer(self) -> None: ...
    def add_journal(self, journal: Journal) -> bool: ...
    def add_file_journal(self, location_name: str, fname: str,
                         default_level: Optional[EJournalLevel] = None) -> Journal: ...
    def get_journal(self, name: str) -> Journal: ...
    def delete_all_journals(self) -> None: ...


class EJournalLevel(Any): ...
class EJournalCategory(Any): ...
class ApplicationReturnStatus(Any): ...
class SolveStatistics(Any): ...
class IndexStyle(Any): ...
class NLPInfo(Any): ...
