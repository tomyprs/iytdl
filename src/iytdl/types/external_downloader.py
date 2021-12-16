__all__ = ["ExternalDownloader", "Aria2c"]

from dataclasses import dataclass
from typing import Dict, List, Union


class ExternalDownloader:
    def _export(self) -> Dict[str, Union[str, List[str]]]:
        attrs = list(self.__dataclass_fields__)
        if "executable_path" in attrs and self.executable_path != "":
            ext_dl = self.executable_path
            attrs.remove("executable_path")
        else:
            ext_dl = self.__class__.__name__.lower()

        return dict(
            external_downloader=ext_dl,
            external_downloader_args=list(
                map(
                    lambda x: f"--{x.replace('_', '-')}={getattr(self, x)}",
                    attrs,
                )
            ),
        )


@dataclass
class Aria2c(ExternalDownloader):
    """Aria2c External Downloader"""

    executable_path: str = "aria2c"
    max_concurrent_downloads: int = 5
    max_connection_per_server: int = 10
    split: int = 5
    min_split_size: str = "20M"
    enable_rpc: str = "true"
    rpc_listen_all: str = "false"
    rpc_max_request_size: str = "1024M"
   # bt_save_metadata: str = "true"
    daemon: str = "true" 
    allow_overwrite: str = "true"
    show_console_readout: str = "false"
    summary_interval: int = 0
    download_result: str = "hide"
    quiet: str = "true"
