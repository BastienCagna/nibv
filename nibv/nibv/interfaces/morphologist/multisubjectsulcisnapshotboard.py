from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class MultiSubjectSulciSnapshotBoardInputSpec(CommandLineInputSpec):
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=3, mandatory=False, argstr='%s')
    labels_translation_map = traits.File(
        exists=True,
        desc='Label Translation, Label Translation,  DEF Label translation',
        position=4, mandatory=False, argstr='%s')
    sulci_name = traits.String(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%s', mandatory=False)
    orientation = traits.Enum(
        "left", "right", "top", "bottom",
        usedefault=False,
        desc='left, right, top,  bottom',
        position=6, mandatory=False)
    label_attribute = traits.Enum(
        "name", "label",
        usedefault=False,
        desc='name,  label',
        position=7, mandatory=False)
    output_image = traits.File(
        exists=False,
        desc='2D Image, aims Image Formats',
        position=8, mandatory=False, argstr='%s')
    pages_number = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%d', mandatory=False)
    rows = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=10, argstr='%d', mandatory=False)
    columns = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=11, argstr='%d', mandatory=False)
    page_size_ratio = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%f', mandatory=False)
    snapshot_width = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=13, argstr='%d', mandatory=False)
    snapshot_height = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=14, argstr='%d', mandatory=False)


class MultiSubjectSulciSnapshotBoardOutputSpec(TraitedSpec):
    output_image = traits.File(
        desc='2D Image, aims Image Formats')


class MultiSubjectSulciSnapshotBoard(BVCommand):
    input_spec = MultiSubjectSulciSnapshotBoardInputSpec
    output_spec = MultiSubjectSulciSnapshotBoardOutputSpec
    _cmd = 'MultiSubjectSulciSnapshotBoard'

