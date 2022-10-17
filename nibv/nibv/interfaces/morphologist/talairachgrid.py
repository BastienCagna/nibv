from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TalairachGridInputSpec(CommandLineInputSpec):
    output_grid = traits.File(
        exists=False,
        desc='Mesh,  aims Mesh Formats',
        position=0, mandatory=False, argstr='%s')
    cylinder_facets = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%d', mandatory=False)


class TalairachGridOutputSpec(TraitedSpec):
    output_grid = traits.File(
        desc='Mesh,  aims Mesh Formats')


class TalairachGrid(BVCommand):
    input_spec = TalairachGridInputSpec
    output_spec = TalairachGridOutputSpec
    _cmd = 'TalairachGrid'

