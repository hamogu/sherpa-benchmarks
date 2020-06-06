"""Benchmarks for import timing for sherpa and its subpackages."""

# https://github.com/airspeed-velocity/asv/pull/832

def timeraw_import_sherpa():
    return """
    import sherpa
    """


def timeraw_import_sherpa_astro():
    return """
    from sherpa import astro
    """


def timeraw_import_sherpa_astro_data():
    return """
    from sherpa.astro import data
    """

def timeraw_import_sherpa_astro_datastack():
    return """
    from sherpa.astro import datastack
    """


def timeraw_import_sherpa_astro_io():
    return """
    from sherpa.astro import io
    """


def timeraw_import_sherpa_astro_models():
    return """
    from sherpa.astro import models
    """


def timeraw_import_sherpa_astro_optical():
    return """
    from sherpa.astro import optical
    """


def timeraw_import_sherpa_astro_sim():
    return """
    from sherpa.astro import sim
    """


def timeraw_import_sherpa_astro_ui():
    return """
    from sherpa.astro import ui
    """


def timeraw_import_sherpa_estmethods():
    return """
    from sherpa import estmethods
    """


def timeraw_import_sherpa_images():
    return """
    from sherpa import images
    """


def timeraw_import_sherpa_models():
    return """
    from sherpa import models
    """


def timeraw_import_sherpa_optmethods():
    return """
    from sherpa import optmethods
    """


def timeraw_import_sherpa_plot():
    return """
    from sherpa import plot
    """


def timeraw_import_sherpa_sim():
    return """
    from sherpa import sim
    """


def timeraw_import_sherpa_stats():
    return """
    from sherpa import stats
    """


def timeraw_import_sherpa_ui():
    return """
    from sherpa import ui
    """


def timeraw_import_sherpa_data():
    return """
    from sherpa import data
    """
