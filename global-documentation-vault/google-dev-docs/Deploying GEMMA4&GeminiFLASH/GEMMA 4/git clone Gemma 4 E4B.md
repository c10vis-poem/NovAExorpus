git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it#

Make sure git-xet is installed (https://hf.co/docs/hub/git-xet)

curl -sSfL https://hf.co/git-xet/install.sh \| sh

Https =

git clone https://huggingface.co/Mer0vin8ian/Gemma-4-E4B-it

SSH=

git clone git@hf.co:Mer0vin8ian/Gemma-4-E4B-it#

\# If you want to clone without large files - just their pointers

GIT_LFS_SKIP_SMUDGE=1 git clone
https://huggingface.co/Mer0vin8ian/Gemma-4-E4B-it

\# Make sure the hf CLI is installed

curl -LsSf https://hf.co/cli/install.sh \| bash

\# Download the model

hf download Mer0vin8ian/Gemma-4-E4B-it
