from pydantic import BaseModel
from typing import Optional


class PlannerOuput(BaseModel):
    """
    Dataclass for planning agent's output with form:
    {
    "model": <name of model as string>,
    "preprocessing": [<name of technique 1 as string>, ... , <name of technique n as string>],
    "hyperparameters":{
        "<hyperparamter name as string>": <value of hyperparameter>
        }
    }
    """

    suggested_model: str
    suggested_preprocessing_techniques: list[str]
    suggested_hyperparameters: dict[str, int | float | str]
