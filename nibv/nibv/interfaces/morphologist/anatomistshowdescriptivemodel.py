from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowDescriptiveModelInputSpec(CommandLineInputSpec):
    read = traits.File(
        exists=True,
        desc='Sulci Segments Model,  Text data table',
        position=0, mandatory=False, argstr='%s')
    levels = traits.Enum(
        "1", "2", "4", "3", "7",
        usedefault=False,
        desc='1: High probability (70% rejected), 2: Intermediate probability (40% rejected), 3: Low probability (20% rejected), 1-2: High-inter probabilities, 1-3: All 3 probabilities thesholds',
        position=1, mandatory=False)
    show_unknown = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    nomenclature = traits.File(
        exists=True,
        desc='Nomenclature,  Hierarchy',
        position=3, mandatory=False, argstr='%s')
    show_mesh = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    white_mesh = traits.File(
        exists=True,
        desc='White SPAM mesh,  anatomist mesh formats',
        position=5, mandatory=False, argstr='%s')
    mesh_to_spam = traits.File(
        exists=True,
        desc='Transformation,  Transformation Matrix',
        position=6, mandatory=False, argstr='%s')


class AnatomistShowDescriptiveModelOutputSpec(TraitedSpec):
    pass


class AnatomistShowDescriptiveModel(BVCommand):
    input_spec = AnatomistShowDescriptiveModelInputSpec
    output_spec = AnatomistShowDescriptiveModelOutputSpec
    _cmd = 'AnatomistShowDescriptiveModel'

