SUPPORT_FORMAT = ('WAVE',)
SAMPLING = 128  # KBPS
CHANNEL = 'STEREO'
BITRATE = 44  # Khz


def wave_out(file):
    print(f"{file} 플레이, {SAMPLING}bps, {BITRATE}Khz, {CHANNEL}채널")
