from enum import Enum
from functools import partial

def every_n_steps(steps: int) -> str:
    return r"&simulator.EveryNStepsOutputCondition{N: " + str(steps) + r"}"


class OutputCondition(Enum):
    nil = r"&simulator.NilOutputCondition{}"
    every_step = r"&simulator.EveryStepOutputCondition{}"
    every_n_steps = partial(every_n_steps)

    def __call__(self, *args) -> str:
        if len(args) == 0:
            return self.value
        else:
            return self.value(*args)
    

class OutputFunction(Enum):
    nil = r"&simulator.NilOutputFunction{}"
    stdout = r"&simulator.StdoutOutputFunction{}"
    variable_store = r"&simulator.VariableStoreOutputFunction{}"

    def __call__(self, *args) -> str:
        if len(args) == 0:
            return self.value
        else:
            return self.value(*args)


def number_of_steps(max_number_of_steps: int) -> str:
    return (
        r"&simulator.NumberOfStepsTerminationCondition{MaxNumberOfSteps: "
        + str(max_number_of_steps)
        + r"}"
    )


def time_elapsed(max_time_elapsed: float) -> str:
    return (
        r"&simulator.TimeElapsedTerminationCondition{MaxTimeElapsed: "
        + str(max_time_elapsed)
        + r"}"
    )


class TerminationCondition(Enum):
    number_of_steps = partial(number_of_steps)
    time_elapsed = partial(time_elapsed)

    def __call__(self, *args) -> str:
        if len(args) == 0:
            return self.value
        else:
            return self.value(*args)
    

def constant(stepsize: float) -> str:
    return (
        r"&simulator.ConstantTimestepFunction{Stepsize: " 
        + str(stepsize) 
        + r"}"
    )


def exponential_distribution(mean: float, seed: int) -> str:
    return (
        r"simulator.NewExponentialDistributionTimestepFunction("
        + str(mean) 
        + r", "
        + str(seed)
        + r")"
    )


class TimestepFunction(Enum):
    constant = partial(constant)
    exponential_distribution = partial(exponential_distribution)

    def __call__(self, *args) -> str:
        if len(args) == 0:
            return self.value
        else:
            return self.value(*args)