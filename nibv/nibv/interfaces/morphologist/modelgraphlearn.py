from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ModelgraphlearnInputSpec(CommandLineInputSpec):
    model_graph = traits.File(
        exists=True,
        desc='Model Graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    labels_translation_map = traits.File(
        exists=True,
        desc='Label Translation, Label Translation,  DEF Label translation',
        position=1, mandatory=False, argstr='%s')
    learner = traits.File(
        exists=True,
        desc='Sigraph Learner,  Sigraph Learner',
        position=2, mandatory=False, argstr='%s')
    stopdelay = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%d', mandatory=False)
    learning_mode = traits.Enum(
        "generateOnly", "generateAndTrain", "readAndTrain",
        usedefault=False,
        desc='generateOnly, generateAndTrain, readAndTrain',
        position=4, mandatory=False)
    cycles = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=7, argstr='%d', mandatory=False)
    cycles_tst = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%d', mandatory=False)
    parallelism_mode = traits.Enum(
        "local", "lag", "grid", "LSF",
        usedefault=False,
        desc='local, lag, grid,  LSF',
        position=9, mandatory=False)


class ModelgraphlearnOutputSpec(TraitedSpec):
    pass


class Modelgraphlearn(BVCommand):
    input_spec = ModelgraphlearnInputSpec
    output_spec = ModelgraphlearnOutputSpec
    _cmd = 'Modelgraphlearn'

