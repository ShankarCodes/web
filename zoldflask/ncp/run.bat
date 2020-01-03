@echo off
title Shankar Command Prompt
prompt $Cshankar-env$F$P$G
cd .
start .flaskenv\Scripts\activate 
start python -m flask run
cls