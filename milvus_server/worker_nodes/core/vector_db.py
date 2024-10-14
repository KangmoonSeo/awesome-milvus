from typing import List, Dict
import numpy as np


# Placeholder for vector storage
vector_db: Dict[str, List[np.ndarray]] = {}


def load_vector_db() -> Dict[str, List[np.ndarray]]:

    # TODO: load vector db from storage or minio

    return vector_db
