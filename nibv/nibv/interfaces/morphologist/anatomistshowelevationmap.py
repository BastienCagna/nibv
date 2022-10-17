from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowElevationMapInputSpec(CommandLineInputSpec):
    read = traits.File(
        exists=True,
        desc='Elevation map,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    scale = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%f', mandatory=False)


class AnatomistShowElevationMapOutputSpec(TraitedSpec):
    pass


class AnatomistShowElevationMap(BVCommand):
    input_spec = AnatomistShowElevationMapInputSpec
    output_spec = AnatomistShowElevationMapOutputSpec
    _cmd = 'AnatomistShowElevationMap'

