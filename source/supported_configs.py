"""
Module to maintain the list of supported functionality for each getter/setter.
New additions can simply be appended here, and followed by 'if' additions in the Orchestrator.

"""

getters_list = [
    "local directory",  # Has to remain at index 0.
    "amazon",
    "spotify"
]

setters_list = [
    "amazon",
    "spotify"
]
