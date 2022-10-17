from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciDeepTrainingInputSpec(CommandLineInputSpec):
    pass


class SulciDeepTrainingOutputSpec(TraitedSpec):
    pass


class SulciDeepTraining(BVCommand):
    input_spec = SulciDeepTrainingInputSpec
    output_spec = SulciDeepTrainingOutputSpec
    _cmd = 'SulciDeepTraining'

