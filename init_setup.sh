echo [$(date)]: 'START'

echo [$(date)]: 'creating env with python'

python -m venv env

echo [$(date)]: 'activating the environment'

source activate ./env

echo [$(date)]: "installing the dev requirements"

pip install -r requirements_dev.txt

echo [$(date)]: 'END'