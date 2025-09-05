_ZW_MAP: dict[str, str] = {
    "00": "\u200b",  # ZERO WIDTH SPACE
    "01": "\u200c",  # ZERO WIDTH NON‑JOINER
    "10": "\u200d",  # ZERO WIDTH JOINER
    "11": "\ufeff",  # ZERO WIDTH NO‑BREAK SPACE (BOM)
}
_ZW_MAP_INV: dict[str, str] = {
    "\u200b": "00",
    "\u200c": "01",
    "\u200d": "10",
    "\ufeff": "11",
}
_ZW = ["\u200c", "\u200d", "\u200b", "\ufeff"]

_ZWS_MONO_MAP = {"0": "\u200c", "1": "\u200d"}
_ZWS_MONO_MAP_INV = {"\u200c": "0", "\u200d": "1"}
_MONOZW = ["\u200c", "\u200d"]


class ZLCoder:
    def strtobin(self, s: str) -> str:
        return "".join(f"{b:08b}" for b in s.encode("utf-8"))

    def bintostr(self, b: str) -> str:
        bytes_arr = bytes(int(b[i : i + 8], 2) for i in range(0, len(b), 8))
        return bytes_arr.decode("utf-8")

    def bintomonozw(self, bin: str) -> str:
        zwtext = ""
        for i in bin:
            zwtext += _ZWS_MONO_MAP[i]
        return zwtext

    def monozwtobin(self, monozwtext: str) -> str:
        text = ""
        for i in monozwtext:
            text += _ZWS_MONO_MAP_INV[i]
        return text

    def bintozw(self, bin: str) -> str:
        text = ""
        # print(bin)
        for i in [f"{bin[i * 2]}{bin[i * 2 + 1]}" for i in range(int(len(bin) / 2))]:
            text += _ZW_MAP[i]
            # print(i)
        return text

    def zwtobin(self, zwtext: str) -> str:
        text = ""
        # print(f"{zwtext}{len(zwtext)}")
        for i in zwtext:
            text += _ZW_MAP_INV[i]
            # print(i)
        return text

    def monozwtostr(self, monozw: str):
        return self.bintostr(self.zwtobin(monozw))

    def strtomonozw(self, text: str) -> str:
        return self.bintozw(self.strtobin(text))


class UI:
    zlc = ZLCoder()

    @classmethod
    def encode(cls, main_text: str, secret_text: str):
        return f"{main_text + cls.zlc.strtomonozw(secret_text)}"

    @classmethod
    def decode(cls, text):
        crypte = ""
        for i in text:
            if i in _ZW:
                crypte += i
        return cls.zlc.monozwtostr(crypte)
