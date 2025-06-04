import importlib.util
import sys
import types
from pathlib import Path


def load_module(module_name: str, file_path: str):
    """Utility to load a module from a file without executing package __init__."""
    path = Path(__file__).resolve().parents[1] / file_path
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def setup_modules():
    """Load minimal modules required for Node.SectionFormating."""
    # Load SubNode.states and create a fake package entry to satisfy imports
    states = load_module("SubNode.states", "SubNode/states.py")
    pkg = types.ModuleType("SubNode")
    pkg.states = states
    sys.modules.setdefault("SubNode", pkg)
    sys.modules["SubNode.states"] = states
    # Load Node.SectionFormating using the fake SubNode package
    section_formating = load_module("Node.SectionFormating", "Node/SectionFormating.py")
    return states, section_formating



def test_format_sections():
    states, sf = setup_modules()

    section1 = states.Section(
        name="Introduction",
        description="Overview of the topic",
        research=True,
        content="Intro content",
    )
    section2 = states.Section(
        name="Background",
        description="Background details",
        research=False,
        content="",
    )

    formatted = sf.format_sections([section1, section2])
    assert "Section 1: Introduction" in formatted
    assert "Section 2: Background" in formatted
    assert "[Not yet written]" in formatted
