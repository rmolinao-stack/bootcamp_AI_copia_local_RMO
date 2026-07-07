from context import cargar_faq

from copy import deepcopy
from pathlib import Path

from config import ASSISTANT_CONFIG_DEFAULT
from context import cargar_faq

DATA_DIR = Path(__file__).parent / "data"

aux = cargar_faq(DATA_DIR / "faq.json")

print()