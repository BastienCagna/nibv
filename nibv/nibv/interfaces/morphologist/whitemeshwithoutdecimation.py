from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class WhitemeshwithoutdecimationInputSpec(CommandLineInputSpec):
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    white_mesh_fine = traits.File(
        exists=False,
        desc='Fine Hemisphere White Mesh, Aims mesh formats',
        position=1, mandatory=False, argstr='%s')
    maxclearance = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%f', mandatory=False)
    maxerror = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%f', mandatory=False)
    maxcurv = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)


class WhitemeshwithoutdecimationOutputSpec(TraitedSpec):
    white_mesh_fine = traits.File(
        desc='Fine Hemisphere White Mesh, Aims mesh formats')


class Whitemeshwithoutdecimation(BVCommand):
    input_spec = WhitemeshwithoutdecimationInputSpec
    output_spec = WhitemeshwithoutdecimationOutputSpec
    _cmd = 'Whitemeshwithoutdecimation'

