from bitarray import bitarray
import sys

_ZW_MAP: dict[str, str] = {
    "00": "\u200b",  # ZERO WIDTH SPACE
    "01": "\u200c",  # ZERO WIDTH NON‑JOINER
    "10": "\u200d",  # ZERO WIDTH JOINER
    "11": "\ufeff",  # ZERO WIDTH NO‑BREAK SPACE (BOM)
}


class ZLCoder:
    _ZWS_MONO_MAP = {"0": "\u200c", "1": "\u200d"}
    _ZWS_MONO_MAP_INV = {"\u200c": "0", "\u200d": "1"}
    MONOZW = ["\u200c", "\u200d"]

    def strtobin(self, text: str) -> str:
        outputbin = bitarray()
        outputbin.frombytes(text.encode())
        return outputbin.to01()

    def bintostr(self, bin: str) -> str:
        return bitarray(bin).tobytes().decode()

    def bintomonozw(self, bin: str) -> str:
        zwtext = ""
        for i in bin:
            zwtext += self._ZWS_MONO_MAP[i]
        return zwtext

    def monozwtobin(self, monozwtext: str) -> str:
        text = ""
        for i in monozwtext:
            text += self._ZWS_MONO_MAP_INV[i]
        return text

    def strtomonozw(self, text: str) -> str:
        return self.bintomonozw(self.strtobin(text))

    def monozwtostr(self, monozw: str):
        return self.bintostr(self.monozwtobin(monozw))


class UI:
    zlc = ZLCoder()

    @classmethod
    def encode(cls, main_text: str, secret_text: str):
        return f"{main_text + cls.zlc.strtomonozw(secret_text)}"

    @classmethod
    def decode(cls, text):
        main_text = ""
        crypte = ""
        for i in text:
            if i in cls.zlc.MONOZW:
                crypte += i
        print(len(crypte))
        return cls.zlc.monozwtostr(crypte)
