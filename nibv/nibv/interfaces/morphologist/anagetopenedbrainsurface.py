from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaGetOpenedBrainSurfaceInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected,  GIS Image',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=True,
        desc='T1 Brain Mask,  GIS Image',
        position=2, mandatory=False, argstr='%s')
    cortex = traits.File(
        exists=False,
        desc='Both CSF+GREY Mask,  GIS Image',
        position=3, mandatory=False, argstr='%s')
    brain_mesh = traits.File(
        exists=False,
        desc='Brain Mesh,  MESH mesh',
        position=4, mandatory=False, argstr='%s')


class AnaGetOpenedBrainSurfaceOutputSpec(TraitedSpec):
    cortex = traits.File(
        desc='Both CSF+GREY Mask,  GIS Image')
    brain_mesh = traits.File(
        desc='Brain Mesh,  MESH mesh')


class AnaGetOpenedBrainSurface(BVCommand):
    input_spec = AnaGetOpenedBrainSurfaceInputSpec
    output_spec = AnaGetOpenedBrainSurfaceOutputSpec
    _cmd = 'AnaGetOpenedBrainSurface'

