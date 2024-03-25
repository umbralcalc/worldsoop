from enum import Enum
from dataclasses import dataclass

@dataclass
class NilOutputCondition:
    def to_yaml(self) -> str:
        return r"&simulator.NilOutputCondition{}"

@dataclass
class EveryStepOutputCondition:
    def to_yaml(self) -> str:
        return r"&simulator.EveryStepOutputCondition{}"

@dataclass
class EveryNStepsOutputCondition:
    steps: int

    def to_yaml(self) -> str:
        return r"&simulator.EveryNStepsOutputCondition{N: " + str(self.steps) + r"}"


class CallableYamlEnum(Enum):
    def __call__(self, **kwargs):
        self.kwargs = kwargs
        return self

    def to_yaml(self) -> str:
        return (
            self.value(**self.kwargs).to_yaml() 
            if hasattr(self, "kwargs") 
            else self.value.to_yaml()
        )


class OutputCondition(CallableYamlEnum):
    nil = NilOutputCondition
    every_step = EveryStepOutputCondition
    every_n_steps = EveryNStepsOutputCondition

@dataclass
class NilOutputFunction:
    def to_yaml(self) -> str:
        return r"&simulator.NilOutputFunction{}"   

@dataclass
class StdoutOutputFunction:
    def to_yaml(self) -> str:
        return r"&simulator.StdoutOutputFunction{}"
    
@dataclass
class VariableStoreOutputFunction:
    def to_yaml(self) -> str:
        return r"&simulator.VariableStoreOutputFunction{}"


class OutputFunction(CallableYamlEnum):
    nil = NilOutputFunction
    stdout = StdoutOutputFunction
    variable_store = VariableStoreOutputFunction


@dataclass
class NumberOfStepsTerminationCondition:
    max_number_of_steps: int

    def to_yaml(self) -> str:
        return (
            r"&simulator.NumberOfStepsTerminationCondition{MaxNumberOfSteps: "
            + str(self.max_number_of_steps)
            + r"}"
        )


@dataclass
class TimeElapsedTerminationCondition:
    max_time_elapsed: int

    def to_yaml(self) -> str:
        return (
            r"&simulator.TimeElapsedTerminationCondition{MaxTimeElapsed: "
            + str(self.max_time_elapsed)
            + r"}"
        )


class TerminationCondition(CallableYamlEnum):
    number_of_steps = NumberOfStepsTerminationCondition
    time_elapsed = TimeElapsedTerminationCondition
    

@dataclass
class ConstantTimestepFunction:
    stepsize: float

    def to_yaml(self) -> str:
        return (
        r"&simulator.ConstantTimestepFunction{Stepsize: " 
        + str(self.stepsize) 
        + r"}"
    )


@dataclass
class ExponentialDistributionTimestepFunction:
    mean: float
    seed: int

    def to_yaml(self) -> str:
        return (
            r"simulator.NewExponentialDistributionTimestepFunction("
            + str(self.mean) 
            + r", "
            + str(self.seed)
            + r")"
        )


class TimestepFunction(CallableYamlEnum):
    constant = ConstantTimestepFunction
    exponential_distribution = ExponentialDistributionTimestepFunction


@dataclass
class ConstantValuesIteration:
    def to_yaml(self) -> str:
        return r"&simulator.ConstantValuesIteration{}"
    
    @staticmethod
    def package() -> str:
        return ""
    

@dataclass
class WienerProcessIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.WienerProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"
    

@dataclass
class PoissonProcessIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.PoissonProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"
    

@dataclass
class CompoundPoissonProcessIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.CompoundPoissonProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class CoxProcessIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.CoxProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class DriftDiffusionIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.DriftDiffusionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class FractionalBrownianMotionIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.FractionalBrownianMotionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class GeometricBrownianMotionIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.GeometricBrownianMotionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class HawkesProcessIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.HawkesProcessIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class OrnsteinUhlenbeckIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.OrnsteinUhlenbeckIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class HistogramNodeIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.HistogramNodeIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class PipelineStageIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.PipelineStageIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


@dataclass
class StateTransitionIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.StateTransitionIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"



@dataclass
class WeightedMeanIteration:
    def to_yaml(self) -> str:
        return r"&phenomena.WeightedMeanIteration{}"
    
    @staticmethod
    def package() -> str:
        return "github.com/umbralcalc/stochadex/pkg/phenomena"


class StochadexIteration(CallableYamlEnum):
    constant_values = ConstantValuesIteration
    wiener_process = WienerProcessIteration
    poisson_process = PoissonProcessIteration
    compound_poisson_process = CompoundPoissonProcessIteration
    cox_process = CoxProcessIteration
    drift_diffusion = DriftDiffusionIteration
    fractional_brownian_motion = FractionalBrownianMotionIteration
    geometric_brownian_motion = GeometricBrownianMotionIteration
    hawkes_process = HawkesProcessIteration
    ornstein_uhlenbeck = OrnsteinUhlenbeckIteration
    histogram_node = HistogramNodeIteration
    pipeline_stage = PipelineStageIteration
    state_transition = StateTransitionIteration
    weighted_mean = WeightedMeanIteration
