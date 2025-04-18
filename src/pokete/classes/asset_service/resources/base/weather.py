# DO NOT EDIT!
# This code was auto generated by the `protoc-gen-pokete-resources-python` plugin,
# part of the pokete project, by <lxgr@protonmail.com>
from typing import TypedDict


class WeatherDict(TypedDict):
    info: str
    effected: dict[str, float]


class Weather:
    def __init__(
        self,
        info: str,
        effected: dict[str, float]
    ):
        self.info: str = info
        self.effected: dict[str, float] = effected

    @classmethod
    def from_dict(cls, _d: WeatherDict | None) -> "Weather | None":
        if _d is None:
            return None
        return cls(
            info=_d["info"],
            effected=_d["effected"],
        )

    @staticmethod
    def validate(_d: WeatherDict) -> bool:
        return all([
            "info" in _d and type(_d["info"]) is str,
            "effected" in _d and all(type(item) is float or type(item) is int for _, item in _d["effected"].items()),
        ])

    def to_dict(self) -> WeatherDict:
        ret: WeatherDict = {}
        
        ret["info"] = self.info
        ret["effected"] = self.effected

        return ret
