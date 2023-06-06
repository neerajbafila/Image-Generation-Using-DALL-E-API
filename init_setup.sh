echo [$(Date)]: "START"
echo [$(Date)]: "Creating conda env with python 3.10"
conda create --prefix ./env python=3.10 -y
echo [$(Date)]: "activate env"
source activate ./env
conda activate ./env
echo [$(date)]: "installing the requirements" 
pip install -r requirements.txt
echo [$(date)]: "END" 