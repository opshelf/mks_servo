def u16s_to_i48(u16_1: int, u16_2: int, u16_3: int) -> int:
    combined = (u16_1 << 32) | (u16_2 << 16) | u16_3
    if combined >= 2**47:  # Check if the highest bit (47th bit) is set
        combined -= 2**48  # Adjust for two's complement if it is a negative number
    return combined


def u16s_to_i32(high: int, low: int) -> int:
    combined = (high << 16) | low
    if combined >= 0x80000000:  # Check if the most significant bit is set
        combined -= 0x100000000  # Adjust for 32-bit signed overflow
    return combined
