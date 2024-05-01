from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# for the model : Parameter TYPE class > Parameter Variable class

@dataclass(frozen=True)           
class PrepareBaseModelConfig:

    '''by setting frozen=True, we are restricting any changes in the class further'''

    '''This class holds the required parameters types for model. @dataclass(frozen=True) set to True, so that the datatypes cann't be changed in further. If user will try to add anything new, it will throw an error'''

    #path parameters
    root_dir : Path
    base_model_path : Path
    base_updated_model_path : Path


    #model parameters
    params_image_size : list
    params_learning_rate : float
    params_include_top : bool
    params_weights : str
    params_classes : int


@dataclass(frozen=True)
class TrainingConfig:

    '''This class defines the datatypes of the training model'''

    root_dir : Path
    trained_model_path : Path
    updated_base_model_path : Path
    training_data : Path

    params_epochs : int
    params_batch_size : int
    params_is_augmentation : bool
    params_image_size : list