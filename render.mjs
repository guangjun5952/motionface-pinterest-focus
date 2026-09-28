import {bundle} from '@remotion/bundler';import {renderFrames,selectComposition} from '@remotion/renderer';import path from 'node:path';
const mode=process.argv.includes('--motion')?'Motion':'Replica';const serveUrl=await bundle({entryPoint:path.resolve('src/index.tsx')});const composition=await selectComposition({serveUrl,id:mode+'Samples'});
await renderFrames({serveUrl,composition,outputDir:path.resolve(process.env.RENDER_OUTPUT_DIR || 'out',mode+'-samples'),imageFormat:'png',concurrency:4,onFrameUpdate:f=>{if(f%270===0)console.log(mode,f+'/1620');}});console.log(mode+' samples complete');
