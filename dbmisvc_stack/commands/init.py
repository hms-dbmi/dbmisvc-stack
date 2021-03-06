"""The init command."""

from dbmisvc_stack.commands.base import Base
from dbmisvc_stack.app import App

import logging

logger = logging.getLogger("stack")


class Init(Base):
    def run(self):

        # Determine the app.
        app = self.options["<app>"]

        # Ensure it's a built app
        logger.debug("({}) Check for need to initialize".format(app))
        if app is not None and App.get_repo_url(app) and App.get_repo_branch(app):

            # Initializer.
            logger.debug(
                "({}) Preparing to initialize with branch: {}".format(
                    app, App.get_repo_branch(app)
                )
            )
            App.init(app)

        else:

            # Iterate through built apps
            for app in App.get_built_apps():

                # Ensure it's a built app
                if App.get_repo_url(app) and App.get_repo_branch(app):

                    # Initializer.
                    logger.debug("({}) Preparing to initialize".format(app))
                    App.init(app)
