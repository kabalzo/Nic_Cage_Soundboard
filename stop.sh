#!/bin/bash
read < pid
kill $(($REPLY))
