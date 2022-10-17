from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowWhiteMatterWithMRIInputSpec(CommandLineInputSpec):
    white_mesh = traits.File(
        exists=True,
        desc='Hemisphere White Mesh, Anatomist mesh formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowWhiteMatterWithMRIOutputSpec(TraitedSpec):
    pass


class AnatomistShowWhiteMatterWithMRI(BVCommand):
    input_spec = AnatomistShowWhiteMatterWithMRIInputSpec
    output_spec = AnatomistShowWhiteMatterWithMRIOutputSpec
    _cmd = 'AnatomistShowWhiteMatterWithMRI'

