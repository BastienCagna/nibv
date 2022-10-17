from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SpamInstallModelsInputSpec(CommandLineInputSpec):
    download_url = traits.String(
        None,
        usedefault=False,
        desc='',
        position=0, argstr='%s', mandatory=False)
    install_talairach_models = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=1, mandatory=False)
    install_global_models = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    install_local_models = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=3, mandatory=False)
    install_additional_models = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    destination_database_directory = traits.File(
        exists=False,
        desc='Directory,  Directory',
        position=6, mandatory=False, argstr='%s')


class SpamInstallModelsOutputSpec(TraitedSpec):
    destination_database_directory = traits.File(
        desc='Directory,  Directory')


class SpamInstallModels(BVCommand):
    input_spec = SpamInstallModelsInputSpec
    output_spec = SpamInstallModelsOutputSpec
    _cmd = 'SpamInstallModels'

