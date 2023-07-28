import os


def get_run_logdir(logging_directory):
    """
    Function to create the separate folder with timestamp
    during the model training. Folder will contain the weights
    and model's checkpoints marked with time when the model training
    was run.
    :param logging_directory: std: The path to the logging (root) directory.
    :return: None
    """
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(logging_directory, run_id)

