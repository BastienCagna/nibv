from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowGreyWhiteClassifInputSpec(CommandLineInputSpec):
    classif = traits.File(
        exists=True,
        desc='Grey White Mask,  Anatomist volume formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowGreyWhiteClassifOutputSpec(TraitedSpec):
    pass


class AnatomistShowGreyWhiteClassif(BVCommand):
    input_spec = AnatomistShowGreyWhiteClassifInputSpec
    output_spec = AnatomistShowGreyWhiteClassifOutputSpec
    _cmd = 'AnatomistShowGreyWhiteClassif'

