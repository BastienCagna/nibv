from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SegmentcorpuscallosumInputSpec(CommandLineInputSpec):
    left_grey_white = traits.File(
        exists=True,
        desc='Left Grey White Mask, aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    right_grey_white = traits.File(
        exists=True,
        desc='Right Grey White Mask, aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    corpus_callosum_mask = traits.File(
        exists=False,
        desc='Corpus Callosum mask, aims writable volume formats',
        position=2, mandatory=False, argstr='%s')
    talairach_transformation = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=3, mandatory=False, argstr='%s')


class SegmentcorpuscallosumOutputSpec(TraitedSpec):
    corpus_callosum_mask = traits.File(
        desc='Corpus Callosum mask, aims writable volume formats')


class Segmentcorpuscallosum(BVCommand):
    input_spec = SegmentcorpuscallosumInputSpec
    output_spec = SegmentcorpuscallosumOutputSpec
    _cmd = 'Segmentcorpuscallosum'

