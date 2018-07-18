#!/bin/sh
cd /code/frontend
/usr/local/bin/npm run build
/usr/local/bin/npm run dev
export PATH=$PATH:node_modules/.bin