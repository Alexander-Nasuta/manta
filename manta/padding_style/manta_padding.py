from manta.padding_style.paddingABC import PaddingABC


class MantaPadding(PaddingABC):
    small_buff: float = 0.1
    med_small_buff: float = 0.2
    med_large_buff: float = 0.4
    large_buff: float = 0.8