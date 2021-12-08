import os

from nipype import LooseVersion
from nipype.utils.filemanip import fname_presuffix
from nipype.interfaces.base import (
    CommandLine,
    Directory,
    CommandLineInputSpec,
    isdefined,
    traits,
    TraitedSpec,
    File,
    PackageInfo,
)

# class Info(PackageInfo):


class BVCommand(CommandLine):
    _cmd_prefix = "bv axon-runprocess "
    #_cmd = self._cmd = "bv axon-runprocess " + self.process_name
    pass
