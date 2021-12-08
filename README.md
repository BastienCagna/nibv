# NiPype wrapping of BrainVISA processes

This python projects is made to automatically generate BrainVISA processes wraps for nipype.

Here is the commands to install it and generate the wraps (here we choose the morphologist toolbox but you can use it also for others):
`̀ `shell
git clone https://github.com/BastienCagna/nibv.git
cd nibv
python setup.py develop
python scripts/generate_wraps.py morphologist ./morphologist.json
``̀̀
