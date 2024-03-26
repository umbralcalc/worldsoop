from abc import abstractmethod
from dataclasses import dataclass


class OutputCondition:
    @abstractmethod
    def to_api_str(self) -> str:
        ...

@dataclass
class NilOutputCondition(OutputCondition):
    def to_api_str(self) -> str:
        return r"&simulator.NilOutputCondition{}"

@dataclass
class EveryStepOutputCondition(OutputCondition):
    def to_api_str(self) -> str:
        return r"&simulator.EveryStepOutputCondition{}"

@dataclass
class EveryNStepsOutputCondition(OutputCondition):
    steps: int

    def to_api_str(self) -> str:
        return r"&simulator.EveryNStepsOutputCondition{N: " + str(self.steps) + r"}"


class OutputFunction:
    @abstractmethod
    def to_api_str(self) -> str:
        ...


@dataclass
class NilOutputFunction(OutputFunction):
    def to_api_str(self) -> str:
        return r"&simulator.NilOutputFunction{}"   

@dataclass
class StdoutOutputFunction(OutputFunction):
    def to_api_str(self) -> str:
        return r"&simulator.StdoutOutputFunction{}"
    
@dataclass
class VariableStoreOutputFunction(OutputFunction):
    def to_api_str(self) -> str:
        return r"&simulator.VariableStoreOutputFunction{}"


class TerminationCondition:
    @abstractmethod
    def to_api_str(self) -> str:
        ...

@dataclass
class NumberOfStepsTerminationCondition(TerminationCondition):
    max_number_of_steps: int

    def to_api_str(self) -> str:
        return (
            r"&simulator.NumberOfStepsTerminationCondition{MaxNumberOfSteps: "
            + str(self.max_number_of_steps)
            + r"}"
        )


@dataclass
class TimeElapsedTerminationCondition(TerminationCondition):
    max_time_elapsed: int

    def to_api_str(self) -> str:
        return (
            r"&simulator.TimeElapsedTerminationCondition{MaxTimeElapsed: "
            + str(self.max_time_elapsed)
            + r"}"
        )


class TimestepFunction:
    @abstractmethod
    def to_api_str(self) -> str:
        ...


@dataclass
class ConstantTimestepFunction(TimestepFunction):
    stepsize: float

    def to_api_str(self) -> str:
        return (
        r"&simulator.ConstantTimestepFunction{Stepsize: " 
        + str(self.stepsize) 
        + r"}"
    )


@dataclass
class ExponentialDistributionTimestepFunction(TimestepFunction):
    mean: float
    seed: int

    def to_api_str(self) -> str:
        return (
            r"simulator.NewExponentialDistributionTimestepFunction("
            + str(self.mean) 
            + r", "
            + str(self.seed)
            + r")"
        )


class StochadexIteration:
    @abstractmethod
    def to_api_str(self) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def package() -> str:
        ...


@dataclass
class ConstantValuesIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&simulator.ConstantValuesIteration{}"
    
    @staticmethod
    def package() -> str:
        return ""
    

@dataclass
class WienerProcessIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.WienerProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"
    

@dataclass
class PoissonProcessIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.PoissonProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"
    

@dataclass
class CompoundPoissonProcessIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.CompoundPoissonProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class CoxProcessIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.CoxProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class DriftDiffusionIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.DriftDiffusionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class FractionalBrownianMotionIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.FractionalBrownianMotionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class GeometricBrownianMotionIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.GeometricBrownianMotionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class HawkesProcessIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.HawkesProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class OrnsteinUhlenbeckIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.OrnsteinUhlenbeckIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class HistogramNodeIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.HistogramNodeIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class PipelineStageIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.PipelineStageIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class StateTransitionIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.StateTransitionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"



@dataclass
class WeightedMeanIteration(StochadexIteration):
    def to_api_str(self) -> str:
        return r"&phenomena.WeightedMeanIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"

