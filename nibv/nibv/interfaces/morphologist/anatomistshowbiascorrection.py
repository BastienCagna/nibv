from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowBiasCorrectionInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=0, mandatory=False, argstr='%s')
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI, Anatomist volume formats, exactType=True',
        position=1, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo analysis,  Histo analysis',
        position=2, mandatory=False, argstr='%s')


class AnatomistShowBiasCorrectionOutputSpec(TraitedSpec):
    pass


class AnatomistShowBiasCorrection(BVCommand):
    input_spec = AnatomistShowBiasCorrectionInputSpec
    output_spec = AnatomistShowBiasCorrectionOutputSpec
    _cmd = 'AnatomistShowBiasCorrection'

