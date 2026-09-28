from pathlib import Path
import subprocess,sys,json,os
import numpy as np
from PIL import Image
r=Path(__file__).parent
mode='Motion' if '--motion' in sys.argv else 'Replica'
output_dir=Path(os.environ.get('RENDER_OUTPUT_DIR',str(r/'out')));output_dir.mkdir(parents=True,exist_ok=True)
samples=sorted((output_dir/f'{mode}-samples').glob('*.png'));assert len(samples)==1620
out=output_dir/f'{mode}-silent.mp4'
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pixel_format','rgb24','-video_size','702x494','-framerate','30','-i','-','-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p','-movflags','+faststart',str(out)],stdin=subprocess.PIPE)
for f in range(540):
 a=sum(np.asarray(Image.open(x).convert('RGB'),dtype=np.float32) for x in samples[f*3:f*3+3])/3
 p.stdin.write(np.uint8(a+.5).tobytes())
 if f%90==0: print(mode,'composite',f,flush=True)
p.stdin.close();assert p.wait()==0
final=output_dir/f'{mode}.mp4'
if mode=='Replica':subprocess.run(['ffmpeg','-v','error','-y','-i',str(out),'-i',str(r/'public/reference-audio.m4a'),'-map','0:v','-map','1:a','-c','copy','-t','18','-movflags','+faststart',str(final)],check=True)
else:out.replace(final)
print(final)
