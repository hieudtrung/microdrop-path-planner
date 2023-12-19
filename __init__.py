from logging_helpers import _L
from microdrop.plugin_manager import PluginGlobals, Plugin, IPlugin, implements

import trollius as asyncio
import requests
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

PluginGlobals.push_env("microdrop.managed")


class PathPlannerPlugin(Plugin):
    implements(IPlugin)

    plugin_name = "path_planner_plugin"
    version = __version__

    @property
    def name(self):
        return self.plugin_name

    @name.setter
    def name(self, value):
        pass

    @asyncio.coroutine
    def on_step_run(self, plugin_kwargs, signals):
        _L().debug("The next step is recalculated after each successful step.")
        # sX, sY, eX, eY = signals
        # current_pos = {"startX": sX, "startY": sY, "endX": eX, "endY": eY}
        current_pos = {"startX": 0, "startY": 0, "endX": 8, "endY": 4}
        resp = requests.post(url="http://127.0.0.1:5000/astar", data=current_pos)
        _L().debug(resp.json())
        if resp.status_code == 200:
            nextX, nextY = resp.json()
        _L().debug((nextX, nextY))

        #
        raise asyncio.Return()


PluginGlobals.pop_env()
