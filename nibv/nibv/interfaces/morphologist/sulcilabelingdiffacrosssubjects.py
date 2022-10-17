from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciLabelingDiffAcrossSubjectsInputSpec(CommandLineInputSpec):
    session1_hint = traits.String(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%s', mandatory=False)
    session2_hint = traits.String(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%s', mandatory=False)
    manual1 = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    manual2_hint = traits.Enum(
        "As sulci1", "Yes", "No",
        usedefault=False,
        desc='As sulci1, Yes,  No',
        position=5, mandatory=False)
    diff_table = traits.File(
        exists=False,
        desc='CSV file,  CSV file',
        position=6, mandatory=False, argstr='%s')


class SulciLabelingDiffAcrossSubjectsOutputSpec(TraitedSpec):
    diff_table = traits.File(
        desc='CSV file,  CSV file')


class SulciLabelingDiffAcrossSubjects(BVCommand):
    input_spec = SulciLabelingDiffAcrossSubjectsInputSpec
    output_spec = SulciLabelingDiffAcrossSubjectsOutputSpec
    _cmd = 'SulciLabelingDiffAcrossSubjects'

