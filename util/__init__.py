#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db.models import get_models

def get_project_models():
    """
    @return     a list of all project-specific models
    """

    project_models = []
    excluded_modules = [ "django", "south" ]

    for model in get_models():
        module_name = model.__module__.split( "." )[0]
        if module_name not in excluded_modules:
            project_models.append( model )

    return project_models


def get_project_models_dict():
    """
    @return     a dictionary of all project-specific models accessible by
                indices.


    """

    output = {}
    project_models = get_project_models()

    for model in project_models:
        output[model.__name__] = model
        output[model.__name__.lower()] = model

    return output


models = get_project_models_dict()