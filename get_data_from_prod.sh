#!/bin/bash

mkdir -p tmp
cd tmp
appcfg.py download_data --application=elephantropy-blog --url=http://elephantropy-blog.appspot.com/_ah/remote_api --filename=1.txt
appcfg.py upload_data --application=elephantropy-blog --url=http://localhost:8082/_ah/remote_api --filename=1.txt
cd ..