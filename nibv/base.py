from nipype.interfaces.base import (
    CommandLine,
    PackageInfo,
)

# class Info(PackageInfo):


class BVCommand(CommandLine):
    _cmd_prefix = "bv axon-runprocess "
