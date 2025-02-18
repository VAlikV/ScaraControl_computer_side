# ScaraControl_computer_side
Program for control scara manipulator for WBS

## For windows

Creating enviroment
```bash
python -m venv .venv
```

Activation

```bash
Set-ExecutionPolicy Unrestricted -Scope Process

.venv\Scripts\Activate.ps1
```

Deactivation
```bash
deactivate
```
Install req
```bash
python -m pip freeze > requirements.txt

python -m pip install -r requirements.txt
```

## For Linux

```bash
python -m venv .venv
source .venv/bin/activate
```
```bash
deactivate
```
