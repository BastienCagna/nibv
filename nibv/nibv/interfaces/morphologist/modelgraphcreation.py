from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ModelgraphcreationInputSpec(CommandLineInputSpec):
    model_graph = traits.File(
        exists=False,
        desc='Model Graph,  Graph',
        position=0, mandatory=False, argstr='%s')
    labels_translation_map = traits.File(
        exists=True,
        desc='Label Translation, Label Translation,  DEF Label translation',
        position=3, mandatory=False, argstr='%s')
    template_node_model = traits.File(
        exists=True,
        desc='Template model,  Template model',
        position=4, mandatory=False, argstr='%s')
    template_rel_model = traits.File(
        exists=True,
        desc='Template model,  Template model',
        position=5, mandatory=False, argstr='%s')
    template_domain_model = traits.File(
        exists=True,
        desc='Template model domain, Template model domain',
        position=6, mandatory=False, argstr='%s')
    fallback_rel_model = traits.File(
        exists=True,
        desc='Template model,  Template model',
        position=7, mandatory=False, argstr='%s')
    model_version = traits.String(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%s', mandatory=False)
    data_compatibility_version = traits.String(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%s', mandatory=False)


class ModelgraphcreationOutputSpec(TraitedSpec):
    model_graph = traits.File(
        desc='Model Graph,  Graph')


class Modelgraphcreation(BVCommand):
    input_spec = ModelgraphcreationInputSpec
    output_spec = ModelgraphcreationOutputSpec
    _cmd = 'Modelgraphcreation'

