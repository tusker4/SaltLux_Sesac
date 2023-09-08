import sound.formats.wave
from sound.effect.echo import echo_out as echo
from sound import music_play

file = 'mymusic.wav'
sound.formats.wave.wave_out(file)
sound.echo(file)
echo.echo_out(file)
music_play(file)
# 초기화파일에서 등록하라
