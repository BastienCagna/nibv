from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciLabelingShowDiffsAcrossSubjectsInputSpec(CommandLineInputSpec):
    column = traits.String(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%s', mandatory=False)
    save_plot = traits.File(
        exists=False,
        desc='SVG figure,  SVG file',
        position=2, mandatory=False, argstr='%s')


class SulciLabelingShowDiffsAcrossSubjectsOutputSpec(TraitedSpec):
    save_plot = traits.File(
        desc='SVG figure,  SVG file')


class SulciLabelingShowDiffsAcrossSubjects(BVCommand):
    input_spec = SulciLabelingShowDiffsAcrossSubjectsInputSpec
    output_spec = SulciLabelingShowDiffsAcrossSubjectsOutputSpec
    _cmd = 'SulciLabelingShowDiffsAcrossSubjects'

