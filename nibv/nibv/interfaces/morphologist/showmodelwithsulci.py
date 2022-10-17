from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ShowModelWithSulciInputSpec(CommandLineInputSpec):
    max_views_per_block = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%d', mandatory=False)
    show_first_mesh_alone = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    spam_model = traits.File(
        exists=True,
        desc='Sulci Segments Model,  Text data table',
        position=3, mandatory=False, argstr='%s')
    show_unknown = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=6, mandatory=False, argstr='%s')
    show_mesh = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=7, mandatory=False)
    white_mesh = traits.File(
        exists=True,
        desc='White SPAM mesh,  anatomist mesh formats',
        position=8, mandatory=False, argstr='%s')
    mesh_to_spam = traits.File(
        exists=True,
        desc='Transformation,  Transformation Matrix',
        position=9, mandatory=False, argstr='%s')


class ShowModelWithSulciOutputSpec(TraitedSpec):
    pass


class ShowModelWithSulci(BVCommand):
    input_spec = ShowModelWithSulciInputSpec
    output_spec = ShowModelWithSulciOutputSpec
    _cmd = 'ShowModelWithSulci'

