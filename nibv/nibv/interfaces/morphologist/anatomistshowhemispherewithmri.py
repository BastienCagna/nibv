from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowHemisphereWithMRIInputSpec(CommandLineInputSpec):
    hemi_mesh = traits.File(
        exists=True,
        desc='Hemisphere Mesh,  Anatomist mesh formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowHemisphereWithMRIOutputSpec(TraitedSpec):
    pass


class AnatomistShowHemisphereWithMRI(BVCommand):
    input_spec = AnatomistShowHemisphereWithMRIInputSpec
    output_spec = AnatomistShowHemisphereWithMRIOutputSpec
    _cmd = 'AnatomistShowHemisphereWithMRI'

