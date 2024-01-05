from __future__ import annotations

from pathlib import Path

from scrapy.settings import BaseSettings


def job_dir(settings: BaseSettings) -> str | None:
    path: str | None = settings["JOBDIR"]
    if not path:
        return None
    if not Path(path).exists():
        Path(path).mkdir(parents=True)
    return path
