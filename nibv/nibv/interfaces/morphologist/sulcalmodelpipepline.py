from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulcalmodelPipeplineInputSpec(CommandLineInputSpec):
    model_graph = traits.File(
        exists=False,
        desc='Model Graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    model_version = traits.String(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%s', mandatory=False)
    data_compatibility_version = traits.String(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%s', mandatory=False)
    template_node_model = traits.File(
        exists=True,
        desc='Template model,  Template model',
        position=6, mandatory=False, argstr='%s')
    template_rel_model = traits.File(
        exists=True,
        desc='Template model,  Template model',
        position=7, mandatory=False, argstr='%s')
    learner = traits.File(
        exists=True,
        desc='Sigraph Learner,  Sigraph Learner',
        position=8, mandatory=False, argstr='%s')
    session = traits.String(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%s', mandatory=False)
    output = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=10, mandatory=False, argstr='%s')
    parallelism_mode = traits.Enum(
        "local", "grid", "duch", "LSF",
        usedefault=False,
        desc='local, grid, duch,  LSF',
        position=11, mandatory=False)


class SulcalmodelPipeplineOutputSpec(TraitedSpec):
    model_graph = traits.File(
        desc='Model Graph,  Graph')
    output = traits.File(
        desc='CSV file,  CSV file')


class SulcalmodelPipepline(BVCommand):
    input_spec = SulcalmodelPipeplineInputSpec
    output_spec = SulcalmodelPipeplineOutputSpec
    _cmd = 'SulcalmodelPipepline'

