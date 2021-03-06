"""The build command."""

import docker

from dbmisvc_stack.commands.base import Base
from dbmisvc_stack.app import App

import logging

logger = logging.getLogger("stack")


class Build(Base):
    def run(self):

        # Get the docker client.
        docker_client = docker.from_env()

        # Determine the app.
        app = self.options["<app>"]
        clean = self.options["--clean"]

        # Ensure it's a built app
        if app is not None and App.get_build_dir(app):

            # Check if we should clean it.
            if clean:
                App.clean_images(docker_client, app)

            App.build(app)

        else:

            # Iterate through built apps
            for app in App.get_built_apps():

                # Check if we should clean it.
                if clean:
                    App.clean_images(docker_client, app)

                App.build(app)
