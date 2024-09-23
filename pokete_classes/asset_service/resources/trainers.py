# DO NOT EDIT!
# This code was auto generated by the `protoc-gen-pokete-resources` plugin,
# part of the pokete project, by <lxgr@protonmail.com>
import logging
from typing import TypedDict


class TrainerPokeArgsDict(TypedDict):
    name: str
    xp: int


class TrainerPokeArgs:
    def __init__(
        self,
        name: str,
        xp: int
    ):
        self.name: str = name
        self.xp: int = xp

    @classmethod
    def from_dict(cls, _d: TrainerPokeArgsDict | None) -> "TrainerPokeArgs | None":
        if _d is None:
            return None
        return cls(
            name=_d["name"],
            xp=_d["xp"],
        )

    @staticmethod
    def validate(_d: TrainerPokeArgsDict) -> bool:
        return all([
            "name" in _d and type(_d["name"]) is str,
            "xp" in _d and type(_d["xp"]) is int,
        ])

    def to_dict(self) -> TrainerPokeArgsDict:
        ret: TrainerPokeArgsDict = {}
        
        ret["name"] = self.name
        ret["xp"] = self.xp

        return ret


class TrainerArgsDict(TypedDict):
    name: str
    gender: str
    texts: list[str]
    lose_texts: list[str]
    win_texts: list[str]
    x: int
    y: int


class TrainerArgs:
    def __init__(
        self,
        name: str,
        gender: str,
        texts: list[str],
        lose_texts: list[str],
        win_texts: list[str],
        x: int,
        y: int
    ):
        self.name: str = name
        self.gender: str = gender
        self.texts: list[str] = texts
        self.lose_texts: list[str] = lose_texts
        self.win_texts: list[str] = win_texts
        self.x: int = x
        self.y: int = y

    @classmethod
    def from_dict(cls, _d: TrainerArgsDict | None) -> "TrainerArgs | None":
        if _d is None:
            return None
        return cls(
            name=_d["name"],
            gender=_d["gender"],
            texts=_d["texts"],
            lose_texts=_d["lose_texts"],
            win_texts=_d["win_texts"],
            x=_d["x"],
            y=_d["y"],
        )

    @staticmethod
    def validate(_d: TrainerArgsDict) -> bool:
        return all([
            "name" in _d and type(_d["name"]) is str,
            "gender" in _d and type(_d["gender"]) is str,
            "texts" in _d and all(type(i) is str for i in _d["texts"]),
            "lose_texts" in _d and all(type(i) is str for i in _d["lose_texts"]),
            "win_texts" in _d and all(type(i) is str for i in _d["win_texts"]),
            "x" in _d and type(_d["x"]) is int,
            "y" in _d and type(_d["y"]) is int,
        ])

    def to_dict(self) -> TrainerArgsDict:
        ret: TrainerArgsDict = {}
        
        ret["name"] = self.name
        ret["gender"] = self.gender
        ret["texts"] = self.texts
        ret["lose_texts"] = self.lose_texts
        ret["win_texts"] = self.win_texts
        ret["x"] = self.x
        ret["y"] = self.y

        return ret


class TrainerDict(TypedDict):
    pokes: list["TrainerPokeArgsDict"]
    args: "TrainerArgsDict"


class Trainer:
    def __init__(
        self,
        pokes: list["TrainerPokeArgs"],
        args: "TrainerArgs"
    ):
        self.pokes: list["TrainerPokeArgs"] = pokes
        self.args: "TrainerArgs" = args

    @classmethod
    def from_dict(cls, _d: TrainerDict | None) -> "Trainer | None":
        if _d is None:
            return None
        return cls(
            pokes=[TrainerPokeArgs.from_dict(i) for i in _d["pokes"]],
            args=TrainerArgs.from_dict(_d["args"]),
        )

    @staticmethod
    def validate(_d: TrainerDict) -> bool:
        return all([
            "pokes" in _d and all(TrainerPokeArgs.validate(i) for i in _d["pokes"]),
            "args" in _d and TrainerArgs.validate(_d["args"]),
        ])

    def to_dict(self) -> TrainerDict:
        ret: TrainerDict = {}
        
        ret["pokes"] = [TrainerPokeArgs.to_dict(i) for i in self.pokes]
        ret["args"] = TrainerArgs.to_dict(self.args)

        return ret
