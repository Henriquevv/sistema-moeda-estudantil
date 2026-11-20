// Grava public/versao.json com o commit do build, para conferir qual versão está publicada.
import { mkdirSync, writeFileSync } from 'node:fs';
import process from 'node:process';

const versao = process.env.VERCEL_GIT_COMMIT_SHA || 'local';
mkdirSync('public', { recursive: true });
writeFileSync('public/versao.json', JSON.stringify({ versao }) + '\n');
console.log(`versao.json gravado: ${versao}`);
