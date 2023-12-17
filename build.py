#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "TicTacToe"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("mockito")
    # Exclude the app module from coverage
    project.set_property("coverage_break_build", False)
    project.get_property("coverage_exceptions").append("app")
