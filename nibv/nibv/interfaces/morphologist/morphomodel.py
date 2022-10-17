from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class MorphoModelInputSpec(CommandLineInputSpec):
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=1, mandatory=False, argstr='%s')
    template_region_model = traits.File(
        exists=True,
        desc='Template model, Template model',
        position=2, mandatory=False, argstr='%s')
    template_domain_model = traits.File(
        exists=True,
        desc='Template model domain, Template model domain',
        position=3, mandatory=False, argstr='%s')
    template_relation_model = traits.File(
        exists=True,
        desc='Template model, Template model',
        position=4, mandatory=False, argstr='%s')
    region = traits.String(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%s', mandatory=False)
    output_prefix = traits.String(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%s', mandatory=False)


class MorphoModelOutputSpec(TraitedSpec):
    pass


class MorphoModel(BVCommand):
    input_spec = MorphoModelInputSpec
    output_spec = MorphoModelOutputSpec
    _cmd = 'MorphoModel'

